def round_robin(processes, burst_time, quantum):
    n = len(processes)
    remaining_burst_time = burst_time[:]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > quantum:
                    time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    time += remaining_burst_time[i]
                    waiting_time[i] = time - burst_time[i]
                    remaining_burst_time[i] = 0

        if done:
            break

    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    print("Processes    Burst Time     Waiting Time    Turnaround Time")
    for i in range(n):
        print(f" {processes[i]}           {burst_time[i]}              {waiting_time[i]}                {turnaround_time[i]}")

# Example usage
processes = ['P1', 'P2', 'P3']
burst_time = [10, 5, 8]
quantum = 2

round_robin(processes, burst_time, quantum)
