from flask import render_template
from app import app
from sqlalchemy import desc
from app.models import Event

@app.route('/')
@app.route('/home')
def events():
    events = Event.query.order_by(desc(Event.timestamp)).all()
    return render_template('home.html', events=events)