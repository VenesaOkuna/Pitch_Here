from flask import render_template
from . import auth

@auth.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the fourowfour error page
    '''
    return render_template('fourowfour.html'),404
