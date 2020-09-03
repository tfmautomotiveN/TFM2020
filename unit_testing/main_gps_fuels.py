import json
import gps_fuels_open_parameters
import gps_fuels_open_expected_results
import gps_fuels_save_results
import testing_gps_fuels
import gps_parameters_save_results
import os


#OK_MSG='OK'
ERROR_MSG='FAIL'
#print(os.getcwd())
fGpsFuels=json.loads(open('./parameters_in_json/gps_fuels_parameters.json').read())
fGpsFuels_expected_results=json.loads(open('./parameters_in_json/gps_fuels_expected_results.json').read())

def test_event_fuels(dict_results,instance_unittest):
    test_checked='test_event_fuels'
    for case in fGpsFuels[test_checked].keys():
        data_provincias_filter=gps_fuels_open_parameters.open_parameters_test_event_fuels(fGpsFuels,case)
        boolean_event=testing_gps_fuels.function_to_test_event_fuels(data_provincias_filter)
        expected_boolean_event=gps_fuels_open_expected_results.open_expected_results_test_event_fuels(fGpsFuels_expected_results,case)
        gps_fuels_save_results.save_results_test_event_fuels(boolean_event,expected_boolean_event,case)
        try:
            instance_unittest.assertEqual(expected_boolean_event,boolean_event,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the position of the event is not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(boolean_event)+' \n\n'+'This is expected result:\n'+' '+str(expected_boolean_event))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results,case,ERROR_MSG,test_checked)
            raise AssertionError(error_message)

def test_setting_classFuels(dict_results,instance_unittest):
    test_checked='test_setting_classFuels'
    for case in fGpsFuels[test_checked].keys():
        data_provincia,provincia,horario,cp,latitud,longitud,localidad,margen,municipio,preciobiodiesel,preciobioetanol,preciogasnatural,preciogasoleoa,preciogasolina95,preciogasolina98,preciogasoleob,timeS,tipoventa=gps_fuels_open_parameters.open_parameters_test_setting_classFuels(fGpsFuels,case)
        boolean_event=testing_gps_fuels.function_to_test_setting_classFuels(data_provincia,provincia,horario,cp,latitud,longitud,localidad,margen,municipio,preciobiodiesel,preciobioetanol,preciogasnatural,preciogasoleoa,preciogasolina95,preciogasolina98,preciogasoleob,timeS,tipoventa)
        expected_boolean_event=gps_fuels_open_expected_results.open_expected_results_test_setting_classFuels(fGpsFuels_expected_results,case)
        gps_fuels_save_results.save_results_test_setting_classFuels(boolean_event,expected_boolean_event,case)
        try:
            instance_unittest.assertEqual(expected_boolean_event,boolean_event,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the position of the event is not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(boolean_event)+' \n\n'+'This is expected result:\n'+' '+str(expected_boolean_event))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results,case,ERROR_MSG,test_checked)
            raise AssertionError(error_message)

def test_save_csv_static_incidents(dict_results,instance_unittest):
    test_checked='test_save_csv_static_incidents'
    for case in fGpsFuels[test_checked].keys():
        dictionary_list=gps_fuels_open_parameters.open_parameters_test_save_csv_static_incidents(fGpsFuels,case)
        boolean_event=testing_gps_fuels.function_to_test_save_csv_static_incidents(dictionary_list,fGpsFuels, case)
        expected_boolean_event=gps_fuels_open_expected_results.open_expected_results_test_save_csv_static_incidents(fGpsFuels_expected_results,case)
        gps_fuels_save_results.save_results_test_save_csv_static_incidents(boolean_event,expected_boolean_event,case)
        try:
            instance_unittest.assertEqual(expected_boolean_event,boolean_event,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the position of the event is not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(boolean_event)+' \n\n'+'This is expected result:\n'+' '+str(expected_boolean_event))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results,case,ERROR_MSG,test_checked)
            raise AssertionError(error_message)

def test_save_csv_dinamic_incidents(dict_results,instance_unittest):
    test_checked='test_save_csv_dinamic_incidents'
    for case in fGpsFuels[test_checked].keys():
        index_incidents_provincia_start,index_incidents_provincia_end,array_distances_start,array_distances_end=gps_fuels_open_parameters.open_parameters_test_save_csv_dinamic_incidents(fGpsFuels,case)
        boolean_event=testing_gps_fuels.function_to_test_save_csv_dinamic_incidents(index_incidents_provincia_start,index_incidents_provincia_end,array_distances_start,array_distances_end,fGpsFuels, case)
        expected_boolean_event=gps_fuels_open_expected_results.open_expected_results_test_save_csv_dinamic_incidents(fGpsFuels_expected_results,case)
        gps_fuels_save_results.save_results_test_save_csv_dinamic_incidents(boolean_event,expected_boolean_event,case)
        try:
            instance_unittest.assertEqual(expected_boolean_event,boolean_event,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the position of the event is not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(boolean_event)+' \n\n'+'This is expected result:\n'+' '+str(expected_boolean_event))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results,case,ERROR_MSG,test_checked)
            raise AssertionError(error_message)