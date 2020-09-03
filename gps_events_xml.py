#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib3.request
import xml.etree.ElementTree
import gps_classXML
#import geocoder
#import requests
from geopy.geocoders import Nominatim
from geopy import distance
import matplotlib.pyplot as plt
import pandas as pd
import json
import os



def read_events(data_provincias_filter):
    http = urllib3.PoolManager()
    incidencias = http.request('GET', "http://www.dgt.es/incidenciasXY.xml")

    raiz = xml.etree.ElementTree.fromstring(incidencias.data)
    claXML = gps_classXML.classXML()


    for incidencia in raiz:

        # tipo
        tipoVar = incidencia.find('tipo').text

        # autonomia
        autonomiaVar = incidencia.find('autonomia').text

        # provincia
        provinciaVar = incidencia.find('provincia').text

        # matricula
        matriculaVar = incidencia.find('matricula').text
        #claXML.set_matricula(matriculaVar)

        # causa
        causaVar = incidencia.find('causa').text

        # poblacion
        poblacionVar = incidencia.find('poblacion').text

        # fechahora_ini
        fechahora_iniVar = incidencia.find('fechahora_ini').text

        # nivel
        nivelVar = incidencia.find('nivel').text

        # carretera
        carreteraVar = incidencia.find('carretera').text

        # pk_inicial
        pk_inicialVar = incidencia.find('pk_inicial').text

        # pk_final
        pk_finalVar = incidencia.find('pk_final').text

        # sentido
        sentidoVar = incidencia.find('sentido').text

        # hacia
        haciaVar = incidencia.find('hacia').text

        # ref_incidencia
        ref_incidenciaVar = incidencia.find('ref_incidencia').text

        # version_incidencia
        version_incidenciaVar = incidencia.find('version_incidencia').text

        # x
        xVar = incidencia.find('x').text

        # y
        yVar = incidencia.find('y').text

        # tipolocalizacion
        tipolocalizacionVar = incidencia.find('tipolocalizacion').text

        #seteamos todos los setters de la clase classXML
        if data_provincias_filter == []:
            data_provincia = 'PONTEVEDRA'
            setting_classXML(data_provincia, claXML, provinciaVar, tipoVar, autonomiaVar, matriculaVar, causaVar,
                             poblacionVar, fechahora_iniVar, nivelVar, carreteraVar, pk_inicialVar, pk_finalVar,
                             sentidoVar, haciaVar, ref_incidenciaVar, version_incidenciaVar, xVar, yVar,
                             tipolocalizacionVar)
        else:
            for i in range(len(data_provincias_filter)):
                setting_classXML(data_provincias_filter[i], claXML, provinciaVar, tipoVar, autonomiaVar, matriculaVar, causaVar,
                                 poblacionVar, fechahora_iniVar, nivelVar, carreteraVar, pk_inicialVar, pk_finalVar,
                                 sentidoVar, haciaVar, ref_incidenciaVar, version_incidenciaVar, xVar, yVar,
                                 tipolocalizacionVar)

    return claXML.get_y(), claXML.get_x(), claXML

def calculate_distances(x, y, data_incidencia_x, data_incidencia_y):
    array_distances = []
    dictionary_list = {}
    index_array = []

    for i in range(len(data_incidencia_x)):
        for j in range(len(x)):
            point_1_incident = (abs(y[j]), abs(x[j]))
            point_2_incident = (abs(data_incidencia_y[i]), abs(data_incidencia_x[i]))
            calculate_distance = distance.distance(point_1_incident, point_2_incident).km
            array_distances.append(calculate_distance)
        dictionary_list.setdefault(str(i), min(array_distances))
        index_array.append(array_distances.index(min(array_distances)))
        array_distances = []


    '''for i in range(len(index_array)):
        variables_legend = []
        names_legend = []
        cont_event = 0
        cont_no_event = 0

        min_a=abs(index_array[i]-5000)
        max_a=index_array[i]+5000
        x=x[min_a:max_a]
        y=y[min_a:max_a]
        for j in range(len(x)):
            if j in index_array:
                event_1, = plt.plot(x[j], y[j], 'xr')
                if cont_event == 0:
                    cont_event = cont_event + 1
                    variables_legend.append(event_1)
                    names_legend.append('Evento en carretera a una distancia de '+str(dictionary_list[str(i)])+' kilometros')
            else:
                event_2, = plt.plot(x[j],y[j], 'xg')
                if cont_no_event == 0:
                    cont_no_event = cont_no_event + 1
                    variables_legend.append(event_2)
                    names_legend.append('No hay evento en carretera')

        plt.legend(variables_legend, names_legend, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
        #plt.title('Hay evento en carretera a una distancia de'+str(dictionary_list['1'])+'kilometros')
        plt.title('Eventos cercanos en trayectoria')
        plt.savefig('event_lines'+str(i)+'.png', bbox_inches='tight')
        plt.close()'''
    return dictionary_list
