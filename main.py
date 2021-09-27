import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
p = 25
GPIO.setup(p, GPIO.OUT)

pwm = GPIO.PWM(p, 100)

try:
  pwm.start(0)
  while 1:
    for dc in range(101):
      pwm.ChangeDutyCycle(dc)
      sleep(0.01)
except KeyboardInterrupt:
  print('\nExiting')
