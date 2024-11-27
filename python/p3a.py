
import threading
import queue
import time

# Define the buffer size
BUFFER_SIZE = 5

# Create a queue to act as the buffer
buffer = queue.Queue(BUFFER_SIZE)

# Producer function
def producer():
    for i in range(10):
        item = f"item-{i}"
        buffer.put(item)
        print(f"Produced: {item}")
        time.sleep(1)

# Consumer function
def consumer():
    for i in range(10):
        item = buffer.get()
        print(f"Consumed: {item}")
        buffer.task_done()
        time.sleep(2)

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the threads to complete
producer_thread.join()
consumer_thread.join()

print("All items produced and consumed.")

