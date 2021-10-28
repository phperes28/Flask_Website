from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail, Message
from datetime import date


app = Flask(__name__)


mail = Mail(app)
ckeditor = CKEditor(app)
Bootstrap(app)




@app.route("/")
def home():
    return render_template("index.html")











if __name__ == "__main__":
    app.run(debug=True)


