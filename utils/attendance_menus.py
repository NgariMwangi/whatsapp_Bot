import json,requests
url = "https://api.gupshup.io/sm/api/v1/msg"
def attendanceSubMenus(x):
    headers = {
        "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    options=[]
    menu_instruction=x["text"]
    json_options=x["options"]
    for key, value in json_options.items():
        dict1 = {"type": "text", "title": value, "description": ""}
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

def attendance_slot_error(user_number,message):
    url = "https://api.gupshup.io/sm/api/v1/msg"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
    "Cache-Control": "no-cache",
}
    t={"type":"text","text":f'{message}'}
    j=json.dumps(t)
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": j,
        "src.name": "LittleWhatsappBot",
    }

    response = requests.post(url, headers=headers, data=data)

def sendCurrentLocation(user_number):
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
}
    url = "https://api.gupshup.io/sm/api/v1/msg"
    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": "254712658775",
        "message": '{"type":"location_request_message","body":{"type":"text","text":"Current Location"},"action":{"name":"send_location"}}',
        "src.name": "LittleWhatsappBot",
    }
    response = requests.post(url, headers=headers, data=data)
    return response.text
def slotsMenu(x):
    headers = {
        "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    options=[]
    menu_instruction="Choose one slot"
 
    for key, value in x.items():
        dict1 = {"type": "text", "title": value, "description": ""}
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