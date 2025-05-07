from flask import render_template, request, redirect, url_for
from models import Person
from app import db

def reg_routes(app,db): 
    @app.route('/')
    def index():
        people = Person.query.all()
        return render_template('index.html',people= people)

    @app.route('/add', methods=['POST'])
    def add():
        formdata = request.form
        
        person = Person(name=formdata['name'], age=formdata['age'], job=formdata['job'])

        db.session.add(person)

        db.session.commit()

        return redirect(url_for('index'))

