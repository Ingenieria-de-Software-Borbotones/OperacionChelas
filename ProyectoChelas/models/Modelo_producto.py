from alchemyClasses.Producto import Producto

def obten_todo():
    '''
    Regresa la informacion de todos los productos de la base de datos
    :return: Lista de Producto
    '''
    return Producto.query.all()

def obten_producto_id(id):
    '''
    Regresa el Producto con cierto id
    :param id: id del Producto a buscar
    :return: Producto
    '''
    return Producto.query.get(id)