## Vytvoř webovou stránku

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
V tomto kroku vytvoříš webovou stránku, kterou může webový server běžící na tvém Raspberry Pi Pico W odeslat do klientského webového prohlížeče. Nejprve si ale webovou stránku otestuj na počítači, ať víš, že se zobrazuje tak, jak má. V dalším kroku můžeš přidat kód do svého skriptu v Pythonu, aby Raspberry Pi Pico W mohlo webovou stránku zobrazovat.
</div>
<div>
![Snímek obrazovky z Chromu zobrazující webovou stránku se dvěma tlačítky pro zapínání a vypínání LED diody a s několika stručnými popisky.](images/index.png)
</div>
</div>

Webová stránka může být tak jednoduchá, jako nějaký text, formátovaný tak, aby ji webový prohlížeč vykreslil a poskytoval určitou interaktivitu. Ačkoliv Thonny není určen pro psaní HTML, lze jej k tomuto účelu použít. Můžeš však použít svůj preferovaný textový editor, pokud chceš, ať už je to VSCode, TextEdit nebo Poznámkový blok.

\--- task ---

V textovém editoru nebo v Thonny vytvoř nový soubor. Můžeš jej nazvat, jak chceš, ale `index.html` je standardní název pro první stránku, se kterou uživatel interaguje. Nezapomeň přidat příponu souboru `.html`. Pokud používáš Thonny, nezapomeň soubor uložit do složky **Tento počítač**.

\--- /task ---

\--- task ---

Existuje určitý standard pro HTML kód, který budeš muset respektovat.

## --- code ---

language: html
filename: index.html
line_numbers: true
line_number_start:
line_highlights:
-----------------------------------------------------

<!DOCTYPE html>

<html>
<body>
</body>
</html>

\--- /code ---

\--- /task ---

\--- task ---

Dále můžeš vytvořit tlačítko, které bude sloužit k zapnutí nebo vypnutí integrované LED diody.

## --- code ---

language: html
filename: index.html
line_numbers: true
line_number_start:
line_highlights: 4-6
---------------------------------------------------------

<!DOCTYPE html>

<html>
<body>
<form action="./lighton">
<input type="submit" value="Light on" />
</form>
</body>
</html>

\--- /code ---

\--- /task ---

\--- task ---

Ulož soubor a poté jej vyhledej ve správci souborů. Po dvojitém kliknutí na soubor by se měl otevřít ve výchozím webovém prohlížeči. Takto vypadá webová stránka v prohlížeči Google Chrome.

![Google Chrome zobrazuje stránku s jediným tlačítkem s označením Zapnout světlo.](images/button.png)

\--- /task ---

\--- task ---

Přidej druhé tlačítko pro vypnutí LED diody.

## --- code ---

language: html
filename: index.html
line_numbers: true
line_number_start:
line_highlights: 7-9
---------------------------------------------------------

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

\--- /code ---

\--- /task ---

\--- task ---

Lze přidat další tlačítko pro zavření webového serveru, aniž bys musel používat Thonny.

## --- code ---

language: html
filename: index.html
line_numbers: true
line_number_start:
line_highlights: 10-12
-----------------------------------------------------------

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

\--- /code ---

\--- /task ---

\--- task ---

Pro dokončení webové stránky můžeš přidat další data, jako je stav LED diody a teplota tvého Raspberry Pi Pico W.

## --- code ---

language: html
filename: index.html
line_numbers: true
line_number_start:
line_highlights: 13-14
-----------------------------------------------------------

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
<p>LED dioda je {state}</p>
<p>Teplota je {temperature}</p>
</body>
</html>

\--- /code ---

Tvá webová stránka by měla vypadat takto:

![Webová stránka v prohlížeči Google Chrome zobrazující dvě tlačítka a text týkající se stavu LED diod a teploty Pica.](images/button_and_state.png)

\--- /task ---

Nyní, když máš funkční webovou stránku, můžeš přidat tento kód do skriptu Pythonu. Nejdříve se budeš muset přepnout zpět na kód Pythonu v Thonny.

\--- task ---

Vytvoř novou funkci s názvem `webpage`, která má dva parametry. These are `temperature` and `state`.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 44
line_highlights:
-----------------------------------------------------

def webpage(temperature, state):
\#Template HTML

\--- /code ---

\--- /task ---

\--- task ---

You can now store all your HTML code that you have written and tested in a variable. Using **fstrings** for the text means that the placeholders you have in the HTML for `temperature` and `state` can be inserted into your string.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 44
line_highlights: 46-62
-----------------------------------------------------------

def webpage(temperature, state):
\#Template HTML
html = f"""<!DOCTYPE html><html>
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

\--- /code ---

\--- /task ---

\--- task ---

Lastly, you can return the `html` string from your function.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 44
line_highlights: 63
--------------------------------------------------------

def webpage(temperature, state):
\#Template HTML
html = f"""<!DOCTYPE html><html>
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

\--- /code ---

\--- /task ---

\--- save ---

You can't test this code yet, as your program is not yet serving the HTML. That will be tackled in the next step.

The simple HTML code you have just written will be stored in your MicroPython script and served to the browser of any computers that connect to it over your network, just like a webpage stored on any other server in the world. An important difference is that only devices connected to your WiFi network can access the webpage or control your Raspberry Pi Pico W. This page is a very simple demonstration of what is possible. To learn more about HTML coding and creating websites, see some of our [other projects on this site!](https://projects.raspberrypi.org/en/collections/html_and_css)

