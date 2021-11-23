from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail, Message
from forms import ContactForm
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") or "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"



mail = Mail(app)
ckeditor = CKEditor(app)
Bootstrap(app)




# @app.route("/")
# def home():
#     return render_template("index.html")



# @app.route("/", methods=["GET", "POST"])
# def home():
#     form = ContactForm()
#     email = request.form.get("email")
#     name = request.form.get("name")
#     message = request.form.get("message")
#     if request.method == "POST":
#         if form.validate() == False:
#             flash('Preencha todos os campos')
#             return render_template('/', form=form)
#         else:
#             server = smtplib.SMTP("smtp.gmail.com", 587)
#             server.starttls()
#             server.login("pedro.tramit@gmail.com", "necrophagist289")
#             server.sendmail(from_addr= "pedro.tramit@gmail.com",
#             to_addrs= email,
#             msg=f'Subject: Novo contato@ \n\n{name} {email}\nEnviou a seguinte mensagem: {message}'
#             )
#             flash('Mensagem enviada!')
#             return redirect(url_for('home'))
#     return render_template("index.html", form=form)





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

            msg = MIMEMultipart()
            Message = 'This is a Test Message'
            msg['from'] = "residencialleonidio@gmail.com"
            msg['to'] = {email}		# Target's Email
            msg['subject'] = 'Novo Contato'
            msg.attach(MIMEText(Message,'plain'))
            print('Sending the Mail..')
            try:
                # server = smtplib.SMTP("smtp.gmail.com", 587)
                # server.starttls()
                # server.login("residencialleonidio@gmail.com", os.getenv("PASSWORD"))
                # server.sendmail(from_addr= "residencialleonidio@gmail.com",
                #                 to_addrs= email,
                #                 msg=f'Subject: Novo contato@ \n\n{name} {email}\nEnviou a seguinte mensagem: {message}'
                #                 )
                # print("message sent")
                # server.quit()
                flash("Sua mensagem foi enviada!")
            except Exception as e :
                print(f'Exception Occured ! \n {e}')
                error = 'Erro ao enviar mensagem'
            finally:

                return render_template("index.html", scrollToAnchor="contact", form=form)

    return render_template("index.html", form=form)





















if __name__ == "__main__":
    app.run(debug=True)


