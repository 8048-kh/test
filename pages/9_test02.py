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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=[23.97565, 120.9738819], zoom=4)
        debris = "https://github.com/8048-kh/test/raw/refs/heads/main/debris1736_20240611_twd97_UTF8.shp"
        Route = "https://github.com/8048-kh/test/raw/refs/heads/main/Bus%20Route.shp"

        m.add_shp(Route, layer_name="Route")
        m.add_shp(debris, layer_name="debris")
        m.split_map(
            left_layer = debris,
            right_layer = Route 
        )
        m.add_legend(title="debris", builtin_legend="Route")

m.to_streamlit(height=700)

