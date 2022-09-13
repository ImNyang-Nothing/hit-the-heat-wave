import time
import Adafruit_DHT
import tkinter as tkall
import tkinter.font as tkFont
from tkinter import *

root = Tk()

root.title("온도 표시중!")
root.geometry("800x480+0+0")
root.resizable(False, False)

sensor = Adafruit_DHT.DHT11
temperature_humidity_pin = 2

fontStyle = tkFont.Font(family="NanumGothic", size=50)

h, t = Adafruit_DHT.read_retry(sensor, temperature_humidity_pin)
if h is not None and t is not None :
    labeltemp = tkall.Label(root, text=f"온도 : {t}℃", font=fontStyle)
    labelhumidity = tkall.Label(root, text=f"습도 : {h}%", font=fontStyle)
else :
    pass 

labeltemp.place(relx=0.5, rely=0.3, anchor=CENTER)
labelhumidity.place(relx=0.5, rely=0.7, anchor=CENTER)

root.attributes('-fullscreen', True)

root.mainloop()
while True:
    labeltemp = tkall.Label(root, text=f"온도 : {t}℃", font=fontStyle)
    labelhumidity = tkall.Label(root, text=f"습도 : {h}%", font=fontStyle)
    root.update()
