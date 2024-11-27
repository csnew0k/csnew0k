import threading

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")

def print_letters():

    for letter in 'abcde':
        print(f"Letter: {letter}")

# Create two threads
number_thread = threading.Thread(target=print_numbers)
letter_thread = threading.Thread(target=print_letters)

# Start the threads
number_thread.start()
letter_thread.start()

# Wait for both threads to finish
number_thread.join()
letter_thread.join()

print("Both threads have finished.")
