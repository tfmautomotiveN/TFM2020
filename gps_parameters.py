#!/usr/bin/python
# -*- coding: utf-8 -*-
import utm
import csv, operator

def convert_latlong_to_utm(long,lat):
    x_utm=[]
    y_utm=[]
    for i in range(len(long)):
        coords = utm.from_latlon(long[i], lat[i])
        x_utm.append(coords[0])
        y_utm.append(coords[1])
    return x_utm,y_utm


def open_data():
    #Longitude --> x coord
    #Latitude --> y coord
    sats=[]
    time=[]
    lat=[]
    long=[]
    velocity=[]
    heading=[]
    '''
    height=[]
    vert_vel=[]
    Longacc=[]
    Latacc=[]
    glonass_sats=[]
    gps_sats=[]
    solution_type=[]
    vel_quality=[]
    event1=[]
    avifileindex=[]
    avitime=[]
    '''
    VB3i_AD2=[]
    '''
    latitude_raw=[]
    longitude_raw=[]
    speed_raw=[]
    heading_raw=[]
    height_raw=[]
    vertical_velocity_raw=[]
    m_Heading=[]
    m_Height=[]
    m_Latitude=[]
    m_Longitude=[]
    m_Satellites=[]
    m_Speed=[]
    m_UTC_time=[]
    m_Vertical_velocity=[]
    Speed=[]
    Time_Since_Midnight=[]
    dgps_status=[]
    Speed_Smoothed=[]
    '''
    with open('Racelogic_csv.csv') as csvarchivo:
        #entrada = csv.reader(csvarchivo)
        for row in csv.reader(csvarchivo, delimiter=';'):
            sats.append(row[0])
            time.append(row[1])
            lat.append(row[2])
            long.append(row[3])
            velocity.append(row[4])
            heading.append(row[5])
            '''height.append(row[6])
            vert_vel.append(row[7])
            Longacc.append(row[8])
            Latacc.append(row[9])
            glonass_sats.append(row[10])
            gps_sats.append(row[11])
            solution_type.append(row[12])
            vel_quality.append(row[13])
            event1.append(row[14])
            avifileindex.append(row[15])
            avitime.append(row[16])'''
            #este es el evento
            VB3i_AD2.append(row[17])
            '''latitude_raw.append(row[18])
            longitude_raw.append(row[19])
            speed_raw.append(row[20])
            heading_raw.append(row[21])
            height_raw.append(row[22])
            vertical_velocity_raw.append(row[23])
            m_Heading.append(row[24])
            m_Height.append(row[25])
            m_Latitude.append(row[26])
            m_Longitude.append(row[27])
            m_Satellites.append(row[28])
            m_Speed.append(row[29])
            m_UTC_time.append(row[30])
            m_Vertical_velocity.append(row[31])
            Speed.append(row[32])
            Time_Since_Midnight.append(row[33])
            dgps_status.append(row[34])
            Speed_Smoothed.append(row[35])'''

        sats=sats[3:len(sats)]
        sats = map(int, sats)
        lat=lat[3:len(lat)]
        lat=map(float,lat)
        lat = [x/60 for x in lat]
        long=long[3:len(long)]
        long=map(float,long)
        long = [x/60 for x in long]
        heading=heading[3:len(heading)]
        heading=map(float,heading)
        VB3i_AD2=VB3i_AD2[3:len(VB3i_AD2)]
        #el evento ahora hay que buscar los que
        #tengan el valor 5
        bool_event=map(float,VB3i_AD2)
        #for i in range(len(bool_event)):
            #if int(bool_event[i])!=2:
                #print("Soy el evento")
                #print(int(bool_event[i]))
        x_utm,y_utm=convert_latlong_to_utm(long,lat)
        return x_utm,y_utm,heading,bool_event