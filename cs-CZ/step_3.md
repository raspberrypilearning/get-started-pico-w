## Připoj Raspberry Pi Pico W k WLAN síti

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Zde se naučíš používat MicroPython k připojení Raspberry Pi Pico W k bezdrátové lokální síti (WLAN), častěji známá jako WiFi síť.
</div>
<div>
![Shell MicroPythonu zobrazující připojení k WLAN.](images/WiFi_connect.png){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Hesla</span> je třeba uchovávat bezpečně a v soukromí. V tomto kroku přidáš heslo k WiFi do souboru Pythonu. Ujisti se, že svůj soubor nesdílíš s nikým, komu nechceš sdělit své heslo.</p>

Chceš-li se připojit k síti WiFi, musíš znát identifikátor své služby (SSID). Toto je název WiFi sítě. Také budeš potřebovat heslo k WiFi. Tyto kódy obvykle najdeš napsané na bezdrátovém routeru, i když byste měli změnit výchozí heslo na něco jedinečného.

\--- task ---

V Thonny importuješ balíčky, které budeš potřebovat pro připojení k WiFi síti, načtení integrovaného teplotního senzoru a rozsvícení integrované LED diody.

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

Ulož si tento kód a vyber možnost uložení do **Tento počítač**

\--- /task ---

\--- task ---

Dále nastav Raspberry Pi Pico W tak, aby používalo integrovanou LED diodu, a navíc přidej SSID a heslo pro vaši síť.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 9
line_highlights:
-----------------------------------------------------

ssid = 'NÁZEV VAŠÍ WIFI SÍTĚ'
password = 'VAŠE TAJNÉ HESLO'

\--- /code ---

\--- /task ---

\--- task ---

Nyní začni vytvářet funkci pro připojení k vaší WLAN síti. Je třeba nastavit objekt `wlan`, aktivovat bezdrátové připojení a poskytnout objektu vaše `ssid` a `password`.

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

Pokud jsi někdy připojil zařízení k síti WiFi, budeš vědět, že se to nestane okamžitě. Tvé zařízení bude odesílat žádosti na WiFi router pro připojení a po odpovědi routeru, vykoná to, čemu se říká ruční zatřesení, aby navázaly spojení. Abys toho v Pythonu dosáhl, můžete nastavit smyčku, která bude odesílat požadavky každou sekundu, dokud nebude provedeno navázání spojení.

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

Nyní si vytiskni konfiguraci WLAN a vše otestuj. You'll need to call your function. Keep all your function calls at the bottom of your file, so they are the last lines of code that are run.

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
