help/wikiedit/formatting_guide
==============================
Inhaltsverzeichnis
^^^^^^^^^^^^^^^^^^

#. `Wiki Bearbeitung - Tipps und
   Tricks <../wikiedit.html#WikiBearbeitung-TippsundTricks>`__

   #. `Erste Schritte <../wikiedit.html#ErsteSchritte>`__
   #. `Weitere Lektüre <../wikiedit.html#WeitereLektüre>`__

#. `Wiki Goodies <goodies.html#WikiGoodies>`__

   #. `Smileys <goodies.html#Smileys>`__
   #. `Symbols <goodies.html#Symbols>`__
   #. `Entities <goodies.html#Entities>`__

#. `Formatierungs-Guidelines <formatting_guide.html#Formatierungs-Guidelines>`__

   #. `Beispiel-Artikel <formatting_guide.html#Beispiel-Artikel>`__
   #. `Inhaltsverzeichnis <formatting_guide.html#Inhaltsverzeichnis>`__
   #. `Überschriften <formatting_guide.html#Überschriften>`__
   #. `Artikeltext <formatting_guide.html#Artikeltext>`__
   #. `Screenshots <formatting_guide.html#Screenshots>`__
   #. `Besondere
      Formatierungen <formatting_guide.html#BesondereFormatierungen>`__
   #. `Weiterführende
      Links <formatting_guide.html#WeiterführendeLinks>`__
   #. `Tags <formatting_guide.html#Tags>`__

#. `Tabellen <tables.html#Tabellen>`__

   #. `Überblick der verschiedenen
      Formate <tables.html#ÜberblickderverschiedenenFormate>`__

      #. `Standard <tables.html#Standard>`__
      #. `RST <tables.html#RST>`__
      #. `MediaWiki <tables.html#MediaWiki>`__

   #. `Anwendung: Wie erstelle ich eine
      Tabelle? <tables.html#Anwendung:WieerstelleicheineTabelle>`__

      #. `Standard <tables.html#Standard1>`__
      #. `RST <tables.html#RST1>`__
      #. `MediaWiki <tables.html#MediaWiki1>`__

         #. `Einfaches Beispiel <tables.html#EinfachesBeispiel>`__
         #. `komplexeres Beispiel <tables.html#komplexeresBeispiel>`__

#. `Inhaltsverzeichnis erstellen
   (lassen) <toc.html#Inhaltsverzeichniserstellenlassen>`__

   #. `Unterseiten einbeziehen <toc.html#Unterseiteneinbeziehen>`__
   #. `Ebenentiefe einschränken <toc.html#Ebenentiefeeinschränken>`__
   #. `Mehrere TOC Blöcke <toc.html#MehrereTOCBlöcke>`__
   #. `Weitere Möglichkeiten <toc.html#WeitereMöglichkeiten>`__

#. `Tagging <tagging.html#Tagging>`__

   #. `Was und wozu sind Tags? <tagging.html#WasundwozusindTags>`__
   #. `Wie vergibt man Tags? <tagging.html#WievergibtmanTags>`__
   #. `Welche Tags sollte man
      vergeben? <tagging.html#WelcheTagssolltemanvergeben>`__
   #. `Was ist noch zu beachten? <tagging.html#Wasistnochzubeachten>`__

#. `Screenshots <screenshots.html#Screenshots>`__

   #. `Screenhots hochladen <screenshots.html#Screenhotshochladen>`__
   #. `Screenhots finden <screenshots.html#Screenhotsfinden>`__

      #. `Screenshot Matrix <screenshots.html#ScreenshotMatrix>`__
      #. `Screenshots Liste <screenshots.html#ScreenshotsListe>`__

   #. `Screenshots
      referenzieren <screenshots.html#Screenshotsreferenzieren>`__

.. _Formatierungs-Guidelines:

Formatierungs-Guidelines
========================

Damit ein Wiki "wie aus einem Guss" wirken kann, sind einheitliche
Formatierungen vonnöten. Daher soll an dieser Stelle einmal kurz
aufgezeigt werden, nach welchen "Richtlinien" bislang vorgegangen wurde
- was natürlich als Anhaltspunkt bei der Erstellung neuer sowie der
Bearbeitung existierender Artikel gut geeignet sein sollte.

.. _Beispiel-Artikel:

Beispiel-Artikel
----------------

Die Zusammenfassung einmal vorab: So könnte der Artikel für ein fiktives
Paket namens *dummy* aussehen:

