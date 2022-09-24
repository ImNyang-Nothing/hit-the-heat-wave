import os; import time
import Adafruit_DHT
from senddm import send

def speak(text):
    os.system(f"./Files/speech.sh {text}")

sensor = Adafruit_DHT.DHT11     #  sensor 객체 생성

pin = 2                        # Data핀의 GPIO핀 넘버

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)   # 센서 객체에서 센서 값(ㅇ노도, 습도) 읽기

while True:
    if humidity is not None and temperature is not None:   #습도 및 온도 값이 모두 제대로 읽혔다면 
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))  # 온도, 습도 순으로 표시
        if temperature >= 30 and temperature <= 34:
            speak("실내온도가 높습니다. 냉방장치를 가동해주시고 수분 섭취를 충분히 하세요.")
            time.sleep(3600)

        elif temperature <= 34:
            speak("온열질환이 발생할 수 있습니다. 안전하게 시원한 장소로 이동해주세요.")
            time.sleep(1800)
        else:
            pass
    else:                                                  # 에러가 생겼다면 
        print('Failed to get reading. Try again!')        #  에러 표시
    time.sleep(60)
