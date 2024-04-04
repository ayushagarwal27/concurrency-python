from threading import Thread


class Producer(Thread):

    def __init__(self, store: list, max_capacity: int):
        super().__init__()
        self.store = store
        self.max_capacity = max_capacity

    def run(self):
        while True:
            if len(self.store) < self.max_capacity:
                self.store.append(object())
                print(f'Store now have {len(self.store)} items')


class Consumer(Thread):
    def __init__(self, store: list):
        super().__init__()
        self.store = store

    def run(self):
        while True:
            if len(self.store) > 0:
                self.store.pop()
                print(f'Consumer consumed 1 item {len(self.store)} items')


store_obj = []
store_capacity = 5

for i in range(11):
    producer = Producer(store_obj, store_capacity)
    producer.start()

for i in range(11):
    consumer = Consumer(store_obj)
    consumer.start()
