import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#top
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.LOW)
#bottom
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,GPIO.LOW)
#right
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
#left
GPIO.setup(27,GPIO.OUT)
GPIO.output(27,GPIO.LOW)
