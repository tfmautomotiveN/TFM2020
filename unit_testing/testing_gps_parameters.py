import json
import gps_parameters


def function_to_test_return_position_event(bool_event):
    position_event=gps_parameters.return_position_event(bool_event)
    return position_event

def function_to_test_open_address():
    direcciones, data_provincias = gps_parameters.open_address()
    return direcciones,data_provincias

def function_to_test_open_data():
    longitud, lat, heading, bool_event=gps_parameters.open_data()

    for i in range(len(longitud)):
        longitud[i]=round(longitud[i],2)
        lat[i]=round(lat[i],2)
        heading[i]=round(heading[i],2)

    return longitud,lat,heading,bool_event