#!/usr/bin/python
# Python Skript zum Laden von Wetterdaten in die Loxone
# Michael Pilgermann (kichkasch@gmx.de)
# Letzte Aenderung: 2016-04-19
#
# Dieses Script muss auf einen Python-faehigen Rechner gespeichert und dort regelmaessig ausgefuehrt (CRON) werden (vorzugsweise also ein Server)
# Als Croneintrag bietet sich an (entsprechende Lokation des Skriptes vorausgesetzt) - mit diesem Eintrag wird alle 10 Minuten aktualisiert:
# */10 *  * * *	root	/usr/bin/fetchWetter.py
#
# Die Werte werden auf Virtuelle Eingaenge in der Loxone umgelegt - sollten andere Namen Verwendung finden, muss das entsprechend angepasst werden:
# - LoxVirtuellerEingang (WetterSonnig): ein digitaler Eingang, der 0 bzw. 1 schaltet, wenn die Sonne scheint oder nicht
# - LoxVirtuellerEingangTemp (Aussentemperatur): ein analoger Eingang, der die Temperatur aufnimmt
#
# Die Daten kommen vom deutschen Wetterdienst und sind auf Berlin eingestellt. Fuer andere Lokationen muessten die Parameter <URL> und <findLineStr> angepasst werden.
# Neu Arpil 2016: Die Daten kommen von der Yahoo Wetter API (DWD hat umgestellt und laesst sich nicht mehr sauber parsen) - https://developer.yahoo.com/weather/

# Spezifische Parameter fuer die Quelle der Klima-Daten (beim Deutschen Wetterdienst)
#URL="http://www.dwd.de/bvbw/appmanager/bvbw/dwdwwwDesktop?_nfpb=true&_pageLabel=_dwdwww_wetter_warnungen_regionenwetter&T1400077811143553394835gsbDocumentPath=Content%2FOeffentlichkeit%2FWV%2FWV11%2FWarnungen%2FWetter__Aktuell%2FRegionenwetter%2FRegion__Nordost__Teaser.html&_state=maximized&_windowLabel=T1400077811143553394835&lastPageLabel=_dwdwww_wetter_warnungen_regionenwetter"
# Parameter Yahoo
CITY = "Berlin"
URL= "https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22" + CITY + "%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

himmelOK = ["Sunny","Mostly Sunny","Clear"]

# Loxone Parameter
LoxPrefix = "http://"
LoxIP = "192.168.200.19"
LoxPath = "/dev/sps/io"
LoxVirtuellerEingang = "/WetterSonnig/"
LoxVirtuellerEingangTemp = "/Aussentemperatur/"
LoxUsername = "michael"
LoxPassword = "*****"

import urllib2
import base64
import json

# Hole Daten 
response = urllib2.urlopen(URL)
html = response.read()

# zerlege die Antwort und schnapp dir den Wert fuer Berlin 
data = json.loads(html)
values = data['query']['results']['channel']['item']['condition']

temp = values['temp']
temp = (int(temp) - 32) * 5.0/9.0	# Fahrenheit in Celsius
temp = str(int(temp * 10) / 10.0)		# Runden auf eine Nachkommastelle
himmel = values['text']
if himmel in himmelOK:
	sonnig = "0"
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

