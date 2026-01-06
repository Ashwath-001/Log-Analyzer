# Smart Log Analyzer (C++)

A simple C++ tool that parses web/server logs, analyzes request patterns, and generates summary reports.  
Designed as a backend-focused project to demonstrate log parsing, data aggregation, and analysis using C++.

---

## Features

- Parses web access logs
- Extracts IP, timestamp, HTTP method, URL, status code, and bytes
- Aggregates requests by IP, URL, and status code
- Generates CSV reports
- Optional visualization using Python

---

## Project Structure

web-log-analyzer/
│
├── logs/
│   ├── sample1.log
│   └── sample2.log
│
├── reports/            # Generated reports
│
├── main.cpp            # Entry point
├── parser.cpp          # Log parsing logic
├── analyzer.cpp        # Analysis & report generation
├── visualize.py        # Report visualization
├── Makefile
└── README.md

---

## Build

Requires a C++17 compatible compiler.


make


This generates the executable `log_analyzer`.

---

## Usage

Analyze a single log file:


./log_analyzer logs/sample.log


Analyze multiple log files:


./log_analyzer logs/sample.log logs/sample2.log


---

## Output

- Console summary
- CSV report generated in the `reports/` directory

Example:
reports/report.csv

---

## Optional Visualization

If Python is available, you can visualize the generated report:
Requirements: Plotly, Pandas


    python visualize.py reports/report.csv

---

## Tech Stack

- C++ ==> STL, regex
- Python ==> visualization using plotly,pandas

---
