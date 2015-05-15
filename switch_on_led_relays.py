import RPi.GPIO as GPIO

RELAY_PIN_1 = 18
RELAY_PIN_2 = 23
RELAY_PIN_3 = 24
RELAY_PIN_4 = 25

def main():

        print "starting relay init"
        
	GPIO.setmode(GPIO.BCM)

        #print "setting up relay1"
	#GPIO.setup(RELAY_PIN_1, GPIO.OUT)
        print "setting up relay2"
	GPIO.setup(RELAY_PIN_2, GPIO.OUT)
        print "setting up relay3"
	GPIO.setup(RELAY_PIN_3, GPIO.OUT)
        print "setting up relay4"
	GPIO.setup(RELAY_PIN_4, GPIO.OUT)

        #print "setting up relay1 to LOW"
	#GPIO.output(RELAY_PIN_1, GPIO.HIGH)
        print "setting up relay2 to LOW"
	GPIO.output(RELAY_PIN_2, GPIO.LOW)
        print "setting up relay3 to LOW"
	GPIO.output(RELAY_PIN_3, GPIO.LOW)
        print "setting up relay4 to LOW"
	GPIO.output(RELAY_PIN_4, GPIO.LOW)

        print "done setting up relays"

if __name__ == "__main__":
	main()
