import json
import gps_classFuels


def function_to_test_get_horario(horario):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_horario(horario)
    horario=claFuels.get_horario()
    return horario

def function_to_test_set_horario(horario):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_horario(horario)
    horario=claFuels.horarioC
    return horario

def function_to_test_get_cp(cp):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_cp(cp)
    cp=claFuels.get_cp()
    return cp

def function_to_test_set_cp(cp):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_cp(cp)
    cp=claFuels.cpC
    return cp

def function_to_test_get_latitud(latitud):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_latitud(latitud)
    latitud=claFuels.get_latitud()
    return latitud

def function_to_test_set_latitud(latitud):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_latitud(latitud)
    latitud=claFuels.latitudC
    return latitud

def function_to_test_get_longitud(longitud):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_longitud(longitud)
    longitud=claFuels.get_longitud()
    return longitud

def function_to_test_set_longitud(longitud):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_longitud(longitud)
    longitud=claFuels.longitudC
    return longitud

def function_to_test_get_localidad(localidad):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_localidad(localidad)
    localidad=claFuels.get_localidad()
    return localidad

def function_to_test_set_localidad(localidad):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_localidad(localidad)
    localidad=claFuels.localidadC
    return localidad

def function_to_test_get_margen(margen):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_margen(margen)
    margen=claFuels.get_margen()
    return margen

def function_to_test_set_margen(margen):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_margen(margen)
    margen=claFuels.margenC
    return margen

def function_to_test_get_municipio(municipio):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_municipio(municipio)
    municipio=claFuels.get_municipio()
    return municipio

def function_to_test_set_municipio(municipio):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_municipio(municipio)
    municipio=claFuels.municipioC
    return municipio

def function_to_test_get_preciobiodiesel(preciobiodiesel):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciobiodiesel(preciobiodiesel)
    preciobiodiesel=claFuels.get_preciobiodiesel()
    return preciobiodiesel

def function_to_test_set_preciobiodiesel(preciobiodiesel):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciobiodiesel(preciobiodiesel)
    preciobiodiesel=claFuels.preciobiodieselC
    return preciobiodiesel

def function_to_test_get_preciobioetanol(preciobioetanol):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciobioetanol(preciobioetanol)
    preciobioetanol=claFuels.get_preciobioetanol()
    return preciobioetanol

def function_to_test_set_preciobioetanol(preciobioetanol):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciobioetanol(preciobioetanol)
    preciobioetanol=claFuels.preciobioetanolC
    return preciobioetanol

def function_to_test_get_preciogasnatural(preciogasnatural):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciogasnatural(preciogasnatural)
    preciogasnatural=claFuels.get_preciogasnatural()
    return preciogasnatural

def function_to_test_set_preciogasnatural(preciogasnatural):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciogasnatural(preciogasnatural)
    preciogasnatural=claFuels.preciogasnaturalC
    return preciogasnatural

def function_to_test_get_preciogasoleoa(preciogasoleoa):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciogasoleoa(preciogasoleoa)
    preciogasoleoa=claFuels.get_preciogasoleoa()
    return preciogasoleoa

def function_to_test_set_preciogasoleoa(preciogasoleoa):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciogasoleoa(preciogasoleoa)
    preciogasoleoa=claFuels.preciogasoleoaC
    return preciogasoleoa

def function_to_test_get_preciogasolina95(preciogasolina95):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciogasolina95(preciogasolina95)
    preciogasolina95=claFuels.get_preciogasolina95()
    return preciogasolina95

def function_to_test_set_preciogasolina95(preciogasolina95):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciogasolina95(preciogasolina95)
    preciogasolina95=claFuels.preciogasolina95C
    return preciogasolina95

def function_to_test_get_preciogasolina98(preciogasolina98):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciogasolina98(preciogasolina98)
    preciogasolina98=claFuels.get_preciogasolina98()
    return preciogasolina98

def function_to_test_set_preciogasolina98(preciogasolina98):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciogasolina98(preciogasolina98)
    preciogasolina98=claFuels.preciogasolina98C
    return preciogasolina98

def function_to_test_get_preciogasoleob(preciogasoleob):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciogasoleob(preciogasoleob)
    preciogasoleob=claFuels.get_preciogasoleob()
    return preciogasoleob

def function_to_test_set_preciogasoleob(preciogasoleob):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_preciogasoleob(preciogasoleob)
    preciogasoleob=claFuels.preciogasoleobC
    return preciogasoleob

def function_to_test_get_provincia(provincia):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_provincia(provincia)
    provincia=claFuels.get_provincia()
    return provincia

def function_to_test_set_provincia(provincia):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_provincia(provincia)
    provincia=claFuels.provinciaC
    return provincia

def function_to_test_get_tipoventa(tipoventa):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_tipoventa(tipoventa)
    tipoventa=claFuels.get_tipoventa()
    return tipoventa

def function_to_test_set_tipoventa(tipoventa):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_tipoventa(tipoventa)
    tipoventa=claFuels.tipoventaC
    return tipoventa

def function_to_test_get_timeS(timeS):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_timeS(timeS)
    timeS=claFuels.get_timeS()
    return timeS

def function_to_test_set_timeS(timeS):
    claFuels = gps_classFuels.classFuels()
    claFuels.set_timeS(timeS)
    timeS=claFuels.timeC
    return timeS