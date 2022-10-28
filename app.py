import streamlit as st
from requests_toolkit import  AirQualityQuery

st.markdown('''# Country Air Quality Ranking''')
country =  st.text_input(
    label=' ',
    placeholder=' Which country do you want to query?',
    label_visibility = 'collapsed'
)

if country is not None and country != '':
    md_head = '''| ID | City |Province | US AQI |
| -------- | -------- | -------- | -------- |
'''
    md= st.empty()
    generator =  AirQualityQuery.air_quality_by_country(country,return_frequency=10)
    for i in generator:
        new_md = ''
        for id, j in enumerate(i):
            new_md += f'''|{id + 1}|{j[0]}|{j[1]}|{j[2]}|\n'''
        md.markdown(md_head + new_md)


