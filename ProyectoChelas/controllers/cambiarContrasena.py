from flask import Blueprint, render_template, request
from alchemyClasses.__init__ import db
from alchemyClasses.Vendedor import Vendedor

cambiarContrasenaBlueprint = Blueprint('cambiar_contrasena', __name__)

@cambiarContrasenaBlueprint.route('/cambiar-contrasena', methods=['GET', 'POST'])
def cambiar_contrasena():
    if request.method == 'POST':
        correo = request.form.get('correo')
        nueva_contrasena = request.form.get('nueva_contrasena')
        confirmar_contrasena = request.form.get('confirmar_contrasena')

        # Verificar si el correo existe en la base de datos
        vendedor = Vendedor.query.filter_by(correo=correo).first()
        if vendedor:
            if nueva_contrasena == confirmar_contrasena:
                vendedor.set_contrasena_v(nueva_contrasena)
                db.session.commit()
                mensaje_exito = 'Contraseña cambiada exitosamente.'
                return render_template('ActualizarContrasenaVendedor.html', mensaje_exito=mensaje_exito)
            else:
                mensaje_error = 'Las contraseñas no coinciden. Por favor, inténtalo de nuevo.'
                return render_template('ActualizarContrasenaVendedor.html', mensaje_error=mensaje_error)
        else:
            mensaje_error = 'El correo proporcionado no está registrado en nuestra base de datos.'
            return render_template('ActualizarContrasenaVendedor.html', mensaje_error=mensaje_error)

    return render_template('ActualizarContrasenaVendedor.html')
