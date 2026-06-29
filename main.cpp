#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
#include <fstream>
#include <chrono>

// Mutex to synchronize access to the shared log file across multiple threads
std::mutex logMutex; 

// Shared resource: Output file stream for generating simulation logs
std::ofstream logFile("simulation.log"); 

// Worker function executed concurrently by each thread
void simulateWork(int threadId) {
    for (int i = 1; i <= 5; ++i) {
        // Simulate an operation taking some time (e.g., 500 milliseconds)
        std::this_thread::sleep_for(std::chrono::milliseconds(500));

        // Use lock_guard for RAII-based thread safety. 
        // Automatically locks logMutex here and unlocks it when going out of scope.
        std::lock_guard<std::mutex> lock(logMutex);
        
        // Write standard formatted log entry for the Python parser to ingest later
        logFile << "[INFO] " << __TIMESTAMP__ << " | Thread_ID: " << threadId 
                << " | Step: " << i << " | Task successfully completed." << std::endl;
        
        // Console feedback to trace runtime execution
        std::cout << "Thread " << threadId << " wrote step " << i << " to log." << std::endl;
    } 
}

int main() {
    std::cout << "Starting Multi-Threaded Simulation..." << std::endl;
    
    // Container to keep track of all spawned threads
    std::vector<std::thread> threads;
    int numberOfThreads = 4; 

    // Spawn and activate worker threads
    for (int i = 1; i <= numberOfThreads; ++i) {
        threads.push_back(std::thread(simulateWork, i));
    }

    // Block the main thread until all worker threads finish execution
    for (auto& th : threads) {
        th.join();
    }

    // Clean up resources
    logFile.close();
    std::cout << "Simulation finished. 'simulation.log' has been generated!" << std::endl;
    return 0;
}