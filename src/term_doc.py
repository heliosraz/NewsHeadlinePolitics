#import packages
import numpy as np
import random
from collections import Counter
import os
import pandas as pd
from pathlib import Path
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
key={'nyt_headlines.csv':-1,'foxnews_headlines.csv':2,'washingtonpost_headlines.csv':-1,'csmonitor_headlines.csv':0,'nypost_headlines.csv':1,'cnn_headlines.csv':-2}
y=[]

# Input parameters
samples = 2000

# methods
# get tdms 
dir = Path(__file__).parents[1]
tdm= str(dir) + "/data/data_collection/processed_data/term_matrices"

def count(title, query):
    c = 0
    for word in title:
        if (str(query).lower() in str(word).lower()):
            c = c + 1
    return c

#generating the term document matrix
def term_matrix(samples=100, t_headline: str=None):
    results=set()
    for filename in os.listdir(data):
        file_path = "/".join([data,filename])
        
        rows = pd.read_csv(file_path, on_bad_lines='skip')
        if samples<=len(rows):
            keeps[filename] = sorted(random.sample(range(len(rows)),samples))
        else:
            keeps[filename] = range(len(rows))
        rows_compressed = rows.iloc[keeps[filename],:]
        rows_compressed = rows_compressed.iloc[:, 1]

        for row in rows_compressed:
            results.update(str(row).lower().split("\n")[0].strip().split(" "))

    results = list(results)
    print(os.listdir(data))  
    for filename in os.listdir(data):
        file_path = "/".join([data,filename])
        rows=pd.read_csv(file_path, on_bad_lines='skip')
        rows_compressed = rows.iloc[keeps[filename],:]
        rows_compressed = rows_compressed.iloc[:, 1]
        
        term_document_matrix = []
        
        for title in rows_compressed:
            title = str(title).strip().split(" ")
            for t in title:
                t=t.strip()
            array = np.zeros(len(results))
            word_p=[]
            for word in set(title):
                idf=np.log(len(rows_compressed)/count(rows_compressed,word))
                array[results.index(str(word).lower().strip())] = idf*count(title, str(word).lower()) / len(title)
                word_p.append(count(title, str(word).lower()) / len(title))
            
            # if sum(array)<1:
            #     print(sum(array))
            #     print(word_p)
            #     print(title)
            term_document_matrix.append(array)
                
        term_document_matrices.append(term_document_matrix)
        y.append([key[filename]]*len(rows_compressed))
    return term_document_matrices,y