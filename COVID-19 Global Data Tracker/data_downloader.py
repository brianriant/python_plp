"""
Module for downloading COVID-19 data from Our World in Data.

This module provides functionality to download the latest COVID-19 dataset
from Our World in Data, save it locally, and display basic information
about the downloaded dataset.
"""

import os
import pandas as pd
import requests


def download_covid_data():
    """
    Downloads the latest COVID-19 dataset from Our World in Data and saves it locally.

    The function performs the following operations:
    1. Creates a 'data' directory if it doesn't exist
    2. Downloads the dataset from Our World in Data
    3. Saves the data as a CSV file in the 'data' directory
    4. Displays basic information about the downloaded dataset

    Prints status messages during the download process and dataset information
    upon successful download.
    """
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    # URL for Our World in Data COVID-19 dataset
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

    try:
        print("Downloading COVID-19 data...")
        df = pd.read_csv(url)

        # Save to local file
        output_path = os.path.join('data', 'owid-covid-data.csv')
        df.to_csv(output_path, index=False)
        print(f"Data successfully downloaded and saved to {output_path}")

        # Print basic dataset info
        print("\nDataset Info:")
        print(f"Number of rows: {len(df)}")
        print(f"Number of columns: {len(df.columns)}")
        print(f"Date range: {df['date'].min()} to {df['date'].max()}")

    except Exception as e:
        print(f"Error downloading data: {str(e)}")

if __name__ == "__main__":
    download_covid_data()
