import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Heatmap")
bus_stops = pd.read_csv("https://github.com/8048-kh/GIS-files/raw/refs/heads/main/CSV/Kaohsiung%20Bus%20Stop.csv")

for index, row in bus_stops.iterrows():
    township = row["TOWNNAME"]  # 將 "township" 替換為實際欄位名稱
    if township in bus_stop_counts:
        bus_stop_counts[township] += 1
    else:
        bus_stop_counts[township] = 1

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=[40, -100], zoom=4)
        m.add_heatmap(
            filepath,
            latitude="Lat",
            longitude="Lon",
            value="bus_stop_counts",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
