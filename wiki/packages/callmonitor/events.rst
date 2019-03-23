packages/callmonitor/events
===========================
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

.. _Ereignisse:

Ereignisse
==========

Ein erfolgreicher eingehender Anruf erzeugt nacheinander folgende
Ereignisse (analog für ausgehende Anrufe mit ``out:*``):

#. in:request
#. in:connect
#. in:disconnect

Ein Anruf, der abgebrochen wird, bevor die Gegenseite ihn annimmt,
erzeugt folgende Ereignisse:

#. in:request
#. in:cancel

Die Ereignisse sind nicht direkt die Rohereignisse, wie sie an der
JFritz-Schnittstelle (Port 1012) sichtbar sind, sondern entstehen aus
diesen (bei gleicher ID) mit Hilfe eines endlichen Automaten (an den
Kanten sind oben die Eingangsereignisse angegeben, unten die
Ausgangsereignisse; das Ereignis ``in:accept`` wird nur intern benutzt):

.. figure:: /screenshots/36.png
   :alt: CallMonitor: Ereignisse

   CallMonitor: Ereignisse

-  Tags
-  `callmonitor </tags/callmonitor>`__
