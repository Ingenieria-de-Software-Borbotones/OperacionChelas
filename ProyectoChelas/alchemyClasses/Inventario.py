from alchemyClasses.__init__ import db

class Inventario(db.Model):
    '''
    Clase de Inventario de la base de datos
    '''
    id_inventario = db.Column('id_inventario', db.Integer, primary_key = True)
    fecha_inv = db.Column('fecha_inv', db.Date)
    correo_inv = db.Column('correo_inv', db.String(50))

    def __int__(self, id_inventario, fecha_inv, correo_inv):
        '''
        Init de Inventario
        :param id_inventario: id del Inventario
        :param fecha_inv: fecha en la que se genero este Inventario
        :param correo_inv: correo del Vendedor que genero este Inventario
        '''
        self.id_inventario = id_inventario
        self.fecha_inv = fecha_inv
        self.correo_inv = correo_inv

    def set_id_inv(self, id_inventario):
        '''
        Asigna un valor al atributo id_inventario
        :param id_inventario: id para el Inventario
        '''
        self.id_inventario = id_inventario

    def set_fecha_inv(self, fecha_inv):
        '''
        Asigna un valor al atributo fecha_inv
        :param fecha_inv: fecha en la que se genero este Inventario
        '''
        self.fecha_inv = fecha_inv

    def set_correo_inv(self, correo_inv):
        '''
        Asigna un valor al atributo correo_inv
        :param correo_inv: correo del Vendedor que genero este Inventario
        '''
        self.correo_inv = correo_inv

    def inv_a_bd(self):
        '''
        Agrega este Inventario a la base de datos
        '''
        db.session.add(self)
        db.session.commit()