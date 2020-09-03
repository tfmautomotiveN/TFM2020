import json
import os
import matplotlib.pyplot as plt
import time

def save_results_test_return_position_event(position_event,expected_position_event,case):
    results = {
        case: {
            "expected_results": {
                "position_event": expected_position_event
            },

            "obtained_results": {
                "position_event": position_event
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_return_position_event.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()


def save_results_in_json(dict_results, amount):
    time_test = time.strftime("%c")
    results = {
        "Timestamp": time_test,
        "Tests fail": dict_results,
        "Number of the tests": amount
    }

    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/report_tests.json", "w")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_open_address(direcciones,expected_direcciones,data_provincias,expected_data_provincias,case):
    results = {
        case: {
            "expected_results": {
                "direcciones": expected_direcciones,
                "data_provincias":expected_data_provincias
            },

            "obtained_results": {
                "direcciones": direcciones,
                "data_provincias":data_provincias
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_open_address.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_open_data(longitud,expected_long,lat,expected_lat,heading,expected_heading,bool_event,expected_bool_event,case):
    results = {
        case: {
            "expected_results": {
                "longitud": expected_long,
                "lat":expected_lat,
                "heading":expected_heading,
                "bool_event":expected_bool_event
            },

            "obtained_results": {
                "longitud": longitud,
                "lat":lat,
                "heading": heading,
                "bool_event": bool_event
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_open_data.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()


def update_results(dict_results,case,message,test_checked):
    if dict_results.has_key(test_checked)==False:
        dict_results.update({test_checked:{}})
        dict_results[test_checked].update({case:message})
    else:
        dict_results[test_checked].update({case:message})