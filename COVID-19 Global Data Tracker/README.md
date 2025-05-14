# COVID-19 Global Data Tracker

This project analyzes global COVID-19 trends including cases, deaths, recoveries, and vaccinations across countries and time. It provides insights through data visualization and statistical analysis using Python.

## Project Structure

```
COVID-19 Global Data Tracker/
│
├── data/                      # Data directory (created when running data_downloader.py)
│   └── owid-covid-data.csv   # Downloaded dataset
│
├── data_downloader.py        # Script to download latest COVID-19 data
├── covid19_analysis.ipynb    # Main analysis notebook
└── README.md                 # Project documentation
```

## Requirements

- Python 3.x
- Required packages:
  - pandas
  - numpy
  - matplotlib
  - requests
  - jupyter

## Setup & Usage

1. Install required packages:
```bash
pip install pandas numpy matplotlib requests jupyter
```

2. Download the COVID-19 dataset:
```bash
python data_downloader.py
```

3. Open and run the Jupyter notebook:
```bash
jupyter notebook covid19_analysis.ipynb
```

## Analysis Components

1. **Data Collection**
   - Download data from Our World in Data
   - Save locally for analysis

2. **Data Loading & Exploration**
   - Load the dataset
   - Examine data structure
   - Check for missing values

3. **Data Cleaning**
   - Convert date formats
   - Handle missing values
   - Filter relevant countries

4. **Exploratory Data Analysis**
   - Total cases over time
   - Death rates analysis
   - Daily new cases trends
   - Country comparisons

5. **Vaccination Analysis**
   - Vaccination progress by country
   - Population percentage coverage
   - Vaccination rate trends

6. **Key Insights**
   - Analysis of trends
   - Country comparisons
   - Notable patterns and findings

## Data Source

This project uses the Our World in Data COVID-19 dataset:
https://covid.ourworldindata.org/data/owid-covid-data.csv

## License

This project is open-source and available under the MIT License.
