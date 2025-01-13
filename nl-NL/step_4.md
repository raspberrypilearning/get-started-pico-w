## Open een socket

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In deze stap gebruik je de verbinding met jouw WLAN om een socket te openen.
</div>
<div>
![MicroPython shell die de verbinding met een WLAN en een socketverbinding laat zien.](images/socket.png){:width="300px"}
</div>
</div>

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 10px;">
<div style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px; display:flex; margin-bottom: 27px;"><p><span style="color: #0faeb0">Een socket</span> is de manier waarop een **server** kan luisteren naar een **client** die verbinding met hem wil maken. De webpagina die je momenteel bekijkt, wordt gehost op servers van de Raspberry Pi Foundation. Deze servers hebben een open socket die wacht tot jouw webbrowser verbinding maakt. Op dat moment wordt de inhoud van de webpagina naar jouw computer verzonden. In dit geval is jouw server je Raspberry Pi Pico W en de client een webbrowser op een andere computer.</p>
</div>
</div>
</div>

Om een socket te openen, moet je het IP-adres en een poortnummer opgeven. Poortnummers worden door computers gebruikt om te identificeren waar verzoeken naartoe moeten worden verzonden. Zo wordt poort `80` normaal gesproken gebruikt voor webverkeer; Stardew Valley gebruikt poort `24642` wanneer je een multiplayer-spel speelt. Wanneer je een webserver instelt, gebruik je poort `80`.

\--- task ---

Maak een nieuwe functie die kan worden aangeroepen om een socket te openen. Begin met het toekennen van een IP-adres en een poortnummer aan de socket.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 35
line_highlights:
-----------------------------------------------------

def open_socket(ip):
\# Open een socket
adres = (ip, 80)

connect()

\--- /code ---

\--- /task ---

\--- task ---

Maak nu je socket aan en laat deze luisteren naar verzoeken op poort `80`. Vergeet niet om je functie onderaan je code aan te roepen.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 35
line_highlights: 38-41
-----------------------------------------------------------

def open_socket(ip):
\# Open een socket
adres = (ip, 80)
verbinding = socket.socket()
verbinding.bind(adres)
verbinding.listen(1)
print(verbinding)

ip = connect()
open_socket(ip)

\--- /code ---

\--- /task ---

\--- task ---

**Test:** Voer je code uit. Je zou dan een uitvoer moeten zien die er ongeveer zo uitziet.

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

`socket state=1` vertelt je dat je socket werkt.

\--- /task ---

\--- task ---

Vervang ten slotte `print` door een `return` en sla de geretourneerde socketverbinding op als een variabele.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 35
line_highlights: 41, 46
------------------------------------------------------------

def open_socket(ip):
\# Open een socket
adres = (ip, 80)
verbinding = socket.socket()
verbinding.bind(adres)
verbinding.listen(1)
return verbinding

ip = connect()
connection = open_socket(ip)

\--- /code ---

\--- /task ---

Je Raspberry Pi Pico W luistert nu naar verbindingen met zijn IP-adres op poort `80`. Dit betekent dat het klaar is om HTML-code te gaan weergeven, zodat een aangesloten webbrowser een webpagina kan zien.

\--- save ---
