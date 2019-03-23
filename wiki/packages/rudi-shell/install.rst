packages/rudi-shell/install
===========================
Inhaltsverzeichnis
^^^^^^^^^^^^^^^^^^

#. `Rudi-Shell <../rudi-shell.html#Rudi-Shell>`__

   #. `Feature-Übersicht <../rudi-shell.html#Feature-Übersicht>`__
   #. `Systemvoraussetzungen <../rudi-shell.html#Systemvoraussetzungen>`__

      #. `Server <../rudi-shell.html#Server>`__
      #. `Client <../rudi-shell.html#Client>`__
      #. `Was NICHT gebraucht
         wird <../rudi-shell.html#WasNICHTgebrauchtwird>`__
      #. `Platzbedarf der
         Rudi-Shell <../rudi-shell.html#PlatzbedarfderRudi-Shell>`__

#. `Installation <install.html#Installation>`__
#. `Funktionsweise <functions.html#Funktionsweise>`__
#. `Illustrierte
   Anwendungsfälle <usage.html#IllustrierteAnwendungsfälle>`__

   #. `Shell-Skript ausführen <usage.html#Shell-Skriptausführen>`__
   #. `Historie verwenden <usage.html#Historieverwenden>`__
   #. `Download Tar-Archiv <usage.html#DownloadTar-Archiv>`__
   #. `Download langer
      Konsolenausgabe <usage.html#DownloadlangerKonsolenausgabe>`__
   #. `Datei-Upload <usage.html#Datei-Upload>`__

#. `Grenzen & Einschränkungen <limits.html#GrenzenEinschränkungen>`__
#. `Tips & Tricks <tips.html#TipsTricks>`__

   #. `Sicherer Zugriff via HTTPS <tips.html#SichererZugriffviaHTTPS>`__
   #. `HTTPS-Zugriff reloaded &
      improved <tips.html#HTTPS-Zugriffreloadedimproved>`__
   #. `Firmware remote flashen <tips.html#Firmwareremoteflashen>`__

*Die Rudi-Shell ist fester Bestandteil von allen Freetz-Versionen. Diese
Anleitung bezieht sich auf den Vorgänger DS-Mod.*

.. _Installation:

Installation
============

Das Archiv ``rudi_shell.zip`` kann man als Dateianhang des ersten
Postings aus dem `​Forums-Thread zur
Rudi-Shell <http://www.ip-phone-forum.de/showthread.php?p=810641>`__
herunter laden und entpacken.

Nehmen wir an, wir setzen den DS-Mod ein (falls nicht, entfällt dieser
erste Schritt). Dann müssen wir das Menü anpassen. Schauen wir uns im
Mod-Verzeichnis die Datei ``root/usr/lib/libmodcgi.sh`` an und suchen
nach dem Menüeintrag "Extras". Dort fügen wir die Zeile für Rudi ein (im
Beispiel sieht man noch die bei Ihnen evtl. nicht vorhandene Zeile für
meinen Backup/Restore-Mod):

.. code:: wiki

   cat << EOF
   <div id="extras"><a href="/cgi-bin/extras.cgi">Extras</a></div>
   <div id="backup_restore"><a href="/cgi-bin/backup_restore.cgi">Sichern/Wiederherstellen</a></div>
   <div id="rudi_shell"><a href="/cgi-bin/rudi_shell.cgi" target="_blank">Rudi-Shell</a></div>
   </div>
   EOF

Der zweite einfache Schritt ist das Kopieren der drei CGI-Dateien

-  ``rudi_shell.cgi`` (Hauptseite)
-  ``rudi_shellcmd.cgi`` (Befehlsausführung, Download)
-  ``rudi_upload.cgi`` (Upload)

nach ``root/usr/mww/cgi-bin``. Bitte anschließend nicht vergessen, die
Dateien mit ``chmod +x rudi*`` ausführbar zu machen!

Schritt drei fällt nur an, falls Sie *Haserl* nicht sowieso schon in den
Mod integriert haben: Kopieren Sie eine der im Archiv enthaltenen
Dateien *haserl-0.9.16_26* (für Kernel 2.6) oder *haserl-0.8.0_24*
(Kernel 2.4) nach ``root/usr/bin/haserl`` und machen Sie sie ebenfalls
mit ``chmod`` ausführbar. Der Grund für die ältere Version für Kernel
2.4 ist einfach, daß ich für die dortige *uClibc-0.9.26* nicht selbst
kompiliere und mir eine vorhandene Version aus dem Forum, gebaut von
Oliver (olistudent), geschnappt habe. Ansonsten würde die 0.9.16 sicher
auch unter dem alten Kernel laufen, nur müßte man sie dafür mal
kompilieren.

-  Tags
-  `rudi-shell </tags/rudi-shell>`__
