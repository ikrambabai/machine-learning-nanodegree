# Import libraries necessary for this project
import numpy as np
import pandas as pd
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

# Print the first few entries of the RMS Titanic data
print (full_data.head())
