import json
import os
import matplotlib.pyplot as plt
import time

def save_results_test_get_horario(horario,expected_horario,case):
    results = {
        case: {
            "expected_results": {
                "horario": expected_horario
            },

            "obtained_results": {
                "horario": horario
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_horario.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_horario(horario,expected_horario,case):
    results = {
        case: {
            "expected_results": {
                "horario": expected_horario
            },

            "obtained_results": {
                "horario": horario
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_horario.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_cp(cp, expected_cp, case):
    results = {
        case: {
            "expected_results": {
                "cp": expected_cp
            },

            "obtained_results": {
                "cp": cp
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_cp.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_cp(cp, expected_cp, case):
    results = {
        case: {
            "expected_results": {
                "cp": expected_cp
            },

            "obtained_results": {
                "cp": cp
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_cp.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_latitud(latitud, expected_latitud, case):
    results = {
        case: {
            "expected_results": {
                "latitud": expected_latitud
            },

            "obtained_results": {
                "latitud": latitud
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_latitud.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_latitud(latitud, expected_latitud, case):
    results = {
        case: {
            "expected_results": {
                "latitud": expected_latitud
            },

            "obtained_results": {
                "latitud": latitud
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_latitud.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_longitud(longitud, expected_longitud, case):
    results = {
        case: {
            "expected_results": {
                "longitud": expected_longitud
            },

            "obtained_results": {
                "longitud": longitud
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_longitud.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_longitud(longitud, expected_longitud, case):
    results = {
        case: {
            "expected_results": {
                "longitud": expected_longitud
            },

            "obtained_results": {
                "longitud": longitud
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_longitud.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_localidad(localidad, expected_localidad, case):
    results = {
        case: {
            "expected_results": {
                "localidad": expected_localidad
            },

            "obtained_results": {
                "localidad": localidad
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_localidad.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_localidad(localidad, expected_localidad, case):
    results = {
        case: {
            "expected_results": {
                "localidad": expected_localidad
            },

            "obtained_results": {
                "localidad": localidad
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_localidad.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_margen(margen, expected_margen, case):
    results = {
        case: {
            "expected_results": {
                "margen": expected_margen
            },

            "obtained_results": {
                "margen": margen
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_margen.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_margen(margen, expected_margen, case):
    results = {
        case: {
            "expected_results": {
                "margen": expected_margen
            },

            "obtained_results": {
                "margen": margen
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_margen.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_municipio(municipio, expected_municipio, case):
    results = {
        case: {
            "expected_results": {
                "municipio": expected_municipio
            },

            "obtained_results": {
                "municipio": municipio
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_municipio.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_municipio(municipio, expected_municipio, case):
    results = {
        case: {
            "expected_results": {
                "municipio": expected_municipio
            },

            "obtained_results": {
                "municipio": municipio
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_municipio.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_preciobiodiesel(preciobiodiesel, expected_preciobiodiesel, case):
    results = {
        case: {
            "expected_results": {
                "preciobiodiesel": expected_preciobiodiesel
            },

            "obtained_results": {
                "preciobiodiesel": preciobiodiesel
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_preciobiodiesel.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_preciobiodiesel(preciobiodiesel, expected_preciobiodiesel, case):
    results = {
        case: {
            "expected_results": {
                "preciobiodiesel": expected_preciobiodiesel
            },

            "obtained_results": {
                "preciobiodiesel": preciobiodiesel
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_preciobiodiesel.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_preciobioetanol(preciobioetanol, expected_preciobioetanol, case):
    results = {
        case: {
            "expected_results": {
                "preciobioetanol": expected_preciobioetanol
            },

            "obtained_results": {
                "preciobioetanol": preciobioetanol
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_preciobioetanol.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_preciobioetanol(preciobioetanol, expected_preciobioetanol, case):
    results = {
        case: {
            "expected_results": {
                "preciobioetanol": expected_preciobioetanol
            },

            "obtained_results": {
                "preciobioetanol": preciobioetanol
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_preciobioetanol.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_preciogasnatural(preciogasnatural, expected_preciogasnatural, case):
    results = {
        case: {
            "expected_results": {
                "preciogasnatural": expected_preciogasnatural
            },

            "obtained_results": {
                "preciogasnatural": preciogasnatural
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_preciogasnatural.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_preciogasnatural(preciogasnatural, expected_preciogasnatural, case):
    results = {
        case: {
            "expected_results": {
                "preciogasnatural": expected_preciogasnatural
            },

            "obtained_results": {
                "preciogasnatural": preciogasnatural
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_preciogasnatural.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_preciogasoleoa(preciogasoleoa, expected_preciogasoleoa, case):
    results = {
        case: {
            "expected_results": {
                "preciogasoleoa": expected_preciogasoleoa
            },

            "obtained_results": {
                "preciogasoleoa": preciogasoleoa
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_preciogasoleoa.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_preciogasoleoa(preciogasoleoa, expected_preciogasoleoa, case):
    results = {
        case: {
            "expected_results": {
                "preciogasoleoa": expected_preciogasoleoa
            },

            "obtained_results": {
                "preciogasoleoa": preciogasoleoa
             }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_preciogasoleoa.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_preciogasolina95(preciogasolina95, expected_preciogasolina95, case):
    results = {
        case: {
            "expected_results": {
                "preciogasolina95": expected_preciogasolina95
            },

            "obtained_results": {
                "preciogasolina95": preciogasolina95
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_preciogasolina95.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_preciogasolina95(preciogasolina95, expected_preciogasolina95, case):
    results = {
        case: {
            "expected_results": {
                "preciogasolina95": expected_preciogasolina95
            },

            "obtained_results": {
                "preciogasolina95": preciogasolina95
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_preciogasolina95.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_preciogasolina98(preciogasolina98, expected_preciogasolina98, case):
    results = {
        case: {
            "expected_results": {
                "preciogasolina98": expected_preciogasolina98
            },

            "obtained_results": {
                "preciogasolina98": preciogasolina98
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_preciogasolina98.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_preciogasolina98(preciogasolina98, expected_preciogasolina98, case):
    results = {
        case: {
            "expected_results": {
                "preciogasolina98": expected_preciogasolina98
            },

            "obtained_results": {
                "preciogasolina98": preciogasolina98
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_preciogasolina98.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_preciogasoleob(preciogasoleob, expected_preciogasoleob, case):
    results = {
        case: {
            "expected_results": {
                "preciogasoleob": expected_preciogasoleob
            },

            "obtained_results": {
                "preciogasoleob": preciogasoleob
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_preciogasoleob.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_preciogasoleob(preciogasoleob, expected_preciogasoleob, case):
    results = {
        case: {
            "expected_results": {
                "preciogasoleob": expected_preciogasoleob
            },

            "obtained_results": {
                "preciogasoleob": preciogasoleob
            }
         }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_preciogasoleob.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_provincia(provincia, expected_provincia, case):
    results = {
        case: {
            "expected_results": {
                "provincia": expected_provincia
            },

            "obtained_results": {
                "provincia": provincia
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_provincia.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_provincia(provincia, expected_provincia, case):
    results = {
        case: {
            "expected_results": {
                "provincia": expected_provincia
            },

            "obtained_results": {
                "provincia": provincia
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_provincia.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_tipoventa(tipoventa, expected_tipoventa, case):
    results = {
        case: {
            "expected_results": {
                "tipoventa": expected_tipoventa
               },

            "obtained_results": {
                "tipoventa": tipoventa
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_tipoventa.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_tipoventa(tipoventa, expected_tipoventa, case):
    results = {
        case: {
            "expected_results": {
                "tipoventa": expected_tipoventa
            },

            "obtained_results": {
                "tipoventa": tipoventa
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_tipoventa.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_timeS(timeS, expected_timeS, case):
    results = {
        case: {
            "expected_results": {
                "timeS": expected_timeS
            },

            "obtained_results": {
                "timeS": timeS
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_timeS.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_timeS(timeS, expected_timeS, case):
    results = {
        case: {
            "expected_results": {
                "timeS": expected_timeS
            },

            "obtained_results": {
                "timeS": timeS
             }
         }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_timeS.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()