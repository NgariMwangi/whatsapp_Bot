import json, requests
from models.sessionmodel import RupdateSession
url = "https://api.gupshup.io/sm/api/v1/msg"

# this is the main menu. It has the four main services
def service_buttons(initial_page_json):
    headers = {
        "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    options=[]
    menu_instruction=initial_page_json["text"]
    json_options=initial_page_json["options"]
    for key, value in json_options.items():
        dict1 = {"type": "text", "title": value[4:], "description": ""}
        options.append(dict1)
    button_title="Main Menu"
    if menu_instruction !="Welcome to Little. Ride a Little Better.\n":
        button_title="Menu"
        back_to_main_menu={"type":"text", "title":"Go back to main menu", "description":""}
        options.append(back_to_main_menu)
    menu={"type":"list","title":"Little","body":menu_instruction,"globalButtons":[{"type":"text","title":button_title}],"items":[{"title":"Services","subtitle":"Services","options":options}]}
    menu=json.dumps(menu)
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": menu,
        "src.name": "LittleWhatsappBot",
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code


# this are the submenus from the menu json. Branches of the four main services
def subMenus(x):   
    headers = {
        "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    options=[]
    menu_instruction=x["text"]
    json_options=x["options"]
    for key, value in json_options.items():
        dict1 = {"type": "text", "title": value[4:], "description": ""}
        options.append(dict1)
     
    back_to_main_menu={"type":"text", "title":"Go back to main menu", "description":""}
    options.append(back_to_main_menu)
    v={"type":"list","title":"Little","body":menu_instruction,"globalButtons":[{"type":"text","title":"Menu"}],"items":[{"title":"Services","subtitle":"Services","options":options}]}
    j=json.dumps(v)
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": j,
        "src.name": "LittleWhatsappBot",
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code


# this is the suggested location menu
def suggestedLocationMenus(locations,user_number):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
        "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    options=[]
    menu_instruction="Choose Drop-off Location from suggested Locations"
    id=1
    for location in locations:
        
        combined_location=location["description"]+" , "+ location["state"]
        dict1 = {"type": "text", "title":id , "description":combined_location}
        options.append(dict1)
        id=id+1  
    back_to_main_menu={"type":"text", "title":"Go back to main menu", "description":""}
    options.append(back_to_main_menu)
    v={"type":"list","title":"Little","body":menu_instruction,"globalButtons":[{"type":"text","title":"Menu"}],"items":[{"title":"Services","subtitle":"Services","options":options}]}
    j=json.dumps(v)
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": j,
        "src.name": "LittleWhatsappBot",
    }
    response = requests.post(url, headers=headers, data=data)
    if response.json()["status"]=="submitted":
        state="SUGGESTED-LOCATION"
        RupdateSession(state,user_number)   
    return response.status_code


# this is the menu used to get the current user location
def sendLocation():
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
}
    url = "https://api.gupshup.io/sm/api/v1/msg"
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": '{"type":"location_request_message","body":{"type":"text","text":"Where would you like to be picked?"},"action":{"name":"send_location"}}',
        "src.name": "LittleWhatsappBot",
    }
    response = requests.post(url, headers=headers, data=data)
    return response.text


# this is the menu used to request for user card number
def proviveCardNo(user_number):
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
    "Cache-Control": "no-cache",
}
    url = "https://api.gupshup.io/sm/api/v1/msg"
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": '{"type":"text","text":"Type in your drop off location:"}',
        "src.name": "LittleWhatsappBot",
    }
    response = requests.post(url, headers=headers, data=data)
    if response.json()["status"]=="submitted":
        state="BOOK-CAB"
        RupdateSession(state,user_number)

# this is the menu used for asking the user to type his desired drop off location
def dropOffLocation(user_number):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
    "Cache-Control": "no-cache",
}

    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": '{"type":"text","text":"Type in your drop off location:"}',
        "src.name": "LittleWhatsappBot",
    }

    response = requests.post(url, headers=headers, data=data)
    if response.json()["status"]=="submitted":
        state="BOOK-CAB"
        RupdateSession(state,user_number)
def requesting(user_number):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
    "Cache-Control": "no-cache",
}

    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": '{"type":"text","text":"Requesting.....:"}',
        "src.name": "LittleWhatsappBot",
    }

    response = requests.post(url, headers=headers, data=data)
def trip_id(user_number,trip_id):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
    "Cache-Control": "no-cache",
}
    t={"type":"text","text":f'Your trip id: {trip_id}'}
    j=json.dumps(t)
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": j,
        "src.name": "LittleWhatsappBot",
    }

    response = requests.post(url, headers=headers, data=data)

def driver_name(user_number,name,time,distance):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
    "Cache-Control": "no-cache",
}
    t={"type":"text","text":f'Your driver {name} is {time} mins and {distance} m away'}
    j=json.dumps(t)
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": j,
        "src.name": "LittleWhatsappBot",
    }

    response = requests.post(url, headers=headers, data=data)
def call(user_number,driver_no):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
    "Cache-Control": "no-cache",
}
    t={"type":"text","text":f'Driver Phone Number: {driver_no}'}
    j=json.dumps(t)
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": j,
        "src.name": "LittleWhatsappBot",
    }

    response = requests.post(url, headers=headers, data=data)
def cardetails(user_number,model,plate,color):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
    "Cache-Control": "no-cache",
}
    t={"type":"text","text":f' {model}\nPlate: {plate}\nColor:{color}'}
    j=json.dumps(t)
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": j,
        "src.name": "LittleWhatsappBot",
    }

    response = requests.post(url, headers=headers, data=data)

def driverPic(user_number,image_url):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded",
        "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
    }
    
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": '{"type":"image","originalUrl":"' + image_url + '","caption":"Driver`s Photo","filename":"CustomImage.jpeg"}',
        "src.name": "LittleWhatsappBot",
    }

    response = requests.post(url, headers=headers, data=data)

    print("Response Code:", response.status_code)
    print("Response Content:", response.text)
