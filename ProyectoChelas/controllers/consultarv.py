from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from models.Modelo_rv import obten_reportes_venta
from models.Modelo_pedido import obten_pedidos_r_id
from models.Modelo_estar import obten_productos_estar

consultarRvBlueprint = Blueprint('consultarv', __name__, url_prefix='/consultarv')

@consultarRvBlueprint.route('/', methods=['GET', 'POST'])
def consultar_rv():
    '''
    Obtiene id, correo y/o fecha de ConsultarRepVenta.html y obtiene los Reportes que
    cumplan con esas caracteristicas
    :return: ConsultarRepVenta.html con la informacion devuelta, Reportes o mensajes
    Flash
    '''
    if session.get('correo') != None:
        if request.method == "POST":
            id = request.form["id"]
            correo = request.form["correo"]
            fecha = request.form["fecha"]
            if '-' in str(id):
                flash("ERROR: id invalido.")
                return redirect(url_for('consultarv.consultar_rv'))
            if (id == None or id == '') and (correo == None or correo == '') and (fecha == None or fecha == ''):
                flash("ERROR: campos invalidos, se debe de llenar al menos un campo.")
                return redirect(url_for('consultarv.consultar_rv'))
            reportes = obten_reportes_venta(id, correo, fecha)
            if reportes == []:
                flash("No se encontraron reportes.")
                return redirect(url_for('consultarv.consultar_rv'))
            return render_template("ConsultarRepVenta.html", reportes=reportes)
        else:
            return render_template("ConsultarRepVenta.html")

@consultarRvBlueprint.route('/rvpedido')
def rv_pedido():
    '''
    Pedidos del Reporte r_id
    :return: RVPedido.html con la informacion correspondiente
    '''
    if session.get('correo') != None:
        r_id = request.args.get('r_id')
        return render_template("RVPedido.html", pedidos=obten_pedidos_r_id(r_id))

@consultarRvBlueprint.route('/rvproducto')
def rv_producto():
    '''
    Productos del Pedido con p_id
    :return: RVProducto.html con la informacion correspondiente
    '''
    if session.get('correo') != None:
        p_id = request.args.get('p_id')
        return render_template("RVProducto.html", productos=obten_productos_estar(p_id))