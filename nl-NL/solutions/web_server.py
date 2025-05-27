import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine


ssid = 'SSID hier''
password = 'psk_hier'


def connect():
    #Maak verbinding met WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Wachten op verbinding...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Verbonden op {ip}')
    return ip
    

def open_socket(ip):
    # Open een socket
    adres = (ip, 80)
    verbinding = socket.socket()
    verbinding.bind(adres)
    verbinding.listen(1)
    return verbinding


def webpagina(temperatuur, status):
    #HTML-sjabloon
    html = f"""
            <!DOCTYPE html>
            <html>
            <form action="./lighton">
            <input type="submit" value="Light on" />
            </form>
            <form action="./lightoff">
            <input type="submit" value="Light off" />
            </form>
            <p>LED is {status}</p>
            <p>Temperatuur is {temperatuur}</p>
            </body>
            </html>
            """
    return str(html)


def serve(verbinding):
    #Start een webserver
    status = 'UIT'
    pico_led.off()
    while True:
        client = verbinding.accept()[0]
        verzoek = client.recv(1024)
        verzoek = str(verzoek)
        try:
            verzoek = verzoek.split()[1]
        except IndexError:
            pass
        if verzoek == '/lighton?':
            #led.on()
            pico_led.on()
            status = 'AAN'
        elif verzoek =='/lightoff?':
            pico_led.off()
            #led.off()
            status = 'UIT'
        temperatuur = pico_temp_sensor.temp
        html = webpagina(temperatuur, status)
        client.send(html)
        client.close()


try:
    ip = connect()
    verbinding = open_socket(ip)
    serve(verbinding)
except KeyboardInterrupt:
    machine.reset()
