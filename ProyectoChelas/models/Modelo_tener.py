from alchemyClasses.Tener import Tener

def nuevo_tener(id_inventario_t, id_producto_t, cantidad):
    '''
    Crea un nuevo tener y lo almacena en la base de datos
    :return: El tener recien creado
    '''
    mas_reciente = Tener.query.order_by(Tener.id_tener.desc()).first()
    nuevo_id = 1
    if mas_reciente:
        nuevo_id = mas_reciente.id_tener + 1
    nuevo_inv = Tener(nuevo_id, id_inventario_t, id_producto_t, cantidad)
    nuevo_inv.inv_a_bd()
    return nuevo_inv