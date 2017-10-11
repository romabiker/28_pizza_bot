import re


import click
from flask.cli import with_appcontext


from models import Pizza, catalog
from extensions import db


def upload_to_db(pizzas):
    for pizza in pizzas:
        for pizza_choice in pizza['choices']:
            height_cm, weight_gr = re.findall(r'\d+', pizza_choice['title'])
            Pizza.create(
                title = pizza.get('title'),
                description = pizza.get('description'),
                height_cm = int(height_cm),
                weight_gr = int(weight_gr),
                price = pizza_choice.get('price'),
            )


@click.command()
@with_appcontext
def create():
    db.create_all()
    click.echo('created {db}'.format(db=db.get_binds()))


@click.command()
@with_appcontext
def drop():
    db.drop_all()
    click.echo('table was dropped')


@click.command()
@with_appcontext
def feed():
    click.echo('from catalog got {count} pizzas'.format(count=len(catalog)))
    upload_to_db(catalog)