.. code:: wiki

   [[TOC(heading=Inhaltsverzeichnis)]]

   = dummy =

   '''dummy''' ist ein Paket, das es nicht wirklich gibt.
   Wirklich geben tut es hingegen Pakete wie [wiki:packages/callmonitor CallMonitor]
   und [wiki:packages/dtmfbox DTMFBox].

   == Installation ==
   Die Installation erfolgt wie bei den meisten Paketen direkt bei der
   [wiki:help/howtos/common/installation Erstellung des Freetz-Images], indem das Paket
   einfach in der
   [wiki:help/howtos/common/installation/menuconfig menuconfig] mit ausgewählt wird.

   == Einrichtung ==
   ''dummy'' verfügt über eine Konfigurations-Oberfläche, in der sich alle notwendigen
   Einstellungen tätigen lassen:
   [[Screenshot(123)]]
    * '''Starttyp''': "Automatisch", wenn ''dummy'' nach jedem Reboot automatisch
   gestartet werden soll.
    * '''Punkt1''': Hier trägt man was ein
    * '''Punkt2''': blabla...

   == Besonderheiten ==
   ''dummy'' kann auch zu Debugging-Zwecken mit {{{dummy -D}}} direkt von der Kommandozeile
   gestartet werden. Ein Skript für Trallalla könnte so aussehen:
   {{{
   #!sh
   # Irgendwas machen
   echo "Trallala!"
   # Tschüß sagen
   echo "Warnurspaß!"
   exit 0
   }}}

   == Weiterführende Links ==
    * [http://de.wikipedia.org/wiki/Lillibullero Wikipedia Artikel zu Trallala]
    * [http://www.wehavemorefun.de/ More fun to come] (Englisch)

.. _Inhaltsverzeichnis:

Inhaltsverzeichnis
------------------

| ``[[TOC(heading=Inhaltsverzeichnis)]]``
| Die erste Zeile unseres Beispiel-Artikels enthält den Aufruf eines
  `Makros <../../TracWikiMacros.html>`__, das ein automatisches
  Inhaltsverzeichnis erstellt. Das macht natürlich nur dann Sinn, wenn
  der Artikel auch mehrere (mindestens 3) Überschriften enthält. In
  userem Beispiel haben wir dem Makro genau einen Parameter mitgegeben:
  Die Überschrift (engl.: heading) des Inhaltverzeichnisses soll
  natürlich bei einem deutschsprachigen Artikel auch Deutsch sein.
  Default wäre hier Englisch, und zwar "Table of Contents".

Ausführlichere Hilfe zum Inhaltsverzeichnis gibt es `hier <toc.html>`__.

.. _Überschriften:

Überschriften
-------------

| ``= dummy =``
| Wir beginnen unseren Artikel mit einer Überschrift "Ebene 1" - nennen
  wir sie der Einfachheit halber "Hauptüberschrift". In der Regel ist
  dies die einzige Hauptüberschrift eines Artikels. Nach "unten" stufen
  wir schrittweise ab - Sprünge machen wenig Sinn.

.. _Artikeltext:

Artikeltext
-----------

| ``'''dummy''' ist ein Paket...``
| Es ist meist sinnvoll, die erste Erwähnung des Paketnamens mit
  Fettdruck zu versehen - insbesondere, wenn man eine davon abweichende
  Hauptüberschrift gewählt hat. Hat das Projekt eine Homepage, so macht
  es auch Sinn, diese hier zu verlinken. In diesem Falle sähe der Anfang
  dann etwa so aus:

``'''[http://www.dummy.dom/ dummy]''' ist ein Paket...``

Anschließend geht es nach gesundem Menschenverstand mit dem passenden
Fließtext weiter, es folgen Aufzählungen, oder was auch sonst in diesem
Zusammenhang benötigt wird.

.. _Screenshots:

Screenshots
-----------

| ``[[Screenshot(123)]]``
| Screenshots und andere Bilder verwalten wir hier mit dem
  ScreenshotsPlugin. Näheres zum Umgang damit findet sich `an dieser
  Stelle <screenshots.html>`__ ausführlich beschrieben.

.. _BesondereFormatierungen:

Besondere Formatierungen
------------------------

Gesondert hervorgehoben werden sollten:

-  Dateinamen, Pfade, Kommandozeilen-Befehle: eingeschlossen in
   dreifache geschweifte Klammern (``{{{Befehl``}}})
-  Bezüge (wie in unserem Beispiel die Beschreibung der einzelnen
   Konfigurationspunkte) in **Fettdruck**
-  weitere Erwähnungen des Paketnamens (oder auch andere Eigennamen)
   *kursiv*
-  mehrzeilige Skript-Fragmente (oder auch vollständige Skripte) in
   Code-Blöcken (siehe Beispiel). Für das Syntax-Highlighting gibt es
   verschiedene `WikiProcessors <../../WikiProcessors.html>`__ - das
   Beispiel benutzt den für Shell-Skript zuständigen.

.. _WeiterführendeLinks:

Weiterführende Links
--------------------

Eine gute Sache ist es auch, interessante Links zum Artikel am Ende
(nochmals) zusammenfassend aufzuzählen - auch wenn sie bereits im
Artikeltext selbst benutzt (verlinkt) wurden. Dann muss man nicht ewig
nach ihnen suchen |:)|

.. _Tags:

Tags
----

**Nach dem Speichern** des Artikels klicken wir nun nochmals auf den
*Edit* Button, um den Artikel mit den passenden `Tags <tagging.html>`__
zu versehen. Gleichzeitig klappt das leider nicht (Bug im TagsPlugin: Es
werden dann zwar die Tags aktualisiert, aber der ganze Artikeltext, bzw.
die gemachten Änderungen, gehen verloren). Wozu Tags nun wiederum
wichtig sind, und wie man sie verwendet, findet sich im gerade dazu
verlinkten Artikel.

-  Tags
-  `help <../../help.html>`__
-  `wikiedit </tags/wikiedit>`__

.. |:)| image:: ../../../chrome/wikiextras-icons-16/smiley.png

