## Connecter ton Raspberry Pi Pico W au WLAN

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ici, tu apprendras à utiliser MicroPython pour connecter ton Raspberry Pi Pico W à un réseau local sans fil (WLAN), plus communément appelé réseau WiFi.
</div>
<div>
![Shell MicroPython montrant la connexion à un réseau local sans fil.](images/WiFi_connect.png){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Les mots de passe</span> doivent être conservés de manière sécurisée et privée. Dans cette étape, tu vas ajouter ton mot de passe WiFi dans ton fichier Python. Assure-toi de ne pas partager ton fichier avec quelqu'un à qui tu ne voudrais pas communiquer ton mot de passe.</p>

Pour te connecter à un réseau WiFi, tu devras connaître ton identifiant de service (SSID). C'est le nom de ton réseau WiFi. Tu auras également besoin de ton mot de passe WiFi. Celui-ci se trouve généralement écrit sur ton routeur sans fil, même si tu aurais dû modifier le mot de passe par défaut en quelque chose d'unique.

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

Ensuite, configure ton Raspberry Pi Pico W pour utiliser la LED intégrée et ajoute également le SSID et le mot de passe de ton réseau.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 9
line_highlights:
-----------------------------------------------------

ssid = 'NOM DE TON RESEAU WIFI'
motdepasse = 'TON MOT DE PASSE SECRET'

\--- /code ---

\--- /task ---

\--- task ---

Maintenant, commence à créer une fonction pour te connecter à ton WLAN. Tu dois configurer un objet `wlan`, activer le réseau sans fil et fournir à l'objet ton `ssid` et ton `mot de passe`.

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

Si tu as déjà connecté un appareil à un réseau Wi-Fi, tu sais que cela ne se produit pas instantanément. Ton appareil enverra des demandes à ton routeur WiFi pour se connecter, et lorsque le routeur répondra, ils effectueront ce que l'on appelle une liaison (handshake) pour établir une connexion. Pour ce faire avec Python, tu peux configurer une boucle qui continuera d'envoyer des requêtes chaque seconde jusqu'à ce que la liaison ait été effectuée.

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

Imprime maintenant ta configuration WLAN et teste-la. Tu devras appeler ta fonction. Garde tous tes appels de fonction au bas de ton fichier, de sorte qu'ils soient les dernières lignes de code à être exécutées.

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

**Test :** enregistre et exécute ton code. Tu devrais voir une sortie dans le shell qui ressemble à ceci, bien que les adresses IP spécifiques soient différentes.

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

## title: Le Raspberry Pi Pico W ne se connecte pas

1. Assure-toi d'utiliser le bon SSID et le bon mot de passe.
2. Si tu es dans une école ou sur un lieu de travail, il se peut que les appareils non autorisés ne soient pas autorisés à accéder au WiFi.
3. Débranche ton Raspberry Pi Pico W de ton ordinateur pour l'éteindre, puis rebranche-le. Cela peut poser un problème lorsque tu t'es connecté une fois et que tu essaies de te connecter à nouveau.

\--- /collapse ---

\--- task ---

Tu n'as pas besoin de toutes les informations fournies par `wlan.ifconfig()`. L’information clé dont tu as besoin est l’adresse IP du Raspberry Pi Pico W, qui est la première information. Tu peux utiliser une **fstring** pour afficher l'**adresse IP**. En plaçant un `f` devant ta chaîne, les variables peuvent être imprimées quand elles sont entourées de `{}`.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 22, 23
------------------------------------------------------------

def connect():
\#Se connecter au WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, motdepasse)
while wlan.isconnected() == False:
print('En attente de connexion...')
sleep(1)
ip = wlan.ifconfig()[0]
print(f'Connected on {ip}')

connect()

\--- /code ---

\--- /task ---

\--- task ---

Tu peux maintenant renvoyer la valeur pour l'adresse IP de ton Raspberry Pi Pico W, et la stocker quand tu appelles ta fonction.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 23, 26
------------------------------------------------------------

def connect():
\#Se connecter au WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, motdepasse)
while wlan.isconnected() == False:
print('En attente de connexion...')
sleep(1)
print(f'Connecté sur {ip}')
return ip

ip = connect()

\--- /code ---

\--- /task ---

Tu souhaiteras peut-être exécuter ce fichier sans utiliser Thonny, ce qui sera abordé plus tard dans ce projet. Il serait utile d'avoir une indication que le Raspberry Pi Pico est connecté au WLAN, et également de pouvoir quitter le programme sans avoir à connecter le Raspberry Pi Pico à un ordinateur.

\--- task ---

Ajoute une condition, où si le bouton bootsel est enfoncé, le programme se fermera.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 20, 21
------------------------------------------------------------

def connect():
\#Se connecter au WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, motdepasse)
while wlan.isconnected() == False:
if rp2.bootsel_button() == 1:
sys.exit()
print('En attente de connexion...')
ip = wlan.ifconfig()[0]
print(f'Connecté sur {ip}')
return ip

\--- /code ---

\--- /task ---

\--- task ---

Ensuite, fais clignoter la LED intégrée à chaque tentative de connexion, puis rester allumée une fois connectée.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 14
line_highlights: 23, 24, 25, 26, 29
------------------------------------------------------------------------

def connect():
\#Se connecter au WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, motdepasse)
while wlan.isconnected() == False:
if rp2.bootsel_button() == 1:
sys.exit()
print('En attente de connexion...')
pico_led.on()
sleep(0.5)
pico_led.off()
sleep(0.5)
ip = wlan.ifconfig()[0]
print(f'Connecté sur {ip}')
pico_led.on()
return ip

\--- /code ---

\--- /task ---

\--- save ---
