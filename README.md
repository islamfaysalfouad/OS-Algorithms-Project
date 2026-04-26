# 🖥️ OS Algorithms Simulation Project
---

## 📝 Project Overview
This project is a comprehensive simulation of core **Operating System Algorithms**, developed as part of the OS course at **Alexandria National University**. It implements key concepts in CPU scheduling, memory management, and page replacement strategies using **Python** and **C**.

> **Target Goal:** To analyze and compare the efficiency of different OS strategies in handling system resources.

---

## 🚀 Implemented Algorithms

### 1. CPU Scheduling (FCFS)
- **Algorithm:** First-Come, First-Served.
- **Metrics Calculated:** Waiting Time (WT), Turnaround Time (TAT), and Average performance.
- **Implementation:** Both in Python for simulation and C for performance benchmarking.

### 2. Memory Management (First Fit)
- **Strategy:** Dynamic memory allocation using the First Fit approach.
- **Features:** Simulates how the OS finds the first available block of memory that fits a process, tracking internal fragmentation.

### 3. Page Replacement (FIFO)
- **Strategy:** First-In, First-Out page replacement.
- **Analysis:** Tracks **Page Faults** and manages the frame stack effectively to simulate virtual memory behavior.

---

## 🛠️ Tech Stack & Tools
- **Languages:** ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
- **Environment:** ![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)
- **Version Control:** ![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)

---

## 📁 Project Structure
```bash
├── OSproject.py      # Main Python simulation (All algorithms)
├── sched.c           # C implementation for CPU Scheduling
├── sched             # Compiled binary for Linux
└── README.md         # Project documentation
