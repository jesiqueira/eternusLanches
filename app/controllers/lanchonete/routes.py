from flask import render_template, flash, redirect, url_for, Blueprint, request, abort
from flask_login import current_user, login_required
from app.controllers.lanchonete.lanchoneteForm import MesasForm, MesaNovaForm
from app.models.bdEternusLanches import Mesas
from app import db
from sqlalchemy import exc

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
            mesas = Mesas.query.all()
            return render_template('lanchonete/mesas.html', title='Mesas', form=form, mesas=mesas)
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/novaMesa', methods=['GET', 'POST'])
@login_required
def novaMesa():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = MesaNovaForm()

            if form.validate_on_submit():
                mesa = Mesas.query.get(int(form.numero.data))
                if not mesa:
                    mesa = Mesas(numero=int(form.numero.data), livre=True)
                    db.session.add(mesa)
                    try:
                        db.session.commit()
                        flash('Mesa cadastrada com sucesso', 'success')
                        return redirect(url_for('lanchonete.mesas'))
                    except Exception as e:
                        print(f'Error: {e}')
                        db.session.flush()
                        db.session.rollback()
                else:
                    flash('Mesa já está cadastrada', 'danger')
                    return redirect(request.referrer)

            return render_template('lanchonete/novaMesa.html', title='Mesas', form=form)
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/atualizarMesa', methods=['POST', 'GET'])
@login_required
def atualizarMesa():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = MesaNovaForm()
            if request.method == 'POST' and request.form.get('idMesa'):
                mesa = Mesas.query.get(int(request.form.get('idMesa')))
                form.id_mesa.data = mesa.id
                form.numero.data = mesa.numero
                return render_template('lanchonete/updateMesa.html', title='Atualizar Mesa', form=form)
            if form.validate_on_submit():
                mesa = Mesas.query.get(int(form.id_mesa.data))
                mesa.numero = int(form.numero.data)
                try:
                    db.session.commit()
                except exc.IntegrityError as e:
                    # print(f'Error: {e}')
                    db.session.flush()
                    db.session.rollback()
                    flash('Erro ao atualizar já existe mesa com número informado.', 'danger')
                    return redirect(url_for('lanchonete.mesas'))
                flash('Mesa atualizada com sucesso.', 'success')
                return redirect(url_for('lanchonete.mesas'))
            else:
                return render_template('lanchonete/updateMesa.html', title='Atualizar Mesa', form=form)
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/removerMesa', methods=['POST', 'GET'])
@login_required
def removerMesa():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = MesaNovaForm()
            if request.method == 'POST' and request.form.get('idMesa'):
                mesa = Mesas.query.get(int(request.form.get('idMesa')))
                form.id_mesa.data = mesa.id
                form.numero.data = mesa.numero
                return render_template('lanchonete/removerMesa.html', title='Remover Mesa', form=form)
            if form.validate_on_submit():
                mesa = Mesas.query.get(int(form.id_mesa.data))
                mesa.numero = int(form.numero.data)
                try:
                    db.session.delete(mesa)
                    db.session.commit()
                except Exception as e:
                    print(f'Error: {e}')
                    db.session.flush()
                    db.session.rollback()
                flash('Mesa removida com sucesso.', 'success')
                return redirect(url_for('lanchonete.mesas'))
            else:
                return render_template('lanchonete/removerMesa.html', title='Remover Mesa', form=form)
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