def save_csv_static_incidents(claXML, dictionary_list):

    dictionary_list_sort = sorted(dictionary_list.items())
    array_distances = []

    for i in range(len(dictionary_list_sort)):
        array_distances.append(dictionary_list_sort[i][1])


    data_csv = {'Distancia_minima_trayectoria': array_distances,
                "Tipo_incidencia": claXML.get_tipo(),
                "Causa_incidencia": claXML.get_causa(),
                "Autonomia": claXML.get_autonomia(),
                "Provincia": claXML.get_provincia(),
                "Poblacion": claXML.get_poblacion(),
                "Carretera": claXML.get_carretera(),
                "Punto_km_inicial": claXML.get_pkinicial(),
                "Punto_km_final": claXML.get_pkfinal(),
                "Sentido": claXML.get_sentido(),
                "Nivel": claXML.get_nivel(),
                "Fecha_Hora": claXML.get_fechahoraini(),
                "Matrícula": claXML.get_matricula(),
                "Referencia_Incidencia": claXML.get_refincidencia(),
                "Version_incidencia": claXML.get_versionincidencia(),
                "Latitud": claXML.get_x(),
                "Longitud": claXML.get_y()
               }
    df = pd.DataFrame(data_csv)

    df.to_csv('Data_incidents_static.csv', encoding='utf-8')

    if os.path.isdir('./output_incidents') == False:
        os.mkdir('./output_incidents')
    out_file = open("./output_incidents/Data_incidents_static.json", "w")
    json.dump(data_csv, out_file, indent=4)
    out_file.close()

def setting_classXML(data_provincia, claXML, provinciaVar, tipoVar, autonomiaVar, matriculaVar, causaVar, poblacionVar, fechahora_iniVar, nivelVar, carreteraVar, pk_inicialVar, pk_finalVar, sentidoVar, haciaVar, ref_incidenciaVar, version_incidenciaVar, xVar, yVar, tipolocalizacionVar):
    if provinciaVar == data_provincia:
        claXML.set_tipo(tipoVar)
        claXML.set_autonomia(autonomiaVar)
        claXML.set_provincia(provinciaVar)
        claXML.set_matricula(matriculaVar)
        claXML.set_causa(causaVar)
        claXML.set_poblacion(poblacionVar)
        claXML.set_fechahoraini(fechahora_iniVar)
        claXML.set_nivel(nivelVar)
        claXML.set_carretera(carreteraVar)
        claXML.set_pkinicial(pk_inicialVar)
        claXML.set_pkfinal(pk_finalVar)
        claXML.set_sentido(sentidoVar)
        claXML.set_hacia(haciaVar)
        claXML.set_refincidencia(ref_incidenciaVar)
        claXML.set_versionincidencia(version_incidenciaVar)
        claXML.set_x(xVar)
        claXML.set_y(yVar)
        claXML.set_tipolocalizacion(tipolocalizacionVar)

def get_latitude_longitude_from_Nominatum(address_to_events):
    x_longitudes = []
    y_latitudes = []
    geolocalizador = Nominatim()
    for i in range(len(address_to_events)):
        direccion = geolocalizador.geocode(address_to_events[i], timeout=15)
        if direccion != None:
            x_longitudes.append(direccion.longitude)
            y_latitudes.append(direccion.latitude)

    return x_longitudes, y_latitudes

