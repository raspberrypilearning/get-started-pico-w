## Serve your web page

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will start up your web server so that it can be connected to by a client, and control your LED and read the temperature.
</div>
<div>
![screenshot from chrome showing a web page with two buttons for turning on and off an LED](images/web_light_on.png)
</div>
</div>

--- task ---

Create a function that will start your web server, using the `connection` object you had saved as a parameter.The `state` and `temperature` variables needs to be set for your HTML data. The state is going to start as being set to `'OFF'`, and the temperature `0` which means you should also ensure that the LED is off when the server starts.

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
    pico_led.off()
    temperature = 0
--- /code ---

--- /task ---

When your web browser asks for a connection to your Raspberry Pi Pico, the connection needs to be accepted. After that, the data that is sent from your web browser must be done in specific chunks (in this case 1024 bytes). You also need to know what the request your web browser is making - is it asking for just a simple page, is it asking for a page that doesn't exist?

--- task ---

You want to keep the web server up and listening all the time, so that any client can connect to it. add a `while True:` loop. Add these four lines of code so that you can accept a request, and `print()` to see what the request was. Add a call to your `serve` function in your calls at the bottom of your code.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 53
line_highlights: 57-61, 67
---
def serve(connection):
    #Start a webserver
    state = 'OFF'
    pico_led.off()
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
--- /code ---

--- /task ---

**Test: ** Run your program and then type in the IP address into a webrowser address bar on your computer.

![image of a browser address bar with the IP of the Pico typed in](images/browser_ip.png)

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

--- task ---

Next you need to send the HTML code you have written to the client web browser.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 53
line_highlights: 58-61, 67
---
def serve(connection):
    #Start a webserver
    state = 'OFF'
    pico_led.off()
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
        html = webpage(temperature, state)
        client.send(html)


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
--- /code ---

--- /task ---


--- task ---

Refresh your page when you've run the code again. Click on the buttons that are displayed. In Thonny you should then see that their are two different outputs from your shell.

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

Split the request string and then fetch the first item in the list. Some times the request string might not be able to be split, so it's best to handle this in a `try`/`except`.

If the 1st item in the split is `lighton?` then you can switch the LED on. If it is `lightoff?` then you can switch the LED off.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 53
line_highlights: 62-69
---
def serve(connection):
    #Start a webserver
    state = 'OFF'
    pico_led.off()

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
        html = webpage(temperature, state)
        client.send(html)

--- /code ---

--- /task ---

--- task ---

Run your code again. This time, when you refresh your browser window and click on the buttons, the onboard LED should turn on and off.

--- /task ---

--- task ---

You can also tell the user of the webpage what the state of the LED is.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 53
line_highlights: 68, 71
---
def serve(connection):
    #Start a webserver
    state = 'OFF'
    pico_led.off()

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
        html = webpage(temperature, state)
        client.send(html)

--- /code ---

Now when you run the code, the text for the state of the LED should also change on the refreshed webpage.

--- /task ---

--- task ---

Lastly you can use the onboard temperature sensor to get an approximate reading of the CPU temperature, and display that on your webpage as well.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 53
line_highlights: 72
---
def serve(connection):
    #Start a webserver
    state = 'OFF'
    pico_led.off()

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
        temperature = pico_temp_sensor.temp
        html = webpage(temperature, state)
        client.send(html)

--- /code ---

--- /task ---

--- task ---

**Test:** You can hold your hand over your Raspberry Pi Pico W to increase it's temperature, then refresh the web page on your computer to see the new value that is displayed.

--- /task ---

