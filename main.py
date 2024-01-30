import os
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
ckeditor = CKEditor(app)
Bootstrap5(app)

f_email = os.environ.get("EMAIL")
f_password = os.environ.get("PASSWORD")
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")



@app.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm()
    if form.validate_on_submit() and request.method=="POST":
        if form.email.data == f_email and form.password.data == f_password:
            return render_template("index.html")

    return render_template("login.html", form=form)

@app.route("/galeri")
def galeri():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)