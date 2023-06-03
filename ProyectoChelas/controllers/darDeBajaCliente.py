import time
from flask import Blueprint, render_template, request, session, redirect, url_for
from alchemyClasses.Cliente import Cliente
from alchemyClasses.__init__ import db

darDeBajaClienteBlueprint = Blueprint('dar_de_baja_cliente', __name__)

@darDeBajaClienteBlueprint.route('/dar-de-baja-cliente', methods=['GET', 'POST'])
def dar_de_baja_cliente():
    mensaje_confirmacion = ''

    # Obtener el correo del cliente desde la sesión
    correo = session.get('correo')

    # Obtener el cliente desde la base de datos
    cliente = Cliente.query.filter_by(correo_cliente=correo).first()

    if request.method == 'POST':
        # Obtener la contraseña y confirmarla
        contrasena = request.form.get('contrasena')
        confirmar_contrasena = request.form.get('confirmar_contrasena')

        if contrasena == confirmar_contrasena:
            # Verificar si la contraseña coincide con la del cliente
            if cliente.get_contrasena_cliente() == contrasena:
                # Eliminar el cliente de la base de datos
                db.session.delete(cliente)
                db.session.commit()

                # Limpiar la sesión
                session.clear()

                # Mostrar mensaje de confirmación
                mensaje_confirmacion = '¡Tu cuenta ha sido eliminada! Serás redireccionado al inicio de sesión en unos segundos...'

                # Pausa de 3 segundos antes de redirigir
                time.sleep(3)

                # Redirigir al inicio de sesión
                return redirect(url_for('login.login'))
            else:
                mensaje_confirmacion = 'La contraseña no coincide con la del cliente.'
        else:
            mensaje_confirmacion = 'Las contraseñas no coinciden.'

    return render_template('DarDeBajaCliente.html', cliente=cliente, mensaje_confirmacion=mensaje_confirmacion)
