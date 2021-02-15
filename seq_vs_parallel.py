import threading

from multithreading.count_three_sum import count_three_sum, read_ints
from multithreading.decorators import measure_time


@measure_time
def run_in_parallel(ints):
    t1 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't1'))
    t2 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't2'))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


@measure_time
def run_sequentially(ints):
    count_three_sum(ints)
    count_three_sum(ints)


if __name__ == "__main__":
    print("start")
    ints = read_ints("./ints/1Kints.txt")

    run_in_parallel(ints)
    run_sequentially(ints)

    print("Ended main")

