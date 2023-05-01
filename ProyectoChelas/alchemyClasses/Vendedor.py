from alchemyClasses.__init__ import db

class Vendedor(db.Model):

    correo = db.Column('correo', db.String(50), primary_key = True)
    contrasena = db.Column('contrasena', db.String(50))
    nombre = db.Column('nombre', db.String(50))
    edad = db.Column('edad', db.Integer)

    def __int__(self, correo, contrasena, nombre, edad):
        self.correo = correo
        self.contrasena = contrasena
        self.nombre = nombre
        self.edad = edad

    def set_correo_v(self, correo):
        self.correo = correo

    def set_contrasena_v(self, contrasena):
        self.contrasena = contrasena