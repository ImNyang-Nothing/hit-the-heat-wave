import discord
import Adafruit_DHT
import os
import time
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT11
pin = 2
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
user_id = []

bot = discord.Bot()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for i in range(len(user_id)):
        user = await bot.fetch_user(user_id[i])
        await user.send("✅ㅣ봇이 준비되었습니다!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="슬커로 알아보세요!"))

@bot.slash_command()
async def 온습도_측정(ctx):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        await ctx.respond('온도={0:0.1f}*C  습도={1:0.1f}%'.format(temperature, humidity))
    else:
        await ctx.respond("문제가 발생했습니다. 잠시후 다시 시도해주세요!")

bot.run(str(os.getenv('TOKEN')))
