#!/usr/bin/python
#Claudio Sebastian Quiroga Lombard September 2017

from matplotlib import pyplot as plt
import matplotlib
import sys

def open_file(name, n_palabras):

     f = open(name, 'r')
     datos = f.read()
     datos_split = datos.split('\n')

     reducido = datos_split[0:n_palabras]

     x = []
     y = []
     names = []
     c = 1
     for linea in reducido:
         linea_split = linea.split()
         names.append(linea_split[0])
         y.append(float(linea_split[2]))
         x.append(int(c))
         c += 1

     font = {'weight' : 'normal','size'   : 10}
     matplotlib.rc('font', **font)
     fig = plt.figure(figsize=(10, 10), dpi=300)
     #fig = figure(1, figsize=(3.25, 3))
     width = .35
     plt.bar(x, y, width=width)
     plt.xlabel('Words')
     plt.ylabel('Relative Frequency')
     name = name.split('.')
     plt.title("%s" % name[0][7:])
     plt.xticks(range(len(x)+1)[1:len(x)+1],names, rotation=90)
     plt.savefig("%s.png" % name[0][7:])

if __name__ == '__main__':
    open_file(sys.argv[1],int(sys.argv[2]))
    #print sys.argv[1], sys.argv[2]
