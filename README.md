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

You will get an HTML dashboard like this:
![Analyzer Output](https://github.com/Ashwath-001/Log-Analyzer/main/images/demo.jpg)
---

## Tech Stack

- C++ ==> STL, regex
- Python ==> visualization using plotly,pandas

---
