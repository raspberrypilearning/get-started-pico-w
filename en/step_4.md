## Open a socket

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will use the connection to your WLAN to open a socket
</div>
<div>
```python
>>> %Run -c $EDITOR_CONTENT
Waiting for connection...
Waiting for connection...
Waiting for connection...
Connected on 192.168.1.143
<socket state=1 timeout=-1 incoming=0 off=0>```
</div>
</div>

A socket is the way a **server** can listen for **client** that want to connect to it. The webpage you are currently looking at is hosted on Raspberry Pi Foundation servers. These servers have an open socket that waits for your web browser to make a connection, at which point the contents of the web page are sent to your computer. In this case your server is going to be your Raspberry Pi Pico and the client will be a web browser on another computer.

--- task ---

Create a new function that can be called to open a socket.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 25
line_highlights: 
---
def open_socket(ip):
    # Open a socket
--- /code ---

--- /task ---

To open a socket you need to provide the IP address, and a port number. Port numbers are used by computers to identify where requests should be sent. For instance port `80` is normally used for web traffic. Stardew Valley uses port `24642` when you're playing a multiplayer game. As you are setting up a web server you will be using port `80`

--- task ---

Add code to your function to create an address for your socket.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 25
line_highlights: 27
---
def open_socket(ip):
    # Open a socket
    address = (ip, 80)

--- /code ---

--- /task ---

--- task ---

Now you can create your socket, and then have it listen for requests on port `80`. Don't forget to call your function at the bottom of your code.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 25
line_highlights: 28-31
---
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)


ip = connect()
open_socket(ip)

--- /code ---

--- /task ---

--- task ---

Run your code, and you should see output that looks something like this. 

--- code ---
---
language: python
filename: 
line_numbers: false
line_number_start: 
line_highlights: 
---
>>> %Run -c $EDITOR_CONTENT
Waiting for connection...
Waiting for connection...
Waiting for connection...
Waiting for connection...
Waiting for connection...
Connected on 192.168.1.143
<socket state=1 timeout=-1 incoming=0 off=0>
--- /code ---

`socket state=1` tells you that your socket is working.

--- /task ---

--- task ---

Lastly you can replace your `print` with a `return` and then store the returned socket connection as a variable.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 25
line_highlights: 31, 35
---
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


ip = connect()
connection = open_socket(ip)

--- /code ---

--- /task ---

--- save ---