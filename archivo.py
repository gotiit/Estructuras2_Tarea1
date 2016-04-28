# -- coding: utf-8 --
import math, numpy
import os, sys

'''
# controlara que se ingresen la cantidad adecuada de parametros
if len(sys.argv) != 3:
	print "\nNumero de argumentos incorrecto"
	print "Uso: %s <asociatividad> <tamaño del caché> <tamaño del bloque>\n" %sys.argv[0]
	sys.exit(1)
'''

tamcache = 256             #pueden ser de 256 512 1024 2048
tambloque = 8            #pueden ser de 16 32 8 4
asociat = 2            #puede ser de 1 2 4
boffset = int(math.log(tambloque, 2))
set =tamcache/(asociat*tambloque)
index= int(math.log(asociat, 2))


print "El tamano del cache es de: ", tamcache,"bytes"
print "El tamano del bloque es de: ", tambloque,"bytes"
print "la asociatividad es de: ", asociat,"way"
print "El cache tiene ",tamcache/tambloque,"bloques."

print "El byte offset es de", boffset ,"bytes"
print "El numero de sets es de ", set ,"bytes"
print "El index esta compuesto de", index ,"bytes"
print "El tag esta compuesto de", 32-int(math.log(asociat, 2))-int(math.log(tamcache, 2)),"bytes"


M = []

for i in range(index*2):
    M.append([0]*set)

print M


#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀

largo = open("aligned2.trace", "r")

leer = largo.read()
long = leer.splitlines()

total= len(long)

largo.close();


#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀


list = open("aligned2.trace", "r")
resultados = open("resultados.txt", "w+")
print "Estamos leyendo del archivo: ", list.name
#print "Cerrado o no : ", list.closed
#print "Modo de apertura : ", list.mode


print "El archivo tiene ",(len(long)),"lineas..."

str2 = list.readline().rstrip('\n');


print "La lectura de linea es : ", str2

aa = len(str2)

print "el largo de la cadena es de: ",aa

print "el caracter de control es ",str2[aa-1]

bb = str2.find(" ")

print "los caracteres donde esta la direccion son : ",bb

print "entonces la direccion es: ",str2[0:bb]

str2 = list.readline().rstrip('\n');


print "La lectura es : ", str2

#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀

contador = 0

while (contador < total+1 ):

    stt = list.readline().rstrip('\n');
    s = str(stt)
    resultados.write(s +'\n')
    #resultados.write('nos vamos a  sacar un 100''\n');
    contador = contador + 1


mi_hexdata = str2[0:bb]

scale = 16 ## equals to hexadecimal

num_of_bits = 32

print bin(int(mi_hexdata, scale))[2:].zfill(num_of_bits)





list.close();
resultados.close();