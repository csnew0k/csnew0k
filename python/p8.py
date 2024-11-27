
from collections import deque

def fifo_page_replacement(pages, capacity):
    memory = deque(maxlen=capacity)
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) == capacity:
                memory.popleft()
            memory.append(page)
            page_faults += 1
        print(f"Page: {page} -> Memory: {list(memory)}")

    return page_faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
capacity = 3
page_faults = fifo_page_replacement(pages, capacity)
print(f"\nTotal Page Faults: {page_faults}")
