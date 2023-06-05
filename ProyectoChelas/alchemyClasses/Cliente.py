from alchemyClasses.__init__ import db

class Cliente(db.Model):

    correo_cliente = db.Column('correo_cliente', db.String(50), primary_key = True)
    contrasena_cliente = db.Column('contrasena_cliente', db.String(50))
    nombre_cliente = db.Column('nombre_cliente', db.String(50))
    edad_cliente = db.Column('edad_cliente', db.Integer)
    direccion = db.Column('direccion', db.String(50))

    def __int__(self, correo, contrasena, nombre, edad, direccion):
        self.correo_cliente = correo
        self.contrasena_cliente = contrasena
        self.nombre_cliente = nombre
        self.edad_cliente = edad
        self.direccion = direccion

    def set_correo_c(self, correo):
        self.correo_cliente = correo

    def set_contrasena_c(self, contrasena):
        self.contrasena_cliente = contrasena

    def set_correo_cliente(self, correo):
        self.correo_cliente = correo

    def set_contrasena_cliente(self, contrasena):
        self.contrasena_cliente = contrasena

    def set_nombre_cliente(self, nombre):
        self.nombre_cliente = nombre

    def set_edad_cliente(self, edad):
        self.edad_cliente = edad

    def set_direccion_cliente(self, direccion):
        self.direccion = direccion

    def get_correo_cliente(self):
        return self.correo_cliente

    def get_contrasena_cliente(self):
        return self.contrasena_cliente

    def get_nombre_cliente(self):
        return self.nombre_cliente

    def get_edad_cliente(self):
        return self.edad_cliente

    def get_direccion(self):
        return self.direccion