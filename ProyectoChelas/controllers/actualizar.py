from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from models.Modelo_actualizar import actualizar_V

loginBlueprint = Blueprint('actualizar', __name__, url_prefix='/')

@loginBlueprint.route('/')
def actualizar():
    return render_template("ActualizarV.html")

'''
def actualiza(correo, nuevo_correo, nueva_contrasenia, nueva_edad):
    if correo == "":
        print('ERROR CAMPO VACIO')
        flash("ERROR: campo vacio")
        return redirect(url_for("actualizar_V.actualizar"))
    else:
        if actualizar_V(correo, nuevo_correo, nueva_contrasenia, nueva_edad):
            print('DATOS ACTUALIZADOS.')
            flash("Datos actualizados con éxito.")
            return render_template("PrincipalAdmin.html")
'''
'''
TODO. Esto va en PrincipalAdmin.html
<!-- TODO. meter otra vista (HTML)-->
<!-- <li><a href="{{ url_for('actualizar_V.actualizar') }}">Actualizar Vendedor</a> </li> -->
'''