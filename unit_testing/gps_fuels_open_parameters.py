
def open_parameters_test_event_fuels(fGpsFuels, case):
    data_provincias_filter = fGpsFuels['test_event_fuels'][case]['data_provincias_filter']
    return data_provincias_filter


def open_parameters_test_setting_classFuels(fGpsFuels, case):
    data_provincia = fGpsFuels['test_setting_classFuels'][case]['data_provincia']
    provincia = fGpsFuels['test_setting_classFuels'][case]['provincia']
    horario = fGpsFuels['test_setting_classFuels'][case]['horario']
    cp = fGpsFuels['test_setting_classFuels'][case]['cp']
    latitud = fGpsFuels['test_setting_classFuels'][case]['latitud']
    longitud = fGpsFuels['test_setting_classFuels'][case]['longitud']
    localidad = fGpsFuels['test_setting_classFuels'][case]['localidad']
    margen = fGpsFuels['test_setting_classFuels'][case]['margen']
    municipio = fGpsFuels['test_setting_classFuels'][case]['municipio']
    preciobiodiesel = fGpsFuels['test_setting_classFuels'][case]['preciobiodiesel']
    preciobioetanol = fGpsFuels['test_setting_classFuels'][case]['preciobioetanol']
    preciogasnatural = fGpsFuels['test_setting_classFuels'][case]['preciogasnatural']
    preciogasoleoa = fGpsFuels['test_setting_classFuels'][case]['preciogasoleoa']
    preciogasolina95 = fGpsFuels['test_setting_classFuels'][case]['preciogasolina95']
    preciogasoleob = fGpsFuels['test_setting_classFuels'][case]['preciogasoleob']
    preciogasolina98 = fGpsFuels['test_setting_classFuels'][case]['preciogasolina98']
    timeS = fGpsFuels['test_setting_classFuels'][case]['timeS']
    tipoventa = fGpsFuels['test_setting_classFuels'][case]['tipoventa']
    return data_provincia, provincia, horario, cp, latitud, longitud, localidad, margen, municipio, preciobiodiesel, preciobioetanol, preciogasnatural, preciogasoleoa, preciogasolina95, preciogasolina98, preciogasoleob, timeS, tipoventa

def open_parameters_test_save_csv_static_incidents(fGpsFuels,case):
    dictionary_list = fGpsFuels['test_save_csv_static_incidents'][case]['dictionary_list']
    return dictionary_list

def open_parameters_test_save_csv_dinamic_incidents(fGpsFuels,case):
    index_incidents_provincia_start = fGpsFuels['test_save_csv_dinamic_incidents'][case]['index_incidents_provincia_start']
    index_incidents_provincia_end = fGpsFuels['test_save_csv_dinamic_incidents'][case]['index_incidents_provincia_end']
    array_distances_start = fGpsFuels['test_save_csv_dinamic_incidents'][case]['array_distances_start']
    array_distances_end = fGpsFuels['test_save_csv_dinamic_incidents'][case]['array_distances_end']
    return index_incidents_provincia_start,index_incidents_provincia_end,array_distances_start,array_distances_end