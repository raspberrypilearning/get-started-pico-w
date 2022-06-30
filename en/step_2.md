## Set up your Raspberry Pi Pico W

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Connect your Raspberry Pi Pico W and set up MicroPython.
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">MicroPython</span> is a version of the Python programming language for microcontrollers, such as your Raspberry Pi Pico W. MicroPython lets you use your Python knowledge to write code to interact with electronics components.</p>

--- task ---

**Connect** the small end of your micro USB cable to the Raspberry Pi Pico W.

![A Raspberry Pi Pico W connected to the small end of a micro USB cable.](images/pico-top-plug.png)

--- /task ---

--- task ---

**Connect** the other end to your computer, laptop, or Raspberry Pi.

![A Raspberry Pi Pico W connected to a laptop via a micro USB cable.](images/plug-in-pico.png)

--- /task ---


--- task ---

Open the Thonny editor. 

--- /task ---

--- task ---

Look at the text in the bottom-right corner of the Thonny editor. It will show you the version of Python that is being used.

If it does not say "MicroPython (Raspberry Pi Pico)", then click on the text and select "MicroPython (Raspberry Pi Pico)".

If you have never used MicroPython on your Raspberry Pi Pico W before, then Thonny will prompt you to add the MicroPython firmware. Click **Install**. 

![MicroPython installation window with the Install button highlighted.](images/thonny-install-micropython-pico.png)

--- /task ---

--- task ---

**Debug:** 

--- collapse ---
---
title: There was an error installing the firmware
---

If you see an error message during the install, then:
+ Disconnect your Raspberry Pi Pico W
+ Reconnect your Raspberry Pi Pico W
+ Try to install the firmware again (you might need to press the stop button first)

![A screenshot of an error message showing that the firmware cannot install correctly.](images/pico-firmware-error.PNG)

--- /collapse ---

--- collapse ---
---
title: I don't know if the firmware is installed and cannot connect to my Pico
---

Make sure your Raspberry Pi Pico W is connected to your computer with a micro USB cable. Click on the list in the bottom-right corner of your Thonny window. A pop-up menu will appear, which lists the available interpreters. 

![A pop-up menu that shows an option saying configure interpreter.](images/no-pico-interpreter.png) 

If you cannot see the Pico in the list (like in the picture), you will need to reconnect your Raspberry Pi Pico W while holding the BOOTSEL button to mount it as a storage volume, and then reinstall the firmware by following the instructions in the section above.

--- /collapse ---

--- collapse ---
---
title: Firmware is installed but I still cannot connect to my Pico
---

You may be using the wrong kind of micro USB cable. Your current micro USB cable may be damaged, or designed to only carry power to devices and not transfer data. Try swapping your cable for another if nothing else has worked. 

If your Pico still won't connect after trying all these things, it may **itself** be damaged and unable to connect. 

--- /collapse ---

You can find further information in the [Raspberry Pi Pico Guide](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"}.

--- /task ---

For newcomers to the Raspberry Pi Pico, `picozero` is a MicroPython library that's beginner-friendly. 

--- task ---

To complete the projects in this path, you will need to install the `picozero` library as a Thonny package.

In Thonny, choose **Tools** > **Manage packages**.

![The Thonny Tools menu with Manage packages highlighted.](images/thonny-manage-packages.jpg)

--- /task ---

--- task ---

In the pop-up 'Manage packages for Raspberry Pi Pico' window, type `picozero` and click **Search on PyPi**.

![Thonny plugins search results showing picozero.](images/thonny-packages-picozero.jpg)

--- /task ---

--- task ---

Click on **picozero** in the search results. 

Click on **Install**.

![The picozero information with 'Install' button highlighted.](images/thonny-install-package.jpg)

When installation has completed, close the package window, then exit and reopen Thonny.

--- /task ---

If you have difficulties installing the `picozero` library in Thonny, you can download the library file and save it to your Raspberry Pi Pico W. 

[[[picozero-offline-install]]]
