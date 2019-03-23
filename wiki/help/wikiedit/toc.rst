help/wikiedit/toc
=================
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

.. _Inhaltsverzeichniserstellenlassen:

Inhaltsverzeichnis erstellen (lassen)
=====================================

Am rechten Rand ist ja ein Inhaltsverzeichnis zu sehen, welches sich
sogar über mehrere Artikel erstreckt. Dafür wurde ein
`Makro <../../TracWikiMacros.html#AvailableMacros>`__ verwendet, dessen
genaue Syntax sich auf der soeben angegebenen Seite findet. Damit die
Überschrift hier auch auf Deutsch ist, verwenden wir auf
deutschsprachigen Seiten das Argument ``heading=Inhaltsverzeichnis`` -
als Beispiel für ein einfaches Inhaltsverzeichnis für die aktuell
bearbeitete Seite sähe das dann so aus:

.. code:: wiki

   [[TOC(heading=Inhaltsverzeichnis)]]

.. _Unterseiteneinbeziehen:

Unterseiten einbeziehen
-----------------------

Es lassen sich auch Unterseiten (oder ganz andere Seiten) mit
einbeziehen, sodass ein Inhaltsverzeichnis entsteht, welches mehrere
Artikel überspannt. Hierzu gibt man die zu indizierenden Seiten explizit
an:

.. code:: wiki

   [[TOC(help/wikiedit,help/wikiedit/toc,help/wikiedit/goodies,heading=Inhaltsverzeichnis)]]

etwa würde die angegebenen Seiten in das automatische Inhaltsverzeichnis
einbeziehen. Da man auf diese Art allerdings jedesmal, wenn eine neue
Unterseite angelegt wird, das TOC-Makro auf allen beteiligten Seiten
wieder anpassen müsste, geht das auch einfacher:

.. code:: wiki

   [[TOC(help/wikiedit,help/wikiedit/*,heading=Inhaltsverzeichnis)]]

Das ist der Vorteil eines hierarchischen Wikis: Das *WildCard* "*"
greift nicht zu weit um sich, sondern bleibt beim Thema.

.. _Ebenentiefeeinschränken:

Ebenentiefe einschränken
------------------------

Werden die Unterseiten dann doch zahlreicher, und die mit dem TOC-Makro
zusammengefassten Überschriften sprengen ob der Schachtelungstiefe die
Seiten (etwa, weil eine oder mehrere Seiten ziemlich viele Überschriften
niedrigerer Ebenen, also quasi "2.1.3.5", haben), lässt sich die
maximale Tiefe der vom TOC-Makro anzuzeigenden Überschriften ebenfalls
einschränken, wozu der Parameter ``depth`` herangezogen werden kann.
Soll das TOC-Makro also beispielsweise nur die Überschriften der Ebenen
1 und 2 anzeigen, sähe das so aus:

.. code:: wiki

   [[TOC(help/wikiedit,help/wikiedit/*,depth=2,heading=Inhaltsverzeichnis)]]

.. _MehrereTOCBlöcke:

Mehrere TOC Blöcke
------------------

Tja, das klappt leider nicht sauber: Das themenüberspannende, jedoch auf
2 Ebenen eingeschränkte TOC-Makro mit einem seitenspezifischen zu
verbinden, welches alle Ebenen umfasst. Auch ein zusätzliches, zweites
TOC-Makro geht gehörig schief: Es positioniert sich nämlich nicht
unterhalb des ersten, sondern unmittelbar links daneben - damit ist von
der Seitenbreite dann nicht mehr viel übrig; ganz davon abgesehen, dass
es ziemlich dämlich aussieht.

Was aber nun tun, wenn ein zweiter Block benötigt wird? Sofern es nur
darum geht, die Überschriften aufzulisten - und es nicht unbedingt der
"schöne gelbe Kasten da rechts" sein muss, bietet das Keyword ``inline``
hier Abhilfe:

.. code:: wiki

   [[TOC(help/wikiedit,help/wikiedit/*,inline,noheading)]]

wäre etwa geeignet, den entsprechenden Index mitten im Artikel - also
so, als hätte man die einzelnen Punkte mit ihren Links selbst abgetippt
- darzustellen.

.. _WeitereMöglichkeiten:

Weitere Möglichkeiten
---------------------

Es gibt noch weitere Parameter, und somit weitere Möglichkeiten, das
TOC-Makro zu manipulieren. Diese werden auf der
`WikiMakros <../../WikiMacros.html>`__ Seite erläutert.

-  Tags
-  `help <../../help.html>`__
-  `wikiedit </tags/wikiedit>`__
