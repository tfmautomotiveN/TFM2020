#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import xmlrunner
import os
import sys
import shutil

# Need to add both '.' and '..' because it is not sure whether unit tests are run under unit_testing/ or it's parent dir
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
#sys.path.insert(0, os.path.abspath('..\lib'))
#sys.path.insert(0, os.path.abspath('lib'))
#os.environ['PATH'] = os.path.abspath('..\lib') + ';' + os.path.abspath('lib') + ';' + os.environ['PATH']

import main_gps_parameters
import gps_parameters_save_results
import main_gps_classFuels
import main_gps_classXML
import main_gps_fuels


# This dictionary saves the tests that fail
dict_results = {}

JUNIT_REPORT_PATH = './test-reports'
OUTPUT_JSON_PATH = './output_tests'


class TestCase_GpsParameters(unittest.TestCase):
    """
    Class to calculate unit tests to the synchronization times and checking objects
    @author: Noelia Riveiro
    @version: 0.0
    @class TestCase_GpsParameters
    """
    instance_unittest = unittest.TestCase('__init__')

    def tearDown(self):
        amount = self.currentResult.testsRun
        self.save_results(amount)

    def run(self, result=None):
        self.currentResult = result
        unittest.TestCase.run(self, result)

    def save_results(self, amount):
        gps_parameters_save_results.save_results_in_json(dict_results, amount)

    def test_return_position_event(self):
        main_gps_parameters.test_return_position_event(dict_results,self.instance_unittest)

    def test_open_address(self):
        main_gps_parameters.test_open_address(dict_results,self.instance_unittest)

    def test_open_data(self):
        main_gps_parameters.test_open_data(dict_results, self.instance_unittest)
       

class TestCase_ClassFuels(unittest.TestCase):
    """
    Class to calculate unit tests to the synchronization times and checking objects
    @author: Noelia Riveiro
    @version: 0.0
    @class TestCase_ClassFuels
    """
    instance_unittest = unittest.TestCase('__init__')

    def tearDown(self):
        amount = self.currentResult.testsRun
        self.save_results(amount)

    def run(self, result=None):
        self.currentResult = result
        unittest.TestCase.run(self, result)

    def save_results(self, amount):
        gps_parameters_save_results.save_results_in_json(dict_results, amount)

    def test_set_horario(self):
        main_gps_classFuels.test_set_horario(dict_results, self.instance_unittest)

    def test_get_horario(self):
        main_gps_classFuels.test_get_horario(dict_results, self.instance_unittest)

    def test_get_cp(self):
        main_gps_classFuels.test_get_cp(dict_results, self.instance_unittest)

    def test_set_cp(self):
        main_gps_classFuels.test_set_cp(dict_results, self.instance_unittest)

    def test_get_latitud(self):
        main_gps_classFuels.test_get_latitud(dict_results, self.instance_unittest)

    def test_set_latitud(self):
        main_gps_classFuels.test_set_latitud(dict_results, self.instance_unittest)

    def test_get_longitud(self):
        main_gps_classFuels.test_get_longitud(dict_results, self.instance_unittest)

    def test_set_longitud(self):
        main_gps_classFuels.test_set_longitud(dict_results, self.instance_unittest)

    def test_get_localidad(self):
        main_gps_classFuels.test_get_localidad(dict_results, self.instance_unittest)

    def test_set_localidad(self):
        main_gps_classFuels.test_set_localidad(dict_results, self.instance_unittest)

    def test_get_margen(self):
        main_gps_classFuels.test_get_margen(dict_results, self.instance_unittest)

    def test_set_margen(self):
        main_gps_classFuels.test_set_margen(dict_results, self.instance_unittest)

    def test_get_municipio(self):
        main_gps_classFuels.test_get_municipio(dict_results, self.instance_unittest)

    def test_set_municipio(self):
        main_gps_classFuels.test_set_municipio(dict_results, self.instance_unittest)

    def test_get_preciobiodiesel(self):
        main_gps_classFuels.test_get_preciobiodiesel(dict_results, self.instance_unittest)

    def test_set_preciobiodiesel(self):
        main_gps_classFuels.test_set_preciobiodiesel(dict_results, self.instance_unittest)

    def test_get_preciobioetanol(self):
        main_gps_classFuels.test_get_preciobioetanol(dict_results, self.instance_unittest)

    def test_set_preciobioetanol(self):
        main_gps_classFuels.test_set_preciobioetanol(dict_results, self.instance_unittest)

    def test_get_preciogasnatural(self):
        main_gps_classFuels.test_get_preciogasnatural(dict_results, self.instance_unittest)

    def test_set_preciogasnatural(self):
        main_gps_classFuels.test_set_preciogasnatural(dict_results, self.instance_unittest)

    def test_get_preciogasoleoa(self):
        main_gps_classFuels.test_get_preciogasoleoa(dict_results, self.instance_unittest)

    def test_set_preciogasoleoa(self):
        main_gps_classFuels.test_set_preciobioetanol(dict_results, self.instance_unittest)

    def test_get_preciogasolina95(self):
        main_gps_classFuels.test_get_preciogasolina95(dict_results, self.instance_unittest)

    def test_set_preciogasolina95(self):
        main_gps_classFuels.test_set_preciogasolina95(dict_results, self.instance_unittest)

    def test_get_preciogasolina98(self):
        main_gps_classFuels.test_get_preciogasolina98(dict_results, self.instance_unittest)

    def test_set_preciogasolina98(self):
        main_gps_classFuels.test_set_preciogasolina98(dict_results, self.instance_unittest)

    def test_get_preciogasoleob(self):
        main_gps_classFuels.test_get_preciogasoleob(dict_results, self.instance_unittest)

    def test_set_preciogasoleob(self):
        main_gps_classFuels.test_set_preciogasoleob(dict_results, self.instance_unittest)

    def test_get_provincia(self):
        main_gps_classFuels.test_get_provincia(dict_results, self.instance_unittest)

    def test_set_provincia(self):
        main_gps_classFuels.test_set_provincia(dict_results, self.instance_unittest)

    def test_get_tipoventa(self):
        main_gps_classFuels.test_get_tipoventa(dict_results, self.instance_unittest)

    def test_set_tipoventa(self):
        main_gps_classFuels.test_set_tipoventa(dict_results, self.instance_unittest)

    def test_get_timeS(self):
        main_gps_classFuels.test_get_timeS(dict_results, self.instance_unittest)

    def test_set_timeS(self):
        main_gps_classFuels.test_set_timeS(dict_results, self.instance_unittest)