def calculate_distances_to_incidents(x_longitudes, y_latitudes, data_incidencia_x, data_incidencia_y, data_provincias_filter, claXML):
    get_provincia = claXML.get_provincia()
    index_incidents_provincia_start = []
    index_incidents_provincia_end = []

    for i in range(len(get_provincia)):
        if get_provincia[i] == data_provincias_filter[0]:
            index_incidents_provincia_start.append(i)
        else:
            index_incidents_provincia_end.append(i)

    array_distances_start = []
    array_distances_end = []

    for i in range(len(data_incidencia_x)):
        for j in range(len(index_incidents_provincia_start)):
            if i == index_incidents_provincia_start[j]:
                point_1_incident = (y_latitudes[0], x_longitudes[0],)
                point_2_incident = (data_incidencia_y[i], data_incidencia_x[i])
                calculate_distance = distance.distance(point_1_incident, point_2_incident).km
                array_distances_start.append(calculate_distance)


    for i in range(len(data_incidencia_x)):
        for j in range(len(index_incidents_provincia_end)):
            if i == index_incidents_provincia_end[j]:
                point_1_incident = (y_latitudes[0], x_longitudes[0],)
                point_2_incident = (data_incidencia_y[i], data_incidencia_x[i])
                calculate_distance = distance.distance(point_1_incident, point_2_incident).km
                array_distances_end.append(calculate_distance)
    return index_incidents_provincia_start, index_incidents_provincia_end, array_distances_start, array_distances_end

