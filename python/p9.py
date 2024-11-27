
def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    lru = {}

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                lru_page = min(lru, key=lru.get)
                memory.remove(lru_page)
                memory.append(page)
            page_faults += 1
        lru[page] = i
        print(f"Page: {page} -> Memory: {memory}")

    return page_faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
capacity = 3
page_faults = lru_page_replacement(pages, capacity)
print(f"\nTotal Page Faults: {page_faults}")
