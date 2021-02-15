from multithreading.count_three_sum import read_ints, count_three_sum


if __name__ == "__main__":
    print('startedMain')

    ints = read_ints("./ints/1Kints.txt")
    count_three_sum(ints)

    print('What are we waiting for?')
    print('ended main')
