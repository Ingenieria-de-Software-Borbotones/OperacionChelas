from alchemyClasses.administrador import Administrador

def verifica_correo_a(correo):
    '''
    Verifica que exista un Administrador con ese correo en la base de datos.
    :param correo: el correo con el que se quiere verificar.
    :return: Administrador si existe, None en otro caso.
    '''
    ans = Administrador.query.filter(Administrador.correo_admin == correo).first()
    return ans

def verifica_contr_a(admin, contrasena):
    '''
    Verifica que dado un Administrador la contrasena dada sea correcta.
    :param contrasena: la contrasena dada por el usuario.
    :return: True si es correcta, False en otro caso.
    '''
    return contrasena == admin.contrasena_admin