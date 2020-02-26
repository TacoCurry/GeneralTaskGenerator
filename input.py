def error(msg):
    print(msg)
    exit(0)


def get_input(input_file="input.txt"):
    try:
        with open(input_file, "r", encoding='UTF8') as f:
            sim_time = int(f.readline())
            arr_rate = float(f.readline())

            temp1 = f.readline().split()

            bt_min = int(temp1[0])
            bt_max = int(temp1[1])

            temp2 = f.readline().split()

            mem_total = int(temp2[0])
            total_memory_usage = int(temp2[1])

            print("=======================================================")
            print("This is the Task Generation Input")

            print("sim_time")
            print(sim_time)

            print("arr_rate")
            print(arr_rate)

            print("bt_min")
            print(bt_min)

            print("bt_max")
            print(bt_max)

            print("mem_total")
            print(mem_total)

            print("total_memory_usage")
            print(total_memory_usage)
            return sim_time, arr_rate, bt_min, bt_max, mem_total, total_memory_usage

    except FileNotFoundError:
        error("task 정보 파일을 찾을 수 없습니다.")
