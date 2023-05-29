from alchemyClasses.Estar import Estar
from models.Modelo_producto import obten_producto_id

def obten_productos_estar(id_p):
    '''
    Regresa todos los Productos que esten en el Pedido con id_p
    :param id_p: id del Pedido
    :return: lista de Productos
    '''
    estar = Estar.query.filter(Estar.id_pedido_e == id_p).all()
    productos = []
    for e in estar:
        productos.append(obten_producto_id(e.id_producto_e))
    return productos