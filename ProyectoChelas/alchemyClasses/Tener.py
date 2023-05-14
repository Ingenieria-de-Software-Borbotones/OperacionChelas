from alchemyClasses.__init__ import db

class Tener(db.Model):
    '''
    Clase de Tener de la base de datos
    '''
    id_tener = db.Column('id_tener', db.Integer, primary_key = True)
    id_inventario_t = db.Column('id_inventario_t', db.Integer)
    id_producto_t = db.Column('id_producto_t', db.Integer)
    cantidad = db.Column('cantidad', db.Integer)

    def __int__(self, id_tener, id_inventario_t, id_producto_t, cantidad):
        '''
        Init de Tener
        :param id_tener: id de Iener de la base de datos
        :param id_inventario_t: id del Inventario al que pertenece Tener
        :param id_producto_t: id del Producto que tiene el Inventario
        :param cantidad: cantidad del Producto que tiene el Inventario
        :return:
        '''
        self.id_tener = id_tener
        self.id_inventario_t = id_inventario_t
        self.id_producto_t = id_producto_t
        self.cantidad = cantidad

    def set_id_tener(self, id_tener):
        '''
        Asigna un valor al atributo id_tener
        :param id_tener: id para Iener de la base de datos
        '''
        self.id_tener = id_tener

    def set_id_inventario_t(self, id_inventario_t):
        '''
        Asigna un valor al atributo id_inventario_t
        :param id_inventario_t: id del Inventario al que pertenece id_producto
        '''
        self.id_inventario_t = id_inventario_t

    def set_id_producto_t(self, id_producto_t):
        '''
        Asigna un valor al atributo id_producto_t
        :param id_producto_t: id del Producto al que pertenece
        '''
        self.id_producto_t = id_producto_t

    def set_cantidad(self, cantidad):
        '''
        Asigna un valor al atributo id_producto_t
        :param cantidad: cantidad de Producto que esta en el Inventario
        '''
        self.cantidad = cantidad

    def tener_a_bd(self):
        '''
        Agrega este Tener a la base de datos
        :return:
        '''
        db.session.add(self)
        db.session.commit()