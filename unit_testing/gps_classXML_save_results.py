import json
import os
import matplotlib.pyplot as plt
import time

def save_results_test_get_tipo(tipo,expected_tipo,case):
    results = {
        case: {
            "expected_results": {
                "tipo": expected_tipo
            },

            "obtained_results": {
                "tipo": tipo
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_tipo.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_tipo(tipo,expected_tipo,case):
    results = {
        case: {
            "expected_results": {
                "tipo": expected_tipo
            },

            "obtained_results": {
                "tipo": tipo
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_tipo.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_autonomia(autonomia, expected_autonomia, case):
    results = {
        case: {
            "expected_results": {
                "autonomia": expected_autonomia
            },

            "obtained_results": {
                "autonomia": autonomia
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_autonomia.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_autonomia(autonomia, expected_autonomia, case):
    results = {
        case: {
            "expected_results": {
                "autonomia": expected_autonomia
            },

            "obtained_results": {
                "autonomia": autonomia
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_autonomia.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_provincia(provincia,expected_provincia,case):
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

def save_results_test_get_matricula(matricula,expected_matricula,case):
    results = {
        case: {
            "expected_results": {
                "matricula": expected_matricula
            },

            "obtained_results": {
                "matricula": matricula
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_matricula.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()


def save_results_test_set_matricula(matricula, expected_matricula, case):
    results = {
        case: {
            "expected_results": {
                "matricula": expected_matricula
            },

            "obtained_results": {
                "matricula": matricula
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_matricula.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_causa(causa,expected_causa,case):
    results = {
        case: {
            "expected_results": {
                "causa": expected_causa
            },

            "obtained_results": {
                "causa": causa
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_causa.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_causa(causa,expected_causa,case):
    results = {
        case: {
            "expected_results": {
                "causa": expected_causa
            },

            "obtained_results": {
                "causa": causa
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_causa.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_poblacion(poblacion,expected_poblacion,case):
    results = {
        case: {
            "expected_results": {
                "poblacion": expected_poblacion
            },

            "obtained_results": {
                "poblacion": poblacion
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_poblacion.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_poblacion(poblacion,expected_poblacion,case):
    results = {
        case: {
            "expected_results": {
                "poblacion": expected_poblacion
            },

            "obtained_results": {
                "poblacion": poblacion
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_poblacion.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_fechahoraini(fechahoraini,expected_fechahoraini,case):
    results = {
        case: {
            "expected_results": {
                "fechahoraini": expected_fechahoraini
            },

            "obtained_results": {
                "fechahoraini": fechahoraini
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_fechahoraini.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_fechahoraini(fechahoraini,expected_fechahoraini,case):
    results = {
        case: {
            "expected_results": {
                "fechahoraini": expected_fechahoraini
            },

            "obtained_results": {
                "fechahoraini": fechahoraini
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_fechahoraini.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_nivel(nivel,expected_nivel,case):
    results = {
        case: {
            "expected_results": {
                "nivel": expected_nivel
            },

            "obtained_results": {
                "nivel": nivel
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_nivel.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_nivel(nivel,expected_nivel,case):
    results = {
        case: {
            "expected_results": {
                "nivel": expected_nivel
            },

            "obtained_results": {
                "nivel": nivel
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_nivel.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_carretera(carretera,expected_carretera,case):
    results = {
        case: {
            "expected_results": {
                "carretera": expected_carretera
            },

            "obtained_results": {
                "carretera": carretera
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_carretera.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_carretera(carretera,expected_carretera,case):
    results = {
        case: {
            "expected_results": {
                "carretera": expected_carretera
            },

            "obtained_results": {
                "carretera": carretera
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_carretera.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_pkinicial(pkinicial,expected_pkinicial,case):
    results = {
        case: {
            "expected_results": {
                "pkinicial": expected_pkinicial
            },

            "obtained_results": {
                "pkinicial": pkinicial
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_pkinicial.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_pkinicial(pkinicial,expected_pkinicial,case):
    results = {
        case: {
            "expected_results": {
                "pkinicial": expected_pkinicial
            },

            "obtained_results": {
                "pkinicial": pkinicial
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_pkinicial.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_pkfinal(pkfinal,expected_pkfinal,case):
    results = {
        case: {
            "expected_results": {
                "pkfinal": expected_pkfinal
            },

            "obtained_results": {
                "pkfinal": pkfinal
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_pkfinal.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_pkfinal(pkfinal,expected_pkfinal,case):
    results = {
        case: {
            "expected_results": {
                "pkfinal": expected_pkfinal
            },

            "obtained_results": {
                "pkfinal": pkfinal
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_pkfinal.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_sentido(sentido,expected_sentido,case):
    results = {
        case: {
            "expected_results": {
                "sentido": expected_sentido
            },

            "obtained_results": {
                "sentido": sentido
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_sentido.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_sentido(sentido,expected_sentido,case):
    results = {
        case: {
            "expected_results": {
                "sentido": expected_sentido
            },

            "obtained_results": {
                "sentido": sentido
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_sentido.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_hacia(hacia,expected_hacia,case):
    results = {
        case: {
            "expected_results": {
                "hacia": expected_hacia
            },

            "obtained_results": {
                "hacia": hacia
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_hacia.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_hacia(hacia,expected_hacia,case):
    results = {
        case: {
            "expected_results": {
                "hacia": expected_hacia
            },

            "obtained_results": {
                "hacia": hacia
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_hacia.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_refincidencia(refincidencia,expected_refincidencia,case):
    results = {
        case: {
            "expected_results": {
                "refincidencia": expected_refincidencia
            },

            "obtained_results": {
                "refincidencia": refincidencia
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_refincidencia.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_refincidencia(refincidencia,expected_refincidencia,case):
    results = {
        case: {
            "expected_results": {
                "refincidencia": expected_refincidencia
            },

            "obtained_results": {
                "refincidencia": refincidencia
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_refincidencia.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_versionincidencia(versionincidencia,expected_versionincidencia,case):
    results = {
        case: {
            "expected_results": {
                "versionincidencia": expected_versionincidencia
            },

            "obtained_results": {
                "versionincidencia": versionincidencia
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_versionincidencia.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_versionincidencia(versionincidencia,expected_versionincidencia,case):
    results = {
        case: {
            "expected_results": {
                "versionincidencia": expected_versionincidencia
            },

            "obtained_results": {
                "versionincidencia": versionincidencia
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_versionincidencia.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_x(x,expected_x,case):
    results = {
        case: {
            "expected_results": {
                "x": expected_x
            },

            "obtained_results": {
                "x": x
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_x.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_x(x,expected_x,case):
    results = {
        case: {
            "expected_results": {
                "x": expected_x
            },

            "obtained_results": {
                "x": x
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_x.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_y(y,expected_y,case):
    results = {
        case: {
            "expected_results": {
                "y": expected_y
            },

            "obtained_results": {
                "x": y
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_y.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_y(y,expected_y,case):
    results = {
        case: {
            "expected_results": {
                "y": expected_y
            },

            "obtained_results": {
                "y": y
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_y.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_get_tipolocalizacion(tipolocalizacion,expected_tipolocalizacion,case):
    results = {
        case: {
            "expected_results": {
                "tipolocalizacion": expected_tipolocalizacion
            },

            "obtained_results": {
                "tipolocalizacion": tipolocalizacion
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_get_tipolocalizacion.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()

def save_results_test_set_tipolocalizacion(tipolocalizacion,expected_tipolocalizacion,case):
    results = {
        case: {
            "expected_results": {
                "tipolocalizacion": expected_tipolocalizacion
            },

            "obtained_results": {
                "tipolocalizacion": tipolocalizacion
            }
        }
    }
    if os.path.isdir('./output_tests') == False:
        os.mkdir('./output_tests')
    out_file = open("./output_tests/results_test_set_tipolocalizacion.json", "a")
    json.dump(results, out_file, indent=4)
    out_file.close()
