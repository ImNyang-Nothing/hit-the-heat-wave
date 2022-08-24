from telegram.ext import Updater
from telegram.ext import CommandHandler
import Adafruit_DHT
import os

sensor = Adafruit_DHT.DHT11
pin = 2
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
token = os.environ['TOKEN']

# updater 
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


# command hander
def 온도(update, context):    
    if humidity is not None and temperature is not None:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="문제가 발생했습니다. 잠시후 다시 시도해주세요!")

start_handler = CommandHandler('온도', 온도)
dispatcher.add_handler(start_handler)

# polling
updater.start_polling()