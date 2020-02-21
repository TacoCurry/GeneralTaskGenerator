def error(msg):
    print(msg)
    exit(0)


def get_input(input_file="input.txt"):
    try:
        with open(input_file, "r", encoding='UTF8') as f:
            sim_time = int(f.readline())
            arr_rate = float(f.readline())

            temp = f.readline().split()

            bt_min = int(temp[0])
            bt_max = int(temp[1])

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

            return sim_time, arr_rate, bt_min, bt_max

    except FileNotFoundError:
        error("task 정보 파일을 찾을 수 없습니다.")
