from alchemyClasses.__init__ import db

class Pedido(db.Model):

    id_pedido = db.Column('id_pedido', db.Integer, primary_key = True)
    correo_ped = db.Column('correo_ped', db.String(50))
    id_reporte_ped = db.Column('id_reporte_ped', db.Integer)
    estatus = db.Column('estatus', db.String(50))
    total = db.Column('total', db.Float)

    def __int__(self, id_pedido, correo_ped, id_reporte_ped, estatus, total):
        self.id_pedido = id_pedido
        self.correo_ped = correo_ped
        self.id_reporte_ped = id_reporte_ped
        self.estatus = estatus
        self.total = total