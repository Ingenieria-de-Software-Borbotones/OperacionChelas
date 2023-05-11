from alchemyClasses.Producto import Producto

def obten_todo():
    '''
    Regresa la informacion de todos los productos de la base de datos
    :return: Lista de Producto
    '''
    return Producto.query.all()