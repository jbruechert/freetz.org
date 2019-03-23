help/wikiedit/tagging
=====================
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

.. _Tagging:

Tagging
=======

.. _WasundwozusindTags:

Was und wozu sind Tags?
-----------------------

*Tags* kann man auf Deutsch am ehesten mit "Markierungen" wiedergeben.
In unserem Kontext sind es "benannte Markierungen", die u.a. bei der
Suche nach bestimmten Informationen hilfreich sind. Am besten erklärt
sich das an einem Beispiel:

Angenommen jemand möchte wissen, welche Dateisysteme auf einer an die
FritzBox angeschlossenen USB-Festplatte unterstützt werden. In der
Beschreibung der Pakete taucht nun nicht unbedingt das Wort
"Dateisystem" auf. Wurden die passenden Tags vergeben, führt hier eine
Suche nach "`packages filesystem </tags?q=packages+filesystem>`__" zum
gewünschten Ziel.

Desweiteren werden Tags auch benutzt, um vorhandene `Packages nach
Anwendungsgebieten <../../packages_tagged.html>`__ sortiert aufzulisten.

Ich denke, allein diese beiden Beispiele zeigen schon, wie sinnvoll und
hilfreich Tags sein können.

.. _WievergibtmanTags:

Wie vergibt man Tags?
---------------------

Um einem Wiki-Artikel (oder auch einem Ticket) passende Tags zu
vergeben, findet sich auf der Bearbeitungsseite ein Formularfeld namens
"Tag under:". Direkt anbei gibt es auch einen Link "`view all
tags </tags>`__", mit dem sich vorhandene Tags anzeigen lassen.

.. _WelcheTagssolltemanvergeben:

Welche Tags sollte man vergeben?
--------------------------------

Das hängt sicher vom Einzelfall ab. Dennoch lassen sich ein paar
"Richtlinien" aufzeigen:

-  "viele Köche verderben den Brei": "Nimm viel" hilft hier nicht
   unbedingt viel. Die ausgewählten Tags sollten schon zutreffend und
   möglichst eingrenzend sein.
-  Die Beschreibung eines Paketes sollte immer auch mit dem Tag
   "`packages </tags?q=packages>`__" versehen sein. Gleiches gilt für
   Patches und das Tag `patches </tags?q=patches>`__.
-  Zu allgemeine Tags ("Wiki") sollten möglichst vermieden werden -
   genau wie zu spezielle (z.B. der Name des Paketes).
-  Der Einheitlichkeit halber schreiben wir alle Tags nur mit
   :sub:`Kleinbuchstaben`.

Für Paketbeschreibungen findet man die passenden Tags am einfachsten,
indem man die `nach Anwendungsgebieten sortierte
Paketliste <../../packages_tagged.html>`__ aufruft, und sich dort die
Tags zu Paketen in der treffenden Anwendungsgruppe anschaut. Es gibt
auch eine `Liste aller Tags </tags>`__ - aus dieser sollte man sich
jedoch in der Regel auf solche Tags konzentrieren, die möglichst groß
dargestellt sind.

.. _Wasistnochzubeachten:

Was ist noch zu beachten?
-------------------------

Wenn man einen Artikel *und* die zugehörigen Tags editieren möchte,
sollte man dies besser in zwei Schritten tun (also z.B. erst die Tags
editieren, speichern, und dann den Artikeltext editieren und speichern).
Versucht man beides gleichzeitig, gehen häufig die Änderungen am
Artikeltext verloren - was wohl ein Bug im Tags-Plugin zu sein scheint.

Ähnlich verhält es sich beim Umbenennen einer Seite: Laut Dokumentation
des Tags-Plugins sollte man hier zunächst die Tags entfernen, den
Artikel umbenennen, und schließlich die Tags wieder hinzufügen.

-  Tags
-  `help <../../help.html>`__
-  `wikiedit </tags/wikiedit>`__
