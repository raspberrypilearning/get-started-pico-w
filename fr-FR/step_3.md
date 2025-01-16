## Connecter ton Raspberry Pi Pico W à un réseau Wi-Fi

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ici, tu apprendras à utiliser MicroPython pour connecter ton Raspberry Pi Pico W à un réseau local sans fil (WLAN), plus communément appelé réseau WiFi.
</div>
<div>
![Shell MicroPython montrant la connexion à un réseau local sans fil.](images/WiFi_connect.png){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Les mots de passe</span> doivent être conservés de manière sécurisée et privée. Dans cette étape, tu vas ajouter ton mot de passe WiFi dans ton fichier Python. Assure-toi de ne pas partager ton fichier avec quelqu'un à qui tu ne voudrais pas communiquer ton mot de passe.</p>

Pour te connecter à un réseau WiFi, tu devras connaître ton identifiant de service (SSID). C'est le nom de ton réseau WiFi. Tu auras également besoin de ton mot de passe WiFi. Ils peuvent généralement être trouvés écrits sur ton routeur sans fil, bien que tu aurais dû changer le mot de passe par défaut en quelque chose d'unique.

\--- task ---

Dans Thonny, importe les paquets dont tu auras besoin pour te connecter à ton réseau WiFi, lire le capteur de température embarqué et allumer la diode électroluminescente (LED) embarquée.

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

Enregistre ce code maintenant et choisis l'option à enregistrer sur **cet ordinateur**

\--- /task ---

\--- task ---

Ensuite, configure ton Raspberry Pi Pico W pour utiliser la LED intégrée et ajoute également le SSID et le mot de passe de ton réseau.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 9
line_highlights:
-----------------------------------------------------

ssid = 'NOM DE TON RESEAU WIFI
motdepasse = 'TON MOT DE PASSE SECRET'

\--- /code ---

\--- /task ---

\--- task ---

Maintenant, commence à créer une fonction pour te connecter à ton WLAN. Tu dois configurer un objet « wlan », activer le réseau sans fil et fournir à l'objet ton « ssid » et ton « mot de passe ».

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights:
-----------------------------------------------------

def connect():
\#Se connecter au WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, motdepasse)

\--- /code ---

\--- /task ---

\--- task ---

Si tu as déjà connecté un appareil à un réseau Wi-Fi, tu sais que cela ne se produit pas instantanément. Ton appareil enverra des demandes à ton routeur WiFi pour se connecter, et lorsque le routeur répondra, ils effectueront ce que l'on appelle une poignée de main (handshake) pour établir une connexion. Pour ce faire avec Python, tu peux configurer une boucle qui continuera d'envoyer des requêtes chaque seconde jusqu'à ce que la liaison ait été effectuée.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 19-21
-----------------------------------------------------------

def connect():
\#Se connecter au WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, motdepasse)
while wlan.isconnected() == False:
print('En attente de connexion...')
sleep(1)

\--- /code ---

\--- /task ---

\--- task ---

Imprime maintenant ta configuration WLAN et teste-la. Tu devras appeler ta fonction. Garde tous tes appels de fonctions en bas de ton fichier, donc ce sont les dernières lignes de code qui sont exécutées.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 25, 22
------------------------------------------------------------

def connect():
\#Se connecter au WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, motdepasse)
while wlan.isconnected() == False:
print('En attente de connexion...')
sleep(1)
print(wlan.ifconfig())

connect()

\--- /code ---

\--- /task ---

\--- task ---

**Test :** Sauvegarde et exécute ton code. Tu devrais voir une sortie dans le shell qui ressemble à ceci, bien que les adresses IP spécifiques soient différentes.

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
En attente de connexion ...
Waiting for connection...
('192.168.1.143', '255.255.255.0', '192.168.1.254', '192.168.1.254')

\--- /code ---

\--- /task ---

\--- collapse ---

---

## title: Le Raspberry Pi Pico W ne se connecte pas

1. Assure-toi d'utiliser le SSID et le mot de passe corrects.
2. Si tu es dans une école ou sur un lieu de travail, il se peut que les appareils non autorisés ne soient pas autorisés à accéder au WiFi.
3. Débranche ton Raspberry Pi Pico W de ton ordinateur pour l'éteindre, puis rebranche-le. Cela peut être un problème lorsque tu t'es connecté une fois, puis essaie de te connecter à nouveau.

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
