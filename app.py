from flask import Flask, redirect, render_template, request, url_for, jsonify
import forms

from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/", methods=['GET', 'POST'])
def index():
    reg_alumno = forms.UserForm(request.form)
    if request.method == 'POST':
        alumno = Alumnos(
            nombre = reg_alumno.nombre.data,
            apellidos = reg_alumno.apellidos.data,
            email = reg_alumno.email.data
        )

        db.session.add(alumno)
        db.session.commit()
    return render_template('index.html', form = reg_alumno)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port = 3000)