"""Forms to render HTML input & validate request data."""

from wtforms import Form, BooleanField, DateTimeField, PasswordField
from wtforms import TextAreaField, TextField
from wtforms.validators import Length, required


class AppointmentForm(Form):
    """Render HTML input for Appointment model & validate submissions.

    This matches the models.Appointment class very closely. Where
    models.Appointment represents the domain and its persistence, this class
    represents how to display a form in HTML & accept/reject the results.
    """
    title = TextField('Title', [Length(max=255)])
    start = DateTimeField('Start', [required()])
    end = DateTimeField('End')
    allday = BooleanField('All Day')
    location = TextField('Location', [Length(max=255)])
    description = TextAreaField('Description')


class LoginForm(Form):
    """Render HTML input for user login form.

    Authentication (i.e. password verification) happens in the view function.
    """
    username = TextField('Email', [required()])
    password = PasswordField('Password', [required()])
