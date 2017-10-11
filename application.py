from os import getenv


from flask import Flask


from extensions import admin, db
import commands
from models import Pizza
from admin import PizzaView



def create_app(bot_db_query=False):
    app = Flask(__name__.split('.')[0])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
                        getenv('SQLALCHEMY_DATABASE_URI', 'pizza.db'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['USER_NAME'] = getenv('USER_NAME', 'admin')
    app.config['PASSWORD'] = getenv('PASSWORD', 'password')
    db.init_app(app)
    if not bot_db_query:
        register_commands(app)
        admin.init_app(app)
        admin.add_view(PizzaView(Pizza, db.session))
    return app


def register_commands(app):
    app.cli.add_command(commands.create)
    app.cli.add_command(commands.drop)
    app.cli.add_command(commands.feed)
