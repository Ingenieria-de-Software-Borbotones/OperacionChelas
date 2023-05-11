from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from models.Modelo_producto import obten_todo
from models.Modelo_inventario import nuevo_inventario
from models.Modelo_tener import nuevo_tener

inventarioBlueprint = Blueprint('inventario', __name__, url_prefix='/inventario')
'''
@inventarioBlueprint.route('/')
def inicia_inventario():
    if session.get('correo') != None:
        productos = obten_todo()
        return render_template("Inventario.html", productos=productos)
    else:
        flash("ERROR: no se ha iniciado sesion")
        return redirect(url_for('login.login'))
'''

@inventarioBlueprint.route('/', methods=['GET', 'POST'])
def hacer_inventario():
    print('Inicio')
    if session.get('correo') != None:
        print('entro a if session')
        productos = obten_todo()
        if request.method == "POST":
            print('entro a if post')
            #productos = obten_todo()
            fecha = request.form["fecha"]
            if fecha == None:
                flash("ERROR: fecha no asiganada")
                return redirect(url_for('inventario.hacer_inventario'))
            inv = nuevo_inventario(fecha, session.get('correo'))
            id_inventario_t = inv.id_inventario
            for p_1 in productos:
                if request.form[p_1.id_producto] == None:
                    flash("ERROR: algun producto no tiene cantidad")
                    return redirect(url_for('inventario.hacer_inventario'))
            for p in productos:
                nuevo_tener(id_inventario_t, p.id_producto, request.form[p.id_producto])
            flash("Inventario agregado exitosamente")
            #return redirect(url_for("inventario.inicia_inventario"))
        return render_template("Inventario.html", productos=productos)
    else:
        flash("ERROR: no se ha iniciado sesion")
        return redirect(url_for('login.login'))