from utility import *


def set_tasks(input_file="input_task.txt"):
    try:
        with open(input_file, "r", encoding='UTF8') as f:
            Variables.n_cores = int(f.readline())
            Variables.n_tasks = int(f.readline())

            temp = f.readline().split()

            Variables.wcet_min = int(temp[0])
            Variables.wcet_max = int(temp[1])
            Variables.mem_total = int(temp[2])
            Variables.util_cpu = float(temp[3]) * Variables.n_cores
            Variables.total_mem_usage = int(temp[4])

            Variables.k = int(temp[5])

            print("=======================================================")
            print("This is the Task Generation Input")

            print("n_cores  n_tasks")
            print(Variables.n_cores, Variables.n_tasks)

            print("wcet_min, wcet_max, mem_total, util_cpu, util_target, k")
            print(Variables.wcet_min, Variables.wcet_max, Variables.mem_total, Variables.util_cpu,
                  Variables.total_mem_usage, Variables.k)

    except FileNotFoundError:
        error("task 정보 파일을 찾을 수 없습니다.")
