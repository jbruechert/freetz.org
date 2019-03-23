help/howtos/troubleshoot/recover_firmware
=========================================
.. _OriginalFirmwarewiederherstellen:

Original Firmware wiederherstellen
==================================

Wenn die Box nicht mehr ansprechbar ist, die Power LED leuchtet und die
übrigen LEDs in regelmäßigen Abständen aufblinken, dann kann folgende
Vorgehensweise die Box wieder zum Leben erwecken. In diesen Fällen ist
mtd1 (Kernel + Filesystem) betroffen, nicht mtd3 / mtd4 (|/!\\| mtd2 auf
**KEINEN** Fall anrühren).

#. Der Computer muss sich im gleichen Subnetz (und auch
   Broadcast-Domäne) wie die Box befinden: 192.168.178.0/24 (|/!\\|
   Achtung: Die Boot-IP der Box muss nicht gleich der IP im normalen
   Betrieb sein!)
#. ``make recover``
#. Den Anweisungen folgen (zur Zeit leider nicht bei allen
   Fritzbox-Typen möglich)

Am bequemsten funktioniert es, wenn nach einem ``make`` Freetz noch
nicht mit ``make clean``, ``make dirclean`` oder ``make distclean``
bereinigt wurde, und noch eine für die Box passende Konfiguartion des
Mods vorhanden ist. In diesem Fall lädt ``make recover`` die
unmodifizierte original Firmware auf die Box.

-  Tags
-  `firmware </tags/firmware>`__
-  `howtos </tags/howtos>`__

.. |/!\\| image:: ../../../../chrome/wikiextras-icons-16/exclamation.png

