import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[23.97565, 120.9738819], zoom=4)
        cities = "https://github.com/8048-kh/test/raw/refs/heads/main/Aboriginal%20Tribes.csv"
        regions = "https://github.com/8048-kh/GIS-files/raw/refs/heads/main/Polygon/county/%E8%A1%8C%E6%94%BF%E5%8D%80.shp"

        m.add_shp(regions, layer_name="Aboriginal Tribes")
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            #color_column="COUNTYNAME",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)

m.to_streamlit(height=700)
