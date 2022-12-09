import os
import csv
import random
import pandas as pd
from pathlib import Path

# Finds path to data folder
p = Path(__file__).parents[1]
data = str(p) + "/data/data_collection/"

# Sets up variables
all_words = []

# Input parameters
samples = 1000

 
# iterate over files in that directory
for filename in os.listdir(data):
    file = os.path.join(data, filename)
    #rows = csv.reader(open('foo.csv', 'rU'),delimiter=',')
    
    csvfile = pd.read_csv('data')
    row_count = sum(1 for row in open(data))
    skip = sorted(random.sample(range(row_count),row_count - samples))
    df = pd.read_csv(data, skiprows=skip)

    print(df)
    # 
