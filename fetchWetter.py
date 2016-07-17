#!/usr/bin/python
# Python Skript zum Laden von Wetterdaten in die Loxone - Hintergrund: Aktivierung der Auto-Beschattung mittels Jalousien
# Michael Pilgermann (kichkasch@gmx.de)
# Letzte Aenderung: 2016-07-17
#
# Dieses Script muss auf einen Python-faehigen Rechner gespeichert und dort regelmaessig ausgefuehrt (CRON) werden (vorzugsweise also ein Server)
# Als Croneintrag bietet sich an (entsprechende Lokation des Skriptes vorausgesetzt) - mit diesem Eintrag wird alle 10 Minuten aktualisiert:
# */10 *  * * *	root	/usr/bin/fetchWetter.py
#
# Die Werte werden auf Virtuelle Eingaenge in der Loxone umgelegt - sollten andere Namen Verwendung finden, muss das entsprechend angepasst werden:
# - LoxVirtuellerEingang (WetterSonnig): ein digitaler Eingang, der 0 bzw. 1 schaltet, wenn die Sonne scheint oder nicht
# - LoxVirtuellerEingangTemp (Aussentemperatur): ein analoger Eingang, der die Temperatur aufnimmt
#
# die Daten kommen von Wunderground (https://www.wunderground.com/). Bei Wunderground kann man sogar auf Wetterdaten einer privaten Station um die Ecke zugreifen.

# Wunderworld-Parameter
WunderKey = "*****"  # get your key here: https://www.wunderground.com/weather/api
WunderLocation = "pws:IBERLIN69"    # Von der Webseite wunderground - Zusammenstellung ist hier gut erklaert: http://www.loxwiki.eu/display/LOX/Weather+Underground+%28Wunderground%29+direkt+in+Loxone+einbinden
WunderURL = "http://api.wunderground.com/api/"+ WunderKey +"/alerts/conditions/forecast/hourly/lang%3ADL/pws%3A1/bestfct%3A1/q/"+WunderLocation+".json"
UV_Threashold = 5   # ab wann gilt das Wetter als sonnig (https://www.wunderground.com/resources/health/uvindex.asp?MR=1)

# Loxone Parameter
LoxPrefix = "http://"
LoxIP = "192.168.200.19"
LoxPath = "/dev/sps/io"
LoxVirtuellerEingang = "/WetterSonnig/"
LoxVirtuellerEingangTemp = "/Aussentemperatur/"
LoxUsername = "michael"     
LoxPassword = "*****"   # hier dein Loxone-Passwort!!!

import urllib2
import base64
import json

# Hole Daten 
response = urllib2.urlopen(WunderURL)
html = response.read()

data = json.loads(html)
values = data["current_observation"]
temp = str(values["temp_c"])
himmel = values['weather']
feuchte = values["relative_humidity"]
luftdruck = values["pressure_mb"]
uv = int(values["UV"])
sichtweite = values["visibility_km"]
messzeitpunkt = values["observation_time_rfc822"]
if uv > UV_Threashold:
    sonnig ="0"
else:
    sonnig = "1"

# das Ganze nun auf der Loxone schalten
url = LoxPrefix + LoxIP + LoxPath + LoxVirtuellerEingang + sonnig
req = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % (LoxUsername, LoxPassword))[:-1]
req.add_header("Authorization", "Basic %s" % base64string)
handle = urllib2.urlopen(req)
response = handle.read()

url = LoxPrefix + LoxIP + LoxPath + LoxVirtuellerEingangTemp + temp 
req = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % (LoxUsername, LoxPassword))[:-1]
req.add_header("Authorization", "Basic %s" % base64string)
handle = urllib2.urlopen(req)
response = handle.read()

