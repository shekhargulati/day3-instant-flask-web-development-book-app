from flask.ext.script import Manager

from sched.app import app, db


# By default, Flask-Script adds the 'runserver' and 'shell' commands to
# interact with the Flask application. Add additional commands using the
# `@manager.command` decorator, where Flask-Script will create help
# documentation using the function's docstring. Try it, and call `python
# manage.py -h` to see the outcome.
manager = Manager(app)


@manager.command
def create_tables():
    "Create relational database tables."
    db.create_all()

@manager.command
def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA."
    db.drop_all()


if __name__ == '__main__':
    manager.run()
