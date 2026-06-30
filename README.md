# 🚀 Multi-Threaded Log Engine & Automated ETL Pipeline

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/hoseen25/MultiThreaded-Log-Engine/pipeline.yml?branch=main&style=for-the-badge&label=CI%20Pipeline&color=22c55e)
![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Database](https://img.shields.io/badge/Database-SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

An enterprise-grade showcase demonstrating core DevOps, backend, and data engineering patterns: **multi-threading synchronization, high-speed Regex parsing, relational database indexing, and cloud-native CI/CD automation.**

---

## 🗺️ System Architecture & Data Flow

```mermaid
graph TD
    %% Node Definitions
    A[simulator.py<br>Multi-Threaded Engine] -->|1. Safe Concurrent Writes| B(simulation.log<br>Raw Shared Resource)
    B -->|2. Extract & Ingest| C[log_analyzer.py<br>Python ETL Engine]
    C -->|3. Structured Load| D[(SQLite Database<br>logs_analysis.db)]
    D -->|4. High-Speed Lookup| E[B-Tree Index<br>thread_id]
    F[GitHub Actions<br>CI/CD Pipeline] -.->|5. Automated Validation| A
    F -.->|5. Automated Validation| C

    %% Style Customizations
    style A fill:#4F46E5,stroke:#312E81,stroke-width:2px,color:#fff
    style B fill:#F59E0B,stroke:#78350F,stroke-width:2px,color:#fff
    style C fill:#10B981,stroke:#065F46,stroke-width:2px,color:#fff
    style D fill:#3B82F6,stroke:#1E3A8A,stroke-width:2px,color:#fff
    style E fill:#EC4899,stroke:#701A75,stroke-width:2px,color:#fff
    style F fill:#8B5CF6,stroke:#4C1D95,stroke-width:2px,color:#fff



Concurrency Layer (simulator.py): Spawns multiple concurrent threads simulating isolated backend tasks. Uses thread synchronization (Threading.Lock) to prevent race conditions during heavy file I/O operations.ETL & Ingestion Layer (log_analyzer.py): A structured data pipeline that extracts raw unstructured log data using Regular Expressions (Regex), transforms it into typed schemas, and loads it to the storage layer.Database Tuning: Implements an explicit B-Tree Index on high-cardinality fields (thread_id) to optimize analytical querying speeds from linear scans $O(N)$ down to logarithmic lookups $O(\log N)$.Cloud Validation (CI): Integrated with GitHub Actions to provision ephemeral Linux containers on every code push, ensuring continuous integration and build stability.


🛠️ Tech Stack & ToolsLayerTechnology / ToolKey Pattern & FeatureLanguage & ConcurrencyPython 3.10+ (threading)Mutex Locks & Thread-SafetyData ParsingPython re (Regex)High-Performance Pattern MatchingStorage EngineSQLite 3Relational Schema & Index OptimizationAutomation & CI/CDGitHub ActionsAutomated Cloud Workflows on UbuntuVersion ControlGit & GitHubCode Management & Architecture Docs


📂 Project StructurePlaintextMultiThreaded-Log-Engine/
├── .github/
│   └── workflows/
│       └── pipeline.yml       # GitHub Actions CI pipeline configuration
├── .gitignore                 # Excludes raw logs and local DB files from Git
├── README.md                  # Enterprise-grade project documentation
├── log_analyzer.py            # ETL engine & SQL analytical query processor
└── simulator.py               # Multi-threaded concurrent log generation script
    style E fill:#EC4899,stroke:#701A75,stroke-width:2px,color:#fff
    style F fill:#8B5CF6,stroke:#4C1D95,stroke-width:2px,color:#fff
