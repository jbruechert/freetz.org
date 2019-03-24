.. _RokuSoundBridge:

Roku SoundBridge
================

Die `​Roku
SoundBridge <http://www.rokulabs.com/products_soundbridge.php>`__ kann
auf ihrem Display Nachrichten darstellen. Seit Callmonitor 1.12.4 stehen
drei Funktionen zur Ansteuerung zur Verfügung:

.. code:: wiki

     sbmessage
     (default_sbmessage)

Zur Anzeige einer statischen Nachricht. Mit der Umgebungsvariable
``SB_TIMEOUT`` kann die Dauer der Anzeige bestimmt werden.

.. code:: wiki

     sbmarquee
     (default_sbmarquee)

Zur Anzeige eines Lauftexts. Mit der Umgebungsvariable ``SB_TIMES`` kann
festgelegt werden, wie oft die Nachricht wiederholt werden soll.

.. code:: wiki

     sbxmessage
     (default_sbxmessage)

Zur Anzeige einer statischen, mehrzeiligen Nachricht. Mit der
Umgebungsvariable SB_TIMEOUT kann die Dauer der Anzeige bestimmt werden.
