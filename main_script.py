#!/usr/bin/python
# -*- coding: utf-8 -*-
import gps_parameters
import relative_coordinates
import gps_fuels
import gps_events_xml
import gps_classXML
import gps_classFuels

claXML_1 = gps_classXML.classXML()
claFuels_1 = gps_classFuels.classFuels()

x, y, heading, bool_event = gps_parameters.open_data()
address_to_events, data_provincias_filter = gps_parameters.open_address()
position_event = gps_parameters.return_position_event(bool_event)

'''print ("Lectura de parámetros GPS ok")'''

if address_to_events == []:
    coor_x_rel, coor_y_rel = relative_coordinates.convert_coordinates_global_to_relative(x, y, heading)
    relative_coordinates.plot_trajectory_EGO(coor_x_rel, coor_y_rel)
    relative_coordinates.plot_events_static(x[10000:20000], y[10000:20000], position_event[10000:20000])


if address_to_events == []:
    #gasolineras
    claFuels = gps_fuels.event_fuels(data_provincias_filter)
    claFuels_1 = claFuels
    longitud_fuels = claFuels_1.get_longitud()
    latitud_fuels = claFuels_1.get_latitud()
    if len(longitud_fuels) >= 5:
        dictionary_list = gps_events_xml.calculate_distances(x, y, longitud_fuels[0:4], latitud_fuels[0:4])
    else:
        dictionary_list = gps_events_xml.calculate_distances(x, y, longitud_fuels, latitud_fuels)
    gps_fuels.save_csv_static_incidents(claFuels_1, dictionary_list)
    #incidencias
    data_incidencia_x, data_incidencia_y, claXML = gps_events_xml.read_events(data_provincias_filter)
    claXML_1 = claXML
    dictionary_list = gps_events_xml.calculate_distances(x, y, data_incidencia_x, data_incidencia_y)
    gps_events_xml.save_csv_static_incidents(claXML_1, dictionary_list)

else:
    #gasolineras
    claFuels = gps_fuels.event_fuels(data_provincias_filter)
    claFuels_1 = claFuels
    x_longitudes, y_latitudes = gps_events_xml.get_latitude_longitude_from_Nominatum(address_to_events)
    index_incidents_provincia_start, index_incidents_provincia_end, array_distances_start, array_distances_end = gps_events_xml.calculate_distances_to_incidents(x_longitudes, y_latitudes, claFuels_1.get_longitud(), claFuels_1.get_latitud(), data_provincias_filter, claFuels_1)
    gps_fuels.save_csv_dinamic_incidents(index_incidents_provincia_start, index_incidents_provincia_end, array_distances_start, array_distances_end, claFuels_1)
    #incidencias
    data_incidencia_x, data_incidencia_y, claXML = gps_events_xml.read_events(data_provincias_filter)
    x_longitudes, y_latitudes = gps_events_xml.get_latitude_longitude_from_Nominatum(address_to_events)
    claXML_1 = claXML
    index_incidents_provincia_start, index_incidents_provincia_end, array_distances_start, array_distances_end = gps_events_xml.calculate_distances_to_incidents(x_longitudes, y_latitudes, data_incidencia_x, data_incidencia_y, data_provincias_filter, claXML_1)
    gps_events_xml.save_csv_dinamic_incidents(index_incidents_provincia_start, index_incidents_provincia_end, array_distances_start, array_distances_end, claXML)