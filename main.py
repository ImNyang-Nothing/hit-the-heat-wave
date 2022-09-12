import discord
import RPi.GPIO as GPIO
import datetime
import time
import tokenpython
import Adafruit_DHT
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)

def speak(text):
    os.system(f"./speech.sh {text}")

bot = discord.Bot()

sensor = Adafruit_DHT.DHT11
pin = 2
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
discord_id = [""]

class ResetButton(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="초기화", style=discord.ButtonStyle.primary, emoji="🔄") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("초기화 신호를 보냈습니다!") # Send a message when the button is clicked
        nonecount = 0

@bot.event
async def on_ready():
    print("Started Bot~")
# command hander
@bot.command()
async def show_status(ctx):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        await ctx.respond('온도={0:0.1f}*C  습도={1:0.1f}%'.format(temperature, humidity))
    else:
        await ctx.respond('문제가 발생했습니다. 잠시후 다시 시도해주세요!')

@bot.command()
async def show_sos(ctx):
    if nonecount != 10:
        await ctx.respond(f"💚 아직까진 안전합니다! 위험지수 : {nonecount}", view=ResetButton()) # Send a message with our View class that contains the button
    else:
        await ctx.respond(f"❤️ 현재 감지되고 있지 않습니다!!!!! 위험지수 : {nonecount}", view=ResetButton())

@bot.command()
async def test(ctx):
    speak("남현석")
    await ctx.respond("잘 들어보세요... 무슨 소리가 나지 않나요?")

bot.run(tokenpython.token)
