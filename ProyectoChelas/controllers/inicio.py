from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

inicioBlueprint = Blueprint('inicio', __name__, url_prefix='/')

@inicioBlueprint.route('/')
def inicio():
    return render_template('PantallaPrincipal.html')