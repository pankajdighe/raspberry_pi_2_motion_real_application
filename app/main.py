import time
import paho.mqtt.client as mqtt
import random
import os
import RPi.GPIO as GPIO


mqttc=mqtt.Client()
mqttc.connect("iot.eclipse.org",1883,60)
mqttc.loop_start()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

#read temperature sfs
def read_motion_data():
	current_state = GPIO.input(11)
	if current_state == 1:
		result=1;
	else:
		print("PIR value is 0")
		result=0;
	return result

#publish temperature
while 1:
    t=read_motion_data()
    print "Publishing data"
    device_uuid=os.environ['RESIN_DEVICE_UUID'];
    print device_uuid
    (result,mid)=mqttc.publish("topic/GeneralizedIoT/"+str(device_uuid),t,2)
    time.sleep(1)

mqttc.loop_stop()
mqttc.disconnect()