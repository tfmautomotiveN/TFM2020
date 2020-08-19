#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib3.request
import xml.etree.ElementTree
import gps_classXML
#import geocoder
#import requests
from geopy.geocoders import Nominatim



def read_events():

    INCIDENCIAS_URI = "http://www.dgt.es/incidenciasXY.xml"

    #incidencias = urllib3.request.urlopen(INCIDENCIAS_URI).read()
    http = urllib3.PoolManager()
    incidencias = http.request('GET',"http://www.dgt.es/incidenciasXY.xml")

    raiz = xml.etree.ElementTree.fromstring(incidencias.data)
    claXML = gps_classXML.classXML()

   
    for incidencia in raiz:

        # tipo
        tipoVar = incidencia.find('tipo').text
        claXML.set_tipo(tipoVar)

        # autonomia
        autonomiaVar = incidencia.find('autonomia').text
        claXML.set_autonomia(autonomiaVar)

        # provincia
        provinciaVar = incidencia.find('provincia').text
        claXML.set_provincia(provinciaVar)


        # matricula
        matriculaVar = incidencia.find('matricula').text
        claXML.set_matricula(matriculaVar)

        # causa
        causaVar = incidencia.find('causa').text
        claXML.set_causa(causaVar)


        # poblacion
        poblacionVar = incidencia.find('poblacion').text
        claXML.set_poblacion(poblacionVar)

        # fechahora_ini
        fechahora_iniVar = incidencia.find('fechahora_ini').text
        claXML.set_fechahoraini(fechahora_iniVar)

        # nivel
        nivelVar = incidencia.find('nivel').text
        claXML.set_nivel(nivelVar)

        # carretera
        carreteraVar = incidencia.find('carretera').text
        claXML.set_carretera(carreteraVar)

        # pk_inicial
        pk_inicialVar = incidencia.find('pk_inicial').text
        claXML.set_pkinicial(pk_inicialVar)

        # pk_final
        pk_finalVar = incidencia.find('pk_final').text
        claXML.set_pkfinal(pk_finalVar)

        # sentido
        sentidoVar = incidencia.find('sentido').text
        claXML.set_sentido(sentidoVar)

        # hacia
        haciaVar = incidencia.find('hacia').text
        claXML.set_hacia(haciaVar)

        # ref_incidencia
        ref_incidenciaVar = incidencia.find('ref_incidencia').text
        claXML.set_refincidencia(ref_incidenciaVar)


        # version_incidencia
        version_incidenciaVar = incidencia.find('version_incidencia').text
        claXML.set_versionincidencia(version_incidenciaVar)

        # x
        xVar = incidencia.find('x').text
        claXML.set_x(xVar)

        # y
        yVar = incidencia.find('y').text
        claXML.set_y(yVar)

        # tipolocalizacion
        tipolocalizacionVar = incidencia.find('tipolocalizacion').text
        claXML.set_tipolocalizacion(tipolocalizacionVar)
        name_country = provinciaVar+','+'Spain'
        #loc=geocoder.google('{},Córdoba, Andalucía, Spain')
        #location = geocoder.google('Calle El Almendro 6, Córdoba, Spain')
        #print(location)


        #url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyAUlORc2i5KOyQe59O6Xf7MBN1kVl9_ngI&address=Calle%20Santa%20Isabel%2052%2028018,%20Madrid'
        #params = {'sensor': 'false', 'address': 'Madrid, Spain'}
        #r = requests.get(url, params=params)
        #results = r.json()['results']
        #print(results)
        #location = results[0]['geometry']['location']
        #print(location['lat'], location['lng'])
        #AIzaSyAUlORc2i5KOyQe59O6Xf7MBN1kVl9_ngI

        #g = geocoder.geonames('New York', key='<USERNAME>')
        #print(g.address)
        geolocalizador = Nominatim()
        direccion = geolocalizador.geocode('Madrid,Spain', timeout=15)
        print(direccion)
        print(direccion.latitude, direccion.longitude)



