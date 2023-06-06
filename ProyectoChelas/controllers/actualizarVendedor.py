from flask import Blueprint, render_template, request, session
#from models.Modelo_actualizar import actualizar_V
from alchemyClasses.Vendedor import Vendedor
from alchemyClasses.__init__ import db

actualizarVendedorBlueprint = Blueprint('actualizar_vendedor', __name__)

@actualizarVendedorBlueprint.route('/actualizar-vendedor', methods=['GET', 'POST'])
def actualizar_vendedor():
    mensaje_exito = ''
    mensaje_error = ''

    # Obtener el correo del vendedor desde la sesión
    correo = session.get('correo')

    # Obtener el vendedor desde la base de datos
    vendedor = Vendedor.query.filter_by(correo=correo).first()

    if request.method == 'POST':
        # Obtener los datos del formulario
        contrasena = request.form.get('contrasena')
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')

        # Actualizar los datos del vendedor en la base de datos
        if vendedor:
            vendedor.set_contrasena_v(contrasena)
            vendedor.set_nombre_v(nombre)
            vendedor.set_edad_v(edad)
            db.session.commit()

            mensaje_exito = 'Los datos se actualizaron correctamente.'
        else:
            mensaje_error = 'No se encontró el vendedor en la base de datos.'

    # Renderizar el formulario con los datos existentes del vendedor
    if vendedor:
        return render_template('ActualizarVendedor.html', vendedor=vendedor, mensaje_exito=mensaje_exito, mensaje_error=mensaje_error)
    else:
        mensaje_error = 'No se encontró el vendedor en la base de datos.'
        return render_template('ActualizarVendedor.html', mensaje_error=mensaje_error)