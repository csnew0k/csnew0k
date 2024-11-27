class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time

def sjf_scheduling(processes):
    # Sort processes by burst time
    processes.sort(key=lambda x: x.burst_time)
    
    total_processes = len(processes)
    current_time = 0
    waiting_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    print("Process ID\tBurst Time\tWaiting Time\tTurnaround Time")
    for p in processes:
        waiting_time = current_time
        turnaround_time = waiting_time + p.burst_time
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        print(f"{p.pid}\t\t{p.burst_time}\t\t{waiting_time}\t\t{turnaround_time}")
        current_time += p.burst_time

    print(f"\nAverage Waiting Time: {total_waiting_time / total_processes:.2f}")
    print(f"Average Turnaround Time: {total_turnaround_time / total_processes:.2f}")

# Example usage
if __name__ == "__main__":
    processes = [Process(1, 6), Process(2, 8), Process(3, 7), Process(4, 3)]
    sjf_scheduling(processes)
