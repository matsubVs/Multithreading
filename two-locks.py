import threading
import time

a = 5 
b = 5

a_lock = threading.Lock()
b_lock = threading.Lock()


def thread1Calc():
    global a
    global b

    print('Thread 1 acquring lock a')
    a_lock.acquire()

    time.sleep(3)

    print('Thread 1 acquring lock b')
    b_lock.acquire()
    time.sleep(3)

    a += 5
    b += 5

    print('Thread 1 releasing both locks')
    a_lock.release()
    b_lock.release()

def thread2Calc():
    global a
    global b

    print('Thread 2 acquring lock b')
    b_lock.acquire()

    time.sleep(3)

    print('Thread 2 acquring lock a')
    a_lock.acquire()
    time.sleep(3)

    a += 10
    b += 10

    print('Thread 2 releasing both locks')
    b_lock.release()
    a_lock.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=thread1Calc)
    t1.start()
    
    t2 = threading.Thread(target=thread2Calc)
    t2.start()