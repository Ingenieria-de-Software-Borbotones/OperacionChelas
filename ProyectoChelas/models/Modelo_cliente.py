from alchemyClasses.Cliente import Cliente

def verifica_correo_c(correo):
    '''
    Verifica que exista un Cliente con ese correo en la base de datos.
    :param correo: el correo con el que se quiere verificar.
    :return: Vendedor si existe, None en otro caso.
    '''
    ans = Cliente.query.filter(Cliente.correo_cliente == correo).first()
    return ans

def verifica_contr_c(cliente, contrasena):
    '''
    Verifica que dado un Cliente la contrasena dada sea correcta.
    :param contrasena: la contrasena dada por el usuario.
    :return: True si es correcta, False en otro caso.
    '''
    return contrasena == cliente.contrasena_cliente