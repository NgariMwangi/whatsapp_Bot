import requests

url = "https://api.safaricom.co.ke/oauth2/v1/generate?grant_type=client_credentials"

payload = {}
headers = {
  'Authorization': 'Basic dDIydktMTFEwYVVnQURwcXBOR2dxbnZJVUhMSDhBNnA6eUczVjJNWWpXbFNxRUVIRA==',
  'Cookie': 'incap_ses_769_2912339=0MXoIoExPnvBPiTYagqsCoksFWUAAAAAorjubdk1tDPQ2v9bqRSOEA==; visid_incap_2912339=tMvSoU2FSlGcFbdOKUrz7YcsFWUAAAAAQUIPAAAAAADYHgNoZxmr88bbBzbcxTmM'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)