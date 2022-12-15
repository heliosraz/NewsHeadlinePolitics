#import packages
import numpy as np
from collections import Counter
from pathlib import Path
import random
import pandas as pd
from pathlib import Path
import naive_bayes as nb
import term_doc as td

# #method to vectorize text
# def vectorize(title):
#     X=[]
#     for i in term_matrix():
#         for j in i:
#             X.append(j)
#     vector=[]
#     title = str(title).strip().split(" ")
#     for t in title:
#         t=t.strip()
#     array = np.zeros(len(results))
#     word_p=[]
#     for word in set(title):
#         X[:,results.index(word)]
#         idf=np.log(len(rows_compressed)/count(rows_compressed,word))
#         array[results.index(str(word).lower().strip())] = idf*count(title, str(word).lower()) / len(title)
#         word_p.append(count(title, str(word).lower()) / len(title))
#     return vector


def main(test, s1=100):
  X,y=td.term_matrix(samples=s1)
  # for matrix in result[0]:
  #   print("_____________________________________________________________")
  #   print(matrix)
  #   for row in matrix:
  #     print(sum(row))
  correct=0
  for t in test:
    t=int(s1/2*t)
    pred = nb.bayes_prediction(X[t,:],X,y)
    target = y[t]
    print(f'predicting: {pred}, true value: {target}')
    if pred==target:
      correct+=1
  print(f"the percent of accuracy is: {correct/12}")

if __name__=="__main__":
    for i in [100,200,300,500]:
      main(range(12),i)
