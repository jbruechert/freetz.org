packages/pptpd/config
=====================
.. _Konfiguration:

Konfiguration
=============

Inhaltsverzeichnis
^^^^^^^^^^^^^^^^^^

#. `PoPTop - PPTP-VPN-Server <../pptpd.html#PoPTop-PPTP-VPN-Server>`__

   #. `What is PPTP? <../pptpd.html#WhatisPPTP>`__
   #. `What is Poptop? <../pptpd.html#WhatisPoptop>`__

#. `Installation <install.html#Installation>`__

   #. `Kernel 2.6 (Freetz) <install.html#Kernel2.6Freetz>`__
   #. `Kernel 2.4 (ds-mod) <install.html#Kernel2.4ds-mod>`__

      #. 

         #. `Vorbereitungen <install.html#Vorbereitungen>`__

      #. `Patch einspielen <install.html#Patcheinspielen>`__
      #. `Kernel konfigurieren und
         kompilieren <install.html#Kernelkonfigurierenundkompilieren>`__
      #. `Kompilieren des Images vorbereiten und
         durchführen <install.html#KompilierendesImagesvorbereitenunddurchführen>`__

#. `Das Web-Frontend zum Paket <webif.html#DasWeb-FrontendzumPaket>`__

   #. `Portweiterleitung <webif.html#Portweiterleitung>`__

#. `Konfiguration <config.html#Konfiguration>`__

   #. `pptpd.conf <config.html#pptpd.conf>`__
   #. `options.pptpd <config.html#options.pptpd>`__
   #. `chap-secrets <config.html#chap-secrets>`__
   #. `Troubleshooting <config.html#Troubleshooting>`__
   #. `Troubleshooting keine
      Fehlermeldung <config.html#TroubleshootingkeineFehlermeldung>`__

Die drei für Poptop relevanten Dateien können entweder über das
`Webinterface <webif.html>`__ oder auf der Shell per vi editiert werden.
Sie liegen im Verzeichnis ``/tmp/flash/ppp``.

pptpd.conf
----------

In der mitgelieferten Konfiguration ist logwtmp standardmäßig aktiviert
(bezieht sich auf Version 1.1.2-stable. Ist im 'trunk' schon gefixed.).
Dies sollte deaktiviert werden, da wtmp auf der fritzbox nicht läuft und
somit eine vpn-Verbindung nicht zustande kommt.

.. code:: wiki

   # TAG: logwtmp
   #       Use wtmp(5) to record client connections and disconnections.
   #
   #logwtmp

Falls die Datenrate vom Wlan ins Internet mit pptpd sehr langsam ist,
sollte die Zeile ``bcrelay`` auskommentiert werden (siehe
`​IPPF <http://www.ip-phone-forum.de/showthread.php?t=201539>`__)

options.pptpd
-------------

In der Datei options.pptpd ist gegebenenfalls ``require-mppe-128``
eingetragen (bezieht sich auf Version 1.1.2-stable. Ist im 'trunk' schon
gefixed.). Der pppd kennt diese Option aber nicht. Beim Aushandeln der
Verschlüsselung per 'Auto' Einstellung im Client kann es unter Umständen
zu Verbindungsproblemen kommen, wenn der Client erstmal verhandeln will
(negotiation), der pppd aber direkt verschlüsselt sprechen will. Man
kann die Verschlüsselung direkt auf 128 Bit fest einstellen. Mit dieser
Einstellung hat eine PPTP Verbindung mit dem iPhone VPN-Client geklappt:

.. code:: wiki

   # Require the peer to authenticate itself using MS-CHAPv2 [Microsoft
   # Challenge Handshake Authentication Protocol, Version 2] authentication.
   require-mschap-v2
   # Require MPPE 128-bit encryption
   # (note that MPPE requires the use of MSCHAP-V2 during authentication)
   #require-mppe-128

   mppe required,no40,no56,stateless

chap-secrets
------------

In der ``options.pptpd`` ist der Name auf ``fritzbox`` eingestellt. Dies
sollte sich dann in einem Benutzereintrag in der ``chap-secrets``
widerspiegeln:

.. code:: wiki

   # client        server  secret                  IP addresses
   username fritzbox password 192.168.x.y
   EOF

In vielen Beispielen im Netz steht in der zweiten Spalte ``pptpd``.
Möchte man das so haben, dann sollte man einfach den ``name`` Eintrag in
``options.pptpd`` entsprechend anpassen.

.. _Troubleshooting:

Troubleshooting
---------------

Um die pptpd Meldungen zu sehen, muss man zunächst einen syslogd
starten:

.. code:: wiki

   /var/tmp/flash/ppp # syslogd -L -C256 -l 7

Und kann sich danach die Meldungen des daemons im syslog per ``logread``
anschauen:

.. code:: wiki

   /var/tmp/flash/ppp # logread

Um mehr Meldungen zu bekommen, kann man in ``options.pptpd`` und/oder
``pptpd.conf`` den Debug-Modus aktivieren:

options.pptpd:

.. code:: wiki

   # Enable connection debugging facilities.
   # (see your syslog configuration for where pppd sends to)
   debug

pptpd.conf:

.. code:: wiki

   # TAG: debug
   #       Turns on (more) debugging to syslog
   #
   debug

.. _TroubleshootingkeineFehlermeldung:

Troubleshooting keine Fehlermeldung
-----------------------------------

Bei mir tauchte im log keine Fehlermeldung auf. Da hilft debuggen auf
der Box mit:

.. code:: wiki

   ./strace pptpd -d -f -c /etc/ppp/pptpd.conf

Dabei kam heraus, dass es folgende Fehlermeldung gibt:

.. code:: wiki

   can't resolve symbol 'bzero'

Dazu gibt es einen Thread im Forum, der letzte Post erklärt wie man die
Toolchain zum fixen neu bauen muss:
`​http://www.ip-phone-forum.de/showpost.php?p=1407147&postcount=25 <http://www.ip-phone-forum.de/showpost.php?p=1407147&postcount=25>`__

Update[18.07.11]: Das Problem sollte mit Freetz-1.2 bzw. einem aktuellen
Trunk nicht mehr auftreten.
