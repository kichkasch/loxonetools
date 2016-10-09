# loxFhem - Integrating Loxone home automation with FHEM


End of 2016 I started extending my Loxone homeautomation by FHEM/HomeMatic components. In here, you will find some documentation, code snippets and links for further information.

###Background:
* [Loxone](http://www.loxone.com) is a company from Austria, which sells (among other products) the so called *Loxone Miniserver*. Its a propriety solution. 
	* Technically, Loxone (wired) requires a star topology cabeling; however, several extensions are available to integrate with other systems (such as Enocean, 1-Wire or KNX).
	* I had realised light, heating and jalousies with Loxone. 
* [FHEM](http://fhem.de/) is an (if not *the*) open source solution for home automation. Several systems can be connected.
* [HomeMatic](http://www.homematic.com/) is a propriety air interface automation solution with tons of sensors / actors provided on low prices.	

I plan to integrate via HomeMatic a wheather station, window sensors (open|close), water sensors (lacking washing machine), as well as a simple LED panel.

###Hardware

Getting the hardware right: 

* Loxone side: I have had the [Loxone Miniserver](http://www.loxone.com/enen/products/miniserver/miniserver.html) in place already.
* FHEM side: FHEM may be installed on quite some devices; such as AVM Fritzbox, several NAS system or Rasperry - check [offical FHEM website](http://fhem.de/fhem.html#Links) for an overview.
	* As FHEM also runs perfectly on any Debian Linux, I decided to install it on my already existing [Plug Computer](https://www.globalscaletechnologies.com/c-14-gtimirabox.aspx). Straight foreward installation instructions for Debian are provided by [FHEM project](https://debian.fhem.de/) itself.	
* HomeMatic side: There are several ways on extending FHEM by HomeMatic. Check again [(German) FHEM wiki](http://www.fhemwiki.de/wiki/HomeMatic#Fhem_als_Zentrale) for an overview.
	* I decided to go for the [USB CUL (CC1101)](http://www.fhemwiki.de/wiki/CUL) and got one for around 40 € from Ebay.

#####Functional components:
For my purposes I am looking to integrate with the following devices:
* Wheather: [EQ3 83346 HomeMatic Kombisensor HM-WDS-OC3](https://www.amazon.de/dp/B001PSMK9A/ref=cm_sw_em_r_mt_dp_LQb7xbHVT4E0F)
* Water lack: [EQ3 HomeMatic Funk Wassermelder easy config 131778](https://www.amazon.de/dp/B00H7UINRS/ref=cm_sw_em_r_mt_dp_DKb7xb3AK43W6)
* Visulisation: LED Panel [eQ-3 104798 HomeMatic Funk-Statusanzeige LED16](https://www.amazon.de/dp/B007VTXP2I/ref=cm_sw_em_r_mt_dp_8Rb7xbRH9YZ5P)
* Window Open|Close sensor: [HomeMatic Funk-Fenster-Drehgriffkontakt](https://www.amazon.de/dp/B0024G9AEA/ref=cm_sw_em_r_mt_dp_E0b7xb7MT252Q)

I have also got some REV radio controlled power sockets; would be grant to also make them joining the automation circle of devices.


###Realisation


###Further information:

1. (German) [MeinTechBlog Overview](http://www.meintechblog.de/2016/07/5-gruende-zur-erweiterung-deines-fhem-servers-mit-loxone-howto/) on integrating FHEM with Loxone via UDP by [Christoph Klima](http://www.meintechblog.de/info/#christoph).

###Contacts

Email me on mailto:kichkasch@gmx.de.

Last change: 2016-10-09.

