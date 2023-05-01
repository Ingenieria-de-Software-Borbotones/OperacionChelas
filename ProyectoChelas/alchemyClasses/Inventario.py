from alchemyClasses.__init__ import db

class Inventario(db.Model):

    id_inventario = db.Column('id_inventario', db.Integer, primary_key = True)
    fecha_inv = db.Column('fecha_inv', db.Date)
    correo_inv = db.Column('correo_inv', db.String(50))

    def __int__(self, id_inventario, fecha_inv, correo_inv):
        self.id_inventario = id_inventario
        self.fecha_inv = fecha_inv
        self.correo_inv = correo_inv