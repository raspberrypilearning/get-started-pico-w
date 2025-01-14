## Bedien je webpagina

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In deze stap start je jouw webserver op, zodat een client er verbinding mee kan maken, jouw LED kan bedienen en de temperatuur kan aflezen.
</div>
<div>
![Schermafbeelding van Chrome met een webpagina met twee knoppen om een LED aan en uit te zetten.](images/web_light_on.png)
</div>
</div>

\--- task ---

Maak een functie die jouw webserver start, met behulp van het `verbinding`-object dat je als parameter hebt opgeslagen. De variabelen `status` en `temperatuur` moeten worden ingevuld voor jouw HTML-gegevens. De status staat in eerste instantie op `UIT` en de temperatuur op `0`. Dit betekent dat je er ook voor moet zorgen dat de LED uit is wanneer de server start.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 66
line_highlights:
-----------------------------------------------------

def serve(verbinding):
\#Start een webserver
status = 'UIT'
pico_led.off()
temperatuur = 0

\--- /code ---

\--- /task ---

Wanneer je webbrowser vraagt om een verbinding met jouw Raspberry Pi Pico W, moet de verbinding worden geaccepteerd. Daarna moeten de gegevens die door je webbrowser worden verzonden, in specifieke stukken worden verdeeld (in dit geval 1024 bytes). Je moet ook weten welk verzoek je webbrowser doet: vraagt hij om een eenvoudige pagina? Vraagt het om een pagina die niet bestaat?

\--- task ---

Je wilt dat de webserver altijd actief is en luistert, zodat elke client er verbinding mee kan maken. Je kunt dit doen door een `while True:`-lus toe te voegen. Voeg deze vijf regels code toe zodat je een verzoek kunt accepteren en `print()` om te zien wat het verzoek was. Voeg een aanroep toe aan jouw `serve`-functie in je aanroepen onderaan je code.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 66
line_highlights: 71-76, 81
---------------------------------------------------------------

def serve(verbinding):
\#Start een webserver
status = 'UIT'
pico_led.off()
temperatuur = 0
while True:
client = verbinding.accept()[0]
verzoek = client.recv(1024)
verzoek = str(verzoek)
print(verzoek)
client.close()

ip = connect()
connection = open_socket(ip)
serve(connection)

\--- /code ---

\--- /task ---

**Test:** Start je programma en typ vervolgens het IP-adres in de adresbalk van een webbrowser op jouw computer.

![Een browseradresbalk met het IP-adres van de Pico ingetypt.](images/browser_ip.png)

You should see something like this in the shell output in Thonny.

```python
>>> %Run -c $EDITOR_CONTENT
Waiting for connection...
Waiting for connection...
Waiting for connection...
Connected on 192.168.1.143
b'GET / HTTP/1.1\r\nHost: 192.168.1.143\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-GB,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
b'GET /favicon.ico HTTP/1.1\r\nHost: 192.168.1.143\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0\r\nAccept: image/avif,image/webp,*/*\r\nAccept-Language: en-GB,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nReferer: http://192.168.1.143/\r\n\r\n'
```

\--- task ---

Next, you need to send the HTML code you have written to the client web browser.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 66
line_highlights: 76, 77
------------------------------------------------------------

def serve(connection):
\#Start a web server
state = 'ON'
pico_led.on()
temperature = 0
while True:
client = connection.accept()[0]
request = client.recv(1024)
request = str(request)
print(request)
html = webpage(temperature, state)
client.send(html)
client.close()

ip = connect()
connection = open_socket(ip)
serve(connection)

\--- /code ---

\--- /task ---

\--- task ---

Refresh your page when you've run the code again. Click on the buttons that are displayed. In Thonny, you should then see that there are two different outputs from your shell.

```python
b'GET /lighton? HTTP/1.1\r\nHost: 192.168.1.143\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-GB,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nReferer: http://192.168.1.143/\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
```

and

```python
b'GET /lightoff? HTTP/1.1\r\nHost: 192.168.1.143\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-GB,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nReferer: http://192.168.1.143/lighton?\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
```

\--- /task ---

Notice that you have `/lighton?`, `lightoff?`, and `close?` in the requests. These can be used to control the onboard LED of your Raspberry Pi Pico W and close your server.

\--- task ---

Split the request string and then fetch the first item in the list. Sometimes the request string might not be able to be split, so it's best to handle this in a `try`/`except`.

If the first item in the split is `lighton?` then you can switch the LED on. If it is `lightoff?` then you can switch the LED off. If it is `close?` you can perform a `sys.exit()`

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 66
line_highlights: 75-85
-----------------------------------------------------------

def serve(connection):
\#Start a web server
state = 'ON'
pico_led.on()
temperature = 0
while True:
client = connection.accept()[0]
request = client.recv(1024)
request = str(request)
try:
request = request.split()[1]
except IndexError:
pass
if request == '/lighton?':
pico_led.on()
elif request =='/lightoff?':
pico_led.off()
elif request == '/close?':
sys.exit()\
html = webpage(temperature, state)
client.send(html)
client.close()

\--- /code ---

\--- /task ---

\--- task ---

Run your code again. This time, when you refresh your browser window and click on the buttons, the onboard LED should turn on and off. If you click on the **Stop Server** button, your server should shutdown.

\--- /task ---

\--- task ---

You can also tell the user of the webpage what the state of the LED is.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 66
line_highlights: 81, 84
------------------------------------------------------------

def serve(connection):
\#Start a web server
state = 'ON'
pico_led.on()
temperature = 0
while True:
client = connection.accept()[0]
request = client.recv(1024)
request = str(request)
try:
request = request.split()[1]
except IndexError:
pass
if request == '/lighton?':
pico_led.on()
state = 'ON'
elif request =='/lightoff?':
pico_led.off()
state = 'OFF'
elif request == '/close?':
sys.exit()
html = webpage(temperature, state)
client.send(html)
client.close()

\--- /code ---

Now when you run the code, the text for the state of the LED should also change on the refreshed webpage.

\--- /task ---

\--- task ---

Lastly, you can use the onboard temperature sensor to get an approximate reading of the CPU temperature, and display that on your webpage as well.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 66
line_highlights: 87
--------------------------------------------------------

def serve(connection):
\#Start a web server
state = 'ON'
pico_led.on()
temperature = 0
while True:
client = connection.accept()[0]
request = client.recv(1024)
request = str(request)
try:
request = request.split()[1]
except IndexError:
pass
if request == '/lighton?':
pico_led.on()
state = 'ON'
elif request =='/lightoff?':
pico_led.off()
state = 'OFF'
elif request == '/close?':
sys.exit()
temperature = pico_temp_sensor.temp
html = webpage(temperature, state)
client.send(html)
client.close()

\--- /code ---

\--- /task ---

\--- task ---

**Test:** You can hold your hand over your Raspberry Pi Pico W to increase its temperature, then refresh the webpage on your computer to see the new value that is displayed.

\--- /task ---
