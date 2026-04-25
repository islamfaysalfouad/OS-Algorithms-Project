import matplotlib.pyplot as plt

# ---------------- CPU SCHEDULING (FCFS) ----------------
def cpu_scheduling_fcfs():
    print("\n--- CPU Scheduling: FCFS ---")
    try:
        n = int(input("Enter number of processes: "))
        processes = []
        for i in range(n):
            at = int(input(f"Arrival Time for P{i+1}: "))
            bt = int(input(f"Burst Time for P{i+1}: "))
            processes.append({'id': i+1, 'at': at, 'bt': bt})

        # ترتيب حسب وقت الوصول
        processes.sort(key=lambda x: x['at'])
        
        current_time = 0
        print("\n--- Step-by-Step Execution ---")
        for p in processes:
            if current_time < p['at']:
                current_time = p['at']
            
            p['wt'] = current_time - p['at']
            p['tat'] = p['wt'] + p['bt']
            
            print(f"Time {current_time}: Process {p['id']} starts")
            current_time += p['bt']
            print(f"Time {current_time}: Process {p['id']} finished")

        avg_wt = sum(p['wt'] for p in processes) / n
        avg_tat = sum(p['tat'] for p in processes) / n

        print("\nFinal Results: PID | Waiting Time | Turnaround Time")
        for p in processes:
            print(f" P{p['id']}  |      {p['wt']}       |       {p['tat']}")
        print(f"\nAverage Waiting Time: {avg_wt:.2f}")
        print(f"Average Turnaround Time: {avg_tat:.2f}")
    except ValueError:
        print("Please enter valid numbers!")

# ---------------- MEMORY ALLOCATION (First Fit) ----------------
def memory_allocation_first_fit():
    print("\n--- Memory Allocation: First Fit ---")
    try:
        blocks_input = input("Enter block sizes (space separated): ").split()
        blocks = [int(x) for x in blocks_input]
        procs_input = input("Enter process sizes (space separated): ").split()
        procs = [int(x) for x in procs_input]

        allocation = [-1] * len(procs)
        
        for i in range(len(procs)):
            for j in range(len(blocks)):
                if blocks[j] >= procs[i]:
                    allocation[i] = j
                    blocks[j] -= procs[i]
                    break

        print("\nAllocation Results:")
        for i in range(len(procs)):
            res = f"Block {allocation[i] + 1}" if allocation[i] != -1 else "Not Allocated"
            print(f"Process {i+1} ({procs[i]}) -> {res}")
    except ValueError:
        print("Invalid input! Use numbers separated by spaces.")

# ---------------- PAGE REPLACEMENT (FIFO) ----------------
def page_replacement_fifo():
    print("\n--- Page Replacement: FIFO ---")
    try:
        pages = [int(x) for x in input("Enter page reference string (space separated): ").split()]
        capacity = int(input("Enter number of frames: "))
        
        frames = []
        page_faults = 0
        print("\nStep-by-step Frame Status:")
        for page in pages:
            if page not in frames:
                if len(frames) < capacity:
                    frames.append(page)
                else:
                    frames.pop(0)
                    frames.append(page)
                page_faults += 1
                print(f"Page {page}: {frames} (Fault)")
            else:
                print(f"Page {page}: {frames} (Hit)")
        print(f"\nTotal Page Faults: {page_faults}")
    except ValueError:
        print("Invalid input!")

# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n================ OS PROJECT MENU ================")
        print("1. CPU Scheduling (FCFS)")
        print("2. Memory Allocation (First Fit)")
        print("3. Page Replacement (FIFO)")
        print("4. Exit")
        
        choice = input("Select a task (1-4): ")
        
        if choice == '1':
            cpu_scheduling_fcfs()
        elif choice == '2':
            memory_allocation_first_fit()
        elif choice == '3':
            page_replacement_fifo()
        elif choice == '4':
            print("Exiting... Good luck with your project!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
