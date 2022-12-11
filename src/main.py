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
def main():
    td.term_matrix()

if __name__=="__main__":
    main()
