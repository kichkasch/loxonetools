#!/usr/bin/python
# Python Skript zum Laden von Wetterdaten in die Loxone
# Michael Pilgermann (kichkasch@gmx.de)
# Letzte Aenderung: 2014-06-13
#
# Dieses Script muss auf einen Python-faehigen Rechner gespeichert und dort regelmaessig ausgefuehrt (CRON) werden (vorzugsweise also ein Server)
# Als Croneintrag bietet sich an (entsprechende Lokation des Skriptes vorausgesetzt) - mit diesem Eintrag wird alle 10 Minuten aktualisiert:
# */10 *  * * *	root	/usr/bin/fetchWetter.py

URL="http://www.dwd.de/bvbw/appmanager/bvbw/dwdwwwDesktop?_nfpb=true&_pageLabel=_dwdwww_wetter_warnungen_regionenwetter&T1400077811143553394835gsbDocumentPath=Content%2FOeffentlichkeit%2FWV%2FWV11%2FWarnungen%2FWetter__Aktuell%2FRegionenwetter%2FRegion__Nordost__Teaser.html&_state=maximized&_windowLabel=T1400077811143553394835&lastPageLabel=_dwdwww_wetter_warnungen_regionenwetter"
findBlockStr = "blockBodyPre"
findLineStr = "Berlin"
himmelOK = ["heiter","wolkenlos"]

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

# Hole Daten vom Deutschen Wetterdienst
response = urllib2.urlopen(URL)
html = response.read()

# zerlege die Antwort und schnapp dir den Wert fuer Berlin aus der Tabelle
blockPos = html.find(findBlockStr)
linePos = html.find(findLineStr, blockPos)
endPos = html.find("\n", linePos)
targetLine = html[linePos:endPos]

values = targetLine.split()
temp = values[1]
himmel = values[2]
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