class TestCase_ClassXML(unittest.TestCase):
    """
    Class to calculate unit tests to the synchronization times and checking objects
    @author: Noelia Riveiro
    @version: 0.0
    @class TestCase_ClassFuels
    """
    instance_unittest = unittest.TestCase('__init__')

    def tearDown(self):
        amount = self.currentResult.testsRun
        self.save_results(amount)

    def run(self, result=None):
        self.currentResult = result
        unittest.TestCase.run(self, result)

    def save_results(self, amount):
        gps_parameters_save_results.save_results_in_json(dict_results, amount)

    def test_get_tipo(self):
        main_gps_classXML.test_get_tipo(dict_results, self.instance_unittest)

    def test_set_tipo(self):
        main_gps_classXML.test_set_tipo(dict_results, self.instance_unittest)

    def test_get_autonomia(self):
        main_gps_classXML.test_get_autonomia(dict_results, self.instance_unittest)

    def test_set_autonomia(self):
        main_gps_classXML.test_set_autonomia(dict_results, self.instance_unittest)

    def test_get_provincia(self):
        main_gps_classXML.test_get_provincia(dict_results, self.instance_unittest)

    def test_set_provincia(self):
        main_gps_classXML.test_set_provincia(dict_results, self.instance_unittest)

    def test_get_matricula(self):
        main_gps_classXML.test_get_matricula(dict_results, self.instance_unittest)

    def test_set_matricula(self):
        main_gps_classXML.test_set_matricula(dict_results, self.instance_unittest)

    def test_get_causa(self):
        main_gps_classXML.test_get_causa(dict_results, self.instance_unittest)

    def test_set_causa(self):
        main_gps_classXML.test_set_causa(dict_results, self.instance_unittest)

    def test_get_poblacion(self):
        main_gps_classXML.test_get_poblacion(dict_results, self.instance_unittest)

    def test_set_poblacion(self):
        main_gps_classXML.test_set_poblacion(dict_results, self.instance_unittest)

    def test_get_fechahoraini(self):
        main_gps_classXML.test_get_fechahoraini(dict_results, self.instance_unittest)

    def test_set_fechahoraini(self):
        main_gps_classXML.test_set_fechahoraini(dict_results, self.instance_unittest)

    def test_get_nivel(self):
        main_gps_classXML.test_get_nivel(dict_results, self.instance_unittest)

    def test_set_nivel(self):
         main_gps_classXML.test_set_nivel(dict_results, self.instance_unittest)

    def test_get_carretera(self):
        main_gps_classXML.test_get_carretera(dict_results, self.instance_unittest)

    def test_set_carretera(self):
         main_gps_classXML.test_set_carretera(dict_results, self.instance_unittest)

    def test_get_pkinicial(self):
        main_gps_classXML.test_get_pkinicial(dict_results, self.instance_unittest)

    def test_set_pkinicial(self):
         main_gps_classXML.test_set_pkinicial(dict_results, self.instance_unittest)

    def test_get_pkfinal(self):
        main_gps_classXML.test_get_pkfinal(dict_results, self.instance_unittest)

    def test_set_pkfinal(self):
         main_gps_classXML.test_set_pkfinal(dict_results, self.instance_unittest)

    def test_get_sentido(self):
        main_gps_classXML.test_get_sentido(dict_results, self.instance_unittest)

    def test_set_sentido(self):
         main_gps_classXML.test_set_sentido(dict_results, self.instance_unittest)

    def test_get_hacia(self):
        main_gps_classXML.test_get_hacia(dict_results, self.instance_unittest)

    def test_set_hacia(self):
         main_gps_classXML.test_set_hacia(dict_results, self.instance_unittest)

    def test_get_refincidencia(self):
        main_gps_classXML.test_get_refincidencia(dict_results, self.instance_unittest)

    def test_set_refincidencia(self):
         main_gps_classXML.test_set_refincidencia(dict_results, self.instance_unittest)

    def test_get_versionincidencia(self):
        main_gps_classXML.test_get_versionincidencia(dict_results, self.instance_unittest)

    def test_set_versionincidencia(self):
         main_gps_classXML.test_set_versionincidencia(dict_results, self.instance_unittest)

    def test_get_x(self):
        main_gps_classXML.test_get_x(dict_results, self.instance_unittest)

    def test_set_x(self):
         main_gps_classXML.test_set_x(dict_results, self.instance_unittest)

    def test_get_y(self):
        main_gps_classXML.test_get_y(dict_results, self.instance_unittest)

    def test_set_y(self):
         main_gps_classXML.test_set_y(dict_results, self.instance_unittest)

    def test_get_tipolocalizacion(self):
        main_gps_classXML.test_get_tipolocalizacion(dict_results, self.instance_unittest)

    def test_set_tipolocalizacion(self):
         main_gps_classXML.test_set_tipolocalizacion(dict_results, self.instance_unittest)


