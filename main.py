import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
p1 = 25
p2 = 12
p3 = 16
I1 = 4
I2 = 27
GPIO.setup(p1, GPIO.OUT)

pwm = GPIO.PWM(p1, 100)

try:
  pwm.start(0)
  while 1:
    for dc in range(101):
        pwm.ChangeDutyCycle(dc)
        sleep(0.01)
        if dc == 100:
          dc = 0
          for dc in range(101):
           pwm.ChangeDutyCycle(100 - dc)
           sleep(0.01) 

except KeyboardInterrupt:
  print('\nExiting')
