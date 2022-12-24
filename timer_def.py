import time
from datetime import datetime


def dev_file(username):
    with open(f'users/{username}.txt', 'x'):
        pass
    with open(f'delta/{username}.txt', 'x'):
        pass


def time_now():
    return datetime.fromtimestamp(int((str(time.time()).split('.'))[0]))


def ref_time(sec):
    hour = sec // 3600
    sec %= 3600
    minute = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, minute, sec)


def start(username):
    start_time = time.time()
    s_time = ((str(time_now())).split(' ')[-1])[:5]
    with open(f'users/{username}.txt', 'a') as file:
        file.write(f'{s_time} start {start_time} \n')
    return s_time


def stop(username):
    stop_time = time.time()
    s_time = ((str(time_now())).split(' ')[-1])[:5]
    with open(f'users/{username}.txt', 'a') as file:
        file.write(f'{s_time} stop {stop_time} \n')
    delta_time(username)
    return s_time


def delta_time(username):
    with open(f'users/{username}.txt', 'r') as file:
        file = file.readlines()
        start_t = float((file[-2].split(' '))[-2])
        stop_t = float((file[-1].split(' '))[-2])
        res = stop_t - start_t
    with open(f'delta/{username}.txt', 'a') as file:
        date = (str(time_now())).split(' ')[0]
        file.write(f'{date} {res} \n')
    return None


def get_delta(username):
    with open(f'delta/{username}.txt', 'r') as file:
        file = file.readlines()
        res = float((file[-1].split(' '))[-2])
        delta = ref_time(res)
    return delta


def sum_delta(username):
    with open(f'delta/{username}.txt', 'r') as file:
        file_sum = file.readlines()
        sum_deltas = 0
        for line in file_sum:
            sum_deltas += float((line.split(' '))[-2])
        sum_res = ref_time(sum_deltas)
    return sum_res
