import telebot
from jinja2 import Template
from os import getenv
import logging
import re


from models import Pizza
from extensions import db
from flask.helpers import get_debug_flag
import application


if get_debug_flag():
    logging.basicConfig(level=logging.INFO, format='%(message)s')


TOKEN = getenv('BOT_TOKEN')
if not TOKEN:
    raise Exception('BOT_TOKEN should be specified')


bot = telebot.TeleBot(TOKEN)


with open('templates/catalog.md', 'r') as catalog_file:
    catalog_tmpl = Template(catalog_file.read())


with open('templates/greetings.md', 'r') as greetings_file:
    greetings_tmpl = Template(greetings_file.read())


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, greetings_tmpl.render())


@bot.message_handler(commands=['menu'])
def show_catalog(message):
    with application.create_app(bot_db_query=True).app_context():
        catalog = Pizza.query.filter(
            Pizza.active.is_(True)).order_by(
            Pizza.title, Pizza.price).all()
    bot.send_message(message.chat.id, catalog_tmpl.render(catalog=catalog), parse_mode='Markdown')


def parse_pizza_order(message):
    raw_pizzas = re.findall(r'\w+\*\w+', message)
    parsed_pizzas = []
    for pizza in raw_pizzas:
        pizza_id, pizza_count = pizza.split('*')
        parsed_pizzas.append((int(pizza_id), int(pizza_count)))
    return parsed_pizzas


@bot.message_handler(func=lambda message: message.text.startswith('='),
                     content_types=["text"])
def calculate_order(message):
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        pizza_order = parse_pizza_order(message.text)
        with application.create_app(bot_db_query=True).app_context():
            order_price = 0
            for pizza_id, pizza_count in pizza_order:
                pizza_price = Pizza.get_by_id(pizza_id).price
                order_price += order_price + pizza_price * pizza_count
        answer = 'Ваш заказ стоит {price} руб'.format(price=order_price)
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        bot.reply_to(message, '= номер*количество номер*количество')


if __name__ == '__main__':
    bot.polling(none_stop=True)
