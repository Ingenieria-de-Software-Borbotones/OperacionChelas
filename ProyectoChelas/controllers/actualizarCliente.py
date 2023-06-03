from flask import Blueprint, render_template, request, session
from alchemyClasses.Cliente import Cliente
from alchemyClasses.__init__ import db

actualizarClienteBlueprint = Blueprint('actualizar_cliente', __name__)

@actualizarClienteBlueprint.route('/actualizar-cliente', methods=['GET', 'POST'])
def actualizar_cliente():
    mensaje_exito = ''
    mensaje_error = ''

    # Obtener el correo del cliente desde la sesión
    correo = session.get('correo')

    # Obtener el cliente desde la base de datos
    cliente = Cliente.query.filter_by(correo_cliente=correo).first()

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        direccion = request.form.get('direccion')

        # Actualizar los datos del cliente en la base de datos
        if cliente:
            cliente.set_nombre_cliente(nombre)
            cliente.set_edad_cliente(edad)
            cliente.set_direccion_cliente(direccion)
            db.session.commit()

            mensaje_exito = 'Los datos se actualizaron correctamente.'
        else:
            mensaje_error = 'No se encontró el cliente en la base de datos.'

    # Renderizar el formulario con los datos existentes del cliente
    if cliente:
        return render_template('ActualizarCliente.html', cliente=cliente, mensaje_exito=mensaje_exito, mensaje_error=mensaje_error)
    else:
        mensaje_error = 'No se encontró el cliente en la base de datos.'
        return render_template('ActualizarCliente.html', mensaje_error=mensaje_error)
