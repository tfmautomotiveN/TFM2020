# !/usr/bin/python
# -*- coding: utf-8 -*-


class classFuels:
    ##Es el constructor
    # En ella se inicializan las variables de la clase classFuels a 0
    # No tiene parámetros de entrada ni de salida
    def __init__(self):
        self.horarioC = []
        self.cpC = []
        self.latitudC = []
        self.longitudC = []
        self.localidadC = []
        self.margenC = []
        self.municipioC = []
        self.preciobiodieselC = []
        self.preciobioetanolC = []
        self.preciogasnaturalC = []
        self.preciogasoleoaC = []
        self.preciogasolina95C = []
        self.preciogasolina98C = []
        self.preciogasoleobC = []
        self.provinciaC = []
        self.tipoventaC = []
        self.timeC = []

    #La función get_num1bytes devuelve el número de bloques de 1 byte de los
    # inputs conectados al coche
    # Esta función es la que se encarga de devolver el número de
    # bloques de 1 byte de los inputs conectados al coche.
    # No tiene parámetros de entrada, pero devuelve uno de salida
    # @return num1bytes con el número de bytes de 1 byte
    def get_horario(self):
        return self.horarioC

    def set_horario(self, horario):
        self.horarioC.append(horario)

    def get_cp(self):
        return self.cpC

    def set_cp(self, cp):
        self.cpC.append(cp)

    def get_latitud(self):
        return self.latitudC

    def set_latitud(self, latitud):
        self.latitudC.append(latitud)

    def get_longitud(self):
        return self.longitudC

    def set_longitud(self, longitud):
        self.longitudC.append(longitud)

    def get_localidad(self):
        return self.localidadC

    def set_localidad(self, localidad):
        self.localidadC.append(localidad)

    def get_margen(self):
        return self.margenC

    def set_margen(self, margen):
        self.margenC.append(margen)

    def get_municipio(self):
        return self.municipioC

    def set_municipio(self, municipio):
        self.municipioC.append(municipio)

    def get_preciobiodiesel(self):
        return self.preciobiodieselC

    def set_preciobiodiesel(self, preciobiodiesel):
        self.preciobiodieselC.append(preciobiodiesel)

    def get_preciobioetanol(self):
        return self.preciobioetanolC

    def set_preciobioetanol(self, preciobioetanol):
        self.preciobioetanolC.append(preciobioetanol)

    def get_preciogasnatural(self):
        return self.preciogasnaturalC

    def set_preciogasnatural(self, preciogasnatural):
        self.preciogasnaturalC.append(preciogasnatural)

    def get_preciogasoleoa(self):
        return self.preciogasoleoaC

    def set_preciogasoleoa(self, preciogasoleoa):
        self.preciogasoleoaC.append(preciogasoleoa)

    def get_preciogasolina95(self):
        return self.preciogasolina95C

    def set_preciogasolina95(self, preciogasolina95):
        self.preciogasolina95C.append(preciogasolina95)

    def get_preciogasolina98(self):
        return self.preciogasolina98C

    def set_preciogasolina98(self, preciogasolina98):
        self.preciogasolina98C.append(preciogasolina98)

    def get_preciogasoleob(self):
        return self.preciogasoleobC

    def set_preciogasoleob(self, preciogasoleob):
        self.preciogasoleobC.append(preciogasoleob)

    def get_provincia(self):
        return self.provinciaC

    def set_provincia(self, provincia):
        self.provinciaC.append(provincia)

    def get_tipoventa(self):
        return self.tipoventaC

    def set_tipoventa(self, tipoventa):
        self.tipoventaC.append(tipoventa)

    def get_timeS(self):
        return self.timeC

    def set_timeS(self, timeS):
        self.timeC.append(timeS)