# Cyber Threat Intelligence Platform User Guide

## Introduction
This guide provides instructions on how to set up and use the Cyber Threat Intelligence Platform to aggregate, analyze, and generate insights from threat intelligence data.

## Prerequisites
- Python 3.x
- Required Python libraries: requests, pandas

## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Barrosleo/Cyber-Threat-Intelligence-Platform.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd Cyber-Threat-Intelligence-Platform
    ```

3. **Install Required Libraries**:
    ```bash
    pip install requests pandas
    ```

## Usage

### Data Aggregation
- Configure your API sources in `data_aggregation.py`.
- Run the data aggregation script:
    ```bash
    python src/data_aggregation.py
    ```

### Data Analysis
- Run the data analysis script:
    ```bash
    python src/data_analysis.py
    ```

### Generating Insights
- Run the insights generation script:
    ```bash
    python src/insights.py
    ```

## Troubleshooting
- Ensure all required libraries are installed.
- Verify the paths to your data files are correct.
