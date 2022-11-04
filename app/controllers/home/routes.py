from flask import render_template, flash, redirect, url_for, Blueprint, request, abort
from flask_login import current_user

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
@home.route('/index', methods=['GET'])
def index():
    if current_user.is_authenticated:
        print(current_user.acesso[0].tipo)
    return render_template('home/index.html')
