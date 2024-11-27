def is_safe(allocated, maximum, available):
    needed = maximum - allocated
    work = available.copy()
    finish = [False] * len(allocated)
    safe_seq = []

    while len(safe_seq) < len(allocated):
        found = False
        for i in range(len(allocated)):
            if not finish[i] and all(needed[i] <= work):
                work += allocated[i]
                safe_seq.append(i)
                finish[i] = True
                found = True
                break


        if not found:
            return False, []
    return True, safe_seq

# Example usage
allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
maximum = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
available = [3, 3, 2]

safe, sequence = is_safe(np.array(allocated), np.array(maximum), np.array(available))
print("Safe" if safe else "Not safe", "sequence:", sequence)
