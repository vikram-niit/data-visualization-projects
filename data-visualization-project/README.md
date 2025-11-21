# Project Overview

A data-visualization project that analyzes and visualizes patterns, trends, and insights from a dataset using interactive and static plots.

## 🔹 Features
- Load raw datasets and clean them for analysis
- Generate multiple types of visualizations: line charts, bar charts, scatter plots, histograms, heatmaps
- Interactive filtering (by category, location, or other features)
- Summary statistics and exploratory data analysis (EDA)
- Export filtered datasets to CSV
- Modular project structure for scripts, notebooks, and reports
- Configurable via config.yaml

## 📁 Project Structure
```arduino
data-visualization-project/
│
├── data/
│   ├── raw/
│   │   └── dataset.csv
│   └── processed/
│       └── cleaned_dataset.csv
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── visualization.py
│   └── utils.py
│
├── reports/
│   ├── figures/
│   │   └── example_chart.png
│   └── summary_report.md
│
├── config.yaml
├── requirements.txt
├── README.md
└── run.py / app.py (optional, depending on framework)

```
