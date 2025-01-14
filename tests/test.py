import requests

def send_sms(phone_number,message):
    api_key = "e304cd3d0deca82bac6d856ba70f70d5530d9ff9b966ccc5"
    url = "https://api.smsmobileapi.com/sendsms/"
    payload = {
    "recipients": f"{phone_number}",
    "message": f"{message}",
    "apikey": f"{api_key}"
    }

    response = requests.post(url, data=payload)

    print(response.text)

send_sms('9877034346','hello this is from the django api to ravi')