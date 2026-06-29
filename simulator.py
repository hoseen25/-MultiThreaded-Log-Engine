import threading
import time
import datetime

# A Lock (Mutex) to synchronize access to the shared log file
log_lock = threading.Lock()

# Worker function executed concurrently by each thread
def simulate_work(thread_id):
    for i in range(1, 6):
        # Simulate an operation taking some time (e.g., 500 milliseconds)
        time.sleep(0.5)
        
        # Get current timestamp formatted nicely
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Acquire the lock (Mutex) before writing to the shared resource (log file)
        with log_lock:
            with open("simulation.log", "a") as log_file:
                log_entry = f"[INFO] {timestamp} | Thread_ID: {thread_id} | Step: {i} | Task successfully completed.\n"
                log_file.write(log_entry)
        
        # Console feedback to trace runtime execution
        print(f"Thread {thread_id} wrote step {i} to log.")

def main():
    print("Starting Multi-Threaded Simulation in Python...")
    
    threads = []
    number_of_threads = 4
    
    # Spawn and activate worker threads
    for i in range(1, number_of_threads + 1):
        t = threading.Thread(target=simulate_work, args=(i,))
        threads.append(t)
        t.start()
        
    # Block the main thread until all worker threads finish execution
    for t in threads:
        t.join()
        
    print("Simulation finished. 'simulation.log' has been generated!")

if __name__ == "__main__":
    main()