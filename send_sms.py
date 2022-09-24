import os; import time
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "SID"
auth_token = "TOKEN"
client = Client(account_sid, auth_token)

Truecount = 0 # Truecount를 0으로 선언 (10초마다 pir 센서가 감지할 경우 1씩 추가, Falsecount는 그 반대로 작동한다.)
Falsecount = 0 # Falsecount를 0으로 선언 (위에서 설명)
while True:
    if Truecount <= Falsecount:
    if GPIO.input(pir_pin) == GPIO.LOW:
        print("Motion detected!")
        Truecount += 1
    else:
        print("No motion")
        Falsecount +=1
    time.sleep(7200)
