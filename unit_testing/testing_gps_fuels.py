import json
import gps_fuels
import gps_classFuels
import os
import gps_fuels_open_parameters

def function_to_test_event_fuels(data_provincias_filter):
    claFuels_1 = gps_fuels.event_fuels(data_provincias_filter)
    if claFuels_1:
        boolean_event = 1
    else:
        boolean_event = 0
    return boolean_event

def function_to_test_setting_classFuels(data_provincia,provincia,horario,cp,latitud,longitud,localidad,margen,municipio,preciobiodiesel,preciobioetanol,preciogasnatural,preciogasoleoa,preciogasolina95,preciogasolina98,preciogasoleob,timeS,tipoventa):
    claFuels = gps_classFuels.classFuels()
    gps_fuels.setting_classFuels(data_provincia,claFuels,provincia,horario,cp,latitud,longitud,localidad,margen,municipio,preciobiodiesel,preciobioetanol,preciogasnatural,preciogasoleoa,preciogasolina95,preciogasolina98,preciogasoleob,timeS,tipoventa)
    provincia_i=claFuels.get_provincia()
    if provincia_i!=[]:
        boolean_event=1
    else:
        boolean_event=0
    return boolean_event

def function_to_test_save_csv_dinamic_incidents(index_incidents_provincia_start,index_incidents_provincia_end,array_distances_start,array_distances_end,fGpsFuels, case):
    claFuels = gps_classFuels.classFuels()
    data_provincia, provincia, horario, cp, latitud, longitud, localidad, margen, municipio, preciobiodiesel, preciobioetanol, preciogasnatural, preciogasoleoa, preciogasolina95, preciogasolina98, preciogasoleob, timeS, tipoventa=gps_fuels_open_parameters.open_parameters_test_setting_classFuels(fGpsFuels, case)
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
    gps_fuels.save_csv_dinamic_incidents(index_incidents_provincia_start,index_incidents_provincia_end,array_distances_start,array_distances_end,claFuels)
    if os.path.isfile('./output_fuels/Data_fuels_dinamic_start.json') == True and os.path.isfile('./output_fuels/Data_fuels_dinamic_end.json')==True:
        boolean_event=1
    else:
        boolean_event=0
    return boolean_event

def function_to_test_save_csv_static_incidents(dictionary_list,fGpsFuels, case):
    claFuels = gps_classFuels.classFuels()
    if case=='case_1' or case=='case_2':
        data_provincia, provincia, horario, cp, latitud, longitud, localidad, margen, municipio, preciobiodiesel, preciobioetanol, preciogasnatural, preciogasoleoa, preciogasolina95, preciogasolina98, preciogasoleob, timeS, tipoventa=gps_fuels_open_parameters.open_parameters_test_setting_classFuels(fGpsFuels, case)
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
    if case == 'case_4':
        horario=["10:00-14:00","10:00-14:00","10:00-14:00","10:00-14:00","10:00-14:00","10:00-14:00"]
        cp=[32400,32400,32400,32400,32400,32400]
        latitud=[-40,-40,-40,-40,-40,-40]
        longitud=[-7,-7,-7,-7,-7,-7]
        localidad=["Ribadavia","Ribadavia","Ribadavia","Ribadavia","Ribadavia","Ribadavia"]
        margen=["derecha","derecha","derecha","derecha","derecha","derecha"]
        municipio=["Ribadavia","Ribadavia","Ribadavia","Ribadavia","Ribadavia","Ribadavia"]
        preciobiodiesel=[1.12,1.12,1.12,1.12,1.12,1.12]
        preciobioetanol=[1.12,1.12,1.12,1.12,1.12,1.12]
        preciogasnatural=[1.12,1.12,1.12,1.12,1.12,1.12]
        preciogasoleoa=[1.12,1.12,1.12,1.12,1.12,1.12]
        preciogasolina95=[1.12,1.12,1.12,1.12,1.12,1.12]
        preciogasolina98=[1.12,1.12,1.12,1.12,1.12,1.12]
        preciogasoleob=[1.12,1.12,1.12,1.12,1.12,1.12]
        provincia=["Ourense","Ourense","Ourense","Ourense","Ourense","Ourense"]
        tipoventa=["particular","particular","particular","particular","particular","particular"]
        timeS=["29/08/2020 22:09:06","29/08/2020 22:09:06","29/08/2020 22:09:06","29/08/2020 22:09:06","29/08/2020 22:09:06","29/08/2020 22:09:06"]

        for i in range(len(timeS)):
            claFuels.set_horario(horario[i])
            claFuels.set_cp(cp[i])
            claFuels.set_latitud(latitud[i])
            claFuels.set_longitud(longitud[i])
            claFuels.set_localidad(localidad[i])
            claFuels.set_margen(margen[i])
            claFuels.set_municipio(municipio[i])
            claFuels.set_preciobiodiesel(preciobiodiesel[i])
            claFuels.set_preciobioetanol(preciobioetanol[i])
            claFuels.set_preciogasnatural(preciogasnatural[i])
            claFuels.set_preciogasoleoa(preciogasoleoa[i])
            claFuels.set_preciogasolina95(preciogasolina95[i])
            claFuels.set_preciogasolina98(preciogasolina98[i])
            claFuels.set_preciogasoleob(preciogasoleob[i])
            claFuels.set_provincia(provincia[i])
            claFuels.set_tipoventa(tipoventa[i])
            claFuels.set_timeS(timeS[i])
    gps_fuels.save_csv_static_incidents(claFuels,dictionary_list)
    if os.path.isfile('./output_fuels/Data_fuels_static.json') == True:
        boolean_event=1
    else:
        boolean_event=0
    return boolean_event