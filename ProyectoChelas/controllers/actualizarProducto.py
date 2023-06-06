from flask import Blueprint, render_template, request, session
from alchemyClasses.Producto import Producto
from alchemyClasses.__init__ import db

actualizarProductoBlueprint = Blueprint('actualizar_producto', __name__)

@actualizarProductoBlueprint.route('/actualizar-producto', methods=['GET', 'POST'])
def actualizar_producto():
    mensaje_exito = ''
    mensaje_error = ''
    menu = """
        ID  |  NOMBRE
        1   |  Cerveza
        2   |  Azulito
        3   |  Tonayan   
    """

    # Obtener el id
    id = request.form.get('id')

    # Obtener el producto desde la base de datos
    producto = Producto.query.filter_by(id_producto=id).first()

    if request.method == 'POST':
        # Obtener los datos del formulario
        #id = request.form.get('id')           # HTML
        nombre = request.form.get('nombre')
        precio = request.form.get('precio')

        # Actualizar los datos del producto en la base de datos
        if producto:
            #producto.set_id_producto(id)
            producto.set_nombre_producto(nombre)
            producto.set_precio(precio)
            db.session.commit()

            mensaje_exito = 'Los datos se actualizaron correctamente.'
        else:
            mensaje_error = 'No se encontró el producto en la base de datos.'

    # Renderizar el formulario con los datos existentes del producto
    if producto:
        return render_template('ActualizarProducto.html', producto=producto, mensaje_exito=mensaje_exito, mensaje_error=mensaje_error)
    else:
        mensaje_error = 'Aún no ingresa un id o no se ha registrado el producto.'
        return render_template('ActualizarProducto.html', mensaje_error=mensaje_error)
