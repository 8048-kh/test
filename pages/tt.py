import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("Aboriginal Tribes")



m = leafmap.Map(center=[23.97565, 120.9738819], zoom=4)
cities = "https://github.com/8048-kh/test/raw/refs/heads/main/Aboriginal%20Tribes%20area.csv"
cities_df = pd.read_csv(cities)
tribe_names = cities_df['部落名稱'].tolist()

# Create a selectbox for tribe names
        
selected_tribe = st.selectbox(
    "選擇部落",  # Label for the selectbox
    tribe_names,  # Options for the selectbox (tribe names)
    key="selectbox_tribe"  # Unique key for the selectbox
    )
selected_tribe_data = cities_df[cities_df['部落名稱'] == selected_tribe].iloc[0]
latitude = selected_tribe_data['latitude']
longitude = selected_tribe_data['longitude']

# Update map center
m.center = (latitude, longitude)  

# Display the updated map and selected tribe
m.to_streamlit(height=700)

# Display the selected tribe
st.write(f"您選擇的部落是：{selected_tribe}")
