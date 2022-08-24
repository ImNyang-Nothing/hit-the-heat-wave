import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# 40Pin SP1_SCLK
GPIO.setup(21, GPIO.IN)

try:
    while True:
        # 40Pin의 버튼에 대한 입력값
        inputIO = GPIO.input(21)

        # 버튼이 눌렸는지 체크
        if inputIO == False:
            # LED를 켜기
            print("SOS!")

        else:
            # LED를 끄기
            print("SOS STOP")

# Ctrl + C키를 누르면 종료 됩니다.
except KeyboardInterrupt:
    print("EXIT")

# GPIO 클린업
finally:
    GPIO.cleanup()