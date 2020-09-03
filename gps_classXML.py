# !/usr/bin/python
# -*- coding: utf-8 -*-
#import time
#import datetime


class classXML:
    ##Es el constructor
    # En ella se inicializan las variables de la clase classXML a 0
    # No tiene parámetros de entrada ni de salida
    def __init__(self):

        self.tipoC = []
        self.autonomiaC = []
        self.provinciaC = []
        self.matriculaC = []
        self.causaC = []
        self.poblacionC = []
        self.fechahora_iniC = []
        self.nivelC = []
        self.carreteraC = []
        self.pk_inicialC = []
        self.pk_finalC = []
        self.sentidoC = []
        self.ref_incidenciaC = []
        self.version_incidenciaC = []
        self.xC = []
        self.yC = []
        self.tipolocalizacionC = []
        self.haciaC = []

    ##La función get_num1bytes devuelve el número de bloques de 1 byte de los inputs conectados al coche
    # Esta función es la que se encarga de devolver el número de bloques de 1 byte de los inputs conectados al coche.
    # No tiene parámetros de entrada, pero devuelve uno de salida
    # @return num1bytes con el número de bytes de 1 byte
    def get_tipo(self):
        return self.tipoC

    ##La función set_num1bytes tiene un parámetro de entrada y ninguno de salida.
    # Esta función tiene un parámetro de entrada num1bytes con el número de bloques de 1 byte de los inputs conectados al coche.
    # Se encarga de cambiar el valor del número de bloques de 1 byte.
    # @param num1bytes que es el número de bloques de 1 byte de los inputs
    def set_tipo(self, tipo):
        self.tipoC.append(tipo)

    ##La función get_id1bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida id1bytes con el identificador del input de 1 byte.
    # Esta función lo que va a hacer es devolver el identificador del input de 1 byte
    # @return id1bytes con el identificador del input de 1 byte

    def get_autonomia(self):
        return self.autonomiaC

    ##La función set_id1bytes tiene un parámetro de entrada y ninguno de salida.
    # Esta función tiene un parámetro de entrada id1bytes con el identificador del input de 1 byte.
    # Se encarga de cambiar el valor del identificador del input de 1 byte.
    # @param id1bytes identificador del input de 1 byte
    def set_autonomia(self, autonomia):
        self.autonomiaC.append(autonomia)

    ##La función get_value1bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida value1bytes con el valor del input de 1 byte.
    # Esta función lo que hace es devolver el valor del input de 1 byte
    # @return value1bytes con el valor del input de 1 byte
    def get_provincia(self):
        return self.provinciaC

    ##La función set_value1bytes tiene un parámetro de entrada, pero ninguno de salida.
    # Esta función tiene un parámetro de entrada value1bytes con el valor del input de 1 byte.
    # Se encarga de cambiar el valor del input de 1 byte.
    # @param value1bytes valor del input de 1 byte
    def set_provincia(self, provincia):
        self.provinciaC.append(provincia)

    ##La función get_num2bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve num2bytes con el número de bloques de 2 bytes de los inputs conectados al coche
    # Esta función lo que hace es devolver el número de bloques de 2 bytes de los inputs conectados al coche
    # @return num2bytes con el número de bloques de 2 bytes de los inputs conectados al coche
    def get_matricula(self):
        return self.matriculaC

    ##La función set_num2bytes tiene un parámetro de entrada y ninguno de salida.
    # Esta función tiene un parámetro de entrada num2bytes con el número de bloques de 2 bytes.
    # Esta función se encarga de cambiar el valor del número de bloques de 2 bytes de los inputs conectados al coche.
    # @return num2bytes con el número de bloques de 2 bytes de los inputs conectados al coche.
    def set_matricula(self, matricula):
        self.matriculaC.append(matricula)

    ##La función get_id2bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida id2bytes con el identificador del input de 2 bytes.
    # Esta función lo que va a hacer es devolver el identificador del input de 2 bytes
    # @return id2bytes con el identificador del input de 2 bytes

    def get_causa(self):
        return self.causaC

    ##La función set_id2bytes tiene un parámetro de entrada y ninguno de salida.
    # Esta función tiene un parámetro de entrada id2bytes con el identificador del input de 2 bytes.
    # Se encarga de cambiar el valor del identificador del input de 2 bytes.
    # @param id2bytes identificador del input de 2 bytes
    def set_causa(self, causa):
        self.causaC.append(causa)

    ##La función get_value2bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida value2bytes con el valor del input de 2 bytes.
    # Esta función lo que hace es devolver el valor del input de 2 bytes
    # @return value2bytes con el valor del input de 2 bytes
    def get_poblacion(self):
        return self.poblacionC

    ##La función set_value2bytes tiene un parámetro de entrada, pero ninguno de salida.
    # Esta función tiene un parámetro de entrada value2bytes con el valor del input de 2 bytes.
    # Se encarga de cambiar el valor del input de 2 bytes.
    # @param value2bytes valor del input de 2 bytes
    def set_poblacion(self, poblacion):
        self.poblacionC.append(poblacion)

    ##La función get_num4bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve num4bytes con el número de bloques de 4 bytes de los inputs conectados al coche
    # Esta función lo que hace es devolver el número de bloques de 4 bytes de los inputs conectados al coche
    # @return num4bytes con el número de bloques de 4 bytes de los inputs conectados al coche
    def get_fechahoraini(self):
        return self.fechahora_iniC

    ##La función set_num4bytes tiene un parámetro de entrada y ninguno de salida.
    # Esta función tiene un parámetro de entrada num4bytes con el número de bloques de 4 bytes.
    # Esta función se encarga de cambiar el valor del número de bloques de 4 bytes de los inputs conectados al coche.
    # @return num4bytes con el número de bloques de 4 bytes de los inputs conectados al coche.
    def set_fechahoraini(self, fechahora_ini):
        self.fechahora_iniC.append(fechahora_ini)

    ##La función get_id4bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida id4bytes con el identificador del input de 4 bytes.
    # Esta función lo que va a hacer es devolver el identificador del input de 4 bytes
    # @return id4bytes con el identificador del input de 4 bytes
    def get_nivel(self):
        return self.nivelC

    ##La función set_id4bytes tiene un parámetro de entrada y ninguno de salida.
    # Esta función tiene un parámetro de entrada id4bytes con el identificador del input de 4 bytes.
    # Se encarga de cambiar el valor del identificador del input de 4 bytes.
    # @param id4bytes identificador del input de 4 bytes
    def set_nivel(self, nivel):
        self.nivelC.append(nivel)

    ##La función get_value4bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida value4bytes con el valor del input de 4 bytes.
    # Esta función lo que hace es devolver el valor del input de 4 bytes
    # @return value4bytes con el valor del input de 4 bytes
    def get_carretera(self):
        return self.carreteraC

    ##La función set_value4bytes tiene un parámetro de entrada, pero ninguno de salida.
    # Esta función tiene un parámetro de entrada value4bytes con el valor del input de 4 bytes.
    # Se encarga de cambiar el valor del input de 4 bytes.
    # @param value4bytes valor del input de 4 bytes
    def set_carretera(self, carretera):
        self.carreteraC.append(carretera)

    ##La función get_num8bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve num8bytes con el número de bloques de 8 bytes de los inputs conectados al coche
    # Esta función lo que hace es devolver el número de bloques de 8 bytes de los inputs conectados al coche
    # @return num8bytes con el número de bloques de 8 bytes de los inputs conectados al coche
    def get_pkinicial(self):
        return self.pk_inicialC

    ##La función set_num8bytes tiene un parámetro de entrada y ninguno de salida.
    # Esta función tiene un parámetro de entrada num8bytes con el número de bloques de 8 bytes.
    # Esta función se encarga de cambiar el valor del número de bloques de 8 bytes de los inputs conectados al coche.
    # @return num8bytes con el número de bloques de 8 bytes de los inputs conectados al coche.
    def set_pkinicial(self, pk_inicial):
        if pk_inicial != None:
            pk_inicial = float(pk_inicial)
        self.pk_inicialC.append(pk_inicial)

    ##La función get_id8bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida id8bytes con el identificador del input de 8 bytes.
    # Esta función lo que va a hacer es devolver el identificador del input de 8 bytes
    # @return id8bytes con el identificador del input de 8 bytes
    def get_pkfinal(self):
        return self.pk_finalC

    ##La función set_id8bytes tiene un parámetro de entrada y ninguno de salida.
    # Esta función tiene un parámetro de entrada id8bytes con el identificador del input de 8 bytes.
    # Se encarga de cambiar el valor del identificador del input de 8 bytes.
    # @param id8bytes identificador del input de 8 bytes
    def set_pkfinal(self, pk_final):
        if pk_final != None:
            pk_final = float(pk_final)
        self.pk_finalC.append(pk_final)

    ##La función get_value8bytes no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida value8bytes con el valor del input de 8 bytes.
    # Esta función lo que hace es devolver el valor del input de 8 bytes
    # @return value8bytes con el valor del input de 8 bytes
    def get_sentido(self):
        return self.sentidoC

    ##La función set_value8bytes tiene un parámetro de entrada, pero ninguno de salida.
    # Esta función tiene un parámetro de entrada value8bytes con el valor del input de 8 bytes.
    # Se encarga de cambiar el valor del input de 8 bytes.
    # @param value8bytes valor del input de 8 bytes
    def set_sentido(self, sentido):
        self.sentidoC.append(sentido)

    ##La función get_contio1 no tiene parámetros de entrada, pero si uno de salida
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida contIO1 que es un contador interno de los elementos inputs conectados al coche
    # Esta función lo que hace es devolver el contador interno de los elementos inputs conectados al coche
    # @return contIO1 con el valor del contador interno de los elementos inputs conectados al coche
    def get_hacia(self):
        return self.haciaC

    ##La función set_contio1 tiene un parámetro de entrada, pero ninguno de salida
    # Esta función tiene un parámetro de entrada contIO1 con el valor del contador interno de los elementos inputs conectados al coche
    # Se encarga de devolver el valor del contador interno de los elementos inputs conectados al coche
    # @param contIO1 el valor del contador interno de los elementos inputs conectados al coche
    def set_hacia(self, hacia):
        self.haciaC.append(hacia)

    ##La función get_contvuelta1 no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve un de salida contvuelta1 que es un contador interno con el número de datos
    # (cabecera+cuerpo) que envía el gps.
    # Esta función lo que hace es devolver el contador interno del número de datos.
    # @return convuelta1 con el número de datos (cabecera+cuerpo)
    def get_refincidencia(self):
        return self.ref_incidenciaC

    ##La función set_convuelta1 tiene un parámetro de entrada, pero ninguno de salida.
    # Esta función tiene un parámetro de entrada contvuelta1 que indica que es un contador interno con el número de(cabecera+cuerpo) que envía el gps
    # Se encarga de devolver el contador del número (cabecera+cuerpo) que envía el gps
    # @param contvuelta1 el contador del número (cabecera+cuerpo) que envía el gps
    def set_refincidencia(self, ref_incidencia):
        self.ref_incidenciaC.append(ref_incidencia)

    ##La función get_cont2 no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida cont2 que es un contador interno auxiliar para parsear los inputs que se conectan al coche
    # Esta función lo que hace es devolver el contador interno auxiliar para parsear los inputs que envía el gps
    # @return cont2 con el contador interno auxiliar para parsear los inputs que envía el gps
    def get_versionincidencia(self):
        return self.version_incidenciaC

    ##La función set_cont2 tiene un parámetro de entrada y ninguno de salida
    # Esta función tiene un parámetro de entrada cont2 que es el contador interno auxiliar para parsear los inputs que se conectan al coche
    # Se encarga de devovler el contador interno auxiliar para parsear los inputs que se conectan al coche
    # @param cont2 el contador interno auxiliar para parsear los inputs que se conectan al coche
    def set_versionincidencia(self, version_incidencia):
        self.version_incidenciaC.append(version_incidencia)

    ##La función get_cont2 no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida cont2 que es un contador interno auxiliar para parsear los inputs que se conectan al coche
    # Esta función lo que hace es devolver el contador interno auxiliar para parsear los inputs que envía el gps
    # @return cont2 con el contador interno auxiliar para parsear los inputs que envía el gps
    def get_x(self):
        return self.xC

    ##La función set_cont2 tiene un parámetro de entrada y ninguno de salida
    # Esta función tiene un parámetro de entrada cont2 que es el contador interno auxiliar para parsear los inputs que se conectan al coche
    # Se encarga de devovler el contador interno auxiliar para parsear los inputs que se conectan al coche
    # @param cont2 el contador interno auxiliar para parsear los inputs que se conectan al coche
    def set_x(self, x):
        if x != None:
            x = float(x)
        self.xC.append(x)

    ##La función get_cont2 no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida cont2 que es un contador interno auxiliar para parsear los inputs que se conectan al coche
    # Esta función lo que hace es devolver el contador interno auxiliar para parsear los inputs que envía el gps
    # @return cont2 con el contador interno auxiliar para parsear los inputs que envía el gps
    def get_y(self):
        return self.yC

    ##La función set_cont2 tiene un parámetro de entrada y ninguno de salida
    # Esta función tiene un parámetro de entrada cont2 que es el contador interno auxiliar para parsear los inputs que se conectan al coche
    # Se encarga de devovler el contador interno auxiliar para parsear los inputs que se conectan al coche
    # @param cont2 el contador interno auxiliar para parsear los inputs que se conectan al coche
    def set_y(self, y):
        if y != None:
            y = float(y)
        self.yC.append(y)

    ##La función get_cont2 no tiene parámetros de entrada, pero si uno de salida.
    # Esta función no tiene parámetros de entrada, pero devuelve uno de salida cont2 que es un contador interno auxiliar para parsear los inputs que se conectan al coche
    # Esta función lo que hace es devolver el contador interno auxiliar para parsear los inputs que envía el gps
    # @return cont2 con el contador interno auxiliar para parsear los inputs que envía el gps
    def get_tipolocalizacion(self):
        return self.tipolocalizacionC

    ##La función set_cont2 tiene un parámetro de entrada y ninguno de salida
    # Esta función tiene un parámetro de entrada cont2 que es el contador interno auxiliar para parsear los inputs que se conectan al coche
    # Se encarga de devovler el contador interno auxiliar para parsear los inputs que se conectan al coche
    # @param cont2 el contador interno auxiliar para parsear los inputs que se conectan al coche
    def set_tipolocalizacion(self, tipolocalizacion):
        if tipolocalizacion != None:
            tipolocalizacion = int(tipolocalizacion)
        self.tipolocalizacionC.append(tipolocalizacion)
