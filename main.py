import telebot

from timer_def import *
from setting import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user = message.from_user.username
    try:
        dev_file(user)
    except(FileExistsError):
        bot.send_message(message.chat.id, f'''О! {message.from_user.first_name}, привет.
Забыл как пользоваться? - /help !''')
    else:
        bot.send_message(message.chat.id, f'''Привет {message.from_user.username}.
Этот бот поможет тебе отслеживать время затраченное на обучение!
Чтобы запустить таймер отправь /go
/help - помощь''')


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, f'''/go - запустить таймер.
/stop - остановить таймер.
/delta - длительность последнего занятия.
/sum - сумма всех занятий.''')


@bot.message_handler(commands=['go'])
def handle_run_timer(message):
    start_time = start(message.from_user.username)
    bot.send_message(message.chat.id, f'''Время начала обучения: {start_time}
Остановить таймер - /stop''')


@bot.message_handler(commands=['stop'])
def handle_run_timer(message):
    stop_time = stop(message.from_user.username)
    delta = get_delta(message.from_user.username)
    bot.send_message(message.chat.id, f'Вы закончили в {stop_time}\nДлительность занятия : {delta}\n/help')


@bot.message_handler(commands=['delta'])
def handle_run_timer(message):
    delta = get_delta(message.from_user.username)
    bot.send_message(message.chat.id, f'Длительность последнего занятия : {delta}\n/help')


@bot.message_handler(commands=['sum'])
def handle_run_timer(message):
    sum_time = sum_delta(message.from_user.username)
    bot.send_message(message.chat.id, f'Сумма всех твоих занятий : {sum_time}\n/help')


@bot.message_handler(content_types=['text'])
def handle_test(message):
    bot.reply_to(message, '/start - начать')


bot.polling(none_stop=True)
