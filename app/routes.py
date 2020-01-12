from flask import render_template, flash, redirect
from app import app, db
from sqlalchemy import desc
from app.models import Event, Message, User
from app.forms import RegistrationForm, LoginForm 
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/events')
def events():
    events = Event.query.order_by(desc(Event.timestamp)).all()
    return render_template('events.html', events=events)

@app.route('/messages')
def messages():
    messages = Message.query.join(User).add_columns(User.id, User.username, Message.text, Message.timestamp).order_by(desc(Message.timestamp)).all()
    return render_template('messages.html', messages=messages)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        return redirect('/events')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/events')
