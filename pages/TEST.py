import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("Aboriginal Tribes")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[23.97565, 120.9738819], zoom=4)
        cities = "https://github.com/8048-kh/test/raw/refs/heads/main/Aboriginal%20Tribes%20area.csv"
        regions = "https://github.com/8048-kh/test/raw/refs/heads/main/REGION.shp"

        m.add_shp(regions, layer_name="Aboriginal Tribes")
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column="region",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
