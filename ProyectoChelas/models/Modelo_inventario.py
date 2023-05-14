from alchemyClasses.Inventario import Inventario

def nuevo_inventario(fecha_inv, correo_inv):
    '''
    Crea un nuevo inventario y lo almacena en la base de datos
    :return: El Inventario recien creado
    '''
    mas_reciente = Inventario.query.order_by(Inventario.id_inventario.desc()).first()
    nuevo_id = 1
    if mas_reciente:
        nuevo_id = mas_reciente.id_inventario + 1
    nuevo_inv = Inventario()
    nuevo_inv.set_id_inv(nuevo_id)
    nuevo_inv.set_fecha_inv(fecha_inv)
    nuevo_inv.set_correo_inv(correo_inv)
    nuevo_inv.inv_a_bd()
    return nuevo_inv