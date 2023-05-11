from alchemyClasses.__init__ import db

class Inventario(db.Model):

    id_inventario = db.Column('id_inventario', db.Integer, primary_key = True)
    fecha_inv = db.Column('fecha_inv', db.Date)
    correo_inv = db.Column('correo_inv', db.String(50))

    def __int__(self, id_inventario, fecha_inv, correo_inv):
        self.id_inventario = id_inventario
        self.fecha_inv = fecha_inv
        self.correo_inv = correo_inv

    def set_id_inv(self, id_inventario):
        self.id_inventario = id_inventario

    def set_fecha_inv(self, fecha_inv):
        self.fecha_inv = fecha_inv

    def set_correo_inv(self, correo_inv):
        self.correo_inv = correo_inv

    def inv_a_bd(self):
        db.session.add(self)
        db.session.commit()