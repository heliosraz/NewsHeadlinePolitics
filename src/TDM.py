import os
import csv
import numpy as np
import random
import pandas as pd
from pathlib import Path

np.random.seed(289)
# Finds path to data folder
p = Path(__file__).parents[1]
data = str(p) + "/data/data_collection/raw_data"

# Sets up variables
word_list = []
keeps = {}
term_document_matrices = []
results = set()

# Input parameters
samples = 1000

def count(title, query):
    c = 0
    for word in title:
        if (word == query):
            c = c + 1
    return c

for filename in os.listdir(data):
    file_path = "/".join([data,filename])
    
    rows = pd.read_csv(file_path, on_bad_lines='skip')
    keeps[filename] = sorted(random.sample(range(len(rows)),samples))
    rows_compressed = rows.iloc[keeps[filename],:]
    rows_compressed = rows_compressed.iloc[:, 1]

    for row in rows_compressed:
        results.update(str(row).lower().split("\n")[0].strip().split(" "))

results = list(results)

for filename in os.listdir(data):    
    file_path = "/".join([data,filename])
    
    rows=pd.read_csv(file_path, on_bad_lines='skip')
    rows_compressed = rows.iloc[keeps[filename],:]
    rows_compressed = rows_compressed.iloc[:, 1]
    
    term_document_matrix = []
    
    for title in rows_compressed:
        title = str(title).split(" ")
        for t in title:
            t=t.strip()
        array = np.zeros(len(results))

        for word in set(title):
            try:
                array[results.index(str(word))] = count(title, word) / len(title)
            except ValueError:
                print(title)
                continue
            
        term_document_matrix.append(array)
            
    term_document_matrices.append(term_document_matrix)
    

    


