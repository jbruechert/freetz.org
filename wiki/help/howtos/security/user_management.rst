help/howtos/security/user_management
====================================
Inhaltsverzeichnis
^^^^^^^^^^^^^^^^^^

#. `Konfiguration des eingebauten
   Switches <switch_config.html#KonfigurationdeseingebautenSwitches>`__

   #. `Vorwort <switch_config.html#Vorwort>`__
   #. `Vordefinierte
      Switch-Konfigurationen <switch_config.html#VordefinierteSwitch-Konfigurationen>`__
   #. `Anpassungen in der
      ar7.cfg <switch_config.html#Anpassungeninderar7.cfg>`__
   #. `Beispiel <switch_config.html#Beispiel>`__
   #. `Sicherheits-Warnung <switch_config.html#Sicherheits-Warnung>`__
   #. `Kompatibilität <switch_config.html#Kompatibilität>`__

#. `Benutzerverwaltung <user_management.html#Benutzerverwaltung>`__

   #. `Benutzer anlegen <user_management.html#Benutzeranlegen>`__
   #. `Benutzer löschen <user_management.html#Benutzerlöschen>`__
   #. `Manuelle
      Anpassungen <user_management.html#ManuelleAnpassungen>`__
   #. `Besonderheiten <user_management.html#Besonderheiten>`__

#. `WLAN von LAN trennen mit
   iptables <split_wlan_lan.html#WLANvonLANtrennenmitiptables>`__

   #. `FRITZBox Einstellung <split_wlan_lan.html#FRITZBoxEinstellung>`__
   #. `iptables <split_wlan_lan.html#iptables>`__

#. `Freetz als interner Router mit
   Firewall <router_and_firewall.html#FreetzalsinternerRoutermitFirewall>`__

   #. `Zielgruppe <router_and_firewall.html#Zielgruppe>`__
   #. `Beispielszenario <router_and_firewall.html#Beispielszenario>`__
   #. `Die Fritzbox
      modden <router_and_firewall.html#DieFritzboxmodden>`__
   #. `Die Fritzbox auf getrennte Netze
      umstellen <router_and_firewall.html#DieFritzboxaufgetrennteNetzeumstellen>`__
   #. `Erstellen der
      Routen <router_and_firewall.html#ErstellenderRouten>`__
   #. `Die Rückrouten <router_and_firewall.html#DieRückrouten>`__
   #. `Firewall <router_and_firewall.html#Firewall>`__
   #. `FIXME kopierter
      Post <router_and_firewall.html#FIXMEkopierterPost>`__

.. _Benutzerverwaltung:

Benutzerverwaltung
==================

.. _Benutzeranlegen:

Benutzer anlegen
----------------

Nehmen wir an, der neue Benutzer soll *picard* heißen. Benutzer *root*
macht dann Folgendes:

.. _Freetz:

Freetz
~~~~~~

::

   # Benutzer hinzufügen
   adduser picard
   # in buffer speichern ???
   # Persistent speichern
   modsave flash

ds-mod
~~~~~~

::

   # Benutzer hinzufügen
   echo "picard:*" >> /tmp/flash/shadow.save
   # Persistent speichern
   modsave flash
   # Alle Benutzer neu laden, fehlende Heimverzeichnisse erzeugen
   modpasswd load
   # Paßwort vergeben (wird automatisch persistent gespeichert)
   modpasswd picard
   # Test
   login picard

.. _Benutzerlöschen:

Benutzer löschen
----------------

Jetzt der umgekehrte Weg - Benutzer *picard* soll wieder weg. Benutzer
*root* macht dann Folgendes:

.. _Freetz1:

Freetz
~~~~~~

::

   # Benutzer löschen
   deluser picard
   # Persistent speichern
   modsave flash

.. _ds-mod1:

ds-mod
~~~~~~

::

   # Heimverzeichnis löschen
   rm -rf /mod/home/picard
   # Temporäre Datei mit gelöschtem Benutzer erzeugen
   grep -v '^picard:' /tmp/flash/shadow.save > /tmp/deleted-user
   # Benutzerdatei überschreiben
   mv /tmp/deleted-user /tmp/flash/shadow.save
   # Persistent speichern
   modsave flash
   # Alle Benutzer neu laden (jetzt einen weniger)
   modpasswd load
   # Test (schlägt mit "Login incorrect" bei PW-Eingabe fehl)
   login picard

.. _ManuelleAnpassungen:

Manuelle Anpassungen
--------------------

Um z.B. die UID anzupassen geht man nach dem erfolgreichen Anlegen wie
oben beschrieben, wie folgt vor:

-  Datei /tmp/passwd bearbeiten
-  modsave flash
-  modsave

.. _Besonderheiten:

Besonderheiten
--------------

.. _Dropbear:

Dropbear
~~~~~~~~

In Freetz akzeptiert Dropbear standardmäßig nur Logins des Benutzers
``root``. Wer auch Anmeldungen anderer Benutzer ermöglichen will, muss
auf der Freetz-Weboberfläche die Option "Login nur für root erlauben"
deaktivieren. Das Entfernen des Patches
``make/dropbear/patches/100-root-login-only.patch`` ist - anders als in
früheren Versionen - nicht mehr nötig.

-  Tags
-  `howtos </tags/howtos>`__
-  `security </tags/security>`__
-  `user </tags/user>`__
