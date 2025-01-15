## Configurer ton Raspberry Pi Pico W

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Connecte ton Raspberry Pi Pico W et configure MicroPython.
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">MicroPython</span> est une version du langage de programmation Python pour les microcontrôleurs, comme ton Raspberry Pi Pico W. MicroPython te permet d'utiliser tes connaissances Python pour écrire du code pour interagir avec des composants électroniques.</p>

\--- task ---

Télécharge la dernière version du firmware Raspberry Pi Pico W à [https://rpf.io/pico-w-firmware](https://rpf.io/pico-w-firmware)

\--- /task ---

\--- task ---

**Connecte** la petite extrémité de ton câble micro USB au Raspberry Pi Pico W.

![A Raspberry Pi Pico W connecté à la petite extrémité d'un câble micro USB.](images/pico-top-plug.png)

\--- /task ---

\--- task ---

Maintiens enfoncé le bouton **BOOTSEL** de ton Raspberry Pi Pico W.

![Un Raspberry Pi Pico W avec le bouton BOOTSEL en surbrillance](images/bootsel.png)

\--- /task ---

\--- task ---

**Connecte** l'autre extrémité à ton ordinateur de bureau, ordinateur portable, ou Raspberry Pi.

![A Raspberry Pi Pico W connecté à un ordinateur portable via un câble micro USB.](images/plug-in-pico.png)

\--- /task ---

\--- task ---

Ton gestionnaire de fichiers devrait s'ouvrir, le Raspberry Pi Pico étant affiché comme un lecteur connecté à l'extérieur. Glisse et dépose le fichier firmware que tu as téléchargé dans le gestionnaire de fichiers. Ton Raspberry Pi Pico devrait se déconnecter et le gestionnaire de fichiers se fermera.

![image du gestionnaire de fichiers Windows ouvert, montrant le Raspberry Pi Pico connecté en tant que lecteur externe](images/file_manager.png)

\--- /task ---

\--- task ---

Ouvre l'éditeur Thonny.

\--- /task ---

\--- task ---

Regarde le texte dans le coin inférieur droit de l'éditeur Thonny. Il te montrera la version de Python utilisée.

Si « MicroPython (Raspberry Pi Pico) » n'est **pas** indiqué, clique sur le texte et sélectionne « MicroPython (Raspberry Pi Pico) » dans les options.

![MicroPython sélectionné comme interprète pour Thonny.](images/thonny-select-interpreter.png)

\--- /task ---

\--- task ---

**Débogage :**

## --- collapse ---

## title: I don't know if the firmware is installed and cannot connect to my Pico

Make sure your Raspberry Pi Pico W is connected to your computer with a micro USB cable. Click on the list in the bottom right-hand corner of your Thonny window. A pop-up menu will appear, which lists the available interpreters.

![A pop-up menu that shows an option saying configure interpreter.](images/no-pico-interpreter.png)

If you cannot see Pico in the list (as shown in the picture), you need to reconnect your Raspberry Pi Pico W while holding the BOOTSEL button to mount it as a storage volume, and then reinstall the firmware by following the instructions in the section above.

\--- /collapse ---

## --- collapse ---

## title: Firmware is installed but I still cannot connect to my Pico

You may be using the wrong kind of micro USB cable. Your current micro USB cable may be damaged, or designed to only carry power to devices and not transfer data. Try swapping your cable for another if nothing else has worked.

If your Pico still won't connect after trying all these things, it may **itself** be damaged and unable to connect.

\--- /collapse ---

\--- /task ---

For newcomers to Raspberry Pi Pico, `picozero` is a MicroPython library that's beginner-friendly.

\--- task ---

To complete the projects in this path, you need to install the `picozero` library as a Thonny package.

In Thonny, choose **Tools** > **Manage packages**.

![The Thonny Tools menu with Manage packages highlighted.](images/thonny-manage-packages.jpg)

\--- /task ---

\--- task ---

In the pop-up 'Manage packages for Raspberry Pi Pico' window, type `picozero` and click **Search on PyPi**.

![Thonny plugins search results showing picozero.](images/thonny-packages-picozero.jpg)

\--- /task ---

\--- task ---

Click on **picozero** in the search results.

Click on **Install**.

![The picozero information with 'Install' button highlighted.](images/thonny-install-package.jpg)

When installation has completed, close the package window, then quit and reopen Thonny.

\--- /task ---

If you have difficulties installing the `picozero` library in Thonny, you can download the library file and save it to your Raspberry Pi Pico W.

[[[picozero-offline-install]]]
