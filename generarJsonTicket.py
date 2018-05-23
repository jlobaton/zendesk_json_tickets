#!/usr/bin/python
# -*- coding: utf-8 -*-
# Bash que permite transformar de CSV a Json 
# Para usarlo en la API Console de Zendesk

# El archivo csv debe de tener los campos tal cual como esta en zendesk
# para los campos personalizados:
# tiene que anteceder el nombre del campo con "custom_fields"
#
# Ej: custom_fields.nombre_campo
#

import sys, argparse, getopt
import csv
import json
import codecs
import os
import re
reload(sys)

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

#sys.setdefaultencoding('utf8')

def salir(mensaje, leer):
	#clear()
	print "-- ERROR EN LA VALIDACION --"
	print "Linea: " + str(leer.line_num)
	print "Mensaje: "+mensaje
	print "----------------------------"
	#break
	exit()

def verificar_correo(correo):
	valido = False
	if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
		valido = True

	return valido


def generar_jsonv2(row_json,campo,custom_fields,cabecera,migrar,output):
	cabecera[migrar] = output #row_json
	arch = cabecera
	return arch

def generar_jsonv_ticket(row_json,campo,custom_fields,cabecera,migrar,output):
  row_json[campo] = custom_fields #Genera 'custom_fields': [{}]
  
  #cabecera[migrar] = row_json
  return row_json 

def generar_archivo(output,archivo,i):
	file = archivo+`i`+'.json'
	salida = open(file,'w')
	json.dump(output, 
					salida, 
					indent=2, 
					sort_keys=False,
					encoding="utf-8",
					ensure_ascii=False)

	#return archivo+`i`+'.json'
	return file

def recortar(palabra, buscar):
	palab = palabra.strip()
	posicion = palab.index(buscar)
	tamano = len(palab)
	return palab[posicion+1:tamano]


def procesar(archivo,row,option):
	entrada = open(archivo+'.csv','r')
	mensaje = "Archivo: "
	migrar = option #'users'

	if migrar == 'users': 
		filtrar1 = 'custom_fields'  #PARAMETRO PARA FILTRAR EL CAMPO FIELDS
		campo = 'user_fields'  #CAMPO QUE VA A COLOCAR EN EL JSON

		#filtrar1 = 'custom_fields_options'	
		#campo2 = 'custom_fields_options'
	else:  #tickets
		filtrar1 = 'custom_fields' 	
		campo1 = 'custom_fields'

		filtrar2 = 'comment' 	
		campo2 = 'comment'

	output = []
	leer = csv.DictReader(entrada)
	fieldnames = leer.fieldnames
	#fieldnames = sorted(fieldnames)
	#print fieldnames
	#exit()
	id_fieldnames = ('','','','0001','0002','0003','0003','0003','0003','0003','0003','0003','0003');
	j = 0
	i = 0

	for valor in leer:			
		cabecera = {}
		row_json = {}
		custom_fields = {}
		custom_fields2 = []

		for field in fieldnames:
			custom_fields = {}
			#Validaciones
			if field.find('email') >= 0 :
				if (verificar_correo(valor[field]) == False):
					salir("Error en el Correo",leer)

			#fin
			
			# USUARIOS
			if migrar == 'users':
				if field.find(filtrar1) >= 0:
					custom_fields[recortar(field,'.')] = valor[field]
					#campo = campo

				else:
					row_json[field] = valor[field]

			# TICKET's
			elif migrar == 'tickets':
				if field.find(filtrar1) >= 0:   #custom_fields
					#custom_fields[recortar(field,'.')] = valor[field]
					#{
          #	"id": "0000001", 
          #	"value": "11111"
          #}
					custom_fields = {}
					custom_fields["id"] = recortar(field,'.')
					custom_fields["value"] = valor[field]

				 	campo = campo1
				 	custom_fields2.append(custom_fields) #Genera un []

					#[ {
          #	"id": "0000001", 
          #	"value": "11111"
          #} ]
					row_json[campo] = custom_fields2 #Genera 'custom_fields': [{}]

				 	#arch = generar_jsonv_ticket(row_json,campo,custom_fields2,cabecera,migrar,output)
		
				elif field.find(filtrar2) >= 0: #comment

					custom_fields["body"] = valor[field]
					campo = campo2
					row_json[campo] = custom_fields
				
				else:					
					row_json[field] = valor[field]

		if (i >= int(row)):
			j = j+1
			i = 0	
			file = generar_archivo(arch,archivo,j)
			print "/// "+mensaje+file
			output = []
			arch = generar_jsonv2(row_json,campo,custom_fields,cabecera,migrar,output)
		else:	
			print ""
			output.append(row_json)  #Genera 'custom_fields': [{}]
			#arch = generar_jsonv2(row_json,campo,custom_fields,cabecera,migrar,output)
		
		i=i+1

	j = j+1
	#cabecera[migrar] = output #row_json
	#arch = cabecera
	arch = generar_jsonv2(row_json,campo,custom_fields,cabecera,migrar,output)
	#print custom_fields2
	#exit()
	file = generar_archivo(arch,archivo,j)
	return "/// "+mensaje+file


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
parser.add_argument("-f", "--file", help="Nombre de archivo CSV a procesar")
parser.add_argument("-r", "--row", help="Cuantos Registros se va a Generar por archivo")
parser.add_argument("-o", "--option", help="Debe especificar si es Users o Tickets")

args = parser.parse_args()
clear()
print "///////////////////////////////////////////////////////"
print "///"
print "/// API: https://developer.zendesk.com/requests/new"
print "/// URL: users/create_many.json"
print procesar(args.file, args.row, args.option)
print "///"
print "//////////////////////////////////////////////////////"

