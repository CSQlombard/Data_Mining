#!/usr/bin/python
#Claudio Sebastian Quiroga Lombard September 2017

import string
import operator
import sys
import io
import string
import re
import unicodedata
import codecs

## TEXT FILE HAS TO BE IN utf-8 !!

def open_file(name):

     f = io.open(name, 'r', encoding='utf-8')
     texto = f.read()
     texto = texto[1:len(texto)]

     ## Lowercase
     texto_low = texto.lower()
     my_string_punct =  string.punctuation[0:6]+string.punctuation[8:32]

     palabras = []
     palabras.append(" mas ")
     palabras.append(" de ")
     palabras.append(" y ")
     palabras.append(" a ")
     palabras.append(" la ")
     palabras.append(" en ")
     palabras.append(" el ")
     palabras.append(" con ")
     palabras.append(" los ")
     palabras.append(" que ")
     palabras.append(" le ")
     palabras.append(" la ")
     palabras.append(" las ")
     palabras.append(" para ")
     palabras.append(" es ")
     palabras.append(" un ")
     palabras.append(" se ")
     palabras.append(" una ")
     palabras.append(" del ")
     palabras.append(" pero ")
     palabras.append(" o ")
     palabras.append(" al ")
     palabras.append(" esta ")
     palabras.append(" eso ")
     palabras.append(" este ")
     palabras.append(" ese ")
     palabras.append(" esa ")
     palabras.append(" esas ")
     palabras.append(" como ")
     palabras.append(" por ")
     palabras.append(" no ")
     palabras.append(" hermanos ")
     palabras.append(" hermanas ")
     palabras.append(" nos ")
     palabras.append(" todos ")
     palabras.append(" lo ")
     palabras.append(" argentinos ")
     palabras.append(" argentinas ")
     palabras.append(" ahora ")
     palabras.append(" antes ")
     palabras.append(" nuestra ")
     palabras.append(" anos ")
     palabras.append(" tenemos ")
     palabras.append(" hemos ")
     palabras.append(" su ")
     palabras.append(" ha ")
     palabras.append(" nuestros ")
     palabras.append(" hay ")
     palabras.append(" cuando ")
     palabras.append(" algunos ")
     palabras.append(" son ")
     palabras.append(" 2015 ")
     palabras.append(" ni ")
     palabras.append(" sociales ")
     palabras.append(" nuestro ")
     palabras.append(" hasta ")
     palabras.append(" ser ")
     palabras.append(" entre ")
     palabras.append(" sin ")
     palabras.append(" ya ")
     palabras.append(" tiene ")
     palabras.append(" contra ")
     palabras.append(" desde ")
     palabras.append(" estan ")
     palabras.append(" todo ")
     palabras.append(" vez ")
     palabras.append(" han ")
     palabras.append(" dos ")
     palabras.append(" sus ")
     palabras.append(" dia ")
     palabras.append(" desde ")
     palabras.append(" aqui ")
     palabras.append(" sino ")
     palabras.append(" sido ")
     palabras.append(" siempre ")
     palabras.append(" nunca ")
     palabras.append(" hacer ")
     palabras.append(" somos ")
     palabras.append(" e ")
     palabras.append(" nuestras ")
     palabras.append(" parte ")
     palabras.append(" mejor ")
     palabras.append(" otros ")
     palabras.append(" fueron ")
     palabras.append(" mucho ")
     palabras.append(" puede ")
     palabras.append(" hace ")
     palabras.append(" primera ")
     palabras.append(" van ")
     palabras.append(" todas ")
     palabras.append(" menos ")
     palabras.append(" sea ")
     palabras.append(" toda ")
     palabras.append(" especialmente ")
     palabras.append(" pueden ")
     palabras.append(" cuenta ")
     palabras.append(" gran ")
     palabras.append(" cada ")
     palabras.append(" hoy ")
     palabras.append(" esto ")
     palabras.append(" estar ")
     palabras.append(" manera ")
     palabras.append(" tan ")
     palabras.append(" seguir ")
     palabras.append(" uno ")
     palabras.append(" estas ")
     palabras.append(" ademas ")
     palabras.append(" esos ")
     palabras.append(" chile ")
     palabras.append(" muchos ")
     palabras.append(" general ")
     palabras.append(" dar ")
     palabras.append(" nueva ")
     palabras.append(" nuevos ")
     palabras.append(" sera ")
     palabras.append(" dias ")
     palabras.append(" bajo ")
     palabras.append(" forma ")
     palabras.append(" mejores ")
     palabras.append(" mayor ")
     palabras.append(" tanto ")
     palabras.append(" medio ")
     palabras.append(" especial ")
     palabras.append(" estan ")
     palabras.append(" momento ")
     palabras.append(" numero ")
     palabras.append(" tengo ")
     palabras.append(" puedo ")
     palabras.append(" queremos ")
     palabras.append(" lugar ")
     palabras.append(" frente ")
     palabras.append(" traves ")
     palabras.append(" mayoria ")
     palabras.append(" del ")
     palabras.append(" a ")
     palabras.append(" un ")
     palabras.append(" grandes ")
     palabras.append(" cuidar ")
     palabras.append(" mismo ")
     palabras.append(" nuevas ")
     palabras.append(" sabemos ")
     palabras.append(" sean ")
     palabras.append(" marco ")
     palabras.append(" periodo ")
     palabras.append(" justo ")
     palabras.append(" fundamental ")
     palabras.append(" conjunto ")
     palabras.append(" debemos ")
     palabras.append(" poner ")
     palabras.append(" nadie ")
     palabras.append(" medidas ")
     palabras.append(" llevar ")
     palabras.append(" primeros ")
     palabras.append(" junto ")
     palabras.append(" unos ")
     palabras.append(" cual ")
     palabras.append(" consejo ")
     palabras.append(" principio ")
     palabras.append(" mantener ")
     palabras.append(" misma ")
     palabras.append(" tenga ")
     palabras.append(" marcha ")
     palabras.append(" ejemplo ")
     palabras.append(" dentro ")
     palabras.append(" vista ")
     palabras.append(" ante ")
     palabras.append(" tengan ")
     palabras.append(" pues ")
     palabras.append(" corresponde ")
     palabras.append(" creemos ")
     palabras.append(" posible ")
     palabras.append(" miembros ")
     palabras.append(" soy ")
     palabras.append(" ella ")
     palabras.append(" etapa ")
     palabras.append(" seran ")
     palabras.append(" ello ")
     palabras.append(" de ")
     palabras.append(" ustedes ")
     palabras.append(u" a\xf1os ") # unicode words
     palabras.append(u" a\xf1o ") # unicode words
     palabras.append(u" acompa\xf1aron ") # unicode words
     palabras.append(u" \xe9sta ") # unicode words
     palabras.append(u" aqu\xed ") # unicode words
     palabras.append(u" m\xe1s ") # unicode words
     palabras.append(u" tambi\xe9n ") # unicode words
     palabras.append(u" s\xf3lo ") # unicode words
     palabras.append(u" m\xed ") # unicode words
     palabras.append(u" s\xe9 ") # unicode words

     texto_low_mod = texto_low
     for elemento in my_string_punct:
         texto_low_mod = texto_low_mod.replace(elemento, '')

     texto_low_mod2 = texto_low_mod
     for palabra in palabras:
         texto_low_mod2 = texto_low_mod2.replace(palabra, ' ')

     texto_split = texto_low_mod2.split()

     # Compute everything

     dict = {}
     for word in texto_split:
         if word in dict.keys():
             value = dict[word]
             dict[word]=value+1
         else:
             dict[word] = []
             dict[word] = 1

     dict = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)

     total_elements=0
     for element in dict :
         total_elements = total_elements + element[1]
         print  unicodedata.normalize('NFKD', element[0]).encode('ascii','ignore'),int(element[1])

     print 'Total Words =',total_elements

     ## Save Data
     NAME = 'Output_' + name
     file = codecs.open(NAME, "w")
     for element in dict:
         file.write("%s %d %.4f\n" % (unicodedata.normalize('NFKD', element[0]).encode('ascii','ignore'), int(element[1]), float(element[1])/float(total_elements)))
     file.write("Total Elements %d\n" % total_elements)
     file.close()

     return dict

if __name__ == '__main__':
    open_file(sys.argv[1])
