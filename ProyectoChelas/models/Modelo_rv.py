from alchemyClasses.Reporte import Reporte

def obten_reportes_venta(id=None, correo=None, fecha=None):
    '''
    Obtiene Reportes que cumplan con tener esos atributos
    :param id: id con el que se quiere buscar el Reporte
    :param correo: correo con el que se quiere buscar el Reporte
    :param fecha: fecha con el que se quiere buscar el Reporte
    :return: lista de Reporte
    '''
    query = Reporte.query
    if id is not None and id is not '':
        query = query.filter(Reporte.id_reporte == id)
    if correo is not None and correo is not '':
        query = query.filter(Reporte.correo_rep == correo)
    if fecha is not None and fecha is not '':
        query = query.filter(Reporte.fecha_rep == fecha)
    reportes = query.all()
    return reportes