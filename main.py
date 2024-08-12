from flask import Flask, request, jsonify
import json, requests,redis
from models.sessionmodel import *
from redis_om import Migrator
from utils.cab_menus import *
from utils.get_suggested_locations import getPlaceSuggestion
from utils.send_message import send_message
from utils.ride_request import requestRide

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)

Migrator().run()

# Fetching the menu json data
json_file_path = 'static/menu.json'
with open(json_file_path, 'r') as json_file:
        menu_json = json.load(json_file)
    
    

# callback url
@app.route('/webhook', methods=['POST'])
def webhook():
    # fetch data from callback url
    incoming_message=request.get_json()
    print(incoming_message)
    #check what type of data has been sent and allow only messages to proceed
    if incoming_message["type"]!="message":   
         return ""
    
    # extract the number from the message sent
    user_number = incoming_message["payload"]['source']

    # check if number is in session
    if RgetSession(user_number):
        # save the user typed location to the session
        if RgetCurrentUserState(user_number)=="SUGGESTED-LOCATION":
            pickedDroffLocation=incoming_message["payload"]["payload"]["description"]
            RchosenDropOffLocation(user_number,pickedDroffLocation)
            state="BOOK-CAB"
            RupdateSession(state,user_number)

        # if user has sent his current pick up destination prompt him to enter his drop of location
        if RgetCurrentUserState(user_number)=="MOJA-EXPRESS":
            card_no=incoming_message["payload"]["payload"]["title"]
            RsavePaymentMode(user_number,card_no)


        if RgetCurrentUserState(user_number)=="MTC" or RgetCurrentUserState(user_number)=="ETC":
            num=incoming_message["payload"]["payload"]["text"]
            RsaveCard_mobile_obu_number(user_number,num)

        # save the user pickup location and update the state to "DROP-OFF-LOCATION" so as to be used on the next user step
        if incoming_message["payload"]["type"]=="location":
            latitude=incoming_message["payload"]["payload"]["latitude"]
            longitude=incoming_message["payload"]["payload"]["longitude"]
            state="DROP-OFF-LOCATION"
            RupdateSession(state,user_number)
            RsaveUserCurrentLocation(user_number,latitude,longitude)
            dropOffLocation(user_number)           
            return ""
        

        try:      
            # if in session check the title of the incoming message
            raw_option=incoming_message["payload"]["payload"]["title"]
          #  format the title so as to be used as a key in the next json step
            json_key= raw_option.strip().replace(" ", "-").upper()  
            print(json_key)    
            # if json key or user action is "GO-BACK-TO-MAIN-MENU" delete the current session and create a new one immediately
            if json_key == "GO-BACK-TO-MAIN-MENU":
                RdeleteSession(user_number)               
                menu_instr=menu_json["menu"]["INITIAL-PAGE"]
                state="INITIAL-PAGE"
                RsetSession(user_number,state)
                service_buttons(menu_instr)
                return ""
            
            # If json key is BOOK-CAB prompt the user to send his/her current location
            if json_key == "BOOK-CAB" and RgetUserstep(user_number):               
                 state="PICK-UP-LOCATION"
                 RupdateSession(state,user_number)
                 sendLocation()
                 return ""

                    



        except:          
        #  if the is no title on the incoming message payload. Extract current user state from redis
            rsession=RgetSession(user_number)
            rsession.dict()
            json_key=rsession.dict()["state"]
           


        try:
            # display the suggested drop off location after user enters his desired drop off location
            if json_key == "BOOK-CAB" and RgetUserstep(user_number)==False:
                location=incoming_message["payload"]["payload"]["text"]           
                sug_locations=getPlaceSuggestion(location)
                suggestedLocationMenus(sug_locations,user_number)
                RsaveDropOfLocation(user_number,location)
                return ""

            # try and locate the specific json data request using the json_key and then save the state and update the stepsTakenByUser
            menu_instr=menu_json["menu"][json_key]
            state=menu_json["menu"][json_key]["id"]
            subMenus(menu_instr)
            RupdateSession(state,user_number)
            if json_key == "BOOK":
                r=requestRide()
                print(r)
                if r["Status"]=="000":
                    print("status 000")
                    try:
                        requesting(user_number)
                        trip_id(user_number,r["TripID"])
                        driver_name(user_number,r["DriverName"],r["TimeDistance"],r["RoadDistance"])
                        call(user_number,r["DriverMobileNumber"])
                        cardetails(user_number,r["CarModel"],r["CarNumber"],r["CarColor"])
                        driverPic(user_number,r["DriverPIC"])
                    except:
                        print("fail")
            
        except:
            # if there is no such key make the user to repeat that last step again by fetching the current state from redis
            rsession=RgetSession(user_number)
            rsession.dict()
            json_key=rsession.dict()["state"]
            menu_instr=menu_json["menu"][json_key]
            service_buttons(menu_instr)

    else:
         #if number is not in session initiate the Initial page menu and set the current user state as "INITIAL-PAGE"
         menu_instr=menu_json["menu"]["INITIAL-PAGE"]
         state="INITIAL-PAGE"
         RsetSession(user_number,state)
         service_buttons(menu_instr)
               
    return ""
 
@app.route('/sendmessage', methods=['POST'])
def message():
    incoming_message=request.get_json()
    number=incoming_message["to"]
    message=incoming_message["text"]
    send_message(number,message)
    return ""


if __name__ == '__main__':
    Migrator().run()
    app.run(debug=True)
