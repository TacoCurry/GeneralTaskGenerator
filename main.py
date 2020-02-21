from input import *
import random

sim_time, arr_rate, bt_min, bt_max = get_input()

with open('generated.txt', 'w', encoding='utf-8') as f:
    for cur_time in range(sim_time):
        if random.random() <= arr_rate:
            f.write("{} {}\n".format(cur_time, random.randint(bt_min, bt_max)))
