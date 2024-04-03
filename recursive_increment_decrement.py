from threading import Thread, RLock


class Counter:
    def __init__(self):
        self.value = 0


counter = Counter()


def increment_count(counter_obj: Counter, times: int, lock: RLock):
    if times == 0:
        return
    lock.acquire()
    counter_obj.value += 1
    increment_count(counter_obj, times - 1, lock)
    lock.release()


def decrement_count(counter_obj: Counter, times: int, lock: RLock):
    if times == 0:
        return
    lock.acquire()
    counter_obj.value -= 1
    decrement_count(counter_obj, times - 1, lock)
    lock.release()


times_val = 100

mutex = RLock()
incre = Thread(target=increment_count, args=(counter, times_val, mutex))
decre = Thread(target=decrement_count, args=(counter, times_val, mutex))

incre.start()
decre.start()

incre.join()
decre.join()

print(counter.value)
