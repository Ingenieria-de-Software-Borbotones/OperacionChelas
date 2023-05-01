from alchemyClasses.__init__ import db

class Estar(db.Model):

    id_estar = db.Column('id_estar', db.Integer, primary_key = True)
    id_producto_e = db.Column('id_producto_e', db.Integer)
    id_pedido_e = db.Column('id_pedido_e', db.Integer)

    def __int__(self, id_estar, id_producto_e, id_pedido_e):
        self.id_estar = id_estar
        self.id_producto_e = id_producto_e
        self.id_pedido_e = id_pedido_e