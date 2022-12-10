#import packages
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import plotly
import random, time
from collections import Counter
from sklearn.model_selection import train_test_split
import json
from sklearn.datasets import fetch_openml
import json
from json import JSONEncoder
import os
import pandas as pd
from pathlib import Path

term_dict={}
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


arch={}
activations={}
file_name=""

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
    X_kj=[X[k,j] for k,item in enumerate(y) if item==i]
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

# # iterate over term documents
# for filename in os.listdir(tdm):
#     file = "/".join([tdm,filename])
#     csvfile = pd.read_csv(file)


