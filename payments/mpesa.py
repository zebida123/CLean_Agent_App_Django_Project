import base64, requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
from datetime import datetime

def get_access_token():
    r = requests.get(settings.MPESA_OAUTH_URL, auth=HTTPBasicAuth(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET))
    r.raise_for_status()
    return r.json().get('access_token')

def generate_password(shortcode, passkey, timestamp):
    s = shortcode + passkey + timestamp
    return base64.b64encode(s.encode()).decode()

def initiate_stk_push(phone, amount):
    token = get_access_token()
    api = settings.MPESA_STK_PUSH_URL
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = generate_password(settings.MPESA_SHORTCODE, settings.MPESA_PASSKEY, timestamp)
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": int(amount),
        "PartyA": phone,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone,
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": "CleanAgent",
        "TransactionDesc": "Payment"
    }
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.post(api, json=payload, headers=headers)
    r.raise_for_status()
    return r.json()
