from utility import *

util_cpu_1task = 0
mem_req_1task = 0
mem_req_total = 0
util_sum_cpu = 0


def gen_task():
    global util_cpu_1task, mem_req_1task
    util_cpu_1task = Variables.util_cpu / Variables.n_tasks
    mem_req_1task = Variables.total_mem_usage / Variables.n_tasks

    print("=======================================================")

    print(f'util_cpu_1task:{format(util_cpu_1task, ".6f")}')
    print(f'mem_req_1task: {format(mem_req_1task, ".0f")}')

    print("=======================================================")

    with open("task_generated.txt", "w", encoding='UTF8') as f:
        f.write("wcet duration mem_req mem_active_ratio m k")
        for i in range(Variables.n_tasks):
            print("--------------------------")
            print(f'Task Number: {i + 1}')
            do_gen_task(f)
            print("--------------------------")

    print(f'util_total_mem: {format(get_util_overhead_by_mem(mem_req_total), ".6f")}')
    print(f'util_total_cpu: {format(util_sum_cpu, ".6f")}')
    print(f'mem_req_total: {format(mem_req_total, ".0f")}')


def do_gen_task(input_file):
    global util_cpu_1task, mem_req_1task, util_sum_cpu, mem_req_total

    wcet = Variables.wcet_min + get_rand(Variables.wcet_max - Variables.wcet_min)
    duration = wcet / util_cpu_1task + int(get_rand(wcet / util_cpu_1task / 2)) - int(
        get_rand(wcet / util_cpu_1task / 2))

    mem_req = mem_req_1task + int(get_rand(mem_req_1task / 2)) - int(get_rand(mem_req_1task / 2))
    mem_active_ratio = 0.1 + get_rand(1000) / 10000.0 - get_rand(1000) / 10000.0

    m = int(Variables.k - get_rand(Variables.k - 1))  # m range

    util_sum_cpu += (wcet / duration) * (m / Variables.k)  # util changes

    mem_req_total += mem_req

    # task parameter
    line = f'{wcet} {format(duration, ".0f")} {format(mem_req, ".0f")} {format(mem_active_ratio, ".6f")} {m} {Variables.k} \n'
    print(f'util_total_mem: {format(get_util_overhead_by_mem(mem_req_total), ".6f")}')
    print(f'util_total_cpu: {format(util_sum_cpu, ".6f")}')
    print(f'mem_req_total: {format(mem_req_total, ".0f")}')
    input_file.write(line)


def get_util_overhead_by_mem(mem_used):
    return mem_used / Variables.mem_total
