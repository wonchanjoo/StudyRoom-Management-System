#subscribe

import time
import RPi.GPIO as GPIO 
import paho.mqtt.client as mqtt

motor = 26 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(motor, GPIO.OUT)

pwm = GPIO.PWM(motor, 50) 
pwm.start(1)

flag = False
def on_connect(client, userdata, flag, rc):
	client.subscribe("fan", qos=0)

def on_message(client, userdata, msg): 
	if int(msg.payload) == 0:
		controlServomotor(0) 
	elif int(msg.payload) == 1:
		controlServomotor(1)

def controlServomotor(n): 
	if n == 1:
		pwm.ChangeDutyCycle(10) 
		time.sleep(0.5) 
		pwm.ChangeDutyCycle(5)
		time.sleep(0.5) 
	else:
		pass

ip = "localhost"
client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 
client.connect(ip, 1883)

client.loop_forever()