## Anslut din Raspberry Pi Pico W till ett WLAN

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Här kommer du att lära dig att använda MicroPython för att ansluta din Raspberry Pi Pico W till ett trådlöst lokalt nätverk (WLAN), mer känt som ett WiFi-nätverk.
</div>
<div>
![MicroPython-skal som visar anslutning till ett WLAN.](images/WiFi_connect.png){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Lösenord</span> måste förvaras säkert och privat. I det här steget lägger du till ditt WiFi-lösenord i din Python-fil. Se till att du inte delar din fil med någon som du inte vill berätta ditt lösenord för.</p>

För att ansluta till ett WiFi-nätverk måste du känna till din nätverksnamn (SSID). Detta är namnet på ditt WiFi-nätverk. Du behöver också ditt WiFi-lösenord. Dessa kan vanligtvis hittas skrivna på din trådlösa router, även om du borde ha ändrat standardlösenordet till något unikt.

\--- task ---

I Thonny importerar du paketen du behöver för att ansluta till ditt WiFi-nätverk, läser den inbyggda temperatursensorn och tänder den inbyggda lysdioden (LED).

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
\--- /code ---

Spara den här koden nu och välj alternativet att spara till **This computer**
\--- /task ---

\--- task ---

Ställ sedan in din Raspberry Pi Pico W för att använda den inbyggda lysdioden och lägg till SSID och lösenord för ditt nätverk.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 7
line_highlights:
-----------------------------------------------------

ssid = 'NAMN PÅ DITT WIFI-NÄTVERK'
password = 'DITT HEMLIGA LÖSENORD'
\--- /code ---

\--- /task ---

\--- task ---

Börja nu att bygga en funktion för att ansluta till ditt WLAN. Du måste ställa in ett `wlan`-objekt, aktivera det trådlösa och förse objektet med ditt `ssid` och `lösenord`.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 12
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

Om du har anslutit en enhet till ett WiFi-nätverk tidigare så vet du att det tar lite tid. Din enhet kommer att skicka förfrågningar till din WiFi-router om att ansluta, och när routern svarar kommer de att utföra vad som kallas en handskakning för att upprätta en anslutning. För att göra detta med Python kan du ställa in en loop som fortsätter att skicka förfrågningar varje sekund tills anslutningshandskakningen har utförts.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 12
line_highlights: 17-19
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

Skriv nu ut din WLAN-konfiguration och testa allt. Du måste anropa din funktion. Behåll alla dina funktionsanrop längst ner i filen, så att de är de sista kodraderna som körs.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 12
line_highlights: 22-25
-----------------------------------------------------------

def connect():
\#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
print('Waiting for connection...')
sleep(1)
print(wlan.ifconfig())

try:\
connect()
except KeyboardInterrupt:
machine.reset()
\--- /code ---

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

## --- collapse ---

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
