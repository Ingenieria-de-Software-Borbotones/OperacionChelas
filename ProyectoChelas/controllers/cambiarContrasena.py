from flask import Blueprint, render_template, request, session
from alchemyClasses.Vendedor import Vendedor
from alchemyClasses.__init__ import db

cambiarContrasenaBlueprint = Blueprint('cambiar_contrasena', __name__)

@cambiarContrasenaBlueprint.route('/cambiar-contrasena', methods=['GET', 'POST'])
def cambiar_contrasena():
    mensaje_exito = ''
    mensaje_error = ''

    # Obtener el correo del vendedor desde la sesión
    correo = session.get('correo')

    # Obtener el vendedor desde la base de datos
    vendedor = Vendedor.query.filter_by(correo=correo).first()

    if request.method == 'POST':
        # Obtener los datos del formulario
        nueva_contrasena = request.form.get('nueva_contrasena')
        confirmar_contrasena = request.form.get('confirmar_contrasena')

        # Validar que las contraseñas coincidan
        if nueva_contrasena == confirmar_contrasena:
            # Cambiar la contraseña del vendedor en la base de datos
            if vendedor:
                vendedor.set_contrasena_v(nueva_contrasena)
                db.session.commit()

                mensaje_exito = 'La contraseña se cambió correctamente.'
            else:
                mensaje_error = 'No se encontró el vendedor en la base de datos.'
        else:
            mensaje_error = 'Las contraseñas no coinciden.'

    return render_template('ActualizarContrasenaVendedor.html', vendedor=vendedor, mensaje_exito=mensaje_exito, mensaje_error=mensaje_error)
