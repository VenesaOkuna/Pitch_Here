from flask import render_template
from . import main

@main.route('/')
@main.route('/iminute')
def index():
    title = 'i-minute'
    return render_template('index.html')


