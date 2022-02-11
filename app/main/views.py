from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user,login_manager
from ..models import User,Task
from .forms import TaskForm
from .. import db


#views
@main.route('/', methods=["GET","POST"])
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    tasks = Task.query.all()

    return render_template('index.html',tasks= tasks)