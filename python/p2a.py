import threading

def print_messages():
    for i in range(5):
        print(f"Thread says: Message {i}")
        # Simulate some work (you can replace this with actual work)
        for _ in range(1000000):
            pass

# Create a thread
my_thread = threading.Thread(target=print_messages)

# Start the thread
my_thread.start()

# Wait for the thread to finish (optional)
my_thread.join()

print("Main thread continues executing...")

