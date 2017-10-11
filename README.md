# Telegram Bot for Pizzeria

This project consists of flask-admin, sqlite and telegram bot.
Use flask to init pizzas database and then with flask-admin to populate the database with new pizzas or remove old ones.
Telegram bot will serve customas to show menu and calculate orders


# How to Use

Step 1. Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)

Step 2. Launch


Run the following commands to install project locally:

```
    # to install dependancies, alternatively try pip3:
    $ $ pip install -r requirements.txt


    #set the ``FLASK_APP`` and ``FLASK_DEBUG`` environment variables :
    $ export FLASK_DEBUG=1
    $ export FLASK_APP=autoapp.py


    # provide db path, by default -- pizza.db
    $ export SQLALCHEMY_DATABASE_URI=path/to/pizza.db


    # by default -- admin
    $ export USER_NAME=<user name>


    # by default -- password
    $ export PASSWORD=<password>


    # creates db and inits  'pizza' table
    $ flask create


    # drops 'pizza' table
    $ flask drop


    # loads or updates pizzas form catalog in models.py
    $ flask feed


    # run server and open http://127.0.0.1:5000/admin/pizzas page in browser
    $ flask run


    # the token below is not actual, you need to register a new one
    $ export BOT_TOKEN="110831855:AAE_GbIeVAUwk11O12vq4UeMnl20iADUtM"


    # run bot and visit it in browser by url obtained from BotFather
    $ python3 bot.py

```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)


