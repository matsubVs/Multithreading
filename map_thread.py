import concurrent.futures

from multithreading.count_three_sum import count_three_sum, read_ints

if __name__ == '__main__':
    print(f"started main")

    data = read_ints('./ints/1Kints.txt')
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(count_three_sum, (data, data), ('t1', 't2'))
        for r in results:
            print(f"{r=}")

    print('ended main')
