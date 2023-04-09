import time
import paho.mqtt.client as mqtt 
import circuit

def on_connect(client, userdata, flag, rc): 
	client.subscribe("led", qos=0)

def on_message(client, userdata, msg): 
	msg = msg.payload
	if msg == "ledOff":
		circuit.controlLED(0) 
	if msg == "ledOn":
		circuit.controlLED(1) 

broker_ip ="localhost"

client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message

client.connect(broker_ip, 1883) 
client.loop_start()

while(True):
	#switch publish
	if circuit.getBtnStatus(1) !=0: 
		client.publish("select", "1", qos=0) 
		imageFileName = myCamera.takePicture()
	if circuit.getBtnStatus(2) !=0: 
		client.publish("select", "2", qos=0)
	if circuit.getBtnStatus(3) !=0: 
		client.publish("select", "3", qos=0)

	#온도 publish
	temperature = circuit.getTemperature() 
	temperature =round(temperature, 1) 
	client.publish("temperature", temperature, qos=0) 

	#습도 publish
	humidity = circuit.getHumidity()
	humidity =round(humidity, 1) 
	client.publish("humidity", humidity, qos=0) 
	time.sleep(1.5)

client.loop_stop() 
client.disconnect()