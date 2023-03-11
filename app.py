from flask import Flask, redirect, render_template, request, url_for, jsonify
import forms

from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/", methods = ['GET', 'POST'])
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

@app.route("/ABCompleto", methods = ['GET', 'POST'])
def ABCompleto():
    reg_aluno = forms.UserForm(request.form)
    # SELECT * FROM alumnos
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', form = reg_aluno, alumnos = alumnos)

@app.route("/modificar", methods = ['GET', 'POST'])
def modificar():
    reg_alumno = forms.UserForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        #SELECT * FROM alumnos WHERE id = id
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        reg_alumno.id.data = alumno.id
        reg_alumno.nombre.data = alumno.nombre
        reg_alumno.apellidos.data = alumno.apellidos
        reg_alumno.email.data = alumno.email

    if request.method == 'POST':
        id = reg_alumno.id.data
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        alumno.nombre = reg_alumno.nombre.data
        alumno.apellidos = reg_alumno.apellidos.data
        alumno.email = reg_alumno.email.data

        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    
    return render_template('modificar.html', form = reg_alumno)

@app.route("/eliminar", methods = ['GET'])
def eliminar():
    reg_alumno = forms.UserForm(request.form)

    id = request.args.get('id')

    alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()

    alumno.nombre = reg_alumno.nombre.data
    alumno.apellidos = reg_alumno.apellidos.data
    alumno.email = reg_alumno.email.data

    db.session.delete(alumno)
    db.session.commit()
    
    return redirect(url_for('ABCompleto'))
    

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port = 3000)