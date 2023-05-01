from alchemyClasses.__init__ import db

class Producto(db.Model):

    id_producto = db.Column('id_producto', db.Integer, primary_key = True)
    nombre_producto = db.Column('nombre_producto', db.String(50))
    precio = db.Column('precio', db.Float)

    def __int__(self, id_producto, nombre_producto, precio):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.precio = precio