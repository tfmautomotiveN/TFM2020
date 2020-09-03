import json
import gps_classFuels_open_parameters
import gps_classFuels_open_expected_results
import gps_classFuels_save_results
import testing_gps_classFuels
import gps_parameters_save_results
import os


#OK_MSG='OK'
ERROR_MSG='FAIL'
#print(os.getcwd())
fGpsFuels=json.loads(open('./parameters_in_json/gps_classFuels_parameters.json').read())
fGpsFuels_expected_results=json.loads(open('./parameters_in_json/gps_classFuels_expected_results.json').read())

def test_get_horario(dict_results,instance_unittest):
    test_checked='test_get_horario'
    for case in fGpsFuels[test_checked].keys():
        horario_set=gps_classFuels_open_parameters.open_parameters_test_get_horario(fGpsFuels,case)
        horario=testing_gps_classFuels.function_to_test_get_horario(horario_set)
        expected_horario=gps_classFuels_open_expected_results.open_expected_results_test_get_horario(fGpsFuels_expected_results,case)
        gps_classFuels_save_results.save_results_test_get_horario(horario,expected_horario,case)
        try:
            instance_unittest.assertEqual(expected_horario,horario,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the position of the event is not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(horario)+' \n\n'+'This is expected result:\n'+' '+str(expected_horario))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results,case,ERROR_MSG,test_checked)
            raise AssertionError(error_message)

