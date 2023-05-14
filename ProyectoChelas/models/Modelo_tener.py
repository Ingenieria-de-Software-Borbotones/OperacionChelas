from alchemyClasses.Tener import Tener

def nuevo_tener(id_inventario_t, id_producto_t, cantidad):
    '''
    Crea un nuevo tener y lo almacena en la base de datos
    :return: El Tener recien creado
    '''
    mas_reciente = Tener.query.order_by(Tener.id_tener.desc()).first()
    nuevo_id = 1
    if mas_reciente:
        nuevo_id = mas_reciente.id_tener + 1
    nuevo_tener = Tener()
    nuevo_tener.set_id_tener(nuevo_id)
    nuevo_tener.set_id_inventario_t(id_inventario_t)
    nuevo_tener.set_id_producto_t(id_producto_t)
    nuevo_tener.set_cantidad(cantidad)
    nuevo_tener.tener_a_bd()
    return nuevo_tener