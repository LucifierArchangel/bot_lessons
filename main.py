import json

from telebot import TeleBot

from users_controller import UsersController

config = json.loads(open('config.json', 'r').read())
token = config['token']

user_controller = UsersController('db/users.json')

bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    text = message.text.split(' ')

    ref = 0
    if len(text) == 2:
        try:
            ref = int(text[1])
        except:
            pass

    username = message.from_user.username
    user_id = message.from_user.id

    user_controller.add_user(username, user_id, ref)

    bot.send_message(message.chat.id, 'Привет, ты запустил этого бота')

bot.infinity_polling()
