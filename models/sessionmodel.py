from redis_om import EmbeddedJsonModel, Field, JsonModel
from typing import Optional
import json

class RSession(JsonModel):
    # Indexed for exact text matching
    phoneNumber: str = Field(index=True)
    state: str = Field(index=True)
    stepsTakenByUser: Optional[str] = Field(index=True)
    longitude: Optional[str] = Field(index=False)
    latitude: Optional[str] = Field(index=False)
    dropoff_location: Optional[str] = Field(index=False)
    paymentModes: Optional[str] = Field(index=False)
    card_mobile_obu_number: Optional[str] = Field(index=False)
    chosenDropOffLocation : Optional[str] = Field(index=False)
    corporateDepartment : Optional[str] = Field(index=True)

 
# create a new session and set session ttl
def RsetSession(phone,state): 
    sess = RSession(
        phoneNumber=phone,
        state=state,
        stepsTakenByUser=state

    )
    sess.save()
    RSession.db().expire(sess.key(), 500)


# check if session exist by searching using a phone number
def RgetSession(phoneNumber):
    try:
        session = RSession.find(RSession.phoneNumber == phoneNumber).first()
      
    except Exception as e:
        session = None

    return session


# used to update state and stepstakenby user in a session so as to keep track of users steps
def RupdateSession( state, phoneNumber):
    session = RSession.find(
        (RSession.phoneNumber== phoneNumber)
    ).first()
    if not session:
        print("NO SESSION UPDATED")
        return {"successful": False, "reason": "no session was found"}
    session.state = state
    session.stepsTakenByUser = str(session.stepsTakenByUser) + f".{state}"
    session.save()
    return json.loads(session.json())


# used to delete a session
def RdeleteSession(phoneNumber):
    session = RSession.find(RSession.phoneNumber == phoneNumber).first() 
    if session:   
        try:
            sess_key=session.key()        
            pk=sess_key[30:]       
            session.delete(pk)
                       
            # Additional code
        except Exception as e:    
            print(f"Error: {str(e)}")
            return {"successful": True, "message": f"Session for {phoneNumber} deleted successfully."}
    else:
        return {"successful": False, "reason": f"No session found for {phoneNumber}."}



def RgetUserstep(phoneNumber): 
    try:
    
        session = RSession.find(
            (RSession.phoneNumber == phoneNumber) & (RSession.state == "INITIAL-PAGE")
        ).first()
        
        return True
    except Exception as e:
        print(str(e))
        return False


# used to save user pickup location in terms of latitude and longitude
def RsaveUserCurrentLocation(phoneNumber, latitude,longitude):
    session = RSession.find(
    (RSession.phoneNumber== phoneNumber)
    ).first()
    if not session:
        print("NO SESSION UPDATED")
        return {"successful": False, "reason": "no session was found"}
    session.longitude = longitude
    session.latitude = latitude
    session.save()


# used to save user typed drop off location
def RsaveDropOfLocation(phoneNumber,location):
    session = RSession.find(
    (RSession.phoneNumber== phoneNumber)
    ).first()
    if not session:
        print("NO SESSION UPDATED")
        return {"successful": False, "reason": "no session was found"}
    session.dropoff_location = location
    session.save()

# used to save user chosen drop off location from the suggested locations
def RchosenDropOffLocation(phoneNumber,location):
    session = RSession.find(
    (RSession.phoneNumber== phoneNumber)
    ).first()
    if not session:
        return {"successful": False, "reason": "no session was found"}
    session.chosenDropOffLocation = location
    session.save()

def RsavePaymentMode(phoneNumber,mode):
    session = RSession.find(
    (RSession.phoneNumber== phoneNumber)
    ).first()
    if not session:
        print("NO SESSION UPDATED")
        return {"successful": False, "reason": "no session was found"}
    session.paymentModes = mode
    session.save()



def RgetCurrentUserState(phoneNumber):
    session = RSession.find(
    (RSession.phoneNumber== phoneNumber)
    ).first()
    if not session:
        print("NO SESSION UPDATED")
        return {"successful": False, "reason": "no session was found"}
    print(session.state)
    return session.state



def RsaveCard_mobile_obu_number(phoneNumber,num):
    session = RSession.find(
    (RSession.phoneNumber== phoneNumber)
    ).first()
    if not session:
        print("NO SESSION UPDATED")
        return {"successful": False, "reason": "no session was found"}
    session.card_mobile_obu_number = num
    session.save()


def RgetUserDepartment(phoneNumber): 
    try:
        # Use your data access mechanism to retrieve the session data
        session = RSession.find(
            (RSession.phoneNumber == phoneNumber) & 
            # (RSession.corporateDepartment == None) & 
            (RSession.state == "STAFF-ATTENDANCE")
        ).first()

        if session.corporateDepartment is not None:
            return False
        else:
            return True
    
    except Exception as e:
        print("Error:", str(e))
        return False
def RgetUserDepartmentName(phoneNumber): 
    try:
        # Use your data access mechanism to retrieve the session data
        session = RSession.find(
            (RSession.phoneNumber == phoneNumber) & 
            # (RSession.corporateDepartment == None) & 
            (RSession.state == "STAFF-ATTENDANCE")
        ).first()
        return session.corporateDepartment
    
    except Exception as e:
        print("Error:", str(e))
        return False

def RsaveCorporateDepartment(phoneNumber,dept):
    session = RSession.find(
    (RSession.phoneNumber== phoneNumber)
    ).first()
    if not session:
        print("NO SESSION UPDATED")
        return {"successful": False, "reason": "no session was found"}
    session.corporateDepartment = dept
    session.save()
