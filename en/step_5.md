## Create a webpage

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step, you will create a webpage that the web server, running on your Raspberry Pi Pico W, can send to a client web browser. You're going to test the webpage on your computer first though, to make sure it displays as it should. In the next step, you can add the code to your Python script, so that your Raspberry Pi Pico W can serve the webpage.
</div>
<div>
![Screenshot from Chrome showing a webpage with two buttons for turning an LED on and off, and some boiler plate text.](images/index.png)
</div>
</div>

A webpage can be as simple as some text, formatted in such a way that a web browser will render it and provide some interactivity. Although Thonny is not designed to write HTML, it can be used for this purpose. However, you can use your preferred text editor if you like, be that VSCode, TextEdit, or Notepad.

--- task ---

In your text editor or in Thonny, create a new file. You can call it whatever you like, but `index.html` is the standard name for the first page that a user interacts with. Make sure you add the `.html` file extension. If using Thonny, make sure to save to **This computer**.

--- /task ---

--- task ---

There is some standard HTML code that you will need to include to begin with.

--- code ---
---
language: html
filename: index.html
line_numbers: true
line_number_start: 
line_highlights: 
---
<!DOCTYPE html>
<html>
<body>
</body>
</html>

--- /code ---

--- /task ---

--- task ---

Next, you can create a button that will be used to turn the onboard LED on or off.

--- code ---
---
language: html
filename: index.html
line_numbers: true
line_number_start: 
line_highlights: 4-6
---
<!DOCTYPE html>
<html>
<body>
<form action="./lighton">
<input type="submit" value="Light on" />
</form>
</body>
</html>

--- /code ---

--- /task ---

--- task ---

Save your file and then find it in your file manager. When you double click the file, it should open in your default web browser. Here is what the webpage looks like in Google Chrome.

![Google Chrome showing a page with a single button labelled Light on.](images/button.png)

--- /task ---

--- task ---

Add a second button to turn the LED off.

--- code ---
---
language: html
filename: index.html
line_numbers: true
line_number_start: 
line_highlights: 7-9
---
<!DOCTYPE html>
<html>
<body>
<form action="./lighton">
<input type="submit" value="Light on" />
</form>
<form action="./lightoff">
<input type="submit" value="Light off" />
</form>
</body>
</html>

--- /code ---

--- /task ---

--- task ---

An additional button can be added to close the webserver, without having to use Thonny.

--- code ---
---
language: html
filename: index.html
line_numbers: true
line_number_start: 
line_highlights: 10-12
---
<!DOCTYPE html>
<html>
<body>
<form action="./lighton">
<input type="submit" value="Light on" />
</form>
<form action="./lightoff">
<input type="submit" value="Light off" />
</form>
<form action="./close">
<input type="submit" value="Stop server" />
</form>
</body>
</html>

--- /code ---


--- /task ---


--- task ---

To finish off the webpage, you can add in some extra data, such as the state of the LED and the temperature of your Raspberry Pi Pico W.

--- code ---
---
language: html
filename: index.html
line_numbers: true
line_number_start: 
line_highlights: 13-14
---
<!DOCTYPE html>
<html>
<body>
<form action="./lighton">
<input type="submit" value="Light on" />
</form>
<form action="./lightoff">
<input type="submit" value="Light off" />
</form>
<form action="./close">
<input type="submit" value="Stop server" />
</form>
<p>LED is {state}</p>
<p>Temperature is {temperature}</p>
</body>
</html>

--- /code ---

Your webpage should look like this:

![Webpage in Google Chrome showing two buttons and text regarding the LED's state and the Pico's temperature.](images/button_and_state.png)

--- /task ---

Now that you have a working webpage, you can add this code into your Python script. You'll need to switch back to your Python code in Thonny first.

--- task ---

Create a new function called `webpage`, that has two parameters. These are `temperature` and `state`.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 44
line_highlights: 
---
def webpage(temperature, state):
    #Template HTML

--- /code ---

--- /task ---

--- task ---

You can now store all your HTML code that you have written and tested in a variable. Using **fstrings** for the text means that the placeholders you have in the HTML for `temperature` and `state` can be inserted into your string.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 44
line_highlights: 46-62
---
def webpage(temperature, state):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <form action="./lighton">
            <input type="submit" value="Light on" />
            </form>
            <form action="./lightoff">
            <input type="submit" value="Light off" />
            </form>
            <form action="./close">
            <input type="submit" value="Stop server" />
            </form>
            <p>LED is {state}</p>
            <p>Temperature is {temperature}</p>
            </body>
            </html>
            """

--- /code ---

--- /task ---

--- task ---

Lastly, you can return the `html` string from your function.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 44
line_highlights: 63
---
def webpage(temperature, state):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <form action="./lighton">
            <input type="submit" value="Light on" />
            </form>
            <form action="./lightoff">
            <input type="submit" value="Light off" />
            </form>
            <p>LED is {state}</p>
            <p>Temperature is {temperature}</p>
            </body>
            </html>
            """
    return str(html)

--- /code ---

--- /task ---

--- save ---

You can't test this code yet, as your program is not yet serving the HTML. That will be tackled in the next step.

The simple HTML code you have just written will be stored in your MicroPython script and served to the browser of any computers that connect to it over your network, just like a webpage stored on any other server in the world. An important difference is that only devices connected to your WiFi network can access the webpage or control your Raspberry Pi Pico W. This page is a very simple demonstration of what is possible. To learn more about HTML coding and creating websites, see some of our [other projects on this site!](https://projects.raspberrypi.org/en/collections/html_and_css)

