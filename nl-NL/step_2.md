## Stel je Raspberry Pi Pico W in

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Sluit je Raspberry Pi Pico W aan en stel MicroPython in.
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">MicroPython</span> is een versie van de programmeertaal Python voor microcontrollers, zoals je Raspberry Pi Pico W. Met MicroPython kun je jouw Python-kennis gebruiken om code te schrijven voor interactie met elektronische componenten.</p>

\--- task ---

Download de nieuwste versie van de Raspberry Pi Pico W-firmware op [https://rpf.io/pico-w-firmware](https://rpf.io/pico-w-firmware)

\--- /task ---

\--- task ---

**Sluit** het kleine uiteinde van je micro-USB-kabel aan op de Raspberry Pi Pico W.

![Een Raspberry Pi Pico W aangesloten op het kleine uiteinde van een micro-USB-kabel.](images/pico-top-plug.png)

\--- /task ---

\--- task ---

Houd de **BOOTSEL**-knop op je Raspberry Pi Pico W ingedrukt.

![Een Raspberry Pi Pico W met de BOOTSEL-knop gemarkeerd](images/bootsel.png)

\--- /task ---

\--- task ---

**Verbind** het andere uiteinde met je desktop computer, laptop of Raspberry Pi.

![Een Raspberry Pi Pico W aangesloten op een laptop via een micro-USB-kabel.](images/plug-in-pico.png)

\--- /task ---

\--- task ---

Je bestandsbeheerder zou nu moeten openen en de Raspberry Pi Pico zou moeten worden weergegeven als een extern aangesloten schijf. Sleep het gedownloade firmwarebestand naar de bestandsbeheerder. De verbinding met je Raspberry Pi Pico wordt verbroken en de bestandsbeheerder wordt gesloten.

![afbeelding van de geopende Windows-bestandsbeheerder, met de Raspberry Pi Pico aangesloten als een externe schijf](images/file_manager.png)

\--- /task ---

\--- task ---

Open de Thonny editor.

\--- /task ---

\--- task ---

Kijk naar de tekst in de rechterbenedenhoek van de Thonny editor. Het zal je de versie van Python laten zien die wordt gebruikt.

Als er **niet** 'MicroPython (Raspberry Pi Pico)' staat, klik dan op de tekst en selecteer 'MicroPython (Raspberry Pi Pico)' uit de opties.

![MicroPython geselecteerd als interpreter voor Thonny.](images/thonny-select-interpreter.png)

\--- /task ---

\--- task ---

**Fouten oplossen:**

## --- collapse ---

## title: Ik weet niet of de firmware is geïnstalleerd en ik kan geen verbinding kan maken met mijn Pico

Zorg ervoor dat je Raspberry Pi Pico W met een micro-USB-kabel op je computer is aangesloten. Klik op de lijst in de rechterbenedenhoek van het Thonny-venster. Er verschijnt een pop-up menu met de beschikbare interpreters.

![Een pop-up menu dat een optie toont met de tekst configure interpreter.](images/no-pico-interpreter.png)

Als je Pico niet in de lijst ziet (zoals in de afbeelding), moet je de Raspberry Pi Pico W opnieuw verbinden terwijl je de BOOTSEL-knop ingedrukt houdt om het als een opslagvolume te koppelen en daarna de firmware opnieuw installeren door de instructies in het bovenstaande gedeelte te volgen.

\--- /collapse ---

## --- collapse ---

## title: Firmware is geïnstalleerd, maar ik kan nog steeds geen verbinding maken met mijn Pico

Mogelijk gebruik je de verkeerde micro-USB-kabel. Je huidige micro-USB-kabel is mogelijk beschadigd of alleen ontworpen om stroom naar apparaten over te brengen en niet om gegevens over te brengen. Probeer de kabel te vervangen door een andere als verder niets heeft gewerkt.

Als je Pico nog steeds geen verbinding kan maken nadat je al deze dingen hebt geprobeerd, kan het **zelf** beschadigd zijn en niet in staat zijn verbinding te maken.

\--- /collapse ---

\--- /task ---

Voor beginners met Raspberry Pi Pico is `picozero` een MicroPython-bibliotheek die speciaal is ontwikkeld voor beginners.

\--- task ---

Om de projecten in dit pad te voltooien, moet je de `picozero` bibliotheek installeren als een Thonny-pakket.

In Thonny, kies **Tools** > **Manage packages**.

![Het Thonny Tools-menu met Manage packages gemarkeerd.](images/thonny-manage-packages.jpg)

\--- /task ---

\--- task ---

In het pop-up 'Manage packages for Raspberry Pi Pico' venster, type `picozero` en klik **Search on PyPi**.

![Zoekresultaten van Thonny-plug-ins tonen picozero.](images/thonny-packages-picozero.jpg)

\--- /task ---

\--- task ---

Klik op **picozero** in de zoekresultaten.

Klik op **Install**.

![De picozero-informatie met de knop 'Install' gemarkeerd.](images/thonny-install-package.jpg)

Wanneer de installatie is voltooid, sluit je het package venster, vervolgens sluit je Thonny af en dan open je Thonny opnieuw.

\--- /task ---

Als je problemen hebt met het installeren van de `picozero` bibliotheek in Thonny, kun je het bibliotheekbestand downloaden en opslaan op je Raspberry Pi Pico.

[[[picozero-offline-install]]]
