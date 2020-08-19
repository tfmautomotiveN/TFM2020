#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import time
import datetime
#import pymongo
#import json
#from pymongo import MongoClient


def event_fuels():
    print("Has entrado aqui")

    URL = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'
    HEADERS = {'Content-Type': 'application/json'}
    # MONGO_URI = 'mongodb://user:pass@localhost:27017/database'

    r = requests.get(URL, headers=HEADERS)
    datos = r.json()
    cont = 0
    print(datos['Fecha'])

    fec = datos['Fecha']

    for dato in datos['ListaEESSPrecio']:
        # sin bucle for seria [1] para que recorra el lo que hay en la posicion 1 del array ListaEESSPrecio. horario=datos['ListaEESSPrecio'][1]['Horario']
        horario = dato['Horario']
        cp = dato['C.P.']
        cp = int(cp)
        #direcion = dato['Direcci'+'\xf3n']

        latitud = dato['Latitud']
        if latitud != None or u'':
            latitud = latitud.replace(",", ".")
            latitud = float(latitud)

        longitud = dato['Longitud (WGS84)']
        if longitud != None:
            longitud = longitud.replace(",", ".")
            longitud = float(longitud)
        localidad = dato['Localidad']
        margen = dato['Margen']
        municipio = dato['Municipio']

        preciobiodiesel = dato['Precio Biodiesel']
        if preciobiodiesel != u'':
            preciobiodiesel = preciobiodiesel.replace(",", ".")
            preciobiodiesel = float(preciobiodiesel)

        preciobioetanol = dato['Precio Bioetanol']
        if preciobioetanol != u'':
            preciobioetanol = preciobioetanol.replace(",", ".")
            preciobioetanol = float(preciobioetanol)

        preciogasnatural = dato['Precio Gas Natural Comprimido']
        if preciogasnatural != u'':
            preciogasnatural = preciogasnatural.replace(",", ".")
            preciogasnatural = float(preciogasnatural)

        preciogasoleoa = dato['Precio Gasoleo A']
        if preciogasoleoa != u'':
            preciogasoleoa = preciogasoleoa.replace(",", ".")
            preciogasoleoa = float(preciogasoleoa)

        preciogasolina95 = dato['Precio Gasolina 95 E5']
        if preciogasolina95 != u'':
            preciogasolina95 = preciogasolina95.replace(",", ".")
            preciogasolina95 = float(preciogasolina95)

        preciogasolina98 = dato['Precio Gasolina 98 E10']
        if preciogasolina98 != u'':
            preciogasolina98 = preciogasolina98.replace(",", ".")
            preciogasolina98 = float(preciogasolina98)

        preciogasoleob = dato['Precio Gasoleo B']
        if preciogasoleob != u'' or None:
            preciogasoleob = preciogasoleob.replace(",", ".")
            preciogasoleob = float(preciogasoleob)

        provincia = dato['Provincia']
        #remision = dato['Remisión']
        #rotulo = dato['Rótulo']
        tipoventa = dato['Tipo Venta']

        # vamos a calcular el timestamp

        timeS = int(time.mktime(datetime.datetime.strptime(fec, "%d/%m/%Y %H:%M:%S").timetuple())) * 1000
        #print("timestamp ", timeS)


