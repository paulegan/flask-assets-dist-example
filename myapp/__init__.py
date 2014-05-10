import sys
from werkzeug.utils import import_string
from flask import Flask
from flask.ext.script import Manager
from flask.ext.assets import Environment, ManageAssets


def run(*args):
    if args:
        return manager.handle(sys.argv[0], args)
    else:
        return manager.run()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    app.config.from_envvar('APP_CONFIG', silent=True)
    assetenv.init_app(app)
    app.register_blueprint(import_string('myapp.root.views.blueprint'))
    return app


assetenv = Environment()
manager = Manager(create_app, with_default_commands=True)
manager.add_command('assets', ManageAssets(assetenv))
