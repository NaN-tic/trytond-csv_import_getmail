#:before:csv_import/csv_import:section:ejemplos#

.. inheritref:: csv_import/csv_import:section:importacion_csv_desde_correos_electronicos

Importación CSV desde correos electrónicos
==========================================

Esta opción nos permite a partir de una cuenta de correo electrónico, importar los ficheros CSV del correo.
Los documentos adjuntos CSV se creará automáticamente para ser procesados y importados. ( |menu_csv_archive| )

La cuenta de correo del remitente (quien envía el correo) debe ser agregada como medio
de contacto del tercero ya que cuando se reciba el correo se buscará un tercero que contenga
este correo electrónico. También en los perfiles, añadir que perfil se usará con este cliente
en la pestanya de Terceros del perfil.

Para la activación de la importación consulte la documentación de la sección Getmail y activa
una tarea planificada (cada 10 minutos).

* En el caso de que el correo no contenga un fichero CSV como adjunto, no se procesará ni se creará ningún registro.
* En el caso que de un error, revise los logs del servidor, logs del CSV/Archivo y/o el correo electrónico.
* Assegurase que el usuario Getmail tenga permisos de creación en los registros a importar.

.. |menu_csv_archive| tryref:: csv_import.menu_csv_archive/complete_name
