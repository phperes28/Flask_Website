from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField




class ContactForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    message = TextAreaField("Assunto", validators=[DataRequired()])
    name = StringField("Nome", validators=[DataRequired()])
    submit = SubmitField("Enviar")



