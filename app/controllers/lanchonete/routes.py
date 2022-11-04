from flask import render_template, flash, redirect, url_for, Blueprint, request, abort
from flask_login import current_user, login_required
from app.controllers.lanchonete.lanchoneteForm import MesasForm

lanchonete = Blueprint('lanchonete', __name__)


@lanchonete.route('/salaoLanchonete', methods=['GET'])
def salaoLanchonete():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = MesasForm()
            return render_template('lanchonete/salao.html')
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/mesas', methods=['GET'])
@login_required
def mesas():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = MesasForm()
            return render_template('lanchonete/mesas.html', title='Mesas', form=form)
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/lanches', methods=['GET'])
@login_required
def lanches():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = MesasForm()
            return render_template('lanchonete/lanches.html', title='Lanches')
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/porcoes', methods=['GET'])
@login_required
def porcoes():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = MesasForm()
            return render_template('lanchonete/porcoes.html', title='Porcoes')
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/bebidas', methods=['GET'])
@login_required
def bebidas():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = MesasForm()
            return render_template('lanchonete/bebidas.html', title='Bebidas')
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/pedidos', methods=['GET'])
@login_required
def pedidos():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = MesasForm()
            return render_template('lanchonete/pedidos.html', title='Pedidos')
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))
