import requests
import json

def send_message(number, message):
    url = "http://api.gupshup.io/sm/api/v1/template/msg"
    headers = {
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': 'application/json',
'apikey': 'lztgzgifb7ok1wwlb9luve90zersbjiz'
}

    


    data = {
        "channel": "whatsapp",
        "source": "917834811114",
        "destination": number,
      "template": '{"id": "ca4918f6-67fc-4664-8aee-c0685ece3dc9","params": ["Little","6000","2hrs"]}',
        "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
        "src.name": "LittleWhatsappBot"
    }
    
    response = requests.post(url, headers=headers, data=data)

    print(response.text)

# Example usage
send_message("254712658775", "7789")
