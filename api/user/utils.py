from ..settings import settings
import requests

ADMIN_NUMBER = settings.ADMIN_MOBILE
BASE_URL = settings.BASE_URL
API_TOKEN = settings.API_TOKEN
SENDER_ID = settings.SENDER_ID
URL_PATH = "api/v3/sms/send"


#send sms function
def send_sms(key:str,name:str):
    params = {
	"recipient":f"94{ADMIN_NUMBER}",
	"sender_id":SENDER_ID,
	"type":"plain",
	"message":f"TOKEN FOR {name} - {key}",
    }

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type" : "application/json",
        "Accept" : "application/json"
    }
    try:
        request = requests.post(url=BASE_URL+URL_PATH,json=params,headers=headers)
        result = request.json()
        if result["status"] == "success":
            return True
        return False
    except Exception:
        return False
