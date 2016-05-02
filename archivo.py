#! /usr/bin/python
# coding: utf-8
import sys
import math
import os
import random
#-------------------------Estructuras de computadoras digitales II---------------------------------
#--------------------------------------Modelado de cache-------------------------------------------
#Estudiantes: Boanerges Martínez Cortez A73791; Brayan Morera A84375
#					Version 2.1
#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀
#Chechea que se ingresen la cantidad de parametros y que sean validos
if (len(sys.argv) != 4):
	print "\nNumero de argumentos incorrecto\n"
	print "Uso:  <asociatividad> <tamaño del caché> <tamaño del bloque>\n"
	sys.exit(1)
elif (float(sys.argv[2]!=1) and not float(sys.argv[2]!=2) and not float(sys.argv[2]!=4)):
	print "\nIngreso un valor de asociatividad invalido\n"
	print "Los valores de asociatividad pueden ser: 1 2 4\n"
	print "Uso: <asociatividad> <tamaño del caché> <tamaño del bloque>\n"
	sys.exit(1)
elif (sys.argv[2]!=256) and not (sys.argv[2]!=512) and not (sys.argv[2]!=1024) and not (sys.argv[2]!=2048):
	print "\nIngreso tamaño de cache invalido\n"
	print "El tamaño de cache puede ser: 256 512 1024 2048\n"
	print "Uso: <asociatividad> <tamaño del caché> <tamaño del bloque>\n"
	sys.exit(1)
elif (sys.argv[3]!=16) and not (sys.argv[3]!=32) and not  (sys.argv[3]!=64) and not  (sys.argv[3]!=128):
	print "\nIngreso tamaño de bloque invalido\n"
	print "El tamaño de cache puede ser: 16 32 64 128\n"
	print "Uso: <asociatividad> <tamaño del caché> <tamaño del bloque>\n"
	sys.exit(1)
else:
	print "\nSe ingresaron los datos correctamente\n"

# Se extraen los valores y se asignan a las varibles de trabajo
asociat = int(sys.argv[1])           #puede ser de 1 2 4
tamcache = int(sys.argv[2])            #pueden ser de 256 512 1024 2048
tambloque = int(sys.argv[3])           #pueden ser de 16 32 64 128

#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀
#Hacemos los calculos de las parametros que utilizaremos
boffset = int(math.log(tambloque, 2))
sett =tamcache/(asociat*tambloque)
index = int(math.log(asociat, 2))
cantidadbloques = tamcache/tambloque
print "la asociatividad es de: ", asociat,"way"
print "El tamano del cache es de: ", tamcache,"bytes"
print "El tamano del bloque es de: ", tambloque,"bytes"
print "El cache tiene ",cantidadbloques,"bloques."
print "El byte offset es de", boffset ,"bytes"
print "El numero de sets es de ", sett ,"bytes"
print "El index esta compuesto de", index ,"bytes"
print "El tag esta compuesto de", 32-int(math.log(asociat, 2))-int(math.log(tamcache, 2)),"bytes"

#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀
#Preparamos los parametros que utilizaremos en para la simulacion del cache
#se declara como tranformar a binario
binary = lambda x: "".join(reversed( [i+j for i,j in zip( *[ ["{0:04b}".format(int(c,16)) for c in reversed("0"+x)][n::2] for n in [1,0] ] ) ] ))
miss = 0
hit = 0
n=0

#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀
#Inicio de la selecion de caches
#Cache de mapeo directo
if asociat==1:
	indexmdirecto =  int(math.log(cantidadbloques, 2))
	print indexmdirecto,"indice para mapeo directo"
	#Se crea un vector de tama = cantidad de bloques
	M2 = []
	for y in range(sett):
		M2.append(y)
	print M2
	with open('aligned2.trace') as f:
		for line in f:
			n=n+1
			#print line
			bb3 = line.find(" ")
			#print bb3
			nhex= str(line[0:bb3])
			#print nhex
			nbin=binary(nhex)
			bbb3= len(nbin)
			#print nbin, "Este es el numero binario completo"
			#print nbin[0:bbb3-boffset], "menos byteofsset"
			idx= nbin[bbb3-indexmdirecto-boffset:bbb3-boffset]
			#print idx, "index para el mapeo directo"
			tagg = nbin[0:bbb3-indexmdirecto-boffset]
			#print tagg, "Este es el tag para mapeo directo"
			idxdecimal=int(idx,2)
			#print idxdecimal, "El valor en decimal del index de mapeo directo"
			#Nos movemos directamente a la posicion del indice y buscamos el dato
			if M2[idxdecimal]==tagg:
				hit=hit+1
			else:
				M2[idxdecimal]=tagg
				miss=miss+1
#Cache n-ways
else:
	indexnways =  int(math.log(asociat, 2))
	print "n-ways"
	M = []
	for i in range(index*2):
		M.append([0]*sett)
	print M
	n2=0
	with open('aligned2.trace') as f:
		for line in f:
			n=n+1
			#print line
			bb3 = line.find(" ")
			#print bb3
			nhex= str(line[0:bb3])
			#print nhex
			nbin=binary(nhex)
			bbb3= len(nbin)
			#print nbin
			#print nbin[0:bbb3-boffset], "menos byteofsset"
			idx= nbin[bbb3-indexnways-boffset:bbb3-boffset]
			tagg = nbin[0:bbb3-indexnways-boffset]
			#print tagg, "menos byteofsset"
			#print idx, "index para el mapeo de n-ways"
			idxdecimal=int(idx,2)
			#print idxdecimal
			if sett==0:
				if M[idxdecimal]==tagg:
					hit=hit+1
				else:
					M[idxdecimal]=tagg
					miss=miss+1
			for j in range(sett):
				
				if M[idxdecimal][j]==0:
					M[idxdecimal][j]=tagg
					miss = miss+1
					#print j
					#print idxdecimal
					break
				elif M[idxdecimal][j]==tagg:
					hit=hit+1
					#print j
					#print idxdecimal
					break
				elif j==sett-1:
					#print j
					#print idxdecimal
					M[idxdecimal][random.randrange(sett)]=tagg
					miss = miss+1
					
#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀						
#imprimimos los datos obtenidos de la simulacion
print "Cache: asociatividad ",asociat,", tamaño de cache ",tamcache,", tamaño de bloque ",tambloque,", se obtuvieron ",hit," hits"
print "Cache: asociatividad ",asociat,", tamaño de cache ",tamcache,", tamaño de bloque ",tambloque,", se obtuvieron ",miss," misses"
print "Total de ingresos a memoria fue de: ",n



