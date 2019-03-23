packages/callmonitor/testcall
=============================
Inhaltsverzeichnis
^^^^^^^^^^^^^^^^^^

#. `Callmonitor <../callmonitor.html#Callmonitor>`__

   #. `Installation <../callmonitor.html#Installation>`__

      #. `Installation neuer
         Versionen <../callmonitor.html#InstallationneuerVersionen>`__

   #. `Konfiguration <../callmonitor.html#Konfiguration>`__
   #. `Weiterführende Links <../callmonitor.html#WeiterführendeLinks>`__

#. `Konfiguration <config.html#Konfiguration>`__

   #. `Basiskonfiguration <config.html#Basiskonfiguration>`__
   #. `Listeners definieren <config.html#Listenersdefinieren>`__
   #. `Testanruf <config.html#Testanruf>`__
   #. `Fehlersuche <config.html#Fehlersuche>`__

#. `Regeln (Listeners) <listeners.html#RegelnListeners>`__

   #. `Format <listeners.html#Format>`__
   #. `Ereignis-Informationen für
      Aktionen <listeners.html#Ereignis-InformationenfürAktionen>`__
   #. `Formatierung der
      Ausgaben <listeners.html#FormatierungderAusgaben>`__
   #. `Muster für Ereignisse <listeners.html#MusterfürEreignisse>`__
   #. `Beispiele: <listeners.html#Beispiele:>`__

#. `Ereignisse <events.html#Ereignisse>`__
#. `Aktionen <actions.html#Aktionen>`__

   #. `Benachrichtigen <actions.html#Benachrichtigen>`__
   #. `Wählen, Wecken,
      Konfigurieren <actions.html#WählenWeckenKonfigurieren>`__
   #. `Eigene Aktionen <actions.html#EigeneAktionen>`__
   #. `Liste verfügbarer
      Aktionen <actions.html#ListeverfügbarerAktionen>`__
   #. `Third-Party Software <actions.html#Third-PartySoftware>`__

#. `Telefonbuch (Callers) <phonebook.html#TelefonbuchCallers>`__
#. `Wartung <maintenance.html#Wartung>`__
#. `Rückwärtssuche <reverse_search.html#Rückwärtssuche>`__
#. `Testanruf <testcall.html#Testanruf>`__

.. _Testanruf:

Testanruf
=========

Nachdem die `Listeners <listeners.html>`__ definiert sind, empfiehlt es
sich, sie auf korrekte Funktion zu testen. Da man nicht immer jede
Konfiguration mit echten Anrufen testen kann, gibt es eine Seite im
Web-Interface, die Anrufe simuliert. Dabei klingeln keine Telefone, es
wird lediglich dem CallMonitor ein Anruf vorgetäuscht, den er wie einen
echten Anruf behandelt.

.. figure:: /screenshots/22.png
   :alt: Callmonitor: Testanruf

   Callmonitor: Testanruf

| 

Die Maske sollte weitgehend selbsterklärend sein. Unter "Ereignis" kann
man einstellen, welches `Ereignis <listeners.html#Format>`__ simuliert
werden soll. Die Quellrufnummer ist diejenige, von der dieses Ereignis
ausgeht und die Zielrufnummer diejenige, die das Ziel des Ereignisses
ist. Man gibt jeweils ein Ereignis mit Rufnummern ein, die zu einem in
den Listeners definierten Muster passen. Nach einem Klick auf
"Testanruf" sollte der Callmonitor nun die zu diesem Listener-Eintrag
gehörende Aktion ausführen. Im Webinterface werden die
Debug-Informationen des Callmonitors angezeigt, die bei einer
eventuellen Fehlersuche helfen.

-  Tags
-  `callmonitor </tags/callmonitor>`__
