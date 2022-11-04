from flask import render_template, flash, redirect, url_for, Blueprint, request, abort
from flask_login import current_user
from app.controllers.lanchonete.lanchoneteForm import MesasForm

lanchonete = Blueprint('lanchonete', __name__)


@lanchonete.route('/salaoLanchonete', methods=['GET'])
def salaoLanchonete():
    if current_user.is_authenticated:
        print(current_user.acesso[0].tipo)
    return render_template('lanchonete/salao.html')


@lanchonete.route('/mesas', methods=['GET'])
def mesas():
    form = MesasForm()
    return render_template('lanchonete/mesas.html', title='Mesas', form=form)


@lanchonete.route('/lanches', methods=['GET'])
def lanches():
    return render_template('lanchonete/lanches.html', title='Lanches')
    
@lanchonete.route('/porcoes', methods=['GET'])
def porcoes():
    return render_template('lanchonete/porcoes.html', title='Porcoes')

@lanchonete.route('/bebidas', methods=['GET'])
def bebidas():
    return render_template('lanchonete/bebidas.html', title='Bebidas')

@lanchonete.route('/pedidos', methods=['GET'])
def pedidos():
    return render_template('lanchonete/pedidos.html', title='Pedidos')
