from telegram.ext import Updater
from telegram.ext import CommandHandler
import Adafruit_DHT
import os
import time
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT11
pin = 2
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
token = os.environ['TOKEN']
telegram_id = ["5745787280"]

# updater 
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

print("Started Bot~")
# command hander
def temphumidity(update, context):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        context.bot.send_message(chat_id=update.effective_chat.id, text='온도={0:0.1f}*C  습도={1:0.1f}%'.format(temperature, humidity))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="문제가 발생했습니다. 잠시후 다시 시도해주세요!")

def sos(update, context):
    for i in range(len[telegram_id]):
        context.bot.sendMessage(chat_id = telegram_id[i], text ="SOS 버튼이 감지되었습니다! 문제가 있는지 확인해주시길 바랍니다!")
    time.sleep(30)

def onButton(channel):
    if channel == 23:
        sos()

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(23, GPIO.FALLING, callback=onButton, bouncetime=1)
start_handler = CommandHandler('show_status', temphumidity)
dispatcher.add_handler(start_handler)

# polling
updater.start_polling()