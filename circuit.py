import time
import RPi.GPIO as GPIO
from adafruit_htu21d import HTU21D 
import busio

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

#LED 점등을 위한 전역 변수 선언 및 초기화
led =6
GPIO.setup(led, GPIO.OUT)

def controlLED(onOff): 
	GPIO.output(led, onOff)

#스위치
button1 =16
button2 =20
button3 =21
GPIO.setup(button1, GPIO.IN, GPIO.PUD_DOWN) 
GPIO.setup(button2, GPIO.IN, GPIO.PUD_DOWN) 
GPIO.setup(button3, GPIO.IN, GPIO.PUD_DOWN) 

#0눌리지않은상태 1눌린상태
def getBtnStatus(n): 
	if n ==1:
		return GPIO.input(button1) 
	elif n ==2:
		return GPIO.input(button2) 
	else:
		return GPIO.input(button3)

#온습도
sda =2 #GPIO핀 번호 
scl =3 #GPIO핀 번호
i2c = busio.I2C(scl, sda) 
sensor = HTU21D(i2c)

def getTemperature():
	return float(sensor.temperature)

def getHumidity():
	return float(sensor.relative_humidity)