from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PostForm(FlaskForm):
    content = StringField('Message Content', validators=[DataRequired(), Length(min = 1)])
    submit = SubmitField('Post to Message Board')
    
class EventForm(FlaskForm):
    title = StringField('Event Title', 
                        validators=[DataRequired()])
    
    date = DateTimeField('Event Time', 
                        format='%Y-%m-%d %H:%M:%S', 
                        validators=[DataRequired()])

    location = StringField('Location',
                            validators=[DataRequired()])

    description = StringField('Description of Event',
                                validators=[DataRequired()])

    submit = SubmitField('Add event to schedule')




    



    
