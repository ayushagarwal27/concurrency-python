from threading import Thread, Lock


class Counter:
    def __init__(self):
        self.value = 0


counter = Counter()


def increment_count(counter_obj: Counter, times: int, lock: Lock):
    for i in range(times):
        lock.acquire()
        counter_obj.value += 1
        lock.release()


def decrement_count(counter_obj: Counter, times: int, lock: Lock):
    for i in range(times):
        lock.acquire()
        counter_obj.value -= 1
        lock.release()


times_val = 10000000

mutex = Lock()
incre = Thread(target=increment_count, args=(counter, times_val, mutex))
decre = Thread(target=decrement_count, args=(counter, times_val, mutex))

incre.start()
decre.start()

incre.join()
decre.join()

print(counter.value)
