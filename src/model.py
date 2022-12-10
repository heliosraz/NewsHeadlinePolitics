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
samples = 1000
# methods
##defining possible activations

##adding words into dictionary
##term document matrix generation

## at some point need
# U, S, V =np.linalg.svd(X)
# X is the term doument matrix
# U is the document-topic matrix
# S is the diagonal matrix of sqrt(eigenvalues)
# V is the word embedding matrix

# training
# get tdms 
dir = Path(__file__).parents[1]
tdm= str(dir) + "/data/data_collection/processed_data/term_matrices"

#naive bayes model
def p(j,X,y): 
    total=0
    for i in y:
        if np.equal(j,i):
            total+=1
    return total/(X.shape[0]-1)

def N(x, mu, var):
    return np.sqrt(1/(2*np.pi*var))*(np.exp(-(1/(2*var))*(x-mu)**2))
    
def p_cond(x,i,j,X,y):
    X_kj=X[np.where(y==i),j]
    print(X_kj)
    # X_kj=[X[k,j] for k,item in enumerate(y) if item==i]
    mu=sum(X_kj)/sum([1 for item in y if item==i])
    Ex=sum([a*p(a,X,X_kj) for a in np.unique(X_kj)])
    Ex2=sum([a**2*p(a,X,X_kj) for a in np.unique(X_kj)])
    var=np.abs(Ex2-Ex**2)
    if var==0:
        var=0.1
    return N(x[j],mu, var)
    
def bayes_prediction(x,X,y):
    label=0
    label_p=0
    for i in range(-2,3):
        theta=sum([1 for item in y if item==i])/X.shape[0]
        l=theta
        for j in range(X.shape[1]):
#             print(j)
#             print(f"p_cond={p_cond(x,i,j,X,y)}" )
            l*=p_cond(x,i,j,X,y)
#             print(f"1={l}")
        if l>label_p:
            label_p=l
            label=i
    return label

def count(title, query):
    c = 0
    for word in title:
        # print(word.lower())
        # print(query.lower())
        # print(query.lower() in word.lower())
        if (str(query).lower() in str(word).lower()):
            c = c + 1
        # print(f"c={c}")
    return c

def term_matrix():
    results=set()
    for filename in os.listdir(data):
        file_path = "/".join([data,filename])
        
        rows = pd.read_csv(file_path, on_bad_lines='skip')
        keeps[filename] = sorted(random.sample(range(len(rows)),samples))
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

