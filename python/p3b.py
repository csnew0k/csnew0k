import threading

# Shared data and lock
data = 0
lock = threading.Lock()

# Reader function
def reader():
    global data
    with lock:
        print(f'Reader reads: {data}')

# Writer function
def writer():
    global data
    with lock:
        data += 1
        print(f'Writer writes: {data}')

# Creating threads
threads = []
for _ in range(3):
    t = threading.Thread(target=reader)
    threads.append(t)
    t.start()

for _ in range(2):
    t = threading.Thread(target=writer)
    threads.append(t)
    t.start()

# Joining threads
for t in threads:
    t.join()
