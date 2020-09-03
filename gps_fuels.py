#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import time
import datetime
import gps_classFuels
import pandas as pd
#import pymongo
#import json
#from pymongo import MongoClient
import json
import os


def event_fuels(data_provincias_filter):
    URL = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'
    HEADERS = {'Content-Type': 'application/json'}
    claFuels = gps_classFuels.classFuels()
    r = requests.get(URL, headers=HEADERS)
    datos = r.json()
    fec = datos['Fecha']


    for dato in datos['ListaEESSPrecio']:
        # sin bucle for seria [1] para que recorra el lo que hay en la posicion 1
        # del array ListaEESSPrecio. horario=datos['ListaEESSPrecio'][1]['Horario']
        horario = dato['Horario']

        cp = dato['C.P.']
        cp = int(cp)

        #direcion = dato['Direcci'+'\xf3n']

        latitud = dato['Latitud']
        if latitud != None or u'':
            latitud = latitud.replace(",", ".")
            latitud = float(latitud)
        else:
            latitud = None

        longitud = dato['Longitud (WGS84)']
        if longitud != None:
            longitud = longitud.replace(",", ".")
            longitud = float(longitud)
        else:
            longitud = None

        localidad = dato['Localidad']

        margen = dato['Margen']

        municipio = dato['Municipio']

        preciobiodiesel = dato['Precio Biodiesel']
        if preciobiodiesel != u'':
            preciobiodiesel = preciobiodiesel.replace(",", ".")
            preciobiodiesel = float(preciobiodiesel)
        else:
            preciobiodiesel = None

        preciobioetanol = dato['Precio Bioetanol']
        if preciobioetanol != u'':
            preciobioetanol = preciobioetanol.replace(",", ".")
            preciobioetanol = float(preciobioetanol)
        else:
            preciobioetanol = None

        preciogasnatural = dato['Precio Gas Natural Comprimido']
        if preciogasnatural != u'':
            preciogasnatural = preciogasnatural.replace(",", ".")
            preciogasnatural = float(preciogasnatural)
        else:
            preciogasnatural = None

        preciogasoleoa = dato['Precio Gasoleo A']
        if preciogasoleoa != u'':
            preciogasoleoa = preciogasoleoa.replace(",", ".")
            preciogasoleoa = float(preciogasoleoa)
        else:
            preciogasoleoa = None

        preciogasolina95 = dato['Precio Gasolina 95 E5']
        if preciogasolina95 != u'':
            preciogasolina95 = preciogasolina95.replace(",", ".")
            preciogasolina95 = float(preciogasolina95)
        else:
            preciogasolina95 = None

        preciogasolina98 = dato['Precio Gasolina 98 E10']
        if preciogasolina98 != u'':
            preciogasolina98 = preciogasolina98.replace(",", ".")
            preciogasolina98 = float(preciogasolina98)
        else:
            preciogasolina98 = None

        preciogasoleob = dato['Precio Gasoleo B']
        if preciogasoleob != u'' or None:
            preciogasoleob = preciogasoleob.replace(",", ".")
            preciogasoleob = float(preciogasoleob)
        else:
            preciogasoleob = None

        provincia = dato['Provincia']

        #remision = dato['Remisión']
        #rotulo = dato['Rótulo']
        tipoventa = dato['Tipo Venta']

        # vamos a calcular el timestamp
        timeS = int(time.mktime(datetime.datetime.strptime(fec, "%d/%m/%Y %H:%M:%S").timetuple())) * 1000

        #seteamos todos los setters de la clase classXML
        if data_provincias_filter == []:
            data_provincia = 'PONTEVEDRA'
            setting_classFuels(data_provincia, claFuels, provincia, horario, cp, latitud, longitud, localidad, margen, municipio, preciobiodiesel, preciobioetanol, preciogasnatural, preciogasoleoa, preciogasolina95, preciogasolina98, preciogasoleob, timeS, tipoventa)
        else:
            for i in range(len(data_provincias_filter)):
                setting_classFuels(data_provincias_filter[i], claFuels, provincia, horario, cp, latitud, longitud, localidad, margen, municipio, preciobiodiesel, preciobioetanol, preciogasnatural, preciogasoleoa, preciogasolina95, preciogasolina98, preciogasoleob, timeS, tipoventa)

    return claFuels


def setting_classFuels(data_provincia, claFuels, provincia, horario, cp, latitud, longitud, localidad, margen, municipio, preciobiodiesel, preciobioetanol, preciogasnatural, preciogasoleoa, preciogasolina95, preciogasolina98, preciogasoleob, timeS, tipoventa):

    if provincia == data_provincia:
        claFuels.set_horario(horario)
        claFuels.set_cp(cp)
        claFuels.set_latitud(latitud)
        claFuels.set_longitud(longitud)
        claFuels.set_localidad(localidad)
        claFuels.set_margen(margen)
        claFuels.set_municipio(municipio)
        claFuels.set_preciobiodiesel(preciobiodiesel)
        claFuels.set_preciobioetanol(preciobioetanol)
        claFuels.set_preciogasnatural(preciogasnatural)
        claFuels.set_preciogasoleoa(preciogasoleoa)
        claFuels.set_preciogasolina95(preciogasolina95)
        claFuels.set_preciogasolina98(preciogasolina98)
        claFuels.set_preciogasoleob(preciogasoleob)
        claFuels.set_provincia(provincia)
        claFuels.set_tipoventa(tipoventa)
        claFuels.set_timeS(timeS)

