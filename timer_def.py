import time
from datetime import datetime


def dev_file(username):
    with open(f'users/{username}.txt', 'x') as f:
        f.write(f'{username}\n')
    with open(f'delta/{username}.txt', 'x') as f:
        f.write(f'{username}\n')


def time_now():
    return datetime.fromtimestamp(int((str(time.time()).split('.'))[0]))


def ref_time(sec):
    hour = sec // 3600
    sec %= 3600
    m = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, m, sec)
    # if hour:
    #     return 'Вы занимались %02d часов %02d минут' % (hour, min)
    # elif min:
    #     return 'Вы занимались %02d минут' % (min)
    # else:
    #     return f'Вы занимались {round(sec)} секунд'


def start(username):
    start_time = time.time()
    s_time = time_now()
    with open(f'users/{username}.txt', 'a') as f:
        f.write(f'{s_time} start {start_time} \n')
    return s_time


def stop(username):
    stop_time = time.time()
    s_time = time_now()
    with open(f'users/{username}.txt', 'a') as f:
        f.write(f'{s_time} stop {stop_time} \n')
    return s_time


def delta_time(username):
    with open(f'users/{username}.txt', 'r') as file:
        file = file.readlines()
        start_t = float((file[-2].split(' '))[-2])
        stop_t = float((file[-1].split(' '))[-2])
        res = stop_t - start_t
    delta = ref_time(res)
    with open(f'delta/{username}.txt', 'a') as f:
        date = (str(time_now())).split(' ')[0]
        f.write(f'{date} {res} \n')
    return delta


def sum_delta(username):
    with open(f'delta/{username}.txt', 'r') as f:
        file = f.readlines()
        sum_deltas = 0
        for line in file:
            sum_deltas += float((line.split(' '))[-2])
        sum_res = ref_time(sum_deltas)
    return sum_res
