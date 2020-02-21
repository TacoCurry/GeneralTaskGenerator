from input import *
import random

sim_time, arr_rate, bt_min, bt_max = get_input()

with open('generated.txt', 'w', encoding='utf-8') as f:
    count = 0
    for cur_time in range(sim_time):
        if random.random() <= arr_rate:
            f.write("{} {}\n".format(cur_time, random.randint(bt_min, bt_max)))
            count += 1

print("\n=======================================================")
print("This is the Task Generation Output")
print("Generate {} tasks.".format(count))
