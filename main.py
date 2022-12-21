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
        bot.reply_to(message, f'''О! {message.from_user.first_name}, привет.
Забыл как пользоваться? Отравь "/help" !''')
    else:
        bot.reply_to(message, f'''Привет {message.from_user.username}.
Этот бот поможет тебе отслеживать время затраченное на обучение!
Чтобы запустить таймер отправь "/go"''')


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, f'''Чтобы запустить таймер отправь - "/go".
Чтобы остановить - "/stop"
Чтобы узнать ддлительность последнего занятия - "/delta"''')


@bot.message_handler(commands=['go'])
def handle_run_timer(message):
    start_time = start(message.from_user.username)
    bot.reply_to(message, f'''Время начала обучения: {start_time}
Остановить таймер - /stop''')


@bot.message_handler(commands=['stop'])
def handle_run_timer(message):
    stop_time = stop(message.from_user.username)
    delta = delta_time(message.from_user.username)
    bot.reply_to(message, f'Вы закончили в {stop_time}.\nДлительность занятия : {delta}')


@bot.message_handler(commands=['delta'])
def handle_run_timer(message):
    delta = delta_time(message.from_user.username)
    bot.reply_to(message, f'Длительность последнего занятия : {delta}')


@bot.message_handler(commands=['sum'])
def handle_run_timer(message):
    sum_time = sum_delta(message.from_user.username)
    bot.reply_to(message, f'Сумма всех ваших занятий : {sum_time}')


bot.polling(none_stop=True)
