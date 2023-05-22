from flask import Flask
from flask import render_template
from controllers.inicio import inicioBlueprint
from controllers.login import loginBlueprint
from controllers.logout import logoutBlueprint
from controllers.inventario import inventarioBlueprint
from alchemyClasses.administrador import db

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(inicioBlueprint)
app.register_blueprint(loginBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(inventarioBlueprint)

# Agregar su informacion de donde tengan la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"
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