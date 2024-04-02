from threading import Thread


class Counter:
    def __init__(self):
        self.value = 0


counter = Counter()


def increment_count(counter_obj: Counter, times: int):
    for i in range(times):
        counter_obj.value += 1


def decrement_count(counter_obj: Counter, times: int):
    for i in range(times):
        counter_obj.value -= 1


times_val = 10000000

incre = Thread(target=increment_count, args=(counter, times_val))
decre = Thread(target=decrement_count, args=(counter, times_val))

incre.start()
decre.start()

incre.join()
decre.join()

print(counter.value)
