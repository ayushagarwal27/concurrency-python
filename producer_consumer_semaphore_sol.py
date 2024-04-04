from threading import Semaphore, Thread

store = list()
store_capacity = 6

producer_semaphore = Semaphore(store_capacity)
consumer_semaphore = Semaphore(0)


def producer(store: list, producer_semaphore: Semaphore, consumer_semaphore: Semaphore):
    while True:
        producer_semaphore.acquire()
        store.append(object())
        print(f'Producer produced 1. Store size: {len(store)} ')
        consumer_semaphore.release()


def consumer(store: list, producer_semaphore: Semaphore, consumer_semaphore: Semaphore):
    while True:
        consumer_semaphore.acquire()
        store.pop()
        print(f'Consumer consumed 1. Store Size: {len(store)} ')
        producer_semaphore.release()


for i in range(10):
    Thread(target=producer, args=(store, producer_semaphore, consumer_semaphore)).start()

for i in range(10):
    Thread(target=consumer, args=(store, producer_semaphore, consumer_semaphore)).start()
