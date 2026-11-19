from flask import Flask, jsonify, request, render_template,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,Length, Regexp
from wtforms.validators import DataRequired,InputRequired,EqualTo,Email
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
app = Flask(__name__)
app.config['SECRET_KEY']='ABC123'
image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREofPdLRAu4-LKbY1GowVhzmCyRD-LGUmw-oaIVu0Dcg&s=10'
class RegisterForm(FlaskForm):
    first_name=StringField('Primeiro nome', validators=[DataRequired()])
    last_name=StringField('Sobrenome',validators=[DataRequired()])
    email=StringField('E-mail',validators=[Email(message='Email invalido!')])
    password = PasswordField('Senha', validators=[
        InputRequired(),
        Length(min=8, message='A senha deve ter no mínimo 8 caracteres'),Regexp(r'(?=.*[a-z])(?=.*[A-Z])',message='A senha deve ter pelo menos uma letra maiúscula e uma minúscula'),EqualTo('confirm', message='As senhas devem ser iguais')])
    confirm=PasswordField('Confirme a senha')
    submit=SubmitField('CADASTRAR')
@app.route('/',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        return redirect('/principal')
    return render_template ('form.html',form=form,image_url=image_url)
@app.route('/principal')
def cartilha():
    return render_template('site.html')
@app.get("/api/status")
def status_fastapi():
    return {"status": "ok", "framework": "FastAPI"}


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')