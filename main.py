from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail, Message
from forms import ContactForm
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") or "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"



mail = Mail(app)
ckeditor = CKEditor(app)
Bootstrap(app)







#Funcionando UTF-8
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

            msg = MIMEMultipart("alternative")
            Message = 'This is a Test Message'
            msg['from'] = "residencialleonidio@gmail.com"
            msg['to'] = {email}		# Target's Email
            msg['subject'] = 'Novo Contato'
            part1 = MIMEText(u'\u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01\n',
                 "plain",)
            msg.attach(part1)
            print('Sending the Mail..')
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login("residencialleonidio@gmail.com", os.getenv("PASSWORD"))
                mensagem = (f'Subject: Novo contato@ \n\n{name} {email}\nEnviou a seguinte mensagem: {message}').encode("utf-8")
                server.sendmail(from_addr= "residencialleonidio@gmail.com",
                                to_addrs="pedrodev28@gmail.com" ,
                                msg= mensagem,

                                mail_options="SMTPUTF8"
                                )
                print("message sent")
                server.quit()
                flash("Sua mensagem foi enviada!")
            except Exception as e :
                flash('Erro ao enviar mensagem')
                print(e)

            finally:
                return render_template("index.html", scrollToAnchor="contact", form=form)


    return render_template("index.html", form=form)














if __name__ == "__main__":
    app.run(debug=True)


