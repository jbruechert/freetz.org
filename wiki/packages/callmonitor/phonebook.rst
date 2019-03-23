packages/callmonitor/phonebook
==============================
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

.. _TelefonbuchCallers:

Telefonbuch (Callers)
=====================

Format:

   <Rufnummer mit Vorwahl>\ ````\ <Name>(``;`` <Adresse>)

Ergebnisse der `Rückwärtssuche <reverse_search.html>`__ können hier
gespeichert werden für schnelleren Zugriff in der Zukunft; natürlich
können auch von Hand Nummer-Name-Paare eingetragen oder geändert werden

-  49er-Rufnummern (ohne 00, länger als 10 Zeichen) werden erkannt
-  Name des Angerufenen steht zur Verfügung (vor allem für SIP0 bis
   SIP9); man kann die Zuordnung zu Namen im Telefonbuch (Callers)
   vornehmen, entweder direkt für SIP0 bis SIP9 oder für Adressen der
   Form "username@registrar" (das zweite hat den Vorteil, dass man im
   Telefonbuch nichts anpassen muss, wenn man seine SIP-Accounts in
   anderer Reihenfolge einträgt). Beim Start werden Kurznamen für alle
   Accounts generiert und als Vorgabe in die Callers eingetragen.
-  Suchstrategie: Erst Nummer unverändert in den lokalen Telefonbüchern
   (Callers, AVM-Telefonbuch) nachschlagen, dann normalisieren (evtl.
   Orts- /Landesvorwahl davor; SIP[0-9] wird zu username@registrar) und
   noch einmal lokal probieren. Dann erst über Rückwärtssuche im
   Internet probieren.

.. figure:: /screenshots/216.png
   :alt: Callmonitor Callers

   Callmonitor Callers

| 

-  Tags
-  `callmonitor </tags/callmonitor>`__