def test_set_horario(dict_results, instance_unittest):
    test_checked = 'test_set_horario'
    for case in fGpsFuels[test_checked].keys():
        horario = gps_classFuels_open_parameters.open_parameters_test_set_horario(fGpsFuels, case)
        horario_new = testing_gps_classFuels.function_to_test_set_horario(horario)
        expected_horario = gps_classFuels_open_expected_results.open_expected_results_test_set_horario(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_horario(horario_new, expected_horario,case)
        try:
            instance_unittest.assertEqual(expected_horario, horario_new,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(horario_new) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_horario))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_cp(dict_results, instance_unittest):
    test_checked = 'test_get_cp'
    for case in fGpsFuels[test_checked].keys():
        cp_i = gps_classFuels_open_parameters.open_parameters_test_get_cp(fGpsFuels, case)
        cp = testing_gps_classFuels.function_to_test_get_cp(cp_i)
        expected_cp = gps_classFuels_open_expected_results.open_expected_results_test_get_cp(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_cp(cp, expected_cp,case)
        try:
            instance_unittest.assertEqual(expected_cp, cp,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(cp) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_cp))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_cp(dict_results, instance_unittest):
    test_checked = 'test_set_cp'
    for case in fGpsFuels[test_checked].keys():
        cp_i = gps_classFuels_open_parameters.open_parameters_test_set_cp(fGpsFuels, case)
        cp = testing_gps_classFuels.function_to_test_set_cp(cp_i)
        expected_cp = gps_classFuels_open_expected_results.open_expected_results_test_set_cp(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_cp(cp, expected_cp,case)
        try:
            instance_unittest.assertEqual(expected_cp, cp,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(cp) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_cp))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_latitud(dict_results, instance_unittest):
    test_checked = 'test_get_latitud'
    for case in fGpsFuels[test_checked].keys():
        latitud_i = gps_classFuels_open_parameters.open_parameters_test_get_latitud(fGpsFuels, case)
        latitud = testing_gps_classFuels.function_to_test_get_latitud(latitud_i)
        expected_latitud = gps_classFuels_open_expected_results.open_expected_results_test_get_latitud(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_latitud(latitud, expected_latitud,case)
        try:
            instance_unittest.assertEqual(expected_latitud, latitud,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(latitud) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_latitud))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_latitud(dict_results, instance_unittest):
    test_checked = 'test_set_latitud'
    for case in fGpsFuels[test_checked].keys():
        latitud_i = gps_classFuels_open_parameters.open_parameters_test_set_latitud(fGpsFuels, case)
        latitud = testing_gps_classFuels.function_to_test_set_latitud(latitud_i)
        expected_latitud = gps_classFuels_open_expected_results.open_expected_results_test_set_latitud(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_latitud(latitud, expected_latitud,case)
        try:
            instance_unittest.assertEqual(expected_latitud, latitud,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(latitud) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_latitud))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_longitud(dict_results, instance_unittest):
    test_checked = 'test_get_longitud'
    for case in fGpsFuels[test_checked].keys():
        longitud_i = gps_classFuels_open_parameters.open_parameters_test_get_longitud(fGpsFuels, case)
        longitud = testing_gps_classFuels.function_to_test_get_longitud(longitud_i)
        expected_longitud = gps_classFuels_open_expected_results.open_expected_results_test_get_longitud(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_longitud(longitud, expected_longitud,case)
        try:
            instance_unittest.assertEqual(expected_longitud, longitud,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(longitud) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_longitud))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_longitud(dict_results, instance_unittest):
    test_checked = 'test_set_longitud'
    for case in fGpsFuels[test_checked].keys():
        longitud_i = gps_classFuels_open_parameters.open_parameters_test_set_longitud(fGpsFuels, case)
        longitud = testing_gps_classFuels.function_to_test_set_longitud(longitud_i)
        expected_longitud = gps_classFuels_open_expected_results.open_expected_results_test_set_longitud(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_longitud(longitud, expected_longitud,case)
        try:
            instance_unittest.assertEqual(expected_longitud, longitud,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(longitud) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_longitud))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_localidad(dict_results, instance_unittest):
    test_checked = 'test_get_localidad'
    for case in fGpsFuels[test_checked].keys():
        localidad_i = gps_classFuels_open_parameters.open_parameters_test_get_localidad(fGpsFuels, case)
        localidad = testing_gps_classFuels.function_to_test_get_localidad(localidad_i)
        expected_localidad = gps_classFuels_open_expected_results.open_expected_results_test_get_localidad(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_localidad(localidad, expected_localidad,case)
        try:
            instance_unittest.assertEqual(expected_localidad, localidad,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(localidad) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_localidad))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_localidad(dict_results, instance_unittest):
    test_checked = 'test_set_localidad'
    for case in fGpsFuels[test_checked].keys():
        localidad_i = gps_classFuels_open_parameters.open_parameters_test_set_localidad(fGpsFuels, case)
        localidad = testing_gps_classFuels.function_to_test_set_localidad(localidad_i)
        expected_localidad = gps_classFuels_open_expected_results.open_expected_results_test_set_localidad(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_localidad(localidad, expected_localidad,case)
        try:
            instance_unittest.assertEqual(expected_localidad, localidad,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(localidad) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_localidad))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_margen(dict_results, instance_unittest):
    test_checked = 'test_get_margen'
    for case in fGpsFuels[test_checked].keys():
        margen_i = gps_classFuels_open_parameters.open_parameters_test_get_margen(fGpsFuels, case)
        margen = testing_gps_classFuels.function_to_test_get_margen(margen_i)
        expected_margen = gps_classFuels_open_expected_results.open_expected_results_test_get_margen(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_margen(margen, expected_margen,case)
        try:
            instance_unittest.assertEqual(expected_margen, margen,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(margen) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_margen))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_margen(dict_results, instance_unittest):
    test_checked = 'test_set_margen'
    for case in fGpsFuels[test_checked].keys():
        margen_i = gps_classFuels_open_parameters.open_parameters_test_set_margen(fGpsFuels, case)
        margen = testing_gps_classFuels.function_to_test_set_margen(margen_i)
        expected_margen = gps_classFuels_open_expected_results.open_expected_results_test_set_margen(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_margen(margen, expected_margen,case)
        try:
            instance_unittest.assertEqual(expected_margen, margen,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(margen) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_margen))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_municipio(dict_results, instance_unittest):
    test_checked = 'test_get_municipio'
    for case in fGpsFuels[test_checked].keys():
        municipio_i = gps_classFuels_open_parameters.open_parameters_test_get_municipio(fGpsFuels, case)
        municipio = testing_gps_classFuels.function_to_test_get_municipio(municipio_i)
        expected_municipio = gps_classFuels_open_expected_results.open_expected_results_test_get_municipio(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_municipio(municipio, expected_municipio,case)
        try:
            instance_unittest.assertEqual(expected_municipio, municipio,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(municipio) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_municipio))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_municipio(dict_results, instance_unittest):
    test_checked = 'test_set_municipio'
    for case in fGpsFuels[test_checked].keys():
        municipio_i = gps_classFuels_open_parameters.open_parameters_test_set_municipio(fGpsFuels, case)
        municipio = testing_gps_classFuels.function_to_test_set_municipio(municipio_i)
        expected_municipio = gps_classFuels_open_expected_results.open_expected_results_test_set_municipio(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_municipio(municipio, expected_municipio,case)
        try:
            instance_unittest.assertEqual(expected_municipio, municipio,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(municipio) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_municipio))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_preciobiodiesel(dict_results, instance_unittest):
    test_checked = 'test_get_preciobiodiesel'
    for case in fGpsFuels[test_checked].keys():
        preciobiodiesel_i = gps_classFuels_open_parameters.open_parameters_test_get_preciobiodiesel(fGpsFuels, case)
        preciobiodiesel = testing_gps_classFuels.function_to_test_get_preciobiodiesel(preciobiodiesel_i)
        expected_preciobiodiesel = gps_classFuels_open_expected_results.open_expected_results_test_get_preciobiodiesel(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_preciobiodiesel(preciobiodiesel, expected_preciobiodiesel,case)
        try:
            instance_unittest.assertEqual(expected_preciobiodiesel, preciobiodiesel,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciobiodiesel) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciobiodiesel))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_preciobiodiesel(dict_results, instance_unittest):
    test_checked = 'test_set_preciobiodiesel'
    for case in fGpsFuels[test_checked].keys():
        preciobiodiesel_i = gps_classFuels_open_parameters.open_parameters_test_set_preciobiodiesel(fGpsFuels, case)
        preciobiodiesel = testing_gps_classFuels.function_to_test_set_preciobiodiesel(preciobiodiesel_i)
        expected_preciobiodiesel = gps_classFuels_open_expected_results.open_expected_results_test_set_preciobiodiesel(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_preciobiodiesel(preciobiodiesel, expected_preciobiodiesel,case)
        try:
            instance_unittest.assertEqual(expected_preciobiodiesel, preciobiodiesel,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciobiodiesel) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciobiodiesel))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_preciobioetanol(dict_results, instance_unittest):
    test_checked = 'test_get_preciobioetanol'
    for case in fGpsFuels[test_checked].keys():
        preciobioetanol_i = gps_classFuels_open_parameters.open_parameters_test_get_preciobioetanol(fGpsFuels, case)
        preciobioetanol = testing_gps_classFuels.function_to_test_get_preciobioetanol(preciobioetanol_i)
        expected_preciobioetanol = gps_classFuels_open_expected_results.open_expected_results_test_get_preciobioetanol(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_preciobioetanol(preciobioetanol, expected_preciobioetanol,case)
        try:
            instance_unittest.assertEqual(expected_preciobioetanol, preciobioetanol,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciobioetanol) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciobioetanol))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_preciobioetanol(dict_results, instance_unittest):
    test_checked = 'test_set_preciobioetanol'
    for case in fGpsFuels[test_checked].keys():
        preciobioetanol_i = gps_classFuels_open_parameters.open_parameters_test_set_preciobioetanol(fGpsFuels, case)
        preciobioetanol = testing_gps_classFuels.function_to_test_set_preciobioetanol(preciobioetanol_i)
        expected_preciobioetanol = gps_classFuels_open_expected_results.open_expected_results_test_set_preciobioetanol(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_preciobioetanol(preciobioetanol, expected_preciobioetanol,case)
        try:
            instance_unittest.assertEqual(expected_preciobioetanol, preciobioetanol,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciobioetanol) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciobioetanol))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_preciogasnatural(dict_results, instance_unittest):
    test_checked = 'test_get_preciogasnatural'
    for case in fGpsFuels[test_checked].keys():
        preciogasnatural_i = gps_classFuels_open_parameters.open_parameters_test_get_preciogasnatural(fGpsFuels, case)
        preciogasnatural = testing_gps_classFuels.function_to_test_get_preciogasnatural(preciogasnatural_i)
        expected_preciogasnatural = gps_classFuels_open_expected_results.open_expected_results_test_get_preciogasnatural(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_preciogasnatural(preciogasnatural, expected_preciogasnatural,case)
        try:
            instance_unittest.assertEqual(expected_preciogasnatural, preciogasnatural,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciogasnatural) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciogasnatural))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_preciogasnatural(dict_results, instance_unittest):
    test_checked = 'test_set_preciogasnatural'
    for case in fGpsFuels[test_checked].keys():
        preciogasnatural_i = gps_classFuels_open_parameters.open_parameters_test_set_preciogasnatural(fGpsFuels, case)
        preciogasnatural = testing_gps_classFuels.function_to_test_set_preciogasnatural(preciogasnatural_i)
        expected_preciogasnatural = gps_classFuels_open_expected_results.open_expected_results_test_set_preciogasnatural(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_preciogasnatural(preciogasnatural, expected_preciogasnatural,case)
        try:
            instance_unittest.assertEqual(expected_preciogasnatural, preciogasnatural,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciogasnatural) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciogasnatural))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_preciogasoleoa(dict_results, instance_unittest):
    test_checked = 'test_get_preciogasoleoa'
    for case in fGpsFuels[test_checked].keys():
        preciogasoleoa_i = gps_classFuels_open_parameters.open_parameters_test_get_preciogasoleoa(fGpsFuels, case)
        preciogasoleoa = testing_gps_classFuels.function_to_test_get_preciogasoleoa(preciogasoleoa_i)
        expected_preciogasoleoa = gps_classFuels_open_expected_results.open_expected_results_test_get_preciogasoleoa(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_preciogasoleoa(preciogasoleoa, expected_preciogasoleoa,case)
        try:
            instance_unittest.assertEqual(expected_preciogasoleoa, preciogasoleoa,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciogasoleoa) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciogasoleoa))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_preciogasoleoa(dict_results, instance_unittest):
    test_checked = 'test_set_preciogasoleoa'
    for case in fGpsFuels[test_checked].keys():
        preciogasoleoa_i = gps_classFuels_open_parameters.open_parameters_test_set_preciogasoleoa(fGpsFuels, case)
        preciogasoleoa = testing_gps_classFuels.function_to_test_set_preciogasoleoa(preciogasoleoa_i)
        expected_preciogasoleoa = gps_classFuels_open_expected_results.open_expected_results_test_set_preciogasoleoa(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_preciogasoleoa(preciogasoleoa, expected_preciogasoleoa,case)
        try:
            instance_unittest.assertEqual(expected_preciogasoleoa, preciogasoleoa,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciogasoleoa) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciogasoleoa))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_preciogasolina95(dict_results, instance_unittest):
    test_checked = 'test_get_preciogasolina95'
    for case in fGpsFuels[test_checked].keys():
        preciogasolina95_i = gps_classFuels_open_parameters.open_parameters_test_get_preciogasolina95(fGpsFuels, case)
        preciogasolina95 = testing_gps_classFuels.function_to_test_get_preciogasolina95(preciogasolina95_i)
        expected_preciogasolina95 = gps_classFuels_open_expected_results.open_expected_results_test_get_preciogasolina95(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_preciogasolina95(preciogasolina95, expected_preciogasolina95,case)
        try:
            instance_unittest.assertEqual(expected_preciogasolina95, preciogasolina95,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciogasolina95) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciogasolina95))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_preciogasolina95(dict_results, instance_unittest):
    test_checked = 'test_set_preciogasolina95'
    for case in fGpsFuels[test_checked].keys():
        preciogasolina95_i = gps_classFuels_open_parameters.open_parameters_test_set_preciogasolina95(fGpsFuels, case)
        preciogasolina95 = testing_gps_classFuels.function_to_test_set_preciogasolina95(preciogasolina95_i)
        expected_preciogasolina95 = gps_classFuels_open_expected_results.open_expected_results_test_set_preciogasolina95(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_preciogasolina95(preciogasolina95, expected_preciogasolina95,case)
        try:
            instance_unittest.assertEqual(expected_preciogasolina95, preciogasolina95,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciogasolina95) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciogasolina95))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_preciogasolina98(dict_results, instance_unittest):
    test_checked = 'test_get_preciogasolina98'
    for case in fGpsFuels[test_checked].keys():
        preciogasolina98_i = gps_classFuels_open_parameters.open_parameters_test_get_preciogasolina98(fGpsFuels, case)
        preciogasolina98 = testing_gps_classFuels.function_to_test_get_preciogasolina98(preciogasolina98_i)
        expected_preciogasolina98 = gps_classFuels_open_expected_results.open_expected_results_test_get_preciogasolina98(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_preciogasolina98(preciogasolina98, expected_preciogasolina98,case)
        try:
            instance_unittest.assertEqual(expected_preciogasolina98, preciogasolina98,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciogasolina98) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciogasolina98))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_preciogasolina98(dict_results, instance_unittest):
    test_checked = 'test_set_preciogasolina98'
    for case in fGpsFuels[test_checked].keys():
        preciogasolina98_i = gps_classFuels_open_parameters.open_parameters_test_set_preciogasolina98(fGpsFuels, case)
        preciogasolina98 = testing_gps_classFuels.function_to_test_set_preciogasolina98(preciogasolina98_i)
        expected_preciogasolina98 = gps_classFuels_open_expected_results.open_expected_results_test_set_preciogasolina98(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_preciogasolina98(preciogasolina98, expected_preciogasolina98,case)
        try:
            instance_unittest.assertEqual(expected_preciogasolina98, preciogasolina98,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciogasolina98) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciogasolina98))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_preciogasoleob(dict_results, instance_unittest):
    test_checked = 'test_get_preciogasoleob'
    for case in fGpsFuels[test_checked].keys():
        preciogasoleob_i = gps_classFuels_open_parameters.open_parameters_test_get_preciogasoleob(fGpsFuels, case)
        preciogasoleob = testing_gps_classFuels.function_to_test_get_preciogasoleob(preciogasoleob_i)
        expected_preciogasoleob = gps_classFuels_open_expected_results.open_expected_results_test_get_preciogasoleob(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_preciogasoleob(preciogasoleob, expected_preciogasoleob,case)
        try:
            instance_unittest.assertEqual(expected_preciogasoleob, preciogasoleob,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciogasoleob) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciogasoleob))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_preciogasoleob(dict_results, instance_unittest):
    test_checked = 'test_set_preciogasoleob'
    for case in fGpsFuels[test_checked].keys():
        preciogasoleob_i = gps_classFuels_open_parameters.open_parameters_test_set_preciogasoleob(fGpsFuels, case)
        preciogasoleob = testing_gps_classFuels.function_to_test_set_preciogasoleob(preciogasoleob_i)
        expected_preciogasoleob = gps_classFuels_open_expected_results.open_expected_results_test_set_preciogasoleob(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_preciogasoleob(preciogasoleob, expected_preciogasoleob,case)
        try:
            instance_unittest.assertEqual(expected_preciogasoleob, preciogasoleob,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(preciogasoleob) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_preciogasoleob))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_provincia(dict_results, instance_unittest):
    test_checked = 'test_get_provincia'
    for case in fGpsFuels[test_checked].keys():
        provincia_i = gps_classFuels_open_parameters.open_parameters_test_get_provincia(fGpsFuels, case)
        provincia = testing_gps_classFuels.function_to_test_get_provincia(provincia_i)
        expected_provincia = gps_classFuels_open_expected_results.open_expected_results_test_get_provincia(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_provincia(provincia, expected_provincia,case)
        try:
            instance_unittest.assertEqual(expected_provincia, provincia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(provincia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_provincia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_provincia(dict_results, instance_unittest):
    test_checked = 'test_set_provincia'
    for case in fGpsFuels[test_checked].keys():
        provincia_i = gps_classFuels_open_parameters.open_parameters_test_set_provincia(fGpsFuels, case)
        provincia = testing_gps_classFuels.function_to_test_set_provincia(provincia_i)
        expected_provincia = gps_classFuels_open_expected_results.open_expected_results_test_set_provincia(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_provincia(provincia, expected_provincia,case)
        try:
            instance_unittest.assertEqual(expected_provincia, provincia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(provincia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_provincia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_tipoventa(dict_results, instance_unittest):
    test_checked = 'test_get_tipoventa'
    for case in fGpsFuels[test_checked].keys():
        tipoventa_i = gps_classFuels_open_parameters.open_parameters_test_get_tipoventa(fGpsFuels, case)
        tipoventa = testing_gps_classFuels.function_to_test_get_tipoventa(tipoventa_i)
        expected_tipoventa = gps_classFuels_open_expected_results.open_expected_results_test_get_tipoventa(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_tipoventa(tipoventa, expected_tipoventa,case)
        try:
            instance_unittest.assertEqual(expected_tipoventa, tipoventa,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(tipoventa) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_tipoventa))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_tipoventa(dict_results, instance_unittest):
    test_checked = 'test_set_tipoventa'
    for case in fGpsFuels[test_checked].keys():
        tipoventa_i = gps_classFuels_open_parameters.open_parameters_test_set_tipoventa(fGpsFuels, case)
        tipoventa = testing_gps_classFuels.function_to_test_set_tipoventa(tipoventa_i)
        expected_tipoventa = gps_classFuels_open_expected_results.open_expected_results_test_set_tipoventa(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_tipoventa(tipoventa, expected_tipoventa,case)
        try:
            instance_unittest.assertEqual(expected_tipoventa, tipoventa,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(tipoventa) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_tipoventa))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_timeS(dict_results, instance_unittest):
    test_checked = 'test_get_timeS'
    for case in fGpsFuels[test_checked].keys():
        timeS_i = gps_classFuels_open_parameters.open_parameters_test_get_timeS(fGpsFuels, case)
        timeS = testing_gps_classFuels.function_to_test_get_timeS(timeS_i)
        expected_timeS = gps_classFuels_open_expected_results.open_expected_results_test_get_timeS(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_get_timeS(timeS, expected_timeS,case)
        try:
            instance_unittest.assertEqual(expected_timeS, timeS,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(timeS) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_timeS))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_timeS(dict_results, instance_unittest):
    test_checked = 'test_set_timeS'
    for case in fGpsFuels[test_checked].keys():
        timeS_i = gps_classFuels_open_parameters.open_parameters_test_set_timeS(fGpsFuels, case)
        timeS = testing_gps_classFuels.function_to_test_set_timeS(timeS_i)
        expected_timeS = gps_classFuels_open_expected_results.open_expected_results_test_set_timeS(fGpsFuels_expected_results, case)
        gps_classFuels_save_results.save_results_test_set_timeS(timeS, expected_timeS,case)
        try:
            instance_unittest.assertEqual(expected_timeS, timeS,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(timeS) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_timeS))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)
