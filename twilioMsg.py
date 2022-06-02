# -*- coding: utf-8 -*-
"""
Created on Sat May 28 02:45:55 2022

@author: asus
"""

from twilio.rest import Client
from datetime import datetime

def sendMsg(name):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msg = name + " has been spotted at " + current_time + " in live cam "
    account_sid = "YOUR_TWILIO_ACCOUNT_SID"
    auth_token  = "YOUR_TWILIO_AUTH_TOKEN"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+91 YOUR_PHONE_NUMBER", 
        from_="TWILIO_PHONE_NUMBER",
        body= msg)
    
    print(message.sid)

