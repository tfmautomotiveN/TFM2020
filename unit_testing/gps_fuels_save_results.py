import json
import os
import matplotlib.pyplot as plt
import time

def save_results_test_event_fuels(boolean_event,expected_boolean_event,case):
    results = {
        case: {
            "expected_results": {
                "boolean_event": expected_boolean_event
            },

            "obtained_results": {
                "boolean_event": boolean_event
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_event_fuels.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_setting_classFuels(boolean_event,expected_boolean_event,case):
    results = {
        case: {
            "expected_results": {
                "boolean_event": expected_boolean_event
            },

            "obtained_results": {
                "boolean_event": boolean_event
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_setting_classFuels.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_save_csv_static_incidents(boolean_event,expected_boolean_event,case):
    results = {
        case: {
            "expected_results": {
                "boolean_event": expected_boolean_event
            },

            "obtained_results": {
                "boolean_event": boolean_event
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_save_csv_static_incidents.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_save_csv_dinamic_incidents(boolean_event,expected_boolean_event,case):
    results = {
        case: {
            "expected_results": {
                "boolean_event": expected_boolean_event
            },

            "obtained_results": {
                "boolean_event": boolean_event
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_save_csv_dinamic_incidents.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

