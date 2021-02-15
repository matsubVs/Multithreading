import threading

from multithreading.count_three_sum import read_ints, count_three_sum

if __name__ == "__main__":
    print('startedMain')

    ints = read_ints("./ints/1Kints.txt")
    t1 = threading.Thread(target=count_three_sum, args=(ints,),daemon=True)
    t1.start()

    print('What are we waiting for?')
    print('ended main')
