from machine import Pin
import time

led = Pin(2, Pin.OUT)  # GPIO2 is usually the built-in LED on ESP32

i = 2
while i:
    led.value(1)  # Turn LED ON
    time.sleep(1)  # Wait 1 second
    led.value(0)  # Turn LED OFF
    time.sleep(1)  # Wait 1 second
    i-=1

led.value(0)  # Turn LED OFF
