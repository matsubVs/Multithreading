import threading
import time


def f1():
    print('First thread \n')
    print('start f1 joining f2\n')
    time.sleep(1)
    t2.join()

    print('f1 sleeping')
    time.sleep(3)
    print('end of f1')

def f2():
    print('Second thread \n')
    print('start f2 joining f1\n')
    time.sleep(1)
    t1.join()

    print('f2 sleeping')
    time.sleep(3)
    print('end of f2')


if __name__ == "__main__":
    t1 = threading.Thread(target=f1)
    t2 = threading.Thread(target=f2)

    t1.start()
    t2.start()