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

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        lotus = "https://github.com/8048-kh/test/raw/refs/heads/main/Lotus.csv"
        m = leafmap.Map(center=[40, -100], zoom=4)
        m.add_heatmap(
            lotus,
            latitude="Y",
            longitude="X",
            value="Area",
            name="Heat map",
            radius=20,
        )
m.to_streamlit(height=700)
