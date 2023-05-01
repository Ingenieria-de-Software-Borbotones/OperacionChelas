from alchemyClasses.__init__ import db

class Tener(db.Model):

    id_tener = db.Column('id_tener', db.Integer, primary_key = True)
    id_inventario_t = db.Column('id_inventario_t', db.Integer)
    id_producto_t = db.Column('id_producto_t', db.Integer)
    cantidad = db.Column('cantidad', db.Integer)

    def __int__(self, id_tener, id_inventario_t, id_producto_t, cantidad):
        self.id_tener = id_tener
        self.id_inventario_t = id_inventario_t
        self.id_producto_t = id_producto_t
        self.cantidad = cantidad