#!/usr/bin/python
#Claudio Sebastian Quiroga Lombard September 2017

import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import sys
import codecs

def comp(files):
    dict = {}
    for i, file in enumerate(files):
        data = open(file,'r')
        data = data.read()
        data_split = data.split('\n')
        for j, element in enumerate(data_split):
            if j < len(data_split)-2:
                element_split = element.split()
                if len(element_split) == 3:
                    #print j
                    word = element_split[0]
                    if word in dict.keys():
                        dict[word].append(element_split[2])
                    else:
                        dict[word] = []
                    #dict[word] = [0]*i
                        dict[word].append(element_split[2])
    #return dict

    #final_dict = dict
    # Palabras comunes a todos los documentos

    final_dict = {}
    for key in dict.keys():
        if len(dict[key]) == len(files):
            final_dict[key] = dict[key]
            average = (float(final_dict[key][0])+float(final_dict[key][1])+float(final_dict[key][2])+float(final_dict[key][3])+float(final_dict[key][4]))/float(len(files))
            final_dict[key].append(float(average))
            #print final_dict[key]

    final_dict = sorted(final_dict.items(), key=lambda kv: kv[1][5], reverse=True)

    #for element in final_dict:
        #print  element[0:]

    ## Save Data

    NAME = 'Output_Total.txt'
    file = codecs.open(NAME, "w")
    for i,element in enumerate(final_dict):
        #print i
        #if len(element[1]) == 1:
        #    file.write("%s %.4f %.4f\n" % (element[0], float(element[1][0]), float(0.0000)))
        #if len(element[1]) == 2:
        #    file.write("%s %.4f %.4f\n" % (element[0], float(element[1][0]), float(element[1][1])))
        if len(element[1]) == 6:
            #suma = float(element[1][0]) + float(element[1][1]) +float(element[1][2]) + float(element[1][3]) + float(element[1][4])
            #suma = float(suma)/float(5)
            file.write("%s %.4f %.4f %.4f %.4f %.4f %.4f\n" % (element[0], float(element[1][0]), float(element[1][1]), float(element[1][2]), float(element[1][3]), float(element[1][4]), float(element[1][5])))
    file.close()

    return final_dict

def stacked_plot(final_dict, n_palabras):

     reducido = final_dict[0:n_palabras]

     x1 = []
     x2 = []
     x3 = []
     x4 = []
     x5 = []
     x = []
     names = []
     c = 1
     for linea in reducido:
         names.append(linea[0])
         x1.append(float(linea[1][0]))
         x2.append(float(linea[1][1]))
         x3.append(float(linea[1][2]))
         x4.append(float(linea[1][3]))
         x5.append(float(linea[1][4]))
         x.append(int(c))
         c += 1

     font = {'weight' : 'normal','size'   : 10}
     matplotlib.rc('font', **font)
     fig = plt.figure(figsize=(10, 10), dpi=300)
     #fig = figure(1, figsize=(3.25, 3))
     width = .35
     p1 = plt.bar(x, x1, width=width)
     p2 = plt.bar(x, x2, width=width, bottom=x1)
     x12 = map(sum, zip(x1,x2))
     p3 = plt.bar(x, x3, width=width, bottom=x12)
     x123 = map(sum, zip(x12,x3))
     p4 = plt.bar(x, x4, width=width, bottom=x123)
     x1234 = map(sum, zip(x123,x4))
     p5 = plt.bar(x, x5, width=width, bottom=x1234)

     plt.xlabel('Words')
     plt.ylabel('Relative Frequency')
     plt.title("Top Rel. Freq.")
     plt.xticks(range(len(x)+1)[1:len(x)+1],names, rotation=90)
     plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Evo', 'Macri', 'Bachelet', 'Cartes', 'Tabare'))
     plt.savefig("Top Rel. Freq.png")

if __name__ == '__main__':
    final_dict = comp(sys.argv[1:])
    n_palabras = 20
    stacked_plot(final_dict,n_palabras)
