from flask import render_template, flash, redirect, url_for, Blueprint, request, abort
from flask_login import current_user, login_required, login_user, logout_user
from app.controllers.users.formUser import LoginForm, CadastroUsersForm
from app import db, bcrypt
from app.models.bdEternusLanches import (Users, Enderecos, Acessos)

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
        
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = Users.query.filter_by(email=form.email.data.lower()).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data.lower()):
                login_user(user=user, remember=form.remember.data)
                next_page = request.args.get('next')
                flash('Logado com sucesso!','success')
                return redirect(next_page) if next_page else redirect(url_for('home.index'))
            else:
                flash('Error, verifique Login/Senha!', 'danger')
                return redirect(request.referrer)
        except Exception as e:
            print(f'Error: {e}')

    return render_template('users/login.html', title='Login', legenda='Login', form=form)

@users.route('/createFuncionario/<login>/<password>', methods=['GET'])
def createFuncionario(login, password):
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))

    user = Users.query.all()
    if not user:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        try:
            endereco = Enderecos(rua='Rua 1', numero=123, cidade='Guaratingueta', bairro='Nova Guara', cep='13230-20', principal=True)
            db.session.add(endereco)
            db.session.commit()
        except Exception as e:
            db.session.flush()
            db.session.rollback()
            print(f'Errors: {e}')
        
        try:
            lista = ['Funcionario','Cliente']
            for l in lista:
                acesso = Acessos(tipo=l)
                db.session.add(acesso)
                db.session.commit()
        except Exception as e:
            db.session.flush()
            db.session.rollback()
            print(f"Errors: {e}")
        
        try:
            acesso = Acessos.query.filter_by(tipo='Funcionario').first()
            user = Users(nome=login.lower(), email=login.lower()+'@eternus.com.br', password=hashed_password, endereco=[endereco], acesso=[acesso])
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.flush()
            db.session.rollback()
            print(f'Error: {e}')
            flash('Erro ao criar usuário!', 'danger')
        
        flash('Users criado com sucesso!', 'success')
        return redirect(url_for('home.index'))
    else:
        flash('Já existe user cadastrado!', 'danger')
        return redirect(url_for('home.index'))

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))

@users.route('/createUser', methods=['GET', 'POST'])
def createUser():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    else:
        form = CadastroUsersForm()
        if form.validate_on_submit():
            endereco = Enderecos(rua=form.rua.data.capitalize(), numero=int(form.numero.data), cidade=form.cidade.data.capitalize(), bairro=form.bairro.data.capitalize(), cep=form.cep.data, principal=True)
            db.session.add(endereco)
            try:
                db.session.commit()
            except Exception as e:
                print(f'Error: {e}')
                db.session.flush()
                db.session.rollback()
            
            try:
                acesso = Acessos.query.filter_by(tipo='Cliente').first()
                users = Users(nome=form.nome.data.title(), email=form.email.data.lower(), password=bcrypt.generate_password_hash(form.password.data).decode('utf-8'), endereco=[endereco], acesso=[acesso])
                db.session.add(users)
                db.session.commit()
            except Exception as e:
                print(f'Error: {e}')
                db.session.flush()
                db.session.rollback()
            flash('Usuário criado com sucesso.', 'success')
            return redirect(url_for('users.login'))

        return render_template('users/cadastro.html', title='Create Users', form=form)
