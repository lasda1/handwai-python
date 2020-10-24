from math import sin, cos, sqrt, atan2, radians
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
TRIP_MORNING_START = datetime.strptime("05:00:00",  '%H:%M:%S').time()
TRIP_MORNING_END = datetime.strptime("11:59:00",  '%H:%M:%S').time()


def calcul_distance_between_two_points(pickup_lat,pickup_lon,dropOff_lat,dropOff_lon):
    R = 6373.0
    lat1 = radians(float(pickup_lat))
    lon1 = radians(float(pickup_lon))
    lat2 = radians(float(dropOff_lat))
    lon2 = radians(float(dropOff_lon))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance
def get_morning_dataframe(vendorId):
    df = pd.read_csv("./tours.csv")
    df["pickup_time"] = df["pickup_time"].apply(lambda x : datetime.strptime(x,  '%H:%M:%S').time())
    df["dropoff_time"] = df["dropoff_time"].apply(lambda x : datetime.strptime(x,  '%H:%M:%S').time())
    return df[(df["pickup_time"] > TRIP_MORNING_START) & (df["pickup_time"] < TRIP_MORNING_END) & (df["dropoff_time"] < TRIP_MORNING_END) & (df["dropoff_time"] > TRIP_MORNING_START) & (df["VendorID"] == int(vendorId))]



def get_morning_distance(df2):
    df2['distance'] = df2.apply(lambda x: calcul_distance_between_two_points(x.pickup_latitude, x.pickup_longitude, x.dropoff_latitude, x.dropoff_longitude), axis=1)
    return df2

def calculate_total_distance_morning(vendorId):
    df2 = get_morning_dataframe(vendorId)
    df2 = get_morning_distance(df2)
    return df2['distance'].sum()

def calculate_totals_amounts_morning(vendorId):
    df2 = get_morning_dataframe(vendorId)
    return df2['total_amount'].sum()

def get_statistic_for_vendor_distance_per_hour(vendor_id):
    df = get_morning_dataframe(vendor_id)
    df["hour"] = df['pickup_time'].apply(lambda x : x.hour)
    df = get_morning_distance(df)
    df.groupby("hour")["distance"].mean().plot(kind="bar")
    plt.savefig("./images/distance_"+vendor_id+".png")
    plt.close()

def get_statistic_for_vendor_fairs_per_hour(vendor_id):
    df = get_morning_dataframe(vendor_id)
    df["hour"] = df['pickup_time'].apply(lambda x : x.hour)
    df.groupby("hour")["total_amount"].mean().plot(kind="bar")
    plt.savefig("./images/fairs_"+ vendor_id+".png")
    plt.close()