class TestCase_GpsFuels(unittest.TestCase):

    instance_unittest = unittest.TestCase('__init__')

    def tearDown(self):
        amount = self.currentResult.testsRun
        self.save_results(amount)

    def run(self, result=None):
        self.currentResult = result
        unittest.TestCase.run(self, result)

    def save_results(self, amount):
        gps_parameters_save_results.save_results_in_json(dict_results, amount)

    def test_event_fuels(self):
        main_gps_fuels.test_event_fuels(dict_results, self.instance_unittest)

    def test_setting_classFuels(self):
        main_gps_fuels.test_setting_classFuels(dict_results, self.instance_unittest)

    def test_save_csv_static_incidents(self):
        main_gps_fuels.test_save_csv_static_incidents(dict_results, self.instance_unittest)

    def test_save_csv_dinamic_incidents(self):
        main_gps_fuels.test_save_csv_dinamic_incidents(dict_results, self.instance_unittest)


if __name__ == "__main__":

        # Run tests and generate JUnit report
        print "### Generating JUnit reports to:", os.path.join(os.getcwd(), JUNIT_REPORT_PATH)

        if os.path.isdir(OUTPUT_JSON_PATH) == True:
            shutil.rmtree(OUTPUT_JSON_PATH, ignore_errors=False)

        if os.path.isdir(JUNIT_REPORT_PATH) == True:
            shutil.rmtree(JUNIT_REPORT_PATH, ignore_errors=False)

        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=JUNIT_REPORT_PATH))