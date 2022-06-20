## Connect Raspberry Pi Pico to a WLAN

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Here you will learn to use MicroPython to connect Raspberry Pi Pico to a Wireless Local Area Network (WLAN)
</div>
<div>
![MicroPython shell showing connection to a WLAN](images/WiFi_connect.png){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Passwords</span> need to be kept securely and privately. In this step you will add your Wi-Fi password into your Python file. Make sure you don't share your file with anyone that you wouldn't want to tell your password to.</p>

To connect to a WLAN, you will need to know your Service Set Identifier (SSID) and your Wi-Fi password. These can usually be found written on your wireless router, although you should have changed the default password to something unique.

--- task ---

In Thonny you can import the packages you will need to connect to your Wi-Fi network, read the onboard temperature sensor and light the onboard LED.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 
line_highlights: 
---
import network
import socket
from time import sleep
from picozero import pico_temp_sensor
from machine import Pin
--- /code ---

--- /task ---

--- task ---

Next you can set up Raspberry Pi Pico to use the onboard LED, and additionally add in the SSID and password for your network.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 7
line_highlights: 
---
led = Pin("LED", machine.Pin.OUT)
ssid = 'NAME OF YOUR WIFI NETWORK'
password = 'YOUR SECRET PASSWORD'
--- /code ---

--- /task ---

--- task ---

Now you can begin to build a function to connect to your WLAN. You need to set up a `wlan` object, activate the wireless functionality and provide the object with your `ssid` and `password`.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 12
line_highlights: 
---
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

--- /code ---

--- /task ---

--- task ---

If you've ever connected a device to a WLAN, you will know that it doesn't happen instantly. Your device will send requests to your Wi-Fi router to connect, and when the router responds they will perform what is called a handshake to establish a connection. To do this with Python, you can set up a loop that will keep sending requests each second until the connection handshake has been performed.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 12
line_highlights: 17-19
---
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
--- /code ---

--- /task ---

--- task ---

You can now print out your WLAN configuration, and test it all. You'll need to call your function. Keep all your function calls at the bottom of your file, so they are the last lines of code that are run. Because the Wi-Fi connection can stay up, even when you stop the code, you can add a `try`/`except` that will reset Raspberry Pi Pico when the script is stopped.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 
line_highlights: 20, 23
---
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())

try:    
    connect()
except KeyboardInterrupt:
        machine.reset()
--- /code ---

--- /task ---

--- task ---

Save and run your code, and you should see some output in the shell that looks something like this, although the specific IP addresses will be different.

--- code ---
---
language: python
filename: 
line_numbers: false
line_number_start: 
line_highlights: 
---
>>> %Run -c $EDITOR_CONTENT
Waiting for connection...
Waiting for connection...
Waiting for connection...
Waiting for connection...
Waiting for connection...
('192.168.1.143', '255.255.255.0', '192.168.1.254', '192.168.1.254')
--- /code ---

--- /task ---

--- collapse ---
---
title: Debug: Raspberry Pi Pico won't connect.
---
1. Make sure that you are using the correct SSID and password.
2. If you are on a school or work WLAN, unauthorised devices might not be permitted access to the Wi-Fi
3. Unplug your Raspberry Pi Pico from your computer to power it off, then plug it back in. This can be a problem when you have connected once, and then try and connect again.

--- /collapse ---

--- task ---

You don't need all the information provided by `wlan.ifconfig()`. The key information you need is the IP address of Raspberry Pi Pico, which is the first piece of information.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 12
line_highlights: 20-21
---
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    

try:
    connect()
except KeyboardInterrupt:
        machine.reset()
--- /code ---

--- /task ---

--- task ---

You can now return the value for the IP address of your Raspberry Pi Pico, and store it when you call your function.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 12
line_highlights: 20-21
---
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    

try:
    ip = connect()
except KeyboardInterrupt:
        machine.reset()
--- /code ---

--- /task ---

--- save ---