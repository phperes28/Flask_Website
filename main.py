from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail, Message
from forms import ContactForm
import os
import smtplib


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") or "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"



mail = Mail(app)
ckeditor = CKEditor(app)
Bootstrap(app)




# @app.route("/")
# def home():
#     return render_template("index.html")



@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    email = request.form.get("email")
    name = request.form.get("name")
    message = request.form.get("message")
    if request.method == "POST":
        if form.validate() == False:
            flash('Preencha todos os campos')
            return render_template('/', form=form)
        else:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("pedro.tramit@gmail.com", "necrophagist289")
            server.sendmail(from_addr= "pedro.tramit@gmail.com",
            to_addrs= email,
            msg=f'Subject: Novo contato@ \n\n{name} {email}\nEnviou a seguinte mensagem: {message}'
            )
            flash('Mensagem enviada!')
            return redirect(url_for('home'))
    return render_template("index.html", form=form)









if __name__ == "__main__":
    app.run(debug=True)


