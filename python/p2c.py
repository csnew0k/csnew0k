import threading

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def compute_fibonacci_range(start, end):
    for i in range(start, end):
        print(f"Fib({i}) = {fibonacci(i)}")

def main():
    num_threads = 4  # You can adjust this based on your system's capabilities
    max_fibonacci_number = 10  # Change this to generate more Fibonacci numbers

    # Divide the work among threads
    chunk_size = max_fibonacci_number // num_threads
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        thread = threading.Thread(target=compute_fibonacci_range, args=(start, end))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
