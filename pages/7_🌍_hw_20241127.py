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

        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = "https://github.com/8048-kh/test/raw/refs/heads/main/Aboriginal%20Tribes.csv"
        regions = "https://github.com/8048-kh/test/blob/c86ae0b27d95b967c9adc8a9355a50075d70d037/county.geojson"

        m.add_geojson(regions, layer_name="county")
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column="County",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
