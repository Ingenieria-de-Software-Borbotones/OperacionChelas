from flask import Flask
from flask import render_template
from controllers.inicio import inicioBlueprint
from controllers.login import loginBlueprint
from controllers.logout import logoutBlueprint
from controllers.inventario import inventarioBlueprint
from controllers.consultarv import consultarRvBlueprint
from alchemyClasses.administrador import db
from controllers.cambiarContrasena import cambiarContrasenaBlueprint
from controllers.consultarCliente import consultarClienteBlueprint
from controllers.actualizarCliente import actualizarClienteBlueprint
from controllers.darDeBajaCliente import darDeBajaClienteBlueprint


app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(inicioBlueprint)
app.register_blueprint(loginBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(inventarioBlueprint)
app.register_blueprint(consultarRvBlueprint)
app.register_blueprint(cambiarContrasenaBlueprint)
app.register_blueprint(consultarClienteBlueprint)
app.register_blueprint(actualizarClienteBlueprint)
app.register_blueprint(darDeBajaClienteBlueprint)






# Agregar su informacion de donde tengan la base de datos
# Administrador -> diego@unCorreo.com | nose666 | Diego Martinez Calzada | 20
# Vendedor -> arjona@unCorreo.com | que-bien-canto | Edgar Ricardo Arjona Morales | 59
# Cliente -> epi@unCorreo.com | el-epi | Epigmenio Perez Lopez | 71 | Avenida siempre viva
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Turandot450;@localhost:3306/operacionchelas_administrador"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Turandot450;@localhost:3306/base" ----DESCOMENTAR ESTO----
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:5665@localhost:3306/base"

app.config.from_mapping(
    SECRET_KEY = 'dev'
)

db.init_app(app)

@app.route('/')
def hello_world():
    #return 'Hello world'
    return render_template('PantallaPrincipal.html')

if __name__ == '__main__':
    app.run()