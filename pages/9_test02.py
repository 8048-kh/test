import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        Tribes = "https://github.com/8048-kh/test/raw/refs/heads/main/Aboriginal%20Tribes.csv"
        #debris = "https://github.com/8048-kh/test/blob/main/debris.geojson"

        m.add_geojson(layer_name="Aboriginal Tribes")
        m.add_points_from_xy(
            Tribes,
            x="經度",
            y="緯度",
            color_column="部落傳統名制_羅馬拼音",
            #icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
