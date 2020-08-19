#!/usr/bin/python
# -*- coding: utf-8 -*-
import gps_parameters
import relative_coordinates
import gps_fuels
import gps_events_xml

x,y,heading,bool_event=gps_parameters.open_data()
position_event=[]
#position_x_event=[]
for i in range(len(bool_event)):
    if round(bool_event[i],0)==5.00:
        position_event.append(1)
    else:
        position_event.append(0)
print ("Lectura de parámetros GPS ok")
coor_x_rel,coor_y_rel=relative_coordinates.convert_coordinates_global_to_relative(x,y,heading)
#relative_coordinates.plot_trajectory_EGO(coor_x_rel,coor_y_rel)
#relative_coordinates.plot_events_static(x[10000:20000],y[10000:20000],position_event[10000:20000])
#print(coor_x_rel)
print("has llegado aqui")
gps_fuels.event_fuels()
gps_events_xml.read_events()
