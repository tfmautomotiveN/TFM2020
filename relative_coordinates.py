#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt



def convert_coordinates_global_to_relative(x_global,y_global,angle):
    # PLOT
    #conversion a radianes
    angle=np.deg2rad(angle)
    x=x_global[0:4000]
    y=y_global[0:4000]
    #figura buena
    #plt.plot(x, y, 'xr')
    #plt.savefig('trajectory_fig_glo.png', bbox_inches='tight')
    #plt.close()
    x_relative=[]
    y_relative=[]
    for i in range(len(x_global)):
        x_relative.append(np.cos(angle[i])*x_global[i] + np.sin(angle[i])*y_global[i])
        y_relative.append((-np.sin(angle[i])*x_global[i]) + np.cos(angle[i])*y_global[i])
    return x_relative,y_relative

def plot_events_static(x,y,position_event):
    # PLOT
    def get_labels(x):
        return x

    variables_legend = []
    names_legend = []
    cont_event = 0
    cont_no_event= 0

    for j in range(len(x)):
        if position_event[j] == 1:
            event_1, = plt.plot(x[j], y[j], 'xr')
            if cont_event == 0:
                cont_event = cont_event + 1
                variables_legend.append(event_1)
                names_legend.append('Evento en carretera')
        if position_event[j] == 0:
            event_2, = plt.plot(x[j],y[j], 'xg')
            if cont_no_event == 0:
                cont_no_event = cont_no_event + 1
                variables_legend.append(event_2)
                names_legend.append('No hay evento en carretera')

    plt.legend(variables_legend, names_legend, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
    plt.title('Trajectory EGO and event')
    plt.savefig('trajectory_with_lanes.png', bbox_inches='tight')
    plt.close()

def plot_trajectory_EGO(x_relative,y_relative):
    x=x_relative[0:4000]
    y=y_relative[0:4000]
    #print(len(x))
    #PLOT
    plt.plot(x_relative,y_relative,'xr')
    plt.savefig('trajectory_fig.png', bbox_inches='tight')
    plt.plot(x, y, 'xr')
    plt.savefig('trajectory_fig_menosPoints.png', bbox_inches='tight')
    plt.close()
    #plt.show()
