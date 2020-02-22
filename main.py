from input import *
import random

sim_time, arr_rate, bt_min, bt_max = get_input()

with open('input_nonrtt.txt', 'w', encoding='utf-8') as f:
    tasks = [(cur_time, random.randint(bt_min, bt_max))
             for cur_time in range(sim_time) if random.random() <= arr_rate]

    f.write("{}\n".format(len(tasks)))
    for task in tasks:
        f.write("{} {}\n".format(*task))

print("\n=======================================================")
print("This is the Task Generation Output")
print("Generate {} tasks.".format(len(tasks)))
