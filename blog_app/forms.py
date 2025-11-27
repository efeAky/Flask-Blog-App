from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    # Form fields for registering a new user
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo('password', message='Passwords must match')]
        # Ensures confirm_password matches password
    )
    submit = SubmitField("Register")  # Submit button

class LoginForm(FlaskForm):
    # Basic login fields
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class PostForm(FlaskForm):
    # Form used to create a new blog post
    title = StringField("Title", validators=[DataRequired()])
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField("Create Post")

class DeleteForm(FlaskForm):
    # Simple form with only a submit button for deleting posts
    submit = SubmitField("Delete Post")
