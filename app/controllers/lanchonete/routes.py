from flask import render_template, flash, redirect, url_for, Blueprint, request, abort
from flask_login import current_user, login_required
from app.controllers.lanchonete.lanchoneteForm import (
    MesasForm, MesaNovaForm, LancheForm, LancheConsultaForm, RemoverLancheForm, PorcaoConsultaForm, PorcaoForm, RemoverPorcaoForm)
from app.models.bdEternusLanches import Mesas, Lanches, Porcoes, Bebidas
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
            return render_template('lanchonete/mesas/mesas.html', title='Mesas', form=form, mesas=mesas)
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
                mesa = db.session.query(Mesas).filter(
                    Mesas.numero == int(form.numero.data)).first()
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

            return render_template('lanchonete/mesas/novaMesa.html', title='Mesas', form=form)
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
                return render_template('lanchonete/mesas/updateMesa.html', title='Atualizar Mesa', form=form)
            if form.validate_on_submit():
                mesa = Mesas.query.get(int(form.id_mesa.data))
                mesa.numero = int(form.numero.data)
                try:
                    db.session.commit()
                except exc.IntegrityError as e:
                    # print(f'Error: {e}')
                    db.session.flush()
                    db.session.rollback()
                    flash(
                        'Erro ao atualizar já existe mesa com número informado.', 'danger')
                    return redirect(url_for('lanchonete.mesas'))
                flash('Mesa atualizada com sucesso.', 'success')
                return redirect(url_for('lanchonete.mesas'))
            else:
                return render_template('lanchonete/mesas/updateMesa.html', title='Atualizar Mesa', form=form)
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
                return render_template('lanchonete/mesas/removerMesa.html', title='Remover Mesa', form=form)
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
                return render_template('lanchonete/mesas/removerMesa.html', title='Remover Mesa', form=form)
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/atualizarlanche', methods=['GET', 'POST'])
@login_required
def atualizarLanches():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = LancheForm()
            if request.method == 'POST' and request.form.get('idLanche'):
                # print(f"Update: {type(request.form.get('idLanche'))}")
                lanche = Lanches.query.get(request.form.get('idLanche'))
                form.id_lanche.data = lanche.id
                form.nome.data = lanche.nome
                form.valor.data = lanche.valor
                form.ingrediente.data = lanche.ingrediente
                return render_template('lanchonete/lanches/updateLanche.html', title='Atualizar lanche', form=form)
            if form.validate_on_submit():
                lanche = Lanches.query.get(int(form.id_lanche.data))
                lanche.nome = form.nome.data
                lanche.valor = float(form.valor.data)
                lanche.ingrediente = form.ingrediente.data
                try:
                    db.session.commit()
                except exc.IntegrityError as e:
                    # print(f'Error: {e}')
                    db.session.flush()
                    db.session.rollback()
                    flash('Erro ao atualizar.', 'danger')
                    return redirect(url_for('lanchonete.lanches'))
                flash('Lanche atualizada com sucesso.', 'success')
                return redirect(url_for('lanchonete.lanchesView'))
            else:
                return render_template('lanchonete/lanches/lanches.html', title='Lanches', form=form)
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/removerlanche', methods=['GET', 'POST'])
@login_required
def removerLanche():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = RemoverLancheForm()
            if request.method == 'POST' and request.form.get('idLanche'):
                # print(f"Update: {type(request.form.get('idLanche'))}")
                lanche = Lanches.query.get(request.form.get('idLanche'))
                form.id_lanche.data = lanche.id
                form.nome.data = lanche.nome
                form.valor.data = lanche.valor
                form.ingrediente.data = lanche.ingrediente
                return render_template('lanchonete/lanches/removerlanche.html', title='Remover lanche', form=form)
            if form.validate_on_submit():
                lanche = Lanches.query.get(int(form.id_lanche.data))
                try:
                    db.session.delete(lanche)
                    db.session.commit()
                except exc.IntegrityError as e:
                    # print(f'Error: {e}')
                    db.session.flush()
                    db.session.rollback()
                    flash('Erro ao remover.', 'danger')
                    return redirect(url_for('lanchonete.lanches'))
                flash('Lanche removido com sucesso.', 'success')
                return redirect(url_for('lanchonete.lanchesView'))
            else:
                return render_template('lanchonete/lanches/removerlanche.html', title='Lanches', form=form)
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/lanchesView', methods=['GET'])
@login_required
def lanchesView():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = LancheConsultaForm()
            lanches = Lanches.query.all()
            return render_template('lanchonete/lanches/lanchesView.html', title='Lanches', form=form, lanches=lanches)
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/novoLanche', methods=['GET', 'POST'])
@login_required
def novoLanche():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = LancheForm()

            if form.validate_on_submit():
                lanche = db.session.query(Lanches).filter(
                    Lanches.nome == form.nome.data.capitalize()).first()
                if not lanche:
                    lanche = Lanches(nome=form.nome.data.capitalize(), valor=float(
                        form.valor.data), ingrediente=form.ingrediente.data.capitalize())
                    db.session.add(lanche)
                    try:
                        db.session.commit()
                        flash('Lanche cadastrada com sucesso', 'success')
                        return redirect(url_for('lanchonete.lanchesView'))
                    except Exception as e:
                        print(f'Error: {e}')
                        db.session.flush()
                        db.session.rollback()
                else:
                    flash('Lanche já está cadastrada', 'danger')
                    return redirect(request.referrer)

            return render_template('lanchonete/lanches/novoLanche.html', title='lanches', form=form)
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
            form = PorcaoConsultaForm()
            porcoes = Porcoes.query.all()
            return render_template('lanchonete/porcoes/porcoes.html', title='Porção View', form=form, porcoes=porcoes)
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/novaPorcao', methods=['GET', 'POST'])
@login_required
def novaPorcao():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = PorcaoForm()
            if form.validate_on_submit():
                porcao = db.session.query(Porcoes.nome).filter(
                    Porcoes.nome == form.nome.data.capitalize()).first()
                if not porcao:
                    porcao = Porcoes(nome=form.nome.data.capitalize(), valor=float(
                        form.valor.data), descricao=form.descricao.data.capitalize())
                    db.session.add(porcao)
                    try:
                        db.session.commit()
                    except Exception as e:
                        print(f'Erro ao cadastrar porcao {e}')
                        db.session.flush()
                        db.session.rollback()
                    flash(
                        f'Porção {porcao.nome} cadastrada com sucesso.', 'success')
                    return redirect(url_for('lanchonete.porcoes'))
                else:
                    form.nome.data = form.nome.data
                    form.descricao.data = form.descricao.data
                    form.valor.data = form.valor.data
                    flash(
                        f'Porção {porcao.nome} já está cadastrada!', 'warning')
                    return render_template('lanchonete/porcoes/novaPorcao.html', title='Porcoes', form=form)
            return render_template('lanchonete/porcoes/novaPorcao.html', title='Porcoes', form=form)
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/updatePorcao', methods=['POST'])
@login_required
def updatePorcao():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = PorcaoForm()
            if request.method == 'POST' and request.form.get('idPorcao'):
                # print(f"Update: {type(request.form.get('idLanche'))}")
                porcao = Porcoes.query.get(request.form.get('idPorcao'))
                form.id_Porcao.data = porcao.id
                form.nome.data = porcao.nome
                form.valor.data = porcao.valor
                form.descricao.data = porcao.descricao
                return render_template('lanchonete/porcoes/updatePorcao.html', title='Atualizar Porcao', form=form)

            if form.validate_on_submit():
                porcao = Porcoes.query.get(int(form.id_Porcao.data))
                porcao.nome = form.nome.data
                porcao.valor = float(form.valor.data)
                porcao.descricao = form.descricao.data
                try:
                    db.session.commit()
                    flash('Porção atualizada com sucesso.', 'success')
                    return redirect(url_for('lanchonete.porcoes'))
                except exc.IntegrityError as e:
                    # print(f'Error: {e}')
                    db.session.flush()
                    db.session.rollback()
                    flash('Erro ao atualizar.', 'danger')
                    return redirect(url_for('lanchonete.updatePorcao'))
            else:
                return render_template('lanchonete/porcoes/updatePorcao.html', title='Atualizar Porcao', form=form)
            
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))


