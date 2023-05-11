from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.administrador import Administrador
from models.Modelo_admin import verifica_correo_a
from models.Modelo_admin import verifica_contr_a
from alchemyClasses.Vendedor import Vendedor
from models.Modelo_vendedor import verifica_correo_v
from models.Modelo_vendedor import verifica_contr_v
from alchemyClasses.Cliente import Cliente
from models.Modelo_cliente import verifica_correo_c
from models.Modelo_cliente import verifica_contr_c


# Administrador -> diego@unCorreo.com | nose666 | Diego Martinez Calzada | 20
# Vendedor -> arjona@unCorreo.com | que-bien-canto | Edgar Ricardo Arjona Morales | 59
# Cliente -> epi@unCorreo.com | el-epi | Epigmenio Perez Lopez | 71 | Avenida siempre viva

loginBlueprint = Blueprint('login', __name__, url_prefix='/login')

@loginBlueprint.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]
        if correo == "" or contrasena == "":
            print('ERROR CAMPO VACIO')
            flash("ERROR: campo vacio")
            return redirect(url_for("login.login"))
        if verifica_correo_a(correo) != None:
            a = verifica_correo_a(correo)
            administrador = Administrador()
            administrador.set_correo_a(correo)
            administrador.set_contrasena_a(contrasena)
            if verifica_contr_a(a, contrasena):
                session.clear()
                session['correo'] = administrador.correo_admin
                session['nombre'] = a.nombre_admin
                g.user = administrador.correo_admin
                return redirect(url_for("login.success_admin"))
            else:
                print('ERROR CONTRASENA INCORRECTA DEL ADMINISTRADOR EN LA BD')
                flash("ERROR: contrasena incorrecta")
                return redirect(url_for("login.login"))
        elif verifica_correo_v(correo) != None:
            v = verifica_correo_v(correo)
            vendedor = Vendedor()
            vendedor.set_correo_v(correo)
            vendedor.set_contrasena_v(contrasena)
            if verifica_contr_v(v, contrasena):
                session.clear()
                session['correo'] = vendedor.correo
                session['nombre'] = v.nombre
                g.user = vendedor.correo
                return redirect(url_for("login.success_vendedor"))
            else:
                print('ERROR CONTRASENA INCORRECTA DEL VENDEDOR EN LA BD')
                flash("ERROR: contrasena incorrecta")
                return redirect(url_for("login.login"))
        elif verifica_correo_c(correo) != None:
            c = verifica_correo_c(correo)
            cliente = Cliente()
            cliente.set_correo_c(correo)
            cliente.set_contrasena_c(contrasena)
            if verifica_contr_c(c, contrasena):
                session.clear()
                session['correo'] = cliente.correo_cliente
                session['nombre'] = c.nombre_cliente
                g.user = cliente.correo_cliente
                return redirect(url_for("login.success_cliente"))
            else:
                print('ERROR CONTRASENA INCORRECTA DEL CLIENTE EN LA BD')
                flash("ERROR: contrasena incorrecta")
                return redirect(url_for("login.login"))
        else:
            print('ERROR NO EXISTE EL CORREO EN LA BD')
            flash("ERROR: correo incorrecto")
            return redirect(url_for("login.login"))
    else:
        return render_template("login.html")

@loginBlueprint.route('/administrador', methods=["GET"])
def success_admin():
    if session.get('correo') != None: #and g.user != None:
        return render_template("PrincipalAdmin.html")
    flash("ERROR: cookie de sesion vacia")
    return redirect(url_for('login.login'))

@loginBlueprint.route('/vendedor', methods=["GET"])
def success_vendedor():
    if session.get('correo') != None: #and g.user != None:
        return render_template("PrincipalVendedor.html")
    flash("ERROR: No ha iniciado sesion")
    return redirect(url_for('login.login'))

@loginBlueprint.route('/cliente', methods=["GET"])
def success_cliente():
    if session.get('correo') != None: #and g.user != None:
        return render_template("PrincipalCliente.html")
    flash("ERROR: cookie de sesion vacia")
    return redirect(url_for('login.login'))