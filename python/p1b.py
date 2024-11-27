import multiprocessing
import time
import random

def producer(queue, empty, full):
    for i in range(10):
        item = random.randint(1, 100)
        empty.acquire()
        queue.put(item)
        print(f'Produced: {item}')
        full.release()
        time.sleep(random.random())

def consumer(queue, empty, full):
    for i in range(10):
        full.acquire()
        item = queue.get()
        print(f'Consumed: {item}')
        empty.release()
        time.sleep(random.random())


if __name__ == '__main__':
    queue = multiprocessing.Queue(5)
    empty = multiprocessing.Semaphore(5)
    full = multiprocessing.Semaphore(0)

    producer_process = multiprocessing.Process(target=producer, args=(queue, empty, full))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue, empty, full))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()
