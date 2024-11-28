import os

import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="NYC Ridesharing Demo", page_icon=":taxi:")


# LOAD DATA ONCE
@st.cache_resource
def load_data():
    path = "kh mrt.csv.gz"
    if not os.path.isfile(path):
        path = f"https://github.com/8048-kh/GIS-files/raw/refs/heads/main/CSV/{path}"

    data = pd.read_csv(
        path,
        nrows=100000,  # approx. 10% of data
        names=[
            "Oct",
            "lat",
            "lon",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=[
            "date/time"
        ],  # set as datetime instead of converting after the fact
    )

    return data


# FUNCTION FOR AIRPORT MAPS
def map(data, lat, lon, zoom):
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )


# FILTER DATA FOR A SPECIFIC HOUR, CACHE

# CALCULATE MIDPOINT FOR GIVEN SET OF DATA
@st.cache_data
def mpoint(lat, lon):
    return (np.average(lat), np.average(lon))


# STREAMLIT APP LAYOUT
data = load_data()

# LAYING OUT THE TOP SECTION OF THE APP

# LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
row1 = st.columns()row2_1, row2_2, row2_3 = st.columns((2, 2, 2))
# SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
Kaohsiung_Main_Station = [22.638855, 120.302974]
Zuoying = [22.688219, 120.308271]
zoom_level = 12
midpoint = mpoint(data["lat"], data["lon"])

with row2_1:
    st.write(
        f"""**KH MRT**"""
    )
    map(filterdata(data, hour_selected), midpoint[0], midpoint[1], 11)

with row2_2:
    st.write("**Kaohsiung_Main_Station**")
    map(data, Kaohsiung_Main_Station[0], Kaohsiung_Main_Station[1], zoom_level)

with row2_3:
    st.write("**Zuoying**")
    map(data, Zuoying[0], Zuoying[1], zoom_level)



# CALCULATING DATA FOR THE HISTOGRAM
