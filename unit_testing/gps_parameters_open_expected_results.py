def open_expected_results_test_return_position_event(fGpsParam_expected_results,case):
    position_event_expected=fGpsParam_expected_results['test_return_position_event'][case]['position_event']
    return position_event_expected

def update_results(dict_results,case,message,test_checked):
    if dict_results.has_key(test_checked)==False:
        dict_results.update({test_checked:{}})
        dict_results[test_checked].update({case:message})
    else:
        dict_results[test_checked].update({case:message})

def open_expected_results_test_open_address(fGpsParam_expected_results,case):
    expected_direcciones=fGpsParam_expected_results['test_open_address'][case]['direcciones']
    expected_data_provincias = fGpsParam_expected_results['test_open_address'][case]['data_provincias']
    return expected_direcciones,expected_data_provincias

def open_expected_results_test_open_data(fGpsParam_expected_results,case):
    expected_long = fGpsParam_expected_results['test_open_data'][case]['long']
    expected_lat = fGpsParam_expected_results['test_open_data'][case]['lat']
    expected_heading = fGpsParam_expected_results['test_open_data'][case]['heading']
    expected_bool_event = fGpsParam_expected_results['test_open_data'][case]['bool_event']
    return expected_long,expected_lat, expected_heading,expected_bool_event