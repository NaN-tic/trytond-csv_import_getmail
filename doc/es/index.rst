==================================================
Importar CSV desde recepción de correo electrónico
==================================================

Importa registros desde ficheros csv enviados por correo electrónico.

Configuración
=============

 * Configure una cuenta de correo electrónico de entrada IMAP a través del menú
|menu_getmail_server_form| tal y como se indica para el módulo Recepción de
correo electrónico, y relacionarlo con el modelo "Importaciones CSV".

 * Cree una acción planificada a accediendo al menú |menu_cron_form| y asigne
al campo "Modelo" el modelo "getmail.server" y al campo "Función" el valor
"getmail_servers" (en ambos casos sin las dobles comillas).

.. |menu_getmail_server_form| tryref:: getmail.menu_getmail_server_form/complete_name
.. |menu_cron_form| tryref:: ir.menu_cron_form/complete_name
