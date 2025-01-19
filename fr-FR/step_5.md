## Créer une page web

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Dans cette étape, tu vas créer une page web que le serveur web, exécuté sur ton Raspberry Pi Pico W, peut envoyer à un navigateur web client. Tu vas d'abord tester la page web sur ton ordinateur pour t'assurer qu'elle s'affiche comme il se doit. Dans l'étape suivante, tu peux ajouter le code à ton script Python, afin que ton Raspberry Pi Pico W puisse diffuser la page web.
</div>
<div>
![Capture d'écran de Chrome montrant une page Web avec deux boutons pour allumer et éteindre une LED, et du texte standard.](images/index.png)
</div>
</div>

Une page web peut être aussi simple qu'un texte, formaté de manière à ce qu'un navigateur web la restitue et offre une certaine interactivité. Bien que Thonny ne soit pas conçu pour écrire du HTML, il peut être utilisé à cette fin. Cependant, tu peux utiliser ton éditeur de texte préféré si tu le souhaites, que ce soit VSCode, TextEdit, ou Notepad.

\--- task ---

Dans ton éditeur de texte ou dans Thonny, crée un nouveau fichier. Tu peux l'appeler comme tu le souhaites, mais `index.html` est le nom standard de la première page avec laquelle un utilisateur interagit. Assure-toi d'ajouter l'extension de fichier `.html`. Si tu utilises Thonny, assure-toi de sauvegarder sur **Cet ordinateur**.

\--- /task ---

\--- task ---

Il y a du code HTML standard que tu devras inclure pour commencer.

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

Ensuite, tu peux créer un bouton qui sera utilisé pour allumer ou éteindre la LED embarquée.

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

Enregistre ton fichier et retrouve-le dans ton gestionnaire de fichiers. Lorsque tu double-cliques sur le fichier, il devrait s'ouvrir dans ton navigateur web par défaut. Voici à quoi ressemble la page web dans Google Chrome.

![Google Chrome affiche une page avec un seul bouton intitulé Lumière allumée.](images/button.png)

\--- /task ---

\--- task ---

Ajoute un deuxième bouton pour éteindre la LED.

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

Un bouton supplémentaire peut être ajouté pour fermer le serveur web, sans avoir à utiliser Thonny.

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

Pour terminer la page web, tu peux ajouter des données supplémentaires, comme l'état de la LED et la température de ton Raspberry Pi Pico W.

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
<p>La LED est {etat}</p>
<p>La température est {temperature}</p>
</body>
</html>

\--- /code ---

Ta page web devrait ressembler à ceci :

![Page Web dans Google Chrome montrant deux boutons et texte concernant l'état de la LED et la température du Pico.](images/button_and_state.png)

\--- /task ---

Maintenant que tu as une page web fonctionnelle, tu peux ajouter ce code dans ton script Python. Tu devras d'abord revenir à ton code Python dans Thonny.

\--- task ---

Crée une nouvelle fonction appelée `pageweb`, qui a deux paramètres. Il s'agit de `temperature` et `etat`.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 44
line_highlights:
-----------------------------------------------------

def pageweb(temperature, etat):
\#Modèle HTML

\--- /code ---

\--- /task ---

\--- task ---

Tu peux maintenant stocker tout ton code HTML que tu as écrit et testé dans une variable. L'utilisation de **fstrings** pour le texte signifie que les espaces réservés que tu as dans le HTML pour `temperature` et `etat` peuvent être insérés dans ta chaîne.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 44
line_highlights: 46-62
-----------------------------------------------------------

def pageweb(temperature, etat):
\#Modèle HTML
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
<p>La LED est {etat}</p>
<p>La température est de {temperature}</p>
</body>
</html>
"""

\--- /code ---

\--- /task ---

\--- task ---

Enfin, tu peux retourner la chaîne `html` de ta fonction.

## --- code ---

language: python
filename: web_server.py
line_numbers: true
line_number_start: 44
line_highlights: 63
--------------------------------------------------------

def pageweb(temperature, etat):
\#Modèle HTML
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
<p>La LED est {etat}</p>
<p>La température est de {temperature}</p>
</body>
</html>
"""
    return str(html)

\--- /code ---

\--- /task ---

\--- save ---

You can't test this code yet, as your program is not yet serving the HTML. That will be tackled in the next step.

The simple HTML code you have just written will be stored in your MicroPython script and served to the browser of any computers that connect to it over your network, just like a webpage stored on any other server in the world. An important difference is that only devices connected to your WiFi network can access the webpage or control your Raspberry Pi Pico W. This page is a very simple demonstration of what is possible. To learn more about HTML coding and creating websites, see some of our [other projects on this site!](https://projects.raspberrypi.org/en/collections/html_and_css)
