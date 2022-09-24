import discord; from discord.ext import tasks; import asyncio
import RPi.GPIO as GPIO; import Adafruit_DHT
import datetime; import time
import os
import tokenpython

def speak(text):
    os.system(f"./Files/speech.sh {text}")

bot = discord.Bot()

temperature_humidity_pin = 2
pir_pin = 21

sensor = Adafruit_DHT.DHT11
humidity, temperature = Adafruit_DHT.read_retry(sensor, temperature_humidity_pin)

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
GPIO.setup(pir_pin, GPIO.IN, GPIO.PUD_UP)
# 몇가지 리스트나 변수 선언
discord_id = [""] # 디스코드 ID 받을려고 만들어둔 리스트 DB나 JSON으로 교체할 가능성 있음
Truecount = 0 # Truecount를 0으로 선언 (10초마다 pir 센서가 감지할 경우 1씩 추가, Falsecount는 그 반대로 작동한다.)
Falsecount = 0 # Falsecount를 0으로 선언 (위에서 설명)

#초기화 버튼(Discord 프로그램에서) 선언
class ResetButton(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="초기화", style=discord.ButtonStyle.primary, emoji="🔄") # "🔄 초기화"라고 써진 남색 버튼 표시
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("초기화 신호를 보냈습니다!") # 초기화 신호 보내기
        TrueCount = 0
        Falsecount = 0

# 아래부터 Event 처리

@bot.event
async def on_ready():
    print("Started Bot~")
    count_pir_status()

# 아래부터 커맨드 처리
# show_status로 보호자가 현재 노인의 집 온습도 정보를 요청할 경우... 
@bot.command(description="show_status로 현재 노인의 집 온습도 정보를 요청합니다.")
async def show_status(ctx):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, temperature_humidity_pin) # humidity에는 습도를 temperature에는 온도를 변수에 저장한다. 이때 변수에 들어갈 값은 온습도 센서의 값을 읽어 처리한다.
    if humidity != None and temperature != None:    await ctx.respond(f'온도={temperature}*C  습도={humidity}%') # 만약 humidity와 temperature가 비어있지 않다면 '온도={temperature}*C  습도={humidity}%' format 형식으로 변수와 str을 보호자에게 전송한다.
    else:   await ctx.respond('문제가 발생했습니다. 잠시후 다시 시도해주세요!') # 위 조건문이 맞지 않는다면 '문제가 발생했습니다. 잠시후 다시 시도해주세요!'를 보호자에게 전송한다.

# show_sos로 보호자가 현재 노인의 위험지수 정보를 요청할 경우...
@bot.command()
async def show_sos(ctx):
    if Falsecount >= Truecount:
        await ctx.respond(f"💚 아직까진 안전합니다! 위험지수 : {Falsecount}/{Truecount}", view=ResetButton()) # Send a message with our View class that contains the button
    else:
        await ctx.respond(f"❤️ 현재 감지되고 있지 않습니다!!!!! 안전한지 확인해주시길 바랍니다! 위험지수 : {Falsecount}/{Truecount}", view=ResetButton())

bot.run(tokenpython.token) # 봇 작동을 위한 tokenpython.py에서 token 스트링 변수 가져오기