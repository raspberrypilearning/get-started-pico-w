## Ouvrir un socket

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Dans cette étape, tu utiliseras la connexion à ton WLAN pour ouvrir un socket.
</div>
<div>
![shell MicroPython montrant la connexion au WLAN et une connexion à un socket
.](images/socket.png){:width="300px"}
</div>
</div>

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 10px;">
<div style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px; display:flex; margin-bottom: 27px;"><p><span style="color: #0faeb0">Un socket</span> est la façon dont un **serveur** peut écouter un **client** qui veut s'y connecter. La page web que tu regardes actuellement est hébergée sur les serveurs de la Raspberry Pi Foundation. Ces serveurs disposent d'un socket ouvert qui attend que ton navigateur web établisse une connexion, moment auquel le contenu de la page web est envoyé à ton ordinateur. Dans ce cas, ton serveur sera ton Raspberry Pi Pico W et le client sera un navigateur web sur un autre ordinateur.</p>
</div>
</div>
</div>

Pour ouvrir un socket, tu dois fournir l'adresse IP et le numéro de port. Les numéros de port sont utilisés par les ordinateurs pour identifier où les requêtes doivent être envoyées. Par exemple, le port `80` est normalement utilisé pour le trafic web ; Stardew Valley utilise le port `24642` lorsque tu joues à un jeu multijoueur. Comme tu configures un serveur web, tu utiliseras le port `80`.

\--- task ---

Crée une nouvelle fonction qui peut être appelée pour ouvrir un socket. Commence par donner au socket une adresse IP et un numéro de port.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 35
line_highlights:
-----------------------------------------------------

def open_socket(ip):
\# Ouvrir un socket
adresse = (ip, 80)

connect()

\--- /code ---

\--- /task ---

\--- task ---

Maintenant, crée ton socket, puis fais-le écouter sur le port `80`. N'oublie pas d'appeler ta fonction en bas de ton code.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 35
line_highlights: 38-41
-----------------------------------------------------------

def open_socket(ip):
\# Ouvrir un socket
adresse = (ip, 80)
connexion = socket.socket()
connection.bind(adresse)
connection.listen(1)
print(connexion)

ip = connect()
open_socket(ip)

\--- /code ---

\--- /task ---

\--- task ---

**Test :** exécute ton code, et tu devrais voir une sortie qui ressemble à ça.

## --- code ---

language: python
filename:
line_numbers: false
line_number_start:
line_highlights:
-----------------------------------------------------

> > > %Run -c $EDITOR_CONTENT
> > > Waiting for connection...
> > > Waiting for connection...
> > > Waiting for connection...
> > > Waiting for connection...
> > > Waiting for connection...
> > > Connected on 192.168.1.143
> > >
> > > <socket state=1 timeout=-1 incoming=0 off=0>

\--- /code ---

`socket state=1` t'indique que ton socket fonctionne.

\--- /task ---

\--- task ---

Enfin, remplace ton `print` par un `return` et stocke la connexion de socket renvoyée en tant que variable.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 35
line_highlights: 41, 46
------------------------------------------------------------

def open_socket(ip):
\# Ouvrir un socket
adresse = (ip, 80)
connexion = socket.socket()
connexion.bind(adresse)
connexion.listen(1)
return connexion

ip = connect()
connection = open_socket(ip)

\--- /code ---

\--- /task ---

Tu as maintenant ton Raspberry Pi Pico W à l'écoute des connexions à son adresse IP sur le port `80`. Cela signifie qu'il est prêt à commencer à diffuser du code HTML, afin qu'un navigateur web connecté puisse voir une page web.

\--- save ---
