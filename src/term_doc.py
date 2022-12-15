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

# Sets up variables
word_list = []
index_keep = {}
results = set()
key={'nyt_headlines.csv':-1,'foxnews_headlines.csv':2,'washingtonpost_headlines.csv':-1,'csmonitor_headlines.csv':0,'nypost_headlines.csv':1,'cnn_headlines.csv':-2}

#initializing path names
# main directory
dir = Path(__file__).parents[1]

# get path to raw_data folder
data = str(dir) + "/data/data_collection/raw_data"

# get path to tdms folder
tdm_path= str(dir) + "/data/data_collection/processed_data/term_matrices"

def join(X):
    tf_idf=[]
    print("test join()")
    c=0
    for matrix in X:
        # print("changed matrix")
        c+=1
        for row in matrix:
            # print("-------------------")
            # print(len(row))
            tf_idf.append(row)
    # print(len(tf_idf))
    # print("end")
    # print(f"c={c}")
    return tf_idf

def count(title, query):
    c = 0
    for word in title:
        if (str(query).lower().strip() in str(word).lower().strip()):
            c = c + 1
    return c

def raw_data_compress(num_samples):
    results=set()
    # reads raw_data files
    for filename in os.listdir(data):
        file_path = data+"/"+filename
        data_rows = pd.read_csv(file_path, on_bad_lines='skip')
        # filtering data for number of samples wanted wanted
        # handling if the number of samples wanted is more than the file contains.
        # saving 
        if num_samples<=len(data_rows):
            index_keep[filename] = random.sample(range(len(data_rows)),num_samples)
        else:
            index_keep[filename] = range(len(data_rows))
        
        data_compressed = data_rows.iloc[index_keep[filename], 1]
        # data_compressed = data_compressed.iloc[:, 1]
        for row in data_compressed:
            results.update(str(row).lower().split("\n")[0].strip().split(" "))
    return results

#generating the term document matrix
def term_matrix(samples=100, test_headline: str=None):
    term_document_matrices=[]
    y=[]
    results=raw_data_compress(samples)
    results = list(results)
    print(os.listdir(data))  
    for filename in os.listdir(data):
        file_path = "/".join([data,filename])
        data_rows=pd.read_csv(file_path, on_bad_lines='skip')
        rows_compressed = data_rows.iloc[index_keep[filename],:]
        rows_compressed = rows_compressed.iloc[:, 1]
        
        term_document_matrix = []
        for title in rows_compressed:
            title = str(title).strip().split(" ")
            for t in title:
                t=t.strip()
            array = np.zeros(len(results))
            for word in set(title):
                idf=np.log(len(rows_compressed)/count(rows_compressed,word))
                array[results.index(str(word).lower().strip())] = idf*count(title, str(word).lower()) / len(title)
            
            # print(len(array))
            term_document_matrix.append(array)
        # print(type(list(term_document_matrix)))        
        term_document_matrices.append(term_document_matrix)
        y.append(list([key[filename]]*len(rows_compressed)))
    # print(type(term_document_matrices))
    # print(join(term_document_matrices))
    # print(np.array(join(term_document_matrices)).shape)
    # print(len(term_document_matrices))
    return np.array(join(term_document_matrices)),np.array(np.ravel(y))

if __name__=="__main__":
    term_matrix()