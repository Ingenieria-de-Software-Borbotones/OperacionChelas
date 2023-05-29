from alchemyClasses.Pedido import Pedido

def obten_pedidos_r_id(r_id):
    '''
    Obtiene los Pedidos que pertenezcan al Reporte con r_id
    :param r_id: id del Reporte
    :return: lista de Pedido
    '''
    return Pedido.query.filter(Pedido.id_reporte_ped == r_id).all()