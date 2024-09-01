# pre-MaximilianoBrandi
3er pre-entrega Python CODERHOUSE 

La pre-entrega se basa en el diseño de un proyecto para un estudio de abogacia.
Tiene 4 botones en la pagina de inicio los cuales son:
1- Inicio
2- Clientes
3- Asesoramientos
4- Citas

1- Inicio:
Inicio lleva al Home, en cualquier parte de la pagina que nos encontremos.
A futuro se incorporara fotos y datos del estudio jurídico.

2- Clientes:
En la página se muestra un listado de los clientes registrados, visaulizando Apellido, nombre y teléfono.
Tiene un botón para dar de alta nuevos clientes, al presionarlo se abre un formulario para agregar los siguientes datos:
    * dni es un campo obligatorio e id para que no haya clientes repetidos
    * nombre y apellido, y teléfono son campos obligatorios
        El contacto con el cliente será telefónicamente.
    * email es opcional
Una vez cargado el cliente se presiona "Registrar". 
Luego vuelve a la página de Cliente para mostrar que fue agregado.
Para modificar algún dato del cliente / eliminar un cliente (método CASCADE) se debe ingresar como administrador.
Para entrar como adminitrador ir a la página: http://127.0.0.1:8000/admin/ y loguearse con los siguientes datos:
Usuario: admin
password: 123

3- Asesoramientos:
En la página se muestra un listado de los asesoramientos registrados en los derechos que brinda el estudio y una descripción de los mismos. 
Tiene un botón para dar de alta nuevos Asesoramientos, al presionarlo se abre un formulario para agregar los siguientes datos:
    * derecho, es un campo obligatorio e id para que no haya derechos repetidos
    * descripción es un campo obligatorio
    * disponible, si se pulsa en el casillero está disponible, si se deja en blanco no estará disponible
Una vez cargado el Asesoramiento se presiona "Registrar". 
Luego vuelve a la página de Asesoramientos para mostrar que fue agregado.
Para modificar nombre, descripción o cambiar su status de "disponible" a "no disponible" / eliminar un asesoramiento (método CASCADE), debe ingresar como administrador.
Para entrar como administrador ir a la página: http://127.0.0.1:8000/admin/ y loguearse con los siguientes datos:
Usuario: admin
password: 123

4- Citas
En la página se muestra un listado de las citas registradas, visualizando:
Nombre, Apellido y DNI del cliente que generó una cita, su nro de teléfono para contactarlo, el motivo de su consulta y la fecha y hora agendada. Si no tiene fecha y hora agendada muestra "NONE - Pendiente"
De esta manera puede hacerse un seguimiento de la agenda de compromisos.
Tiene un botón para dar de alta nuevas Citas, al presionarlo se abre un formulario para agregar los siguientes datos:
    * Cliente, es un ForeingKey a Clientes, por lo tanto se selecciona de un menú desplegable
    * Derecho, es un ForeingKey a Asesoramiento, por lo tanto se selecciona de un menú desplegable. Solo muestra los asesoramientos en derechos que están disponibles.
    * Motivo de la consulta, campo Text Fields para que pueda explicar en detalle su consulta
    * (Fecha de consulta) - No aparece pero guarda el día de hoy
    * Fecha de cita, aparece un calendario donde clickear el día, o muestra una plantilla para digitarlo
    * Hora aparece un reloj donde clickear la hora y los minutos, o muestra una plantilla para digitarlo
    * Permite seleccionar el estado como Pendiente, Agendada o Atendido.
Una vez cargada la cita se presiona "Registrar". 
Luego vuelve a la página de Citas para mostrar que fue agregada.
Para modificar los datos de las citas debe ingresar como administrador.
Para entrar como administrador ir a la página: http://127.0.0.1:8000/admin/ y loguearse con los siguientes datos:
Usuario: admin
password: 123

El funcionamiento fue probado agregando datos en la base de datos como administrador, y también a través de los botones y formularios de la página.
