packages/callmonitor/reverse_search
===================================
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

.. _Rückwärtssuche:

Rückwärtssuche
==============

Die Rückwärtssuche wird in der `Basiskonfiguration <config.html>`__ des
Callmonitors eingestellt. Sie wird bei einem der folgenden Dienste
durchgeführt:

-  `​http://telefonbuch.de/ <http://telefonbuch.de/>`__
-  `​http://inverssuche.de/ <http://inverssuche.de/>`__
-  `​http://goyellow.de/ <http://goyellow.de/>`__
-  `​http://11880.com/ <http://11880.com/>`__
-  `​http://www.dasoertliche.de/ <http://www.dasoertliche.de/>`__
-  `​http://tel.search.ch/ <http://tel.search.ch/>`__
-  `​http://www.das-telefonbuch.at/ <http://www.das-telefonbuch.at/>`__
-  `​http://www.anywho.com/ <http://www.anywho.com/>`__

Optional kann eine zusätzliche Suche bei Google nach dem Ortsnetz des
Anrufers durchgeführt werden. Das Ergebnis dieser Suche wird nur
verwendet, wenn die volle Rückwärtssuche kein Ergebnis liefert.

-  Bei ausgehenden Anrufen wird für die angerufene Nummer ggf. eine
   Anfrage durchgeführt, nicht für die eigene.
-  Rückwärtssuche mit dauerhaftem (im Flash), flüchtigen (im RAM) oder
   ohne Caching möglich

.. figure:: /screenshots/23.png
   :alt: Callmonitor: Rückwärtssuche

   Callmonitor: Rückwärtssuche

| 

-  Tags
-  `callmonitor </tags/callmonitor>`__
