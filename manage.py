from app import create_app
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
import os

app = create_app(default='development')

manage = Manager(app)
manage.add_command('server',Server)


@manage.shell
def make_shell_context():
    return dict(app = app)

@manage.shell
def make_shell_context():
    return dict(app = app)


migrate = Migrate(app)
manage.add_command('db',MigrateCommand)



@manage.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manage.run()