def save_csv_static_incidents(claFuels, dictionary_list):
    array_distances = []
    if len(dictionary_list) != 0:
        dictionary_list_sort = sorted(dictionary_list.items())

        for i in range(len(dictionary_list_sort)):
            array_distances.append(dictionary_list_sort[i][1])

    len_arrays = len(claFuels.get_localidad())

    if len_arrays >= 5:

        data_csv = {'Distancia_minima_trayectoria': array_distances,
                    "Localidad": claFuels.get_localidad()[0:4],
                    "Provincia": claFuels.get_provincia()[0:4],
                    "Municipio": claFuels.get_municipio()[0:4],
                    "Horario": claFuels.get_horario()[0:4],
                    "Codigo_Postal": claFuels.get_cp()[0:4],
                    "Margen": claFuels.get_margen()[0:4],
                    "Tipo_de_venta": claFuels.get_tipoventa()[0:4],
                    "Fecha_Hora": claFuels.get_timeS()[0:4],
                    "Latitud": claFuels.get_latitud()[0:4],
                    "Longitud": claFuels.get_longitud()[0:4],
                    "Precio_biodiesel": claFuels.get_preciobiodiesel()[0:4],
                    "Precio_bioetanol": claFuels.get_preciobioetanol()[0:4],
                    "Precio_gas_natural": claFuels.get_preciogasnatural()[0:4],
                    "Precio_gasoleoA": claFuels.get_preciogasoleoa()[0:4],
                    "Precio_gasolina95": claFuels.get_preciogasolina95()[0:4],
                    "Precio_gasolina98": claFuels.get_preciogasolina98()[0:4],
                    "Precio_gasoleoB": claFuels.get_preciogasoleob()[0:4]
                   }
    else:
        data_csv = {'Distancia_minima_trayectoria': array_distances,
                    "Localidad": claFuels.get_localidad(),
                    "Provincia": claFuels.get_provincia(),
                    "Municipio": claFuels.get_municipio(),
                    "Horario": claFuels.get_horario(),
                    "Codigo_Postal": claFuels.get_cp(),
                    "Margen": claFuels.get_margen(),
                    "Tipo_de_venta": claFuels.get_tipoventa(),
                    "Fecha_Hora": claFuels.get_timeS(),
                    "Latitud": claFuels.get_latitud(),
                    "Longitud": claFuels.get_longitud(),
                    "Precio_biodiesel": claFuels.get_preciobiodiesel(),
                    "Precio_bioetanol": claFuels.get_preciobioetanol(),
                    "Precio_gas_natural": claFuels.get_preciogasnatural(),
                    "Precio_gasoleoA": claFuels.get_preciogasoleoa(),
                    "Precio_gasolina95": claFuels.get_preciogasolina95(),
                    "Precio_gasolina98": claFuels.get_preciogasolina98(),
                    "Precio_gasoleoB": claFuels.get_preciogasoleob()
                   }

    df = pd.DataFrame(data_csv)

    df.to_csv('Data_fuels_static.csv', encoding='utf-8')

    if os.path.isdir('./output_fuels') == False:
        os.mkdir('./output_fuels')
    out_file = open("./output_fuels/Data_fuels_static.json", "w")
    json.dump(data_csv, out_file, indent=4)
    out_file.close()

