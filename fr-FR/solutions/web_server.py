import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine


ssid = 'SSID ici'
motdepasse = 'psk_ici'


def connect():
    #Se connecter au WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, motdepasse)
    while wlan.isconnected() == False:
        print('En attente de connexion...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connecté à {ip}')
    return ip
    

def ouvrir_socket(ip):
    # Ouvrir un socket
    adresse = (ip, 80)
    connexion = socket.socket()
    connexion.bind(adresse)
    connexion.listen(1)
    return connexion


def pageweb(temperature, etat):
    #Modèle HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <form action="./lighton">
            <input type="submit" value="Light on" />
            </form>
            <form action="./lightoff">
            <input type="submit" value="Light off" />
            </form>
            <p>La LED est {etat}</p>
            <p>La température est de {temperature}</p>
            </body>
            </html>
            """
    return str(html)


def serve(connexion):
    #Démarrer un serveur web
    etat = 'OFF'
    pico_led.off()
    while True:
        client = connexion.accept()[0]
        requete = client.recv(1024)
        requete = str(requete)
        try:
            requete = requete.split()[1]
        except IndexError:
            pass
        if requete == '/lighton?':
            #led.on()
            pico_led.on()
            etat = 'ON'
        elif requete =='/lightoff?':
            pico_led.off()
            #led.off()
            etat = 'OFF'
        temperature = pico_temp_sensor.temp
        html = pageweb(temperature, etat)
        client.send(html)
        client.close()


try:
    ip = connect()
    connexion = ouvrir_socket(ip)
    serve(connexion)
except KeyboardInterrupt:
    machine.reset()
