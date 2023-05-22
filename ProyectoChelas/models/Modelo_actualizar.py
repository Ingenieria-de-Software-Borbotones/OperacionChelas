from alchemyClasses.Vendedor import Vendedor
from alchemyClasses.Producto import Producto

# TODO. Cuando se use, verificar antes que el vendedor no sea None, pues en caso de cambiar el correo no habrá manera.
def actualizar_V(correo, nuevo_correo, nueva_contrasenia, nueva_edad):
    '''
    Se ingresa el correo del vendedor y se busca actualizar los demás argumentos.
    :param correo: correo del vendedor a actualizar.
    :param nuevo_correo: correo a sustituir.
    :nueva_contrasenia: contraseña a sustituir.
    :nueva_edad: edad a sustituir.
    :return bool: True si existe el vendedor y se realizó al menos un cambio. False en otro caso.
    '''
    try:
        vendedor = Vendedor.query.filter(Vendedor.correo == correo).first()
        cambio = verificar_cambios_V(vendedor, nuevo_correo, nueva_contrasenia, nueva_edad)
        if nueva_contrasenia is not None:
            vendedor.set_contrasena_v(nueva_contrasenia)
        if nuevo_correo is not None:
            vendedor.set_correo_v(nuevo_correo)
        if nueva_edad is not None:
            vendedor.edad = nueva_edad
        return True if existencia(vendedor) and cambio else False
    except:
        return False

def existencia(elem):
    '''
    Verifica que el argumento no sea None.
    :param elem: Vendedor o Producto.
    '''
    return elem is not None


def verificar_cambios_V(vendedor, nuevo_correo, nueva_contrasenia, nueva_edad):
   '''
   Verifica que los elementos introducidos sean distintos a los datos del Vendedor.
   :param vendedor: vendedor.
   :param nuevo_correo: correo a sustituir.
   :param nueva_contrasenia: contraseña a sustituir.
   :param nueva_edad: edad a sustituir.
   '''
   if existencia(vendedor):
    aux = nuevo_correo != vendedor.correo or nueva_contrasenia != vendedor.contrasena
    return aux or nueva_edad != vendedor.edad
   return False

def verificar_cambios_P(producto, nuevo_id, nuevo_nombre, nuevo_precio):
   '''
   Verifica que los elementos introducidos sean distintos a los datos del Vendedor.
   :param producto: producto.
   :param nuevo_id: id a sustituir.
   :param nuevo_precio: precio a sustituir.
   :param nuevo_nombre: nombre a sustituir.
   '''
   if existencia(producto):
    aux = nuevo_id != producto.id_producto or nuevo_nombre != producto.nombre_producto
    return aux or nuevo_precio != producto.precio
   return False

# TODO. Cuando se use, verificar antes que el producto no sea None, pues en caso de cambiar el id no habrá manera.
def actualizar_P(id, nuevo_id, nuevo_nombre, nuevo_precio):
    '''
    Se ingresa el id del producto y los datos a modificar.
    :param id: id del producto.
    '''
    try:
        producto = Producto.query.filter(Vendedor.id_producto == id).first()
        if nuevo_nombre is not None:
            producto.nombre_producto = nuevo_nombre
        if nuevo_precio is not None:
            producto.precio = nuevo_precio
        if nuevo_id is not None:
            producto.id_producto = nuevo_id
        return True
    except:
        return False