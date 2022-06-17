## Create a web page

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create a web page that your web server can send to the client.
</div>
<div>
![screenshot from chrome showing a web page with two buttons for turning on and off an LED, and some boiler plate text](images/index.png)
</div>
</div>

A web page can be as simple as some text, formatted in such a way that a web browser will render it and provide some interactivity. Although Thonny is not designed to write HTML, it can be used for this purpose. However, you can use your preferred, be that VSCode, TextEdit or Notepad.

--- task ---

In your text editor or in Thonny, create a new file. You can call it whatever you like, but `index.html` is the standard name for the first page that a user interacts with. Make sure you add the `.html` file extension.

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

Next you can create a button that will be used to turn the onboard LED on or off.

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

Save your file and then find it in your file manager. When you double click the file, is should open in your default web browser. Here is what the web page looks like in Google Chrome.

![Google Chrome showing a page with a single button labelled Light on](images/button.png)

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

To finish off the web page, you can add in some extra data, such as the state of the LED and the Temperature of your Raspberry Pi Pico.

--- code ---
---
language: html
filename: index.html
line_numbers: true
line_number_start: 
line_highlights: 10-11
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
<p>LED is {state}</p>
<p>Temperature is {temperature}</p>
</body>
</html>

--- /code ---

Your web page should look like this:

![web page in Google Chrome showing two buttons and text regarding state and temperature](images/button_and_state.png)

--- /task ---

Now that you have a working web page, you can add this code into your Python script. You'll need to switch back to your Python code in Thonny first.

--- task ---

Create a new function called `webpage`, that has two parameters. These are `temperature` and `state`.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 34
line_highlights: 
---
def webpage(temperature, state):
    #Template HTML
--- /code ---

--- /task ---

--- task ---

You can now store all your HTML code that you have written and tested in a variable. Using **f-strings** for the text, means that the place holders you have in the HTML for `temperature` and `state` can be inserted into your string.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 34
line_highlights: 36-49
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
--- /code ---

--- /task ---

--- task ---

Lastly you can return the `html` string from your function.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 34
line_highlights: 50
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

You can't test this code yet, as you're program is not yet serving the HTML. That will be tackled in the next step.

--- save ---