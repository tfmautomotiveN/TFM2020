import json
import gps_classXML_open_parameters
import gps_classXML_open_expected_results
import gps_classXML_save_results
import testing_gps_classXML
import gps_parameters_save_results
import os


#OK_MSG='OK'
ERROR_MSG='FAIL'
#print(os.getcwd())
fGpsXML=json.loads(open('./parameters_in_json/gps_classXML_parameters.json').read())
fGpsXML_expected_results=json.loads(open('./parameters_in_json/gps_classXML_expected_results.json').read())

def test_get_tipo(dict_results,instance_unittest):
    test_checked='test_get_tipo'
    for case in fGpsXML[test_checked].keys():
        tipo_i=gps_classXML_open_parameters.open_parameters_test_get_tipo(fGpsXML,case)
        tipo=testing_gps_classXML.function_to_test_get_tipo(tipo_i)
        expected_tipo=gps_classXML_open_expected_results.open_expected_results_test_get_tipo(fGpsXML_expected_results,case)
        gps_classXML_save_results.save_results_test_get_tipo(tipo,expected_tipo,case)
        try:
            instance_unittest.assertEqual(expected_tipo,tipo,'\n\n'+test_checked+' '+ERROR_MSG+' '+'because the position of the event is not correct. \nTest case: '+(case)+'\n\nThis is the obtained result:\n'+' '+str(tipo)+' \n\n'+'This is expected result:\n'+' '+str(expected_tipo))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results,case,ERROR_MSG,test_checked)
            raise AssertionError(error_message)

def test_set_tipo(dict_results, instance_unittest):
    test_checked = 'test_set_tipo'
    for case in fGpsXML[test_checked].keys():
        tipo_i = gps_classXML_open_parameters.open_parameters_test_set_tipo(fGpsXML, case)
        tipo = testing_gps_classXML.function_to_test_set_tipo(tipo_i)
        expected_tipo = gps_classXML_open_expected_results.open_expected_results_test_set_tipo(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_tipo(tipo, expected_tipo,case)
        try:
            instance_unittest.assertEqual(expected_tipo, tipo,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(tipo) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_tipo))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_autonomia(dict_results, instance_unittest):
    test_checked = 'test_get_autonomia'
    for case in fGpsXML[test_checked].keys():
        autonomia_i = gps_classXML_open_parameters.open_parameters_test_get_autonomia(fGpsXML, case)
        autonomia = testing_gps_classXML.function_to_test_get_autonomia(autonomia_i)
        expected_autonomia = gps_classXML_open_expected_results.open_expected_results_test_get_autonomia(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_autonomia(autonomia, expected_autonomia,case)
        try:
            instance_unittest.assertEqual(expected_autonomia, autonomia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(autonomia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_autonomia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_autonomia(dict_results, instance_unittest):
    test_checked = 'test_set_autonomia'
    for case in fGpsXML[test_checked].keys():
        autonomia_i = gps_classXML_open_parameters.open_parameters_test_set_autonomia(fGpsXML, case)
        autonomia = testing_gps_classXML.function_to_test_set_autonomia(autonomia_i)
        expected_autonomia = gps_classXML_open_expected_results.open_expected_results_test_set_autonomia(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_autonomia(autonomia, expected_autonomia,case)
        try:
            instance_unittest.assertEqual(expected_autonomia, autonomia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(autonomia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_autonomia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_x(dict_results, instance_unittest):
    test_checked = 'test_get_x'
    for case in fGpsXML[test_checked].keys():
        x_i = gps_classXML_open_parameters.open_parameters_test_get_x(fGpsXML, case)
        x = testing_gps_classXML.function_to_test_get_x(x_i)
        expected_x = gps_classXML_open_expected_results.open_expected_results_test_get_x(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_x(x, expected_x,case)
        try:
            instance_unittest.assertEqual(expected_x, x,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(x) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_x))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_x(dict_results, instance_unittest):
    test_checked = 'test_set_x'
    for case in fGpsXML[test_checked].keys():
        x_i = gps_classXML_open_parameters.open_parameters_test_set_x(fGpsXML, case)
        x = testing_gps_classXML.function_to_test_set_x(x_i)
        expected_x= gps_classXML_open_expected_results.open_expected_results_test_set_x(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_x(x, expected_x,case)
        try:
            instance_unittest.assertEqual(expected_x, x,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(x) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_x))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_y(dict_results, instance_unittest):
    test_checked = 'test_get_y'
    for case in fGpsXML[test_checked].keys():
        y_i = gps_classXML_open_parameters.open_parameters_test_get_y(fGpsXML, case)
        y = testing_gps_classXML.function_to_test_get_y(y_i)
        expected_y = gps_classXML_open_expected_results.open_expected_results_test_get_y(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_y(y, expected_y,case)
        try:
            instance_unittest.assertEqual(expected_y, y,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(y) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_y))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_y(dict_results, instance_unittest):
    test_checked = 'test_set_y'
    for case in fGpsXML[test_checked].keys():
        y_i = gps_classXML_open_parameters.open_parameters_test_set_y(fGpsXML, case)
        y = testing_gps_classXML.function_to_test_set_y(y_i)
        expected_y = gps_classXML_open_expected_results.open_expected_results_test_set_y(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_y(y, expected_y,case)
        try:
            instance_unittest.assertEqual(expected_y, y,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(y) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_y))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_poblacion(dict_results, instance_unittest):
    test_checked = 'test_get_poblacion'
    for case in fGpsXML[test_checked].keys():
        poblacion_i = gps_classXML_open_parameters.open_parameters_test_get_poblacion(fGpsXML, case)
        poblacion = testing_gps_classXML.function_to_test_get_poblacion(poblacion_i)
        expected_poblacion = gps_classXML_open_expected_results.open_expected_results_test_get_poblacion(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_poblacion(poblacion, expected_poblacion,case)
        try:
            instance_unittest.assertEqual(expected_poblacion, poblacion,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(poblacion) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_poblacion))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_poblacion(dict_results, instance_unittest):
    test_checked = 'test_set_poblacion'
    for case in fGpsXML[test_checked].keys():
        poblacion_i = gps_classXML_open_parameters.open_parameters_test_set_poblacion(fGpsXML, case)
        poblacion = testing_gps_classXML.function_to_test_set_poblacion(poblacion_i)
        expected_poblacion = gps_classXML_open_expected_results.open_expected_results_test_set_poblacion(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_poblacion(poblacion, expected_poblacion,case)
        try:
            instance_unittest.assertEqual(expected_poblacion, poblacion,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(poblacion) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_poblacion))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_matricula(dict_results, instance_unittest):
    test_checked = 'test_get_matricula'
    for case in fGpsXML[test_checked].keys():
        matricula_i = gps_classXML_open_parameters.open_parameters_test_get_matricula(fGpsXML, case)
        matricula = testing_gps_classXML.function_to_test_get_matricula(matricula_i)
        expected_matricula = gps_classXML_open_expected_results.open_expected_results_test_get_matricula(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_matricula(matricula, expected_matricula,case)
        try:
            instance_unittest.assertEqual(expected_matricula, matricula,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(matricula) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_matricula))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_matricula(dict_results, instance_unittest):
    test_checked = 'test_set_matricula'
    for case in fGpsXML[test_checked].keys():
        matricula_i = gps_classXML_open_parameters.open_parameters_test_set_matricula(fGpsXML, case)
        matricula = testing_gps_classXML.function_to_test_set_matricula(matricula_i)
        expected_matricula = gps_classXML_open_expected_results.open_expected_results_test_set_matricula(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_matricula(matricula, expected_matricula,case)
        try:
            instance_unittest.assertEqual(expected_matricula, matricula,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(matricula) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_matricula))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_causa(dict_results, instance_unittest):
    test_checked = 'test_get_causa'
    for case in fGpsXML[test_checked].keys():
        causa_i = gps_classXML_open_parameters.open_parameters_test_get_causa(fGpsXML, case)
        causa = testing_gps_classXML.function_to_test_get_causa(causa_i)
        expected_causa = gps_classXML_open_expected_results.open_expected_results_test_get_causa(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_causa(causa, expected_causa,case)
        try:
            instance_unittest.assertEqual(expected_causa, causa,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(causa) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_causa))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_causa(dict_results, instance_unittest):
    test_checked = 'test_set_causa'
    for case in fGpsXML[test_checked].keys():
        causa_i = gps_classXML_open_parameters.open_parameters_test_set_causa(fGpsXML, case)
        causa = testing_gps_classXML.function_to_test_set_causa(causa_i)
        expected_causa = gps_classXML_open_expected_results.open_expected_results_test_set_causa(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_causa(causa, expected_causa,case)
        try:
            instance_unittest.assertEqual(expected_causa, causa,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(causa) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_causa))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_fechahoraini(dict_results, instance_unittest):
    test_checked = 'test_get_fechahoraini'
    for case in fGpsXML[test_checked].keys():
        fechahoraini_i = gps_classXML_open_parameters.open_parameters_test_get_fechahoraini(fGpsXML, case)
        fechahoraini = testing_gps_classXML.function_to_test_get_fechahoraini(fechahoraini_i)
        expected_fechahoraini = gps_classXML_open_expected_results.open_expected_results_test_get_fechahoraini(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_fechahoraini(fechahoraini, expected_fechahoraini,case)
        try:
            instance_unittest.assertEqual(expected_fechahoraini, fechahoraini,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(fechahoraini) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_fechahoraini))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_fechahoraini(dict_results, instance_unittest):
    test_checked = 'test_set_fechahoraini'
    for case in fGpsXML[test_checked].keys():
        fechahoraini_i = gps_classXML_open_parameters.open_parameters_test_set_fechahoraini(fGpsXML, case)
        fechahoraini = testing_gps_classXML.function_to_test_set_fechahoraini(fechahoraini_i)
        expected_fechahoraini = gps_classXML_open_expected_results.open_expected_results_test_set_fechahoraini(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_fechahoraini(fechahoraini, expected_fechahoraini,case)
        try:
            instance_unittest.assertEqual(expected_fechahoraini, fechahoraini,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(fechahoraini) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_fechahoraini))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_nivel(dict_results, instance_unittest):
    test_checked = 'test_get_nivel'
    for case in fGpsXML[test_checked].keys():
        nivel_i = gps_classXML_open_parameters.open_parameters_test_get_nivel(fGpsXML, case)
        nivel = testing_gps_classXML.function_to_test_get_nivel(nivel_i)
        expected_nivel = gps_classXML_open_expected_results.open_expected_results_test_get_nivel(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_nivel(nivel, expected_nivel,case)
        try:
            instance_unittest.assertEqual(expected_nivel, nivel,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(nivel) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_nivel))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_nivel(dict_results, instance_unittest):
    test_checked = 'test_set_nivel'
    for case in fGpsXML[test_checked].keys():
        nivel_i = gps_classXML_open_parameters.open_parameters_test_set_nivel(fGpsXML, case)
        nivel = testing_gps_classXML.function_to_test_set_nivel(nivel_i)
        expected_nivel = gps_classXML_open_expected_results.open_expected_results_test_set_nivel(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_nivel(nivel, expected_nivel,case)
        try:
            instance_unittest.assertEqual(expected_nivel, nivel,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(nivel) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_nivel))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_carretera(dict_results, instance_unittest):
    test_checked = 'test_get_carretera'
    for case in fGpsXML[test_checked].keys():
        carretera_i = gps_classXML_open_parameters.open_parameters_test_get_carretera(fGpsXML, case)
        carretera = testing_gps_classXML.function_to_test_get_carretera(carretera_i)
        expected_carretera = gps_classXML_open_expected_results.open_expected_results_test_get_carretera(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_carretera(carretera, expected_carretera,case)
        try:
            instance_unittest.assertEqual(expected_carretera, carretera,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(carretera) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_carretera))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_carretera(dict_results, instance_unittest):
    test_checked = 'test_set_carretera'
    for case in fGpsXML[test_checked].keys():
        carretera_i = gps_classXML_open_parameters.open_parameters_test_set_carretera(fGpsXML, case)
        carretera = testing_gps_classXML.function_to_test_set_carretera(carretera_i)
        expected_carretera = gps_classXML_open_expected_results.open_expected_results_test_set_carretera(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_carretera(carretera, expected_carretera,case)
        try:
            instance_unittest.assertEqual(expected_carretera, carretera,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(carretera) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_carretera))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_pkinicial(dict_results, instance_unittest):
    test_checked = 'test_get_pkinicial'
    for case in fGpsXML[test_checked].keys():
        pkinicial_i = gps_classXML_open_parameters.open_parameters_test_get_pkinicial(fGpsXML, case)
        pkinicial = testing_gps_classXML.function_to_test_get_pkinicial(pkinicial_i)
        expected_pkinicial = gps_classXML_open_expected_results.open_expected_results_test_get_pkinicial(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_pkinicial(pkinicial, expected_pkinicial,case)
        try:
            instance_unittest.assertEqual(expected_pkinicial, pkinicial,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(pkinicial) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_pkinicial))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_pkinicial(dict_results, instance_unittest):
    test_checked = 'test_set_pkinicial'
    for case in fGpsXML[test_checked].keys():
        pkinicial_i = gps_classXML_open_parameters.open_parameters_test_set_pkinicial(fGpsXML, case)
        pkinicial = testing_gps_classXML.function_to_test_set_pkinicial(pkinicial_i)
        expected_pkinicial = gps_classXML_open_expected_results.open_expected_results_test_set_pkinicial(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_pkinicial(pkinicial, expected_pkinicial,case)
        try:
            instance_unittest.assertEqual(expected_pkinicial, pkinicial,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(pkinicial) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_pkinicial))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_pkfinal(dict_results, instance_unittest):
    test_checked = 'test_get_pkfinal'
    for case in fGpsXML[test_checked].keys():
        pkfinal_i = gps_classXML_open_parameters.open_parameters_test_get_pkfinal(fGpsXML, case)
        pkfinal = testing_gps_classXML.function_to_test_get_pkfinal(pkfinal_i)
        expected_pkfinal = gps_classXML_open_expected_results.open_expected_results_test_get_pkfinal(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_pkfinal(pkfinal, expected_pkfinal,case)
        try:
            instance_unittest.assertEqual(expected_pkfinal, pkfinal,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(pkfinal) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_pkfinal))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_pkfinal(dict_results, instance_unittest):
    test_checked = 'test_set_pkfinal'
    for case in fGpsXML[test_checked].keys():
        pkfinal_i = gps_classXML_open_parameters.open_parameters_test_set_pkfinal(fGpsXML, case)
        pkfinal = testing_gps_classXML.function_to_test_set_pkfinal(pkfinal_i)
        expected_pkfinal = gps_classXML_open_expected_results.open_expected_results_test_set_pkfinal(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_pkfinal(pkfinal, expected_pkfinal,case)
        try:
            instance_unittest.assertEqual(expected_pkfinal, pkfinal,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(pkfinal) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_pkfinal))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_sentido(dict_results, instance_unittest):
    test_checked = 'test_get_sentido'
    for case in fGpsXML[test_checked].keys():
        sentido_i = gps_classXML_open_parameters.open_parameters_test_get_sentido(fGpsXML, case)
        sentido = testing_gps_classXML.function_to_test_get_sentido(sentido_i)
        expected_sentido = gps_classXML_open_expected_results.open_expected_results_test_get_sentido(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_sentido(sentido, expected_sentido,case)
        try:
            instance_unittest.assertEqual(expected_sentido, sentido,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(sentido) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_sentido))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_sentido(dict_results, instance_unittest):
    test_checked = 'test_set_sentido'
    for case in fGpsXML[test_checked].keys():
        sentido_i = gps_classXML_open_parameters.open_parameters_test_set_sentido(fGpsXML, case)
        sentido = testing_gps_classXML.function_to_test_set_sentido(sentido_i)
        expected_sentido = gps_classXML_open_expected_results.open_expected_results_test_set_sentido(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_sentido(sentido, expected_sentido,case)
        try:
            instance_unittest.assertEqual(expected_sentido, sentido,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(sentido) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_sentido))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_hacia(dict_results, instance_unittest):
    test_checked = 'test_get_hacia'
    for case in fGpsXML[test_checked].keys():
        hacia_i = gps_classXML_open_parameters.open_parameters_test_get_hacia(fGpsXML, case)
        hacia = testing_gps_classXML.function_to_test_get_hacia(hacia_i)
        expected_hacia = gps_classXML_open_expected_results.open_expected_results_test_get_hacia(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_hacia(hacia, expected_hacia,case)
        try:
            instance_unittest.assertEqual(expected_hacia, hacia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(hacia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_hacia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_hacia(dict_results, instance_unittest):
    test_checked = 'test_set_hacia'
    for case in fGpsXML[test_checked].keys():
        hacia_i = gps_classXML_open_parameters.open_parameters_test_set_hacia(fGpsXML, case)
        hacia = testing_gps_classXML.function_to_test_set_hacia(hacia_i)
        expected_hacia = gps_classXML_open_expected_results.open_expected_results_test_set_hacia(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_hacia(hacia, expected_hacia,case)
        try:
            instance_unittest.assertEqual(expected_hacia, hacia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(hacia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_hacia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_provincia(dict_results, instance_unittest):
    test_checked = 'test_get_provincia'
    for case in fGpsXML[test_checked].keys():
        provincia_i = gps_classXML_open_parameters.open_parameters_test_get_provincia(fGpsXML, case)
        provincia = testing_gps_classXML.function_to_test_get_provincia(provincia_i)
        expected_provincia = gps_classXML_open_expected_results.open_expected_results_test_get_provincia(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_provincia(provincia, expected_provincia,case)
        try:
            instance_unittest.assertEqual(expected_provincia, provincia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(provincia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_provincia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_provincia(dict_results, instance_unittest):
    test_checked = 'test_set_provincia'
    for case in fGpsXML[test_checked].keys():
        provincia_i = gps_classXML_open_parameters.open_parameters_test_set_provincia(fGpsXML, case)
        provincia = testing_gps_classXML.function_to_test_set_provincia(provincia_i)
        expected_provincia = gps_classXML_open_expected_results.open_expected_results_test_set_provincia(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_provincia(provincia, expected_provincia,case)
        try:
            instance_unittest.assertEqual(expected_provincia, provincia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(provincia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_provincia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_refincidencia(dict_results, instance_unittest):
    test_checked = 'test_get_refincidencia'
    for case in fGpsXML[test_checked].keys():
        refincidencia_i = gps_classXML_open_parameters.open_parameters_test_get_refincidencia(fGpsXML, case)
        refincidencia = testing_gps_classXML.function_to_test_get_refincidencia(refincidencia_i)
        expected_refincidencia = gps_classXML_open_expected_results.open_expected_results_test_get_refincidencia(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_refincidencia(refincidencia, expected_refincidencia,case)
        try:
            instance_unittest.assertEqual(expected_refincidencia, refincidencia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(refincidencia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_refincidencia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_refincidencia(dict_results, instance_unittest):
    test_checked = 'test_set_refincidencia'
    for case in fGpsXML[test_checked].keys():
        refincidencia_i = gps_classXML_open_parameters.open_parameters_test_set_refincidencia(fGpsXML, case)
        refincidencia = testing_gps_classXML.function_to_test_set_refincidencia(refincidencia_i)
        expected_refincidencia = gps_classXML_open_expected_results.open_expected_results_test_set_refincidencia(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_refincidencia(refincidencia, expected_refincidencia,case)
        try:
            instance_unittest.assertEqual(expected_refincidencia, refincidencia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(refincidencia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_refincidencia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_versionincidencia(dict_results, instance_unittest):
    test_checked = 'test_get_versionincidencia'
    for case in fGpsXML[test_checked].keys():
        versionincidencia_i = gps_classXML_open_parameters.open_parameters_test_get_versionincidencia(fGpsXML, case)
        versionincidencia = testing_gps_classXML.function_to_test_get_versionincidencia(versionincidencia_i)
        expected_versionincidencia = gps_classXML_open_expected_results.open_expected_results_test_get_versionincidencia(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_versionincidencia(versionincidencia, expected_versionincidencia,case)
        try:
            instance_unittest.assertEqual(expected_versionincidencia, versionincidencia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(versionincidencia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_versionincidencia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_versionincidencia(dict_results, instance_unittest):
    test_checked = 'test_set_versionincidencia'
    for case in fGpsXML[test_checked].keys():
        versionincidencia_i = gps_classXML_open_parameters.open_parameters_test_set_versionincidencia(fGpsXML, case)
        versionincidencia = testing_gps_classXML.function_to_test_set_versionincidencia(versionincidencia_i)
        expected_versionincidencia = gps_classXML_open_expected_results.open_expected_results_test_set_versionincidencia(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_versionincidencia(versionincidencia, expected_versionincidencia,case)
        try:
            instance_unittest.assertEqual(expected_versionincidencia, versionincidencia,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(versionincidencia) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_versionincidencia))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_get_tipolocalizacion(dict_results, instance_unittest):
    test_checked = 'test_get_tipolocalizacion'
    for case in fGpsXML[test_checked].keys():
        tipolocalizacion_i = gps_classXML_open_parameters.open_parameters_test_get_tipolocalizacion(fGpsXML, case)
        tipolocalizacion = testing_gps_classXML.function_to_test_get_tipolocalizacion(tipolocalizacion_i)
        expected_tipolocalizacion = gps_classXML_open_expected_results.open_expected_results_test_get_tipolocalizacion(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_get_tipolocalizacion(tipolocalizacion, expected_tipolocalizacion,case)
        try:
            instance_unittest.assertEqual(expected_tipolocalizacion, tipolocalizacion,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(tipolocalizacion) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_tipolocalizacion))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)

def test_set_tipolocalizacion(dict_results, instance_unittest):
    test_checked = 'test_set_tipolocalizacion'
    for case in fGpsXML[test_checked].keys():
        tipolocalizacion_i = gps_classXML_open_parameters.open_parameters_test_set_tipolocalizacion(fGpsXML, case)
        tipolocalizacion = testing_gps_classXML.function_to_test_set_tipolocalizacion(tipolocalizacion_i)
        expected_tipolocalizacion = gps_classXML_open_expected_results.open_expected_results_test_set_tipolocalizacion(fGpsXML_expected_results, case)
        gps_classXML_save_results.save_results_test_set_tipolocalizacion(tipolocalizacion, expected_tipolocalizacion,case)
        try:
            instance_unittest.assertEqual(expected_tipolocalizacion, tipolocalizacion,'\n\n' + test_checked + ' ' + ERROR_MSG + ' ' + 'because the position of the event is not correct. \nTest case: ' + (case) + '\n\nThis is the obtained result:\n' + ' ' + str(tipolocalizacion) + ' \n\n' + 'This is expected result:\n' + ' ' + str(expected_tipolocalizacion))
        except AssertionError as error_message:
            gps_parameters_save_results.update_results(dict_results, case, ERROR_MSG, test_checked)
            raise AssertionError(error_message)