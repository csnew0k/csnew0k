
import multiprocessing, time, random

BUFFER_SIZE = 10
buffer = multiprocessing.Array('i', BUFFER_SIZE)
index = multiprocessing.Value('i', 0)
empty = multiprocessing.Semaphore(BUFFER_SIZE)
full = multiprocessing.Semaphore(0)
mutex = multiprocessing.Lock()

def producer():
    while True:
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        buffer[index.value] = item
        index.value = (index.value + 1) % BUFFER_SIZE
        print(f'Produced: {item}')
        mutex.release()
        full.release()
        time.sleep(random.random())

def consumer():
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer[(index.value - 1) % BUFFER_SIZE]
        print(f'Consumed: {item}')
        mutex.release()
        empty.release()
        time.sleep(random.random())

if __name__ == '__main__':
    multiprocessing.Process(target=producer).start()
    multiprocessing.Process(target=consumer).start()
