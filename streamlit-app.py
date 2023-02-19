import streamlit as st


st.title('Golden Map')
st.write('''
    A map depicting Golden sightings in Barcelona!
''')

@st.cache_data()
def get_golden_map():
    HtmlFile = open("map.html", 'r', encoding='utf-8')
    bcn_map_html = HtmlFile.read()
    return bcn_map_html


bcn_map_html = get_golden_map()


import streamlit.components.v1 as components

with st.container():
    components.html(bcn_map_html,width=1000, height=1000)
