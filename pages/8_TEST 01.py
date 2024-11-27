# -*- coding: utf-8 -*-
# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An example of showing geographic data."""

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
    path = "Kaohsiung%20Bus%20Stop.csv.gz"
    if not os.path.isfile(path):
        path = f"https://github.com/8048-kh/GIS-files/raw/refs/heads/main/CSV/{path}"
    
    data = pd.read_csv(
        path, # approx. 10% of data
        names=[
            "TOWNENG",
            "Lat",
            "Lon",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=[
            "TOWNENG"
        ],  # set as datetime instead of converting after the fact
    )

    return data


# FUNCTION FOR AIRPORT MAPS
def map(data, Lat, Lon, zoom):
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": Lat,
                "longitude": Lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["Lon", "Lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )

def CBS(df):
    """Calculates the number of bus stops per town."""
    return df.groupby("TOWNENG")["TOWNENG"].count().reset_index(name="bus_stop_count")

def mpoint(Lat, Lon):
    return (np.average(Lat), np.average(Lon))

data = load_data()

row2_1, row2_2, row2_3 = st.columns((2, 2, 2))

# SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
Gangshan = [22.792234, 120.299717]
Qishan = [22.883892, 120.484421]
zoom_level = 12
midpoint = mpoint(data["Lat"], data["Lon"])

with row2_1:
    st.write("**高雄市所有公車站**")  
    map(data, midpoint[0], midpoint[1], 11)


with row2_2:
    st.write("**Gangshan**")
    map(data, Gangshan[0], Gangshan[1], zoom_level)

with row2_3:
    st.write("**Qishan**")
    map(data, Qishan[0], Qishan[1], zoom_level)

chart_data = CBS(data)

st.write("**Bus Stop NUM**")

st.altair_chart(
    alt.Chart(chart_data)
    .mark_bar()
    .encode(
        x=alt.X("TOWNENG:N", title="區域"),
        y=alt.Y("BSC:Q", title="公車站數量"),
        tooltip=["TOWNENG", "bus_stop_count"],
    )
    .configure_mark(color="blue"),
    use_container_width=True,
)


