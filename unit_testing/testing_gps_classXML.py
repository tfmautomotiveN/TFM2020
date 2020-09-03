import json
import gps_classXML


def function_to_test_get_tipo(tipo):
    claXML = gps_classXML.classXML()
    claXML.set_tipo(tipo)
    tipo=claXML.get_tipo()
    return tipo

def function_to_test_set_tipo(tipo):
    claXML = gps_classXML.classXML()
    claXML.set_tipo(tipo)
    tipo=claXML.tipoC
    return tipo

def function_to_test_get_autonomia(autonomia):
    claXML = gps_classXML.classXML()
    claXML.set_autonomia(autonomia)
    autonomia=claXML.get_autonomia()
    return autonomia

def function_to_test_set_autonomia(autonomia):
    claXML = gps_classXML.classXML()
    claXML.set_autonomia(autonomia)
    autonomia=claXML.autonomiaC
    return autonomia

def function_to_test_get_provincia(provincia):
    claXML = gps_classXML.classXML()
    claXML.set_provincia(provincia)
    provincia=claXML.get_provincia()
    return provincia

def function_to_test_set_provincia(provincia):
    claXML = gps_classXML.classXML()
    claXML.set_provincia(provincia)
    provincia=claXML.provinciaC
    return provincia

def function_to_test_get_matricula(matricula):
    claXML = gps_classXML.classXML()
    claXML.set_matricula(matricula)
    matricula=claXML.get_matricula()
    return matricula

def function_to_test_set_matricula(matricula):
    claXML = gps_classXML.classXML()
    claXML.set_matricula(matricula)
    matricula=claXML.matriculaC
    return matricula

def function_to_test_get_causa(causa):
    claXML = gps_classXML.classXML()
    claXML.set_causa(causa)
    causa=claXML.get_causa()
    return causa

def function_to_test_set_causa(causa):
    claXML = gps_classXML.classXML()
    claXML.set_causa(causa)
    causa=claXML.causaC
    return causa

def function_to_test_get_poblacion(poblacion):
    claXML = gps_classXML.classXML()
    claXML.set_poblacion(poblacion)
    poblacion=claXML.get_poblacion()
    return poblacion

def function_to_test_set_poblacion(poblacion):
    claXML = gps_classXML.classXML()
    claXML.set_poblacion(poblacion)
    poblacion=claXML.poblacionC
    return poblacion

def function_to_test_get_fechahoraini(fechahoraini):
    claXML = gps_classXML.classXML()
    claXML.set_fechahoraini(fechahoraini)
    fechahoraini=claXML.get_fechahoraini()
    return fechahoraini

def function_to_test_set_fechahoraini(fechahoraini):
    claXML = gps_classXML.classXML()
    claXML.set_fechahoraini(fechahoraini)
    fechahoraini=claXML.fechahora_iniC
    return fechahoraini

def function_to_test_get_nivel(nivel):
    claXML = gps_classXML.classXML()
    claXML.set_nivel(nivel)
    nivel=claXML.get_nivel()
    return nivel

def function_to_test_set_nivel(nivel):
    claXML = gps_classXML.classXML()
    claXML.set_nivel(nivel)
    nivel=claXML.nivelC
    return nivel

def function_to_test_get_carretera(carretera):
    claXML = gps_classXML.classXML()
    claXML.set_carretera(carretera)
    carretera=claXML.get_carretera()
    return carretera

def function_to_test_set_carretera(carretera):
    claXML = gps_classXML.classXML()
    claXML.set_carretera(carretera)
    carretera=claXML.carreteraC
    return carretera

def function_to_test_get_pkinicial(pkinicial):
    claXML = gps_classXML.classXML()
    claXML.set_pkinicial(pkinicial)
    pkinicial=claXML.get_pkinicial()
    return pkinicial

def function_to_test_set_pkinicial(pkinicial):
    claXML = gps_classXML.classXML()
    claXML.set_pkinicial(pkinicial)
    pkinicial=claXML.pk_inicialC
    return pkinicial

def function_to_test_get_pkfinal(pkfinal):
    claXML = gps_classXML.classXML()
    claXML.set_pkfinal(pkfinal)
    pkfinal=claXML.get_pkfinal()
    return pkfinal

def function_to_test_set_pkfinal(pkfinal):
    claXML = gps_classXML.classXML()
    claXML.set_pkfinal(pkfinal)
    pkfinal=claXML.pk_finalC
    return pkfinal

def function_to_test_get_sentido(sentido):
    claXML = gps_classXML.classXML()
    claXML.set_sentido(sentido)
    sentido=claXML.get_sentido()
    return sentido

def function_to_test_set_sentido(sentido):
    claXML = gps_classXML.classXML()
    claXML.set_sentido(sentido)
    sentido=claXML.sentidoC
    return sentido

def function_to_test_get_hacia(hacia):
    claXML = gps_classXML.classXML()
    claXML.set_hacia(hacia)
    hacia=claXML.get_hacia()
    return hacia

def function_to_test_set_hacia(hacia):
    claXML = gps_classXML.classXML()
    claXML.set_hacia(hacia)
    hacia=claXML.haciaC
    return hacia

def function_to_test_get_refincidencia(refincidencia):
    claXML = gps_classXML.classXML()
    claXML.set_refincidencia(refincidencia)
    refincidencia=claXML.get_refincidencia()
    return refincidencia

def function_to_test_set_refincidencia(refincidencia):
    claXML = gps_classXML.classXML()
    claXML.set_refincidencia(refincidencia)
    refincidencia=claXML.ref_incidenciaC
    return refincidencia

def function_to_test_get_versionincidencia(versionincidencia):
    claXML = gps_classXML.classXML()
    claXML.set_versionincidencia(versionincidencia)
    versionincidencia=claXML.get_versionincidencia()
    return versionincidencia

def function_to_test_set_versionincidencia(versionincidencia):
    claXML = gps_classXML.classXML()
    claXML.set_versionincidencia(versionincidencia)
    versionincidencia=claXML.version_incidenciaC
    return versionincidencia

def function_to_test_get_x(x):
    claXML = gps_classXML.classXML()
    claXML.set_x(x)
    x=claXML.get_x()
    return x

def function_to_test_set_x(x):
    claXML = gps_classXML.classXML()
    claXML.set_x(x)
    x=claXML.xC
    return x

def function_to_test_get_y(y):
    claXML = gps_classXML.classXML()
    claXML.set_y(y)
    y=claXML.get_y()
    return y

def function_to_test_set_y(y):
    claXML = gps_classXML.classXML()
    claXML.set_y(y)
    y=claXML.yC
    return y

def function_to_test_get_tipolocalizacion(tipolocalizacion):
    claXML = gps_classXML.classXML()
    claXML.set_tipolocalizacion(tipolocalizacion)
    tipolocalizacion=claXML.get_tipolocalizacion()
    return tipolocalizacion

def function_to_test_set_tipolocalizacion(tipolocalizacion):
    claXML = gps_classXML.classXML()
    claXML.set_tipolocalizacion(tipolocalizacion)
    tipolocalizacion=claXML.tipolocalizacionC
    return tipolocalizacion

