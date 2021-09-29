import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
p1 = 25
p2 = 12
p3 = 16
I1 = 4
I2 = 27
GPIO.setup(p1, GPIO.OUT)
GPIO.setup(p2, GPIO.OUT)
GPIO.setup(p3, GPIO.OUT)

GPIO.setup(I1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(I2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

in1 = GPIO.input(I1)
in2 = GPIO.input(I2)

#pwm1 = GPIO.PWM(p1, 100)
#pwm2 = GPIO.PWM(p2, 100)

def myCallback(pin):

  if pin == I1:
    pwm = GPIO.PWM(p1, 100)
    pwm.start(0)

    for dc in range(101):
      pwm.ChangeDutyCycle(dc)
      sleep(0.01)
      if dc == 100:
        dc = 0
        for dc in range(101):
         pwm.ChangeDutyCycle(100 - dc)
         sleep(0.01) 
  if pin == I2:
    pwm = GPIO.PWM(p2, 100)
    pwm.start(0)

    for dc in range(101):
      pwm.ChangeDutyCycle(dc)
      sleep(0.01)
      if dc == 100:
        dc = 0
        for dc in range(101):
         pwm.ChangeDutyCycle(100 - dc)
         sleep(0.01) 



GPIO.add_event_detect(I1, GPIO.RISING, callback=myCallback, bouncetime=100)
GPIO.add_event_detect(I2, GPIO.RISING, callback=myCallback, bouncetime=100)




try:
    while 1:
            GPIO.output(p3,0)
            sleep(0.5)
            GPIO.output(p3,1)
            sleep(0.5)
except KeyboardInterrupt:
    print('\nExiting')
    GPIO.cleanup()