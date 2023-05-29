from flask import Flask
from flask import render_template
from controllers.inicio import inicioBlueprint
from controllers.login import loginBlueprint
from controllers.logout import logoutBlueprint
from controllers.inventario import inventarioBlueprint
from controllers.consultarv import consultarRvBlueprint
from alchemyClasses.administrador import db

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(inicioBlueprint)
app.register_blueprint(loginBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(inventarioBlueprint)
app.register_blueprint(consultarRvBlueprint)

# Agregar su informacion de donde tengan la base de datos
# Administrador -> diego@unCorreo.com | nose666 | Diego Martinez Calzada | 20
# Vendedor -> arjona@unCorreo.com | que-bien-canto | Edgar Ricardo Arjona Morales | 59
# Cliente -> epi@unCorreo.com | el-epi | Epigmenio Perez Lopez | 71 | Avenida siempre viva
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Turandot450;@localhost:3306/operacionchelas_administrador"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Turandot450;@localhost:3306/base"
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