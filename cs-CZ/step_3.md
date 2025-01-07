## Connect your Raspberry Pi Pico W to a WLAN

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Here, you will learn to use MicroPython to connect your Raspberry Pi Pico W to a wireless local area network (WLAN), more commonly known as a WiFi network.
</div>
<div>
![MicroPython shell showing connection to a WLAN.](images/WiFi_connect.png){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Passwords</span> need to be kept securely and privately. In this step, you will add your WiFi password into your Python file. Make sure you don't share your file with anyone that you wouldn't want to tell your password to.</p>

To connect to a WiFi network, you will need to know your service set identifier (SSID). This is the name of your WiFi network. You will also need your WiFi password. These can usually be found written on your wireless router, although you should have changed the default password to something unique.

\--- task ---

In Thonny, import the packages you will need to connect to your WiFi network, read the onboard temperature sensor, and light the onboard light-emitting diode (LED).

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start:
line_highlights:
-----------------------------------------------------

import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
import rp2
import sys

\--- /code ---

Save this code now, and choose the option to save to **This computer**

\--- /task ---

\--- task ---

Next, set up your Raspberry Pi Pico W to use the onboard LED, and additionally add in the SSID and password for your network.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 9
line_highlights:
-----------------------------------------------------

ssid = 'NAME OF YOUR WIFI NETWORK'
password = 'YOUR SECRET PASSWORD'

\--- /code ---

\--- /task ---

\--- task ---

Now, begin to build a function to connect to your WLAN. You need to set up a `wlan` object, activate the wireless, and provide the object with your `ssid` and `password`.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights:
-----------------------------------------------------

def connect():
\#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

\--- /code ---

\--- /task ---

\--- task ---

If you've ever connected a device to a WiFi network, you will know that it doesn't happen instantly. Your device will send requests to your WiFi router to connect, and when the router responds, they will perform what is called a handshake to establish a connection. To do this with Python, you can set up a loop that will keep sending requests each second until the connection handshake has been performed.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 19-21
-----------------------------------------------------------

def connect():
\#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
print('Waiting for connection...')
sleep(1)

\--- /code ---

\--- /task ---

\--- task ---

Now print out your WLAN configuration, and test it all. You'll need to call your function. Keep all your function calls at the bottom of your file, so they are the last lines of code that are run.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 25, 22
------------------------------------------------------------

def connect():
\#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
print('Waiting for connection...')
sleep(1)
print(wlan.ifconfig())

connect()

\--- /code ---

\--- /task ---

\--- task ---

**Test:** Save and run your code. You should see some output in the shell that looks something like this, although the specific IP addresses will be different.

## --- code ---

language: python
filename:
line_numbers: false
line_number_start:
line_highlights:
-----------------------------------------------------

Waiting for connection...
Waiting for connection...
Waiting for connection...
Waiting for connection...
Waiting for connection...
('192.168.1.143', '255.255.255.0', '192.168.1.254', '192.168.1.254')

\--- /code ---

\--- /task ---

\--- collapse ---

---

## title: The Raspberry Pi Pico W won't connect

1. Make sure that you are using the correct SSID and password.
2. If you are on a school or work WLAN, unauthorised devices might not be permitted access to the WiFi.
3. Unplug your Raspberry Pi Pico W from your computer to power it off, then plug it back in. This can be a problem when you have connected once, and then try to connect again.

\--- /collapse ---

\--- task ---

You don't need all the information provided by `wlan.ifconfig()`. The key information you need is the IP address of the Raspberry Pi Pico W, which is the first piece of information. You can use an **fstring** to output the **IP address**. By placing an `f` in front of your string, variables can be printed when they are surrounded by `{}`.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 22, 23
------------------------------------------------------------

def connect():
\#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
print('Waiting for connection...')
sleep(1)
ip = wlan.ifconfig()[0]
print(f'Connected on {ip}')

connect()

\--- /code ---

\--- /task ---

\--- task ---

You can now return the value for the IP address of your Raspberry Pi Pico W, and store it when you call your function.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 23, 26
------------------------------------------------------------

def connect():
\#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
print('Waiting for connection...')
sleep(1)
print(f'Connected on {ip}')
return ip

ip = connect()

\--- /code ---

\--- /task ---

You might want to run this file without using Thonny, which will be covered later in this project. It would be useful to have some indication that the the Raspberry Pi Pico has connected to the WLAN, and also to be able to quit the program without having to have the Raspberry Pi Pico connected to a computer.

\--- task ---

Add a condition, where if the bootsel button is pressed, the program will quit.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 20, 21
------------------------------------------------------------

def connect():
\#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
if rp2.bootsel_button() == 1:
sys.exit()
print('Waiting for connection...')
ip = wlan.ifconfig()[0]
print(f'Connected on {ip}')
return ip

\--- /code ---

\--- /task ---

\--- task ---

Then make the onboard LED blink each time it attempts a connection, and then stay on once connected.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 23, 24, 25, 26, 29
------------------------------------------------------------------------

def connect():
\#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
if rp2.bootsel_button() == 1:
sys.exit()
print('Waiting for connection...')
pico_led.on()
sleep(0.5)
pico_led.off()
sleep(0.5)
ip = wlan.ifconfig()[0]
print(f'Connected on {ip}')
pico_led.on()
return ip

\--- /code ---

\--- /task ---

\--- save ---
