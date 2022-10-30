from flask import render_template, flash, redirect, url_for, Blueprint, request, abort
from app.controllers.users.formUser import LoginForm

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logado com sucesso!','success')
        return redirect(url_for('home.index'))
    return render_template('users/login.html', title='Login', legenda='Login', form=form)
