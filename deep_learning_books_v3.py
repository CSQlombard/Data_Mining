import numpy as np
from sklearn.feature_extraction import DictVectorizer
import nltk
import string
import io
import urllib2
from sklearn.decomposition import TruncatedSVD

#file = io.open('xtrain.txt','r',encoding='utf-8')
url = 'https://s3.eu-central-1.amazonaws.com/deeplearningbookssebidata/Deep_Learning_Books_Data/xtrain.txt'
file = urllib2.urlopen(url)

## Create tokens
#tokens_filtered = []
#for line in data:
def filter_line(line, stopwords, my_string_punct,L):

    line = line.lower()
    for elemento in string.punctuation:
        line = line.replace(elemento, "")

    line = unicode(line, "utf-8")
    all_tokens = []
    all_tokens = line.split('\n')
    all_tokens = all_tokens[0]
    all_tokens = all_tokens.split(" ")

    ## Filtered tokens

    dict = {} # un dicionrio por linea
    for index, token in enumerate(all_tokens):
        if index < len(all_tokens) and len(token) > L: # no consideres /n
            if token not in stopwords:
                if token not in dict.keys():
                    dict[token]=1
                else:
                    dict[token]=dict[token]+1

    return dict

## Complete text

def filter_text(file,N,L):
    lista = []
    ## Clean the data correctly
    my_string_punct = string.punctuation

    ## Eliminate stopwords
    stopwords = nltk.corpus.stopwords.words('english')

    for index,line in enumerate(file.readlines()):
        if index < N:
            dict = []
            dict = filter_line(line, stopwords, my_string_punct,L)
            lista.append(dict)

    return lista

## Get Term Doc Matrix
def concept_function(mini_matrix, K, type):
    if type == 1:
        ## Apply Singular Value Decomposition
        U,s,V = np.linalg.svd(mini_matrix, full_matrices=True)
        # Choose number of Concepts
        x,y = mini_matrix.shape
        S = np.zeros((x,y), dtype=complex)
        S[:K, :K] = np.diag(s[0:K])
        #doc_term_mat_aprox = np.dot(U, np.dot(S,V))
        concept_matrix = np.dot(U,S)
        concept_matrix = concept_matrix[:][:,0:K]
        del U
        del s
        del V
    else:
        svd = TruncatedSVD(n_components=K, n_iter=10, random_state=42) ## keep this constant, the method suffers of "sign indeterminancy"
        svd.fit(mini_matrix)
        concept_matrix = svd.transform(mini_matrix)

    return concept_matrix

def total_concept_func(lista, n_datos_por_particion,K,type):

    dict_vectorizer = DictVectorizer(sparse=True)
    doc_term_mat = dict_vectorizer.fit_transform(lista)

    start = 0
    index = n_datos_por_particion

    particiones = np.divide(doc_term_mat.shape[0], index)
    particiones = np.trunc(particiones) + 1
    particiones = int(particiones)

    stop = 0
    for i in range(particiones):
        if stop == 0:
            mini_matrix = []
            if index >= doc_term_mat.shape[0]:
                mini_matrix = doc_term_mat[start:doc_term_mat.shape[0]]
                index = doc_term_mat.shape[0]
                stop = 1
            else:
                mini_matrix = doc_term_mat[start:index]

            mini_matrix = mini_matrix.toarray()
            concept_matrix = concept_function(mini_matrix,K,type)

            if i==0:
                total_concept_matrix = concept_matrix
            else:
                total_concept_matrix = np.concatenate((total_concept_matrix, concept_matrix), axis =0)

            print(start, index, stop)
            start = index
            index = start + concept_matrix.shape[0]

    return total_concept_matrix
