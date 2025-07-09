# Race Data Analysis Tool

This repository includes a simple Python script to analyze racing lap times.

## Files

- `race_analysis.py` - Script that reads a CSV file, prints summary statistics, and displays graphs of the results.
- `sample_race_data.csv` - Example dataset used with the script.

## Usage

Run the script with Python and provide a CSV file as argument:

```bash
python race_analysis.py sample_race_data.csv
```

The script outputs the average lap time for each driver and the fastest lap in each race.
It then opens a window showing bar charts of these statistics. Ensure `matplotlib` is installed:

```bash
pip install matplotlib
```
