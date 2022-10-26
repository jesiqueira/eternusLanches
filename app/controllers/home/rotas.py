from crypt import methods
from flask import render_template, flash, redirect, url_for, Blueprint, request, abort

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
@home.route('/index', methods=['GET'])
def index():
    return render_template('home/index.html')