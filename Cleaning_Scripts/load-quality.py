"""
Python script to clean, process, and insert the quality data
into our SQL data tables.

Enter branch: git checkout Donny
Exit branch: git checkout main

Algo:
**Create data tables in ssh psql**
1. Load Data into pandas
2. Clean data as pandas df
3. Insert into sql data table
"""

import pandas as pd
import numpy as np
import sys
import psycopg2  # Can't find this module even though I installed itS
import credentials


# Connect to server
conn = psycopg2.connect(
    host="sculptor.stat.cmu.edu", dbname=credentials.DB_USER,
    user=credentials.DB_USER, password=credentials.DB_PASSWORD
)

# hhs_df = pd.read_csv(sys.argv[1])  # Argument input
hhs_df = pd.read_csv("Data/HHS/2022-09-23-hhs-data.csv")

# Data Cleaning
hhs_df.replace(-999999.0, np.nan, inplace=True)  # Replace -999999.0 with np.nan
hhs_df["collection_week"] = pd.to_datetime(hhs_df["collection_week"])  # Make date type

