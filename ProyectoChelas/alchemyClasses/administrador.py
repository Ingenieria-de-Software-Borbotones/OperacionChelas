from alchemyClasses.__init__ import db

class Administrador(db.Model):

    correo_admin = db.Column('correo_admin', db.String(50), primary_key=True)
    contrasena_admin = db.Column('contrasena_admin', db.String(50))
    nombre_admin = db.Column('nombre_admin', db.String(50))
    edad_admin = db.Column('edad_admin', db.Integer)

    def __int__(self, correo, contrasena, nombre=None, edad=None):
        self.correo_admin = correo
        self.contrasena_admin = contrasena
        self.nombre_admin = nombre
        self.edad_admin = edad

    def set_correo_a(self, correo):
        self.correo_admin = correo

    def set_contrasena_a(self, contrasena):
        self.contrasena_admin = contrasena