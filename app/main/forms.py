from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import input_required



class TaskForm(FlaskForm):
    title = StringField('Title', validators=[input_required()])
    task = TextAreaField('Work Session Description', validators=[input_required()])
    submit = SubmitField('Save')
