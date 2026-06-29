import sqlite3
import re

def setup_database():
    # Connect to SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect("logs_analysis.db")
    cursor = conn.cursor()
    
    # Create a structured table for our logs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS server_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        log_level TEXT,
        timestamp TEXT,
        thread_id INTEGER,
        step INTEGER,
        message TEXT
    )
    """)
    
    # CRITICAL PERFORMANCE STEP: Create an index on thread_id to accelerate queries
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_thread_id ON server_logs(thread_id)")
    
    conn.commit()
    return conn

def parse_and_load_logs(conn):
    cursor = conn.cursor()
    
    # Regex pattern to extract structured data from the C++/Python log format
    # Example line: [INFO] 2026-06-29 21:45:00 | Thread_ID: 2 | Step: 3 | Task successfully completed.
    log_pattern = re.compile(
        r"\[(?P<level>\w+)\]\s+(?P<time>[\d\s:-]+)\s*\|\s*Thread_ID:\s*(?P<thread>\d+)\s*\|\s*Step:\s*(?P<step>\d+)\s*\|\s*(?P<msg>.*)"
    )
    
    try:
        with open("simulation.log", "r") as file:
            for line in file:
                match = log_pattern.match(line.strip())
                if match:
                    # Insert parsed data directly into the SQL Database
                    cursor.execute("""
                        INSERT INTO server_logs (log_level, timestamp, thread_id, step, message)
                        VALUES (?, ?, ?, ?, ?)
                    """, (
                        match.group("level"),
                        match.group("time"),
                        int(match.group("thread")),
                        int(match.group("step")),
                        match.group("msg")
                    ))
        conn.commit()
        print("[ETL SUCCESS] All logs parsed and loaded into Indexed SQL Database.")
    except FileNotFoundError:
        print("[ERROR] simulation.log not found. Please run simulator.py first.")

def run_indexed_queries(conn):
    cursor = conn.cursor()
    
    print("\n--- Running Root Cause Analysis (SQL Query) ---")
    # Simulation of a production query: Finding all steps executed by a specific thread
    target_thread = 2
    
    cursor.execute("""
        SELECT timestamp, step, message 
        FROM server_logs 
        WHERE thread_id = ? 
        ORDER BY step ASC
    """, (target_thread,))
    
    results = cursor.fetchall()
    
    print(f"Logs found for Thread_ID {target_thread}:")
    for row in results:
        print(f" -> Time: {row[0]} | Step: {row[1]} | Status: {row[2]}")

def main():
    conn = setup_database()
    parse_and_load_logs(conn)
    run_indexed_queries(conn)
    conn.close()

if __name__ == "__main__":
    main()