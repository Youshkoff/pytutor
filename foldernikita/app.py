from flask import render_template, redirect, request
from flask_security import current_user, login_required

from init import app
from extensions import db
from form import ContactForm,Contacts
from models import UserSubmit, User
from mail import send_email



@app.before_first_request
def init():
    """Создание таблиц"""
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def index():
    """Главная страница"""
    page_title = "Главная страница"
    form = ContactForm()
    if form.validate_on_submit():
        print(f"Name: {request.form.get('name')}, \nEmail: {request.form.get('email')}, \nMessage: {request.form.get('message')}")
        user_db = UserSubmit(
            name = request.form.get('name'),
            email = request.form.get('email'),
            message = request.form.get('message')
        )
        db.session.add(user_db)
        db.session.commit()
        user_list_db = UserSubmit.query.all()
        for user in user_list_db:
            print(user.id, user.name, user.email, user.message)
        return redirect(url_for('index'))
    return render_template("index.j2", form=form)


@app.route("/mail", methods=["GET", "POST"])
def test_mail():
    page_title = "Главная"
    send_email("Тестовое письмо")
    return render_template("test.j2", page_title=page_title)


@app.route('/test')
def test():
    return render_template("test.j2")


@app.route('/elements')
def elements():
    return render_template("elements.j2")


@app.route('/users')
@login_required
def users():
    """Список пользователей"""
    page_title = "Список пользователей"
    user_list_db = UserSubmit.query.all()
    return render_template("users.j2", users=User.query.all())

@app.route('/lk', methods=["GET", "POST"])
@login_required
def lk():
    """Личный кабинет"""
    page_title = "Личный кабинет"
    form = Contacts()
    if form.validate_on_submit():
        contacts_db = Contacts(
            adress = request.form.get('adress'),
            phone = request.form.get('phone'),
            telegram = request.form.get('telegram'),
            instagram = request.form.get('instagram')
        )
        db.session.add(contacts_db)
        db.session.commit()
        return redirect(url_for('lk'))
    return render_template("lk.j2", email = current_user.email, form=form)