@lanchonete.route('/removerPorcao', methods=['GET', 'POST'])
@login_required
def removerPorcao():
    if current_user.is_authenticated:
        if current_user.acesso[0].tipo == 'Funcionario':
            form = RemoverPorcaoForm()
            if request.method == 'POST' and request.form.get('idPorcao'):
                # print(f"Update: {type(request.form.get('idLanche'))}")
                porcao = Porcoes.query.get(request.form.get('idPorcao'))
                form.id_Porcao.data = porcao.id
                form.nome.data = porcao.nome
                form.valor.data = porcao.valor
                form.descricao.data = porcao.descricao
                return render_template('lanchonete/porcoes/removerPorcao.html', title='Remover porcao', form=form)
            if form.validate_on_submit():
                porcao = Porcoes.query.get(int(form.id_Porcao.data))
                try:
                    db.session.delete(porcao)
                    db.session.commit()
                except exc.IntegrityError as e:
                    # print(f'Error: {e}')
                    db.session.flush()
                    db.session.rollback()
                    flash('Erro ao remover.', 'danger')
                    return redirect(url_for('lanchonete.removerPorcao'))
                flash('Porção removido com sucesso.', 'success')
                return redirect(url_for('lanchonete.porcoes'))
            else:
                return render_template('lanchonete/porcoes/removerPorcao.html', title='Remover Porção', form=form)
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
            return render_template('lanchonete/bebidas/bebidas.html', title='Bebidas')
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
            return render_template('lanchonete/pedidos/pedidos.html', title='Pedidos')
        else:
            flash('Não tem permissão para acessar essa página', 'danger')
            return redirect(url_for('home.index'))
    else:
        flash('Faça o login para acessar essa página.', 'danger')
        return redirect(url_for('users.login'))
