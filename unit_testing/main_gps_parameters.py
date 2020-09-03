import json
import gps_parameters_open_parameters
import testing_gps_parameters
import gps_parameters_open_expected_results
import gps_parameters_save_results
import os


#OK_MSG='OK'
ERROR_MSG='FAIL'
#print(os.getcwd())
fGpsParam=json.loads(open('./parameters_in_json/gps_parameters_parameters.json').read())
fGpsParam_expected_results=json.loads(open('./parameters_in_json/gps_parameters_expected_results.json').read())

def test_return_position_event(dict_results,instance_unittest):
    test_checked='test_return_position_event'
    for case in fGpsParam[test_checked].keys():
        bool_event=gps_parameters_open_parameters.open_parameters_test_return_position_event(fGpsParam,case)
        position_event=testing_gps_parameters.function_to_test_return_position_event(bool_event)
        expected_position_event=gps_parameters_open_expected_results.open_expected_results_test_return_position_event(fGpsParam_expected_results,case)
        gps_parameters_save_results.save_results_test_return_position_event(position_event,expected_position_event,case)
        try:
            instance_unittest.assertEqual(expected_position_event,position_event,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the position of the event is not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(position_event)+' \n\n'+'This is expected result:\n'+' '+str(expected_position_event))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results,case,ERROR_MSG,test_checked)
            raise AssertionError(error_message)

def test_open_address(dict_results,instance_unittest):
    test_checked='test_open_address'
    for case in fGpsParam[test_checked].keys():
        #gps_parameters_open_parameters.open_parameters_test_open_address(fGpsParam,case)
        direcciones,data_provincias=testing_gps_parameters.function_to_test_open_address()
        expected_direcciones,expected_data_provincias=gps_parameters_open_expected_results.open_expected_results_test_open_address(fGpsParam_expected_results,case)
        gps_parameters_save_results.save_results_test_open_address(direcciones,expected_direcciones,data_provincias,expected_data_provincias,case)
        try:
            instance_unittest.assertEqual(expected_direcciones,direcciones,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the addresses are not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(direcciones)+' \n\n'+'This is expected result:\n'+' '+str(expected_direcciones))
            instance_unittest.assertEqual(expected_data_provincias, data_provincias,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the provincias are not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(data_provincias) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_data_provincias))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results,case,ERROR_MSG,test_checked)
            raise AssertionError(error_message)

def test_open_data(dict_results, instance_unittest):
    test_checked='test_open_data'
    for case in fGpsParam[test_checked].keys():
        #gps_parameters_open_parameters.open_parameters_test_open_address(fGpsParam,case)
        longitud,lat,heading,bool_event=testing_gps_parameters.function_to_test_open_data()
        expected_long,expected_lat, expected_heading,expected_bool_event=gps_parameters_open_expected_results.open_expected_results_test_open_data(fGpsParam_expected_results,case)
        gps_parameters_save_results.save_results_test_open_data(longitud,expected_long,lat,expected_lat,heading,expected_heading,bool_event,expected_bool_event,case)
        try:
            instance_unittest.assertEqual(expected_long,longitud,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the longitudes are not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(longitud)+' \n\n'+'This is expected result:\n'+' '+str(expected_long))
            instance_unittest.assertEqual(expected_lat, lat,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the latitudes are not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(lat) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_lat))
            instance_unittest.assertEqual(expected_heading,heading,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the heading are not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(heading)+' \n\n'+'This is expected result:\n'+' '+str(expected_heading))
            instance_unittest.assertEqual(expected_bool_event,bool_event,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the boolean of the events are not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(bool_event)+' \n\n'+'This is expected result:\n'+' '+str(expected_bool_event))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results,case,ERROR_MSG,test_checked)
            raise AssertionError(error_message)
