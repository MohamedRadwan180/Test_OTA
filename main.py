# main.py

from ota import ota_update
from time import sleep
from machine import Pin

# Interval in seconds between OTA checks (e.g., every 24 hours)
OTA_CHECK_INTERVAL = 3 # 24 hours in seconds

# Main loop
while True:
    # Check for OTA updates
    print("Checking for OTA updates...")
    ota_update()
    
    # Add your main application logic below
    print("Running main program logic...")
    
    # Example of main application logic: blinking an LED (adjust this to your needs)
    led = Pin('LED', Pin.OUT)
    
    # Blink the LED as the main application logic
    for i in range(10):  # Blink 10 times
        led.toggle()
        sleep(4)  # Delay for 0.5 seconds

    # Sleep for OTA_CHECK_INTERVAL to avoid continuous checking
    print(f"Sleeping for {OTA_CHECK_INTERVAL} seconds before the next OTA check.")
    sleep(OTA_CHECK_INTERVAL)  # Sleep for the defined interval
