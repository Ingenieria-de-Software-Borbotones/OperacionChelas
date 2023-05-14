from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from models.Modelo_producto import obten_todo
from models.Modelo_inventario import nuevo_inventario
from models.Modelo_tener import nuevo_tener

inventarioBlueprint = Blueprint('inventario', __name__, url_prefix='/inventario')

@inventarioBlueprint.route('/', methods=['GET', 'POST'])
def hacer_inventario():
    '''
    Funcion que se encarga del caso de uso hacer inventario
    :return redirect(url_for('inventario.hacer_inventario')): cuando hay un error, junto con el mensaje que especifica
            ese error
    :return render_template("Inventario.html", productos=productos): cuando se registro el invenatrio exitosamente
            junto con un mensaje que lo menciona, o cuando lo llama con un metodo GET
    :return redirect(url_for('login.login')): cuando no se ha iniciado sesion
    '''
    if session.get('correo') != None:
        productos = obten_todo()
        if request.method == "POST":
            fecha = request.form["fecha"]
            if fecha == None or fecha == '':
                flash("ERROR: fecha no asiganada")
                return redirect(url_for('inventario.hacer_inventario'))
            inv = nuevo_inventario(fecha, session.get('correo'))
            id_inventario_t = inv.id_inventario
            for p_1 in productos:
                if request.form[str(p_1.id_producto)] == None or request.form[str(p_1.id_producto)] == '':
                    flash("ERROR: algun producto no tiene cantidad")
                    return redirect(url_for('inventario.hacer_inventario'))
                if '-' in request.form[str(p_1.id_producto)]:
                    flash("ERROR: cantidad negativa de algun producto")
                    return redirect(url_for('inventario.hacer_inventario'))
            for p in productos:
                nuevo_tener(id_inventario_t, p.id_producto, request.form[str(p.id_producto)])
            flash("Inventario agregado exitosamente")
            return render_template("Inventario.html", productos=productos)
        else:
            return render_template("Inventario.html", productos=productos)
    else:
        flash("ERROR: no se ha iniciado sesion")
        return redirect(url_for('login.login'))