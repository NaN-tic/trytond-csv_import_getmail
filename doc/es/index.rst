==========================================================
CSV Import. Importación CSV a partir de correo electrónico
==========================================================

Importa registros desde ficheros CSV enviados por correo electrónico.

* Configure una cuenta de correo electrónico de entrada IMAP a través del menú
  Getmail Server tal y como se indica para el módulo Recepción de
  correo electrónico, y relacionarlo con el modelo "Importaciones CSV".

* Cree una acción planificada a accediendo al menú Administración/Acciones planificadas
  y asigne al campo "Modelo" el modelo "getmail.server" y al campo "Función" el valor
  "getmail_servers" (en ambos casos sin las dobles comillas).
