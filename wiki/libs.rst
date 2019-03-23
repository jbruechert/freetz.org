libs
====
Inhaltsverzeichnis
^^^^^^^^^^^^^^^^^^

#. `Pakete, Addons und
   CGI-Erweiterungen <packages.html#PaketeAddonsundCGI-Erweiterungen>`__

   #. `Pakete <packages.html#Pakete>`__
   #. `Addons <packages.html#Addons>`__
   #. `CGI-Erweiterungen <packages.html#CGI-Erweiterungen>`__
   #. `Apps <packages.html#Apps>`__
   #. `Weiteres <packages.html#Weiteres>`__

#. `Pakete nach
   Anwendungsgebieten <packages_tagged.html#PaketenachAnwendungsgebieten>`__

   #. `Audio <packages_tagged.html#Audio>`__
   #. `Home Automation <packages_tagged.html#HomeAutomation>`__
   #. `Konsole <packages_tagged.html#Konsole>`__
   #. `Monitoring <packages_tagged.html#Monitoring>`__
   #. `Netzwerk <packages_tagged.html#Netzwerk>`__

      #. `DynDNS <packages_tagged.html#DynDNS>`__
      #. `File Transfer <packages_tagged.html#FileTransfer>`__
      #. `Internet
         Messenging <packages_tagged.html#InternetMessenging>`__
      #. `Konsole <packages_tagged.html#Konsole1>`__
      #. `Proxies <packages_tagged.html#Proxies>`__
      #. `Routing <packages_tagged.html#Routing>`__
      #. `Security <packages_tagged.html#Security>`__
      #. `Tunneling <packages_tagged.html#Tunneling>`__
      #. `VPN <packages_tagged.html#VPN>`__
      #. `Web-Anwendungen <packages_tagged.html#Web-Anwendungen>`__
      #. `Sonstiges <packages_tagged.html#Sonstiges>`__

   #. `Privacy <packages_tagged.html#Privacy>`__
   #. `Programmiersprachen und
      -hilfen <packages_tagged.html#Programmiersprachenund-hilfen>`__
   #. `Security <packages_tagged.html#Security1>`__
   #. `System <packages_tagged.html#System>`__

      #. `Dateisystem <packages_tagged.html#Dateisystem>`__
      #. `Hardware an der Box <packages_tagged.html#HardwareanderBox>`__
      #. `Verschiedenes <packages_tagged.html#Verschiedenes>`__

   #. `Telefonie <packages_tagged.html#Telefonie>`__
   #. `verschiedene Tools <packages_tagged.html#verschiedeneTools>`__

#. `Bibliotheken (libraries) <libs.html#Bibliothekenlibraries>`__

   #. `Abwählen von Bibliotheken <libs.html#AbwählenvonBibliotheken>`__
   #. `Liste der Bibliotheken <libs.html#ListederBibliotheken>`__

#. `Bibliotheken nach
   Anwendungsgebieten <libs_tagged.html#BibliothekennachAnwendungsgebieten>`__

   #. `Hardware <libs_tagged.html#Hardware>`__

      #. `USB <libs_tagged.html#USB>`__

.. _Bibliothekenlibraries:

Bibliotheken (libraries)
========================

.. _AbwählenvonBibliotheken:

Abwählen von Bibliotheken
-------------------------

Bibliotheken (im Nachfolgenden "libs" genannt") zu Paketen, die
abgewählt wurden, werden nicht automatisch mit abgewählt. Um nach der
Abwahl diverser Pakete auch die nicht mehr benötigten libs zu entfernen
(damit das Image nachher auch tatsächlich nicht zu groß wird) gibt es
folgende *make*-Targets:

.. code:: wiki

   # Unnötige Libs und Busybox-Applets deselektieren
   make config-clean-deps

   # Oder nur unnötige Libs deselektieren, Busybox-Applets in Ruhe lassen
   make config-clean-deps-keep-busybox

.. _ListederBibliotheken:

Liste der Bibliotheken
----------------------

Bibliotheken, die als "ex" (external) markiert sind, lassen sich
wahlweise direkt in das Firmware-Image einbauen - oder aber "nach extern
auslagern" (z.B. auf einen USB-Stick). "St" beschreibt den aktuellen
Stand (Status) der Einbindung in Freetz (|{*}| stable, |{o}| testing,
|<!>| unstable), und ist nicht unbedingt immer aktuell (den aktuelleren
Status erkennt man daran, wo das Paket letztendlich in
`menuconfig <help/howtos/common/install/menuconfig.html>`__ auftaucht.

+-------------+-------------+-------------+-------------+-------------+
| **Paketname | **Beschreib | **ex**      | **St**      | **Größe**   |
| **          | ung**       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| `ftdi <libs | ftdi        |             | |{o}|       |             |
| /ftdi.html> | drivers for |             |             |             |
| `__         | RS-232-USB  |             |             |             |
|             | adapters    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

-  Tags
-  `libs <libs.html>`__

.. |{*}| image:: ../chrome/wikiextras-icons-16/stable.png
.. |{o}| image:: ../chrome/wikiextras-icons-16/testing.png
.. |<!>| image:: ../chrome/wikiextras-icons-16/exclamation-red.png

