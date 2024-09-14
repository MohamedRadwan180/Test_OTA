from machine import Pin
from time import sleep

# Initialize the built-in LED (Pin 'LED' on Raspberry Pi Pico)
led = Pin('LED', Pin.OUT)

print('Blinking LED Example')

# Infinite loop to toggle the LED on and off
while True:
    led.value(not led.value())  # Toggle the LED state
    sleep(0.5)  # Wait for 0.5 seconds