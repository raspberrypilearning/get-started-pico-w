## Serve your web page

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will start up your web server so that it can be connected to by a client, and start to serve the HTML you have written.
</div>
<div>
![screenshot from chrome showing a web page with two buttons for turning on and off an LED, and some boiler plate text](images/index.png)
</div>
</div>

--- task ---

Create a function that will start your web server, using the `connection` object you had saved as a parameter.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 53
line_highlights: 
---
def serve(connection):
    #Start a webserver
--- /code ---

--- /task ---

--- task ---

The `state` variable needs to be set for your HTML data. It's going to start as being set to `'OFF'` which means you should also ensure that the LED is off when the server starts.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 53
line_highlights: 57-58
---
def serve(connection):
    #Start a webserver
    state = 'OFF'
    led.off()
--- /code ---

--- /task ---

--- task ---

You want to keep the web server up and listening all the time, so that any client can connect to it. There can be problems though, so start with a `try` statement and then add a `while True:` loop.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 53
line_highlights: 57-58
---
def serve(connection):
    #Start a webserver
    state = 'OFF'
    led.off()
    try:
        while True:
--- /code ---

--- /task ---

When your web browser asks for a connection to your Raspberry Pi Pico, the connection needs to be accepted. After that, the data that is sent from your web browser must be done in specific chunks (in this case 1024 bytes). You also need to know what the request your web browser is making - is it asking for just a simple page, is it asking for a page that doesn't exist?

--- task ---

Add these four lines of code so that you can accept a request, and `print()` to see what the request was.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 53
line_highlights: 57-58
---
def serve(connection):
    #Start a webserver
    state = 'OFF'
    led.off()
    try:
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            print(request)    
--- /code ---

--- /task ---

When you run this code you should see something like this:

```python
>>> %Run -c $EDITOR_CONTENT
Waiting for connection...
Waiting for connection...
Waiting for connection...
Connected on 192.168.1.143
b'GET / HTTP/1.1\r\nHost: 192.168.1.143\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-GB,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
b'GET /favicon.ico HTTP/1.1\r\nHost: 192.168.1.143\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0\r\nAccept: image/avif,image/webp,*/*\r\nAccept-Language: en-GB,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nReferer: http://192.168.1.143/\r\n\r\n'
```

--- task ---

Open a web browser and navigate to the IP address that has been output in the console. Then click on the buttons that are displayed. You should then see that their are two different outputs from your shell.

```python
b'GET /lighton? HTTP/1.1\r\nHost: 192.168.1.143\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-GB,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nReferer: http://192.168.1.143/\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
```

and

```python
b'GET /lightoff? HTTP/1.1\r\nHost: 192.168.1.143\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-GB,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nReferer: http://192.168.1.143/lighton?\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
```

--- /task ---

Notice that you have `/lighton?` and `lightoff?` in the requests. These can be used to control the onboard LED of Raspberry Pi Pico.

--- task ---

Split the request string and then fetch the first item in the list. If it is `lighton?` then you can switch the LED on. If it is `lightoff?` then you can switch the LED off.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 53
line_highlights: 57-58
---
def serve(connection):
    #Start a webserver
    state = 'OFF'
    led.off()
    try:
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            request = request.split()[1]
            if request == '/lighton?':
                led.on()
            elif request =='/lightoff?':
                led.off()
--- /code ---

--- /task ---