def save_csv_dinamic_incidents(index_incidents_provincia_start, index_incidents_provincia_end, array_distances_start, array_distances_end, claXML):

    tipoVar = claXML.get_tipo()
    autonomiaVar = claXML.get_autonomia()
    provinciaVar = claXML.get_provincia()
    matriculaVar = claXML.get_matricula()
    causaVar = claXML.get_causa()
    poblacionVar = claXML.get_poblacion()
    fechahora_iniVar = claXML.get_fechahoraini()
    nivelVar = claXML.get_nivel()
    carreteraVar = claXML.get_carretera()
    pk_inicialVar = claXML.get_pkinicial()
    pk_finalVar = claXML.get_pkfinal()
    sentidoVar = claXML.get_sentido()
    haciaVar = claXML.get_hacia()
    ref_incidenciaVar = claXML.get_refincidencia()
    version_incidenciaVar = claXML.get_versionincidencia()
    xVar = claXML.get_x()
    yVar = claXML.get_y()
    tipolocalizacionVar = claXML.get_tipolocalizacion()

    #punto de inicio
    tipoVar_start = []
    autonomiaVar_start = []
    provinciaVar_start = []
    matriculaVar_start = []
    causaVar_start = []
    poblacionVar_start = []
    fechahora_iniVar_start = []
    nivelVar_start = []
    carreteraVar_start = []
    pk_inicialVar_start = []
    pk_finalVar_start = []
    sentidoVar_start = []
    haciaVar_start = []
    ref_incidenciaVar_start = []
    version_incidenciaVar_start = []
    xVar_start = []
    yVar_start = []
    tipolocalizacionVar_start = []
    distancias_start = []

    w = 0
    for i in range(len(tipoVar)):
        for j in range(len(index_incidents_provincia_start)):
            if i == index_incidents_provincia_start[j]:
                distancias_start.append(array_distances_start[w])
                w = w+1
                tipoVar_start.append(tipoVar[i])
                autonomiaVar_start.append(autonomiaVar[i])
                provinciaVar_start.append(provinciaVar[i])
                matriculaVar_start.append(matriculaVar[i])
                causaVar_start.append(causaVar[i])
                poblacionVar_start.append(poblacionVar[i])
                fechahora_iniVar_start.append(fechahora_iniVar[i])
                nivelVar_start.append(nivelVar[i])
                carreteraVar_start.append(carreteraVar[i])
                pk_inicialVar_start.append(pk_inicialVar[i])
                pk_finalVar_start.append(pk_finalVar[i])
                sentidoVar_start.append(sentidoVar[i])
                haciaVar_start.append(haciaVar[i])
                ref_incidenciaVar_start.append(ref_incidenciaVar[i])
                version_incidenciaVar_start.append(version_incidenciaVar[i])
                xVar_start.append(xVar[i])
                yVar_start.append(yVar[i])
                tipolocalizacionVar_start.append(tipolocalizacionVar[i])

    data_csv = {'Distancia_kilometros': distancias_start,
                "Tipo_incidencia": tipoVar_start,
                "Causa_incidencia": causaVar_start,
                "Autonomia": autonomiaVar_start,
                "Provincia": provinciaVar_start,
                "Poblacion": poblacionVar_start,
                "Carretera": carreteraVar_start,
                "Punto_km_inicial": pk_inicialVar_start,
                "Punto_km_final": pk_finalVar_start,
                "Sentido": sentidoVar_start,
                "Nivel": nivelVar_start,
                "Fecha_Hora": fechahora_iniVar_start,
                "Matrícula": matriculaVar_start,
                "Referencia_Incidencia": ref_incidenciaVar_start,
                "Version_incidencia": version_incidenciaVar_start,
                "Latitud": xVar_start,
                "Longitud": yVar_start
               }
    df = pd.DataFrame(data_csv)

    df.to_csv('Data_incidents_dinamic_start.csv', encoding='utf-8')

    if os.path.isdir('./output_incidents') == False:
        os.mkdir('./output_incidents')
    out_file = open("./output_incidents/Data_incidents_dinamic_start.json", "w")
    json.dump(data_csv, out_file, indent=4)
    out_file.close()

    #punto final
    tipoVar_end = []
    autonomiaVar_end = []
    provinciaVar_end = []
    matriculaVar_end = []
    causaVar_end = []
    poblacionVar_end = []
    fechahora_iniVar_end = []
    nivelVar_end = []
    carreteraVar_end = []
    pk_inicialVar_end = []
    pk_finalVar_end = []
    sentidoVar_end = []
    haciaVar_end = []
    ref_incidenciaVar_end = []
    version_incidenciaVar_end = []
    xVar_end = []
    yVar_end = []
    tipolocalizacionVar_end = []
    distancias_end = []

    w = 0
    for i in range(len(tipoVar)):
        for j in range(len(index_incidents_provincia_end)):
            if i == index_incidents_provincia_end[j]:
                distancias_end.append(array_distances_end[w])
                w = w+1
                tipoVar_end.append(tipoVar[i])
                autonomiaVar_end.append(autonomiaVar[i])
                provinciaVar_end.append(provinciaVar[i])
                matriculaVar_end.append(matriculaVar[i])
                causaVar_end.append(causaVar[i])
                poblacionVar_end.append(poblacionVar[i])
                fechahora_iniVar_end.append(fechahora_iniVar[i])
                nivelVar_end.append(nivelVar[i])
                carreteraVar_end.append(carreteraVar[i])
                pk_inicialVar_end.append(pk_inicialVar[i])
                pk_finalVar_end.append(pk_finalVar[i])
                sentidoVar_end.append(sentidoVar[i])
                haciaVar_end.append(haciaVar[i])
                ref_incidenciaVar_end.append(ref_incidenciaVar[i])
                version_incidenciaVar_end.append(version_incidenciaVar[i])
                xVar_end.append(xVar[i])
                yVar_end.append(yVar[i])
                tipolocalizacionVar_end.append(tipolocalizacionVar[i])

    data_csv = {'Distancia_kilometros': distancias_end,
                "Tipo_incidencia": tipoVar_end,
                "Causa_incidencia": causaVar_end,
                "Autonomia": autonomiaVar_end,
                "Provincia": provinciaVar_end,
                "Poblacion": poblacionVar_end,
                "Carretera": carreteraVar_end,
                "Punto_km_inicial": pk_inicialVar_end,
                "Punto_km_final": pk_finalVar_end,
                "Sentido": sentidoVar_end,
                "Nivel": nivelVar_end,
                "Fecha_Hora": fechahora_iniVar_end,
                "Matrícula": matriculaVar_end,
                "Referencia_Incidencia": ref_incidenciaVar_end,
                "Version_incidencia": version_incidenciaVar_end,
                "Latitud": xVar_end,
                "Longitud": yVar_end
               }
    df = pd.DataFrame(data_csv)

    df.to_csv('Data_incidents_dinamic_end.csv', encoding='utf-8')

    if os.path.isdir('./output_incidents') == False:
        os.mkdir('./output_incidents')
    out_file = open("./output_incidents/Data_incidents_dinamic_end.json", "w")
    json.dump(data_csv, out_file, indent=4)
    out_file.close()

