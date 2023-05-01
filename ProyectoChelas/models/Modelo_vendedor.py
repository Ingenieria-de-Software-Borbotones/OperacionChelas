from alchemyClasses.Vendedor import Vendedor

def verifica_correo_v(correo):
    '''
    Verifica que exista un Vendedor con ese correo en la base de datos.
    :param correo: el correo con el que se quiere verificar.
    :return: Vendedor si existe, None en otro caso.
    '''
    ans = Vendedor.query.filter(Vendedor.correo == correo).first()
    return ans

def verifica_contr_v(vendedor, contrasena):
    '''
    Verifica que dado un Vendedor la contrasena dada sea correcta.
    :param contrasena: la contrasena dada por el usuario.
    :return: True si es correcta, False en otro caso.
    '''
    return contrasena == vendedor.contrasena