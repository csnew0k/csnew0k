def findWaitingTime(processes, n, bt, wt):
    # Waiting time for first process is 0
    wt[0] = 0

    # Calculating waiting time for each process
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def findTurnAroundTime(processes, n, bt, wt, tat):
    # Calculating turnaround time by adding burst time and waiting time
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n

    # Function to find waiting time of all processes
    findWaitingTime(processes, n, bt, wt)

    # Function to find turn around time for all processes
    findTurnAroundTime(processes, n, bt, wt, tat)

    # Display processes along with all details
    print("Processes    Burst time    Waiting time    Turn around time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(f"   {i + 1}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage waiting time = {total_wt / n:.2f}")
    print(f"Average turn around time = {total_tat / n:.2f}")

# Driver code
if __name__ == "__main__":
    processes = [1, 2, 3]
    n = len(processes)
    burst_time = [10, 5, 8]

    findavgTime(processes, n, burst_time)
