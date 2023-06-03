from flask import Blueprint, render_template, session, flash
from alchemyClasses.Cliente import Cliente

consultarClienteBlueprint = Blueprint('consultar_cliente', __name__)

@consultarClienteBlueprint.route('/consultar-cliente', methods=['GET'])
def consultar_cliente():
    # Obtener el correo almacenado en la sesión
    correo = session.get('correo')

    # Verificar si el correo está presente en la sesión
    if correo:
        # El correo está presente en la sesión, puedes utilizarlo para consultar los datos del cliente
        cliente = Cliente.query.filter_by(correo_cliente=correo).first()

        # Resto del código para mostrar los datos del cliente en la plantilla...
        return render_template('ConsultarCliente.html', cliente=cliente)

    else:
        # El correo no está presente en la sesión, redirigir o mostrar un mensaje de error
        flash('Debes iniciar sesión primero')
