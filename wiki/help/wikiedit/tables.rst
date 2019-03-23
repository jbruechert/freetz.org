help/wikiedit/tables
====================
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

.. _Tabellen:

Tabellen
========

Auch hier haben wir dem "schnöden Standard" ein wenig nachgeholfen - und
so gibt es verschiedene Möglichkeiten der Tabellen-Formatierung. Den
einzelnen Details möchte ich eine kurze Übersicht voranstellen:

.. _ÜberblickderverschiedenenFormate:

Überblick der verschiedenen Formate
-----------------------------------

.. _Standard:

Standard
~~~~~~~~

Den Standard haben wir ein klein wenig "aufgebohrt", sodass er im
Allgemeinen ausreichen sollte. Hier stehen innerhalb der einzelnen
Zellen alle Trac-Wiki Formatierungen zur Verfügung - dafür gestaltet es
sich etwas schwieriger, Zeilenumbrüche einzubringen oder Zellen zu
verbinden. Normalerweise ist dieses Format jedoch die erste Wahl.

.. _RST:

RST
~~~

`​Re-Structured Text <http://de.wikipedia.org/wiki/ReStructuredText>`__
bietet bei relativ einfacher Syntax zahlreiche zusätzliche
Formatierungsmöglichkeiten (siehe auch
`hier <../../WikiRestructuredText.html#BiggerReSTExample>`__. Dafür sind
innerhalb eines solchen Blocks keinerlei Wiki-Markups möglich - womit
RST für viele Dinge nicht in Frage kommt.

.. _MediaWiki:

MediaWiki
~~~~~~~~~

Da wir auch das `​MediaWiki
Plugin <http://trac-hacks.org/wiki/MediaWikiPluginMacro>`__ eingebunden
haben, bieten sich damit zahlreiche zusätzliche Möglichkeiten. Aber auch
hier gilt: Trac-Wiki Syntax ist innerhalb eines Media-Wiki Blocks nicht
möglich.

.. _Anwendung:WieerstelleicheineTabelle:

Anwendung: Wie erstelle ich eine Tabelle?
-----------------------------------------

.. _Standard1:

Standard
~~~~~~~~

Mit dem Trac-Wiki Standard (in gepatchter Form |;)|) ist dies am
einfachsten möglich:

.. code:: wiki

   |||   ||| 1 ||| 2 ||| 3 ||
   ||| A ||  X ||    ||  X ||
   ||| B ||    ||  X ||    ||
   ||| C ||  X ||  X ||    ||

wird zu

+------+------+------+------+
| \|   | \| 1 | \| 2 | \| 3 |
+------+------+------+------+
| \| A | X    |      | X    |
+------+------+------+------+
| \| B |      | X    |      |
+------+------+------+------+
| \| C | X    | X    |      |
+------+------+------+------+

.. _RST1:

RST
~~~

Hier sieht das ein wenig anders aus:

.. code:: wiki

   {{{
   #!rst
   =====  =====  ======
      Inputs     Output
   ------------  ------
     A      B    A or B
   =====  =====  ======
   False  False  False
   True   False  True
   False  True   True
   True   True   True
   =====  =====  ======
   }}}

Wird zu

Inputs

Output

A

B

A or B

False

False

False

True

False

True

False

True

True

True

True

True

.. _MediaWiki1:

MediaWiki
~~~~~~~~~

Hier haben wir auch wieder zahlreiche Möglichkeiten - von denen hier nur
zwei aufgezeigt werden sollen:

.. _EinfachesBeispiel:

Einfaches Beispiel
^^^^^^^^^^^^^^^^^^

Gibt man folgendes ein:

.. code:: wiki

   {{{
   #!mediawiki
   {|class="table"
   |-
   ! Überschrift 1. Spalte
   ! Überschrift 2. Spalte
   |-
   | Inhalt 1.Zeile 1.Spalte
   | Inhalt 1.Zeile 2.Spalte
   |}
   }}}

kommt dabei das heraus:

+-------------------------+-------------------------+
| Überschrift 1. Spalte   | Überschrift 2. Spalte   |
+=========================+=========================+
| Inhalt 1.Zeile 1.Spalte | Inhalt 1.Zeile 2.Spalte |
+-------------------------+-------------------------+

.. _komplexeresBeispiel:

komplexeres Beispiel
^^^^^^^^^^^^^^^^^^^^

Zu guter Letzt ein leicht komplexeres Beispiel, bei dem einige
Formatierungen (Hintergrund-Farbe etc.) explizit mit vorgegeben, und
auch ein paar Zellen verbunden werden. Eingegeben wurde also:

.. code:: wiki

   {{{
   #!mediawiki
   {|border="1" cellpadding="2px" style="border-collapse:collapse;border:1px solid #8cacbb;border-width:1px;"
   |-
   !background-color="#ff0"|'''Überschrift'''
   !background-color="#ff0"|'''Zweite Überschrift'''
   |-
   | Inhalt Zelle 1-1
   | Inhalt Zelle 1-2
   |-
   | colspan="2" align="center"|Verbundene Zellen zentriert
   |-
   | Inhalt Zelle 3-1
   | rowspan="2"|Verbundene Zelle
   |-
   | Inhalt Zelle 4-1
   |}
   }}}

Und dabei kam folgendes heraus:

**Überschrift**

**Zweite Überschrift**

Inhalt Zelle 1-1

Inhalt Zelle 1-2

Verbundene Zellen zentriert

Inhalt Zelle 3-1

Verbundene Zelle

Inhalt Zelle 4-1

-  Tags
-  `help <../../help.html>`__
-  `wikiedit </tags/wikiedit>`__

.. |;)| image:: ../../../chrome/wikiextras-icons-16/smiley-wink.png