def save_csv_dinamic_incidents(index_incidents_provincia_start, index_incidents_provincia_end, array_distances_start, array_distances_end, claFuels):
    horario = claFuels.get_horario()
    cp = claFuels.get_cp()
    latitud = claFuels.get_latitud()
    longitud = claFuels.get_longitud()
    localidad = claFuels.get_localidad()
    margen = claFuels.get_margen()
    municipio = claFuels.get_municipio()
    preciobiodiesel = claFuels.get_preciobiodiesel()
    preciobioetanol = claFuels.get_preciobioetanol()
    preciogasnatural = claFuels.get_preciogasnatural()
    preciogasoleoa = claFuels.get_preciogasoleoa()
    preciogasolina95 = claFuels.get_preciogasolina95()
    preciogasolina98 = claFuels.get_preciogasolina98()
    preciogasoleob = claFuels.get_preciogasoleob()
    provincia = claFuels.get_provincia()
    tipoventa = claFuels.get_tipoventa()
    timeS = claFuels.get_timeS()

    #punto de inicio
    horario_start = []
    cp_start = []
    latitud_start = []
    longitud_start = []
    localidad_start = []
    margen_start = []
    municipio_start = []
    preciobiodiesel_start = []
    preciobioetanol_start = []
    preciogasnatural_start = []
    preciogasoleoa_start = []
    preciogasolina95_start = []
    preciogasolina98_start = []
    preciogasoleob_start = []
    provincia_start = []
    tipoventa_start = []
    timeS_start = []
    distancias_start = []


    w = 0
    for i in range(len(horario)):
        for j in range(len(index_incidents_provincia_start)):
            if i == index_incidents_provincia_start[j]:
                distancias_start.append(array_distances_start[w])
                w = w + 1
                horario_start.append(horario[i])
                cp_start.append(cp[i])
                latitud_start.append(latitud[i])
                longitud_start.append(longitud[i])
                localidad_start.append(localidad[i])
                margen_start.append(margen[i])
                municipio_start.append(municipio[i])
                preciobiodiesel_start.append(preciobiodiesel[i])
                preciobioetanol_start.append(preciobioetanol[i])
                preciogasnatural_start.append(preciogasnatural[i])
                preciogasoleoa_start.append(preciogasoleoa[i])
                preciogasolina95_start.append(preciogasolina95[i])
                preciogasolina98_start.append(preciogasolina98[i])
                preciogasoleob_start.append(preciogasoleob[i])
                provincia_start.append(provincia[i])
                tipoventa_start.append(tipoventa[i])
                timeS_start.append(timeS[i])


    data_csv = {'Distancia_minima_trayectoria': array_distances_start,
                "Localidad": localidad_start,
                "Provincia": provincia_start,
                "Municipio": municipio_start,
                "Horario": horario_start,
                "Codigo_Postal": cp_start,
                "Margen": margen_start,
                "Tipo_de_venta": tipoventa_start,
                "Fecha_Hora": timeS_start,
                "Latitud": latitud_start,
                "Longitud": longitud_start,
                "Precio_biodiesel": preciobiodiesel_start,
                "Precio_bioetanol": preciobioetanol_start,
                "Precio_gas_natural": preciogasnatural_start,
                "Precio_gasoleoA": preciogasoleoa_start,
                "Precio_gasolina95": preciogasolina95_start,
                "Precio_gasolina98": preciogasolina98_start,
                "Precio_gasoleoB": preciogasoleob_start
               }

    df = pd.DataFrame(data_csv)

    df.to_csv('Data_fuels_dinamic_start.csv', encoding='utf-8')

    if os.path.isdir('./output_fuels') == False:
        os.mkdir('./output_fuels')
    out_file = open("./output_fuels/Data_fuels_dinamic_start.json", "w")
    json.dump(data_csv, out_file, indent=4)
    out_file.close()

    # punto final
    horario_end = []
    cp_end = []
    latitud_end = []
    longitud_end = []
    localidad_end = []
    margen_end = []
    municipio_end = []
    preciobiodiesel_end = []
    preciobioetanol_end = []
    preciogasnatural_end = []
    preciogasoleoa_end = []
    preciogasolina95_end = []
    preciogasolina98_end = []
    preciogasoleob_end = []
    provincia_end = []
    tipoventa_end = []
    timeS_end = []
    distancias_end = []

    w = 0
    for i in range(len(horario)):
        for j in range(len(index_incidents_provincia_end)):
            if i == index_incidents_provincia_end[j]:
                distancias_end.append(array_distances_end[w])
                w = w + 1
                horario_end.append(horario[i])
                cp_end.append(cp[i])
                latitud_end.append(latitud[i])
                longitud_end.append(longitud[i])
                localidad_end.append(localidad[i])
                margen_end.append(margen[i])
                municipio_end.append(municipio[i])
                preciobiodiesel_end.append(preciobiodiesel[i])
                preciobioetanol_end.append(preciobioetanol[i])
                preciogasnatural_end.append(preciogasnatural[i])
                preciogasoleoa_end.append(preciogasoleoa[i])
                preciogasolina95_end.append(preciogasolina95[i])
                preciogasolina98_end.append(preciogasolina98[i])
                preciogasoleob_end.append(preciogasoleob[i])
                provincia_end.append(provincia[i])
                tipoventa_end.append(tipoventa[i])
                timeS_end.append(timeS[i])

    data_csv = {'Distancia_minima_trayectoria': array_distances_end,
                "Localidad": localidad_end,
                "Provincia": provincia_end,
                "Municipio": municipio_end,
                "Horario": horario_end,
                "Codigo_Postal": cp_end,
                "Margen": margen_end,
                "Tipo_de_venta": tipoventa_end,
                "Fecha_Hora": timeS_end,
                "Latitud": latitud_end,
                "Longitud": longitud_end,
                "Precio_biodiesel": preciobiodiesel_end,
                "Precio_bioetanol": preciobioetanol_end,
                "Precio_gas_natural": preciogasnatural_end,
                "Precio_gasoleoA": preciogasoleoa_end,
                "Precio_gasolina95": preciogasolina95_end,
                "Precio_gasolina98": preciogasolina98_end,
                "Precio_gasoleoB": preciogasoleob_end
               }
    df = pd.DataFrame(data_csv)

    df.to_csv('Data_fuels_dinamic_end.csv', encoding='utf-8')

    if os.path.isdir('./output_fuels') == False:
        os.mkdir('./output_fuels')
    out_file = open("./output_fuels/Data_fuels_dinamic_end.json", "w")
    json.dump(data_csv, out_file, indent=4)
    out_file.close()



