import matplotlib.pyplot as plt
from tabulate import tabulate

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

# ---------------- MEMORY ALLOCATION -------------
def run_memory_algorithm(algo_name, block_sizes, process_sizes):
    blocks = [[size, size, False] for size in block_sizes]
    allocation = [-1] * len(process_sizes)

    for i, p_size in enumerate(process_sizes):
        best_idx = -1
        for j in range(len(blocks)):
            if not blocks[j][2] and blocks[j][0] >= p_size:
                if algo_name == "First Fit":
                    best_idx = j
                    break
                elif algo_name == "Best Fit":
                    if best_idx == -1 or blocks[j][0] < blocks[best_idx][0]:
                        best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx][2] = True
    
    internal_frag = 0
    for i, b_idx in enumerate(allocation):
        if b_idx != -1:
            internal_frag += (blocks[b_idx][1] - process_sizes[i])
    external_frag = sum(b[1] for b in blocks if not b[2])
    
    return allocation, internal_frag, external_frag

def plot_comparison(ff_data, bf_data):
    labels = ['First Fit', 'Best Fit']
    internal = [ff_data['int'], bf_data['int']]
    external = [ff_data['ext'], bf_data['ext']]
    x = [0, 1]
    width = 0.35
    plt.figure(figsize=(7, 4))
    plt.bar(x, internal, width, label='Internal Fragmentation', color='skyblue')
    plt.bar([i + width for i in x], external, width, label='External Fragmentation', color='salmon')
    plt.ylabel('Memory Size (KB)')
    plt.title('Fragmentation Comparison: First Fit vs Best Fit')
    plt.xticks([i + width/2 for i in x], labels)
    plt.legend()
    plt.show()

def memory_allocation():
    print("\n--- MEMORY ALLOCATION (First Fit vs Best Fit) ---\n")
    try:
        b_input = input("Enter block sizes (space separated): ")
        block_sizes = [int(x) for x in b_input.split()]
        p_input = input("Enter process sizes (space separated): ")
        process_sizes = [int(x) for x in p_input.split()]

        ff_alloc, ff_int, ff_ext = run_memory_algorithm("First Fit", block_sizes, process_sizes)
        bf_alloc, bf_int, bf_ext = run_memory_algorithm("Best Fit", block_sizes, process_sizes)

        table_rows = []
        for i in range(len(process_sizes)):
            # 1. First Fit result string
            ff_idx = ff_alloc[i] 
            if ff_idx != -1:
                # Use the index to find the original size in the block_sizes list
                ff_res = f"Block {ff_idx + 1} ({block_sizes[ff_idx]})"
            else:
                ff_res = "Not Allocated"

            # 2. Best Fit result string
            bf_idx = bf_alloc[i] 
            if bf_idx != -1:
                bf_res = f"Block {bf_idx + 1} ({block_sizes[bf_idx]})"
            else:
                bf_res = "Not Allocated"

            table_rows.append([f"P{i+1} ({process_sizes[i]})", ff_res, bf_res])

        print("\nAllocation Results:")
        print(tabulate(table_rows, headers=["Process", "First Fit", "Best Fit"], tablefmt="fancy_grid"))

        summary = [
            ["Metric", "First Fit", "Best Fit"],
            ["Internal Fragmentation", f"{ff_int}", f"{bf_int}"],
            ["External Fragmentation", f"{ff_ext}", f"{bf_ext}"],
            ["Total Waste", f"{ff_int + ff_ext}", f"{bf_int + bf_ext}"]
        ]
        print("\nPerformance Comparison:")
        print(tabulate(summary, headers="firstrow", tablefmt="fancy_grid"))

        plot_comparison({'int': ff_int, 'ext': ff_ext}, {'int': bf_int, 'ext': bf_ext})
        
        input("\nPress Enter to return to the Main Menu...")

    except ValueError:
        print("Error: Please enter numbers separated by spaces.")

# ---------------- PAGE REPLACEMENT (FIFO vs LRU) ----------------
def page_replacement():
    print("\n--- Page Replacement: FIFO vs LRU ---")
    try:
        pages = [int(x) for x in input("Enter page reference string (space separated): ").split()]
        capacity = int(input("Enter number of frames: "))
        
        # --- FIFO Implementation ---
        print("\n--- FIFO Execution Step-by-Step ---")
        frames_fifo = []
        faults_fifo = 0
        for page in pages:
            if page not in frames_fifo:
                if len(frames_fifo) < capacity:
                    frames_fifo.append(page)
                else:
                    frames_fifo.pop(0)
                    frames_fifo.append(page)
                faults_fifo += 1
                print(f"Page {page}: {frames_fifo} (Fault)")
            else:
                print(f"Page {page}: {frames_fifo} (Hit)")
        
        # --- LRU Implementation ---
        print("\n--- LRU Execution Step-by-Step ---")
        frames_lru = []
        faults_lru = 0
        for page in pages:
            if page not in frames_lru:
                if len(frames_lru) < capacity:
                    frames_lru.append(page)
                else:
                    frames_lru.pop(0)  # Removes the least recently used element
                    frames_lru.append(page)
                faults_lru += 1
                print(f"Page {page}: {frames_lru} (Fault)")
            else:
                # If hit, remove it from its current position and append it to the end (Most Recently Used)
                frames_lru.remove(page)
                frames_lru.append(page)
                print(f"Page {page}: {frames_lru} (Hit)")

        # --- Comparison & Analysis ---
        print("\n--- Performance Comparison ---")
        summary = [
            ["Algorithm", "Total Page Faults"],
            ["FIFO", f"{faults_fifo}"],
            ["LRU", f"{faults_lru}"]
        ]
        print(tabulate(summary, headers="firstrow", tablefmt="fancy_grid"))

        # Plotting the results
        labels = ['FIFO', 'LRU']
        faults = [faults_fifo, faults_lru]
        
        plt.figure(figsize=(6, 4))
        plt.bar(labels, faults, color=['skyblue', 'salmon'], width=0.4)
        plt.ylabel('Number of Page Faults')
        plt.title('Page Fault Comparison: FIFO vs LRU')
        plt.show()

        input("\nPress Enter to return to the Main Menu...")

    except ValueError:
        print("Invalid input! Please enter numbers separated by spaces.")

# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n================ OS PROJECT MENU ================")
        print("1. CPU Scheduling (FCFS)")
        print("2. Memory Allocation (First Fit vs Best Fit)")
        print("3. Page Replacement (FIFO vs LRU)")
        print("4. Exit")
        
        choice = input("Select a task (1-4): ")
        
        if choice == '1':
            cpu_scheduling_fcfs()
        elif choice == '2':
            memory_allocation()
        elif choice == '3':
            page_replacement()
        elif choice == '4':
            print("Exiting... Good luck with your project!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
