from alchemyClasses.__init__ import db

class Reporte(db.Model):

    id_reporte = db.Column('id_reporte', db.Integer, primary_key = True)
    correo_rep = db.Column('correo_rep', db.String(50))
    fecha_rep = db.Column('fecha_rep', db.Date)

    def __int__(self, id_reporte, correo_rep, fecha_rep):
        self.id_reporte = id_reporte
        self.correo_rep = correo_rep
        self.fecha_rep = fecha_rep