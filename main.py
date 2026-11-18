from flask import Flask, jsonify, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
app = Flask(__name__)
app.config['SECRET_KEY']='ABC123'
image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREofPdLRAu4-LKbY1GowVhzmCyRD-LGUmw-oaIVu0Dcg&s=10'
class RegisterForm(FlaskForm):
    first_name=StringField('Primeiro nome')
    last_name=StringField('Sobrenome')
    email=StringField('E-mail')
    password=PasswordField('Senha')
    confirm=PasswordField('Confirme a senha')
    submit=SubmitField('CADASTRAR')
@app.route('/')
def register():
    form=RegisterForm()
    return render_template ('base.html',form=form,image_url=image_url)
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')