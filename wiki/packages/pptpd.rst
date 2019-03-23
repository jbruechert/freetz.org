packages/pptpd
==============
Inhaltsverzeichnis
^^^^^^^^^^^^^^^^^^

#. `PoPTop - PPTP-VPN-Server <pptpd.html#PoPTop-PPTP-VPN-Server>`__

   #. `What is PPTP? <pptpd.html#WhatisPPTP>`__
   #. `What is Poptop? <pptpd.html#WhatisPoptop>`__

#. `Installation <pptpd/install.html#Installation>`__

   #. `Kernel 2.6 (Freetz) <pptpd/install.html#Kernel2.6Freetz>`__
   #. `Kernel 2.4 (ds-mod) <pptpd/install.html#Kernel2.4ds-mod>`__

      #. 

         #. `Vorbereitungen <pptpd/install.html#Vorbereitungen>`__

      #. `Patch einspielen <pptpd/install.html#Patcheinspielen>`__
      #. `Kernel konfigurieren und
         kompilieren <pptpd/install.html#Kernelkonfigurierenundkompilieren>`__
      #. `Kompilieren des Images vorbereiten und
         durchführen <pptpd/install.html#KompilierendesImagesvorbereitenunddurchführen>`__

#. `Das Web-Frontend zum
   Paket <pptpd/webif.html#DasWeb-FrontendzumPaket>`__

   #. `Portweiterleitung <pptpd/webif.html#Portweiterleitung>`__

#. `Konfiguration <pptpd/config.html#Konfiguration>`__

   #. `pptpd.conf <pptpd/config.html#pptpd.conf>`__
   #. `options.pptpd <pptpd/config.html#options.pptpd>`__
   #. `chap-secrets <pptpd/config.html#chap-secrets>`__
   #. `Troubleshooting <pptpd/config.html#Troubleshooting>`__
   #. `Troubleshooting keine
      Fehlermeldung <pptpd/config.html#TroubleshootingkeineFehlermeldung>`__

.. _PoPTop-PPTP-VPN-Server:

PoPTop - PPTP-VPN-Server
========================

Paket aus dem Thread: `​PPTP Server auf der Fritzbox und Speedport W701
V/W 900 V
funktioniert <http://www.ip-phone-forum.de/showthread.php?p=714224>`__

Als erstes ein großer Dank an
`​gamf <http://www.ip-phone-forum.de/member.php?u=93421>`__ und
`​hehol <http://www.ip-phone-forum.de/member.php?u=63500>`__ für die
Bereitstellung der Patches und des Pakets.

.. _WhatisPPTP:

What is PPTP?
-------------

PPTP stands for Point to Point Tunneling Protocol. It was developed by a
consortium including Microsoft and is used for establishing VPN (Virtual
Private Network) tunnels across the Internet. This allows remote users
to securely and inexpensively access their corporate network from
anywhere on the Internet.

PPTP uses a client-server model for establishing VPN connections. Most
Microsoft operating systems ship with a PPTP client, so there is no need
to purchase third-party client software. PPTP has the additional
advantage over other VPN technologies of being easy to setup.

.. _WhatisPoptop:

What is Poptop?
---------------

Before Poptop, no solution existed if you wish to connect PPTP clients
to Linux servers. Using Poptop, Linux servers can now function
seamlessly in a PPTP VPN environment. This enables administrators to
leverage the considerable benefits of both Microsoft and Linux operating
systems.

The current release version supports Windows 95/98/Me/NT/2000/XP PPTP
clients and Linux PPTP clients.

Quelle und weitere Infos:
`​http://www.poptop.org/ <http://www.poptop.org/>`__
