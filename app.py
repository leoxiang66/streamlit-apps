import streamlit as st
from requests_toolkit import  AirQualityQuery


st.markdown('''# Country Air Quality Ranking''')
with st.form(key='my form'):
    country = st.text_input(
        label='Country:',
        placeholder=' Which country do you want to query?',
        # label_visibility = 'collapsed'
    )

    # include_province = st.checkbox('search specific province')
    province = st.text_input(
        label='Province:',
        placeholder= f'''Which province do you want to query? Leave blank for all provinces''',
    )

    submit = st.form_submit_button('Search')

# print(dict(
#     country = country,
#     province = province,
# ))

if submit:
    st.markdown(f'''You entered: `{country}`, `{province}`''')

    if country != '':
        # all provinces
        if province == '':
            md_head = '''| ID | City |Province | US AQI |
| -------- | -------- | -------- | -------- |
'''
            md = st.empty()
            generator = AirQualityQuery.air_quality_by_country(country, return_frequency=10)
            while True:
                try:
                    with st.spinner():
                        i = next(generator)
                    new_md = ''
                    for id, j in enumerate(i):
                        new_md += f'''|{id + 1}|{j[0]}|{j[1]}|{j[2]}|\n'''
                    md.markdown(md_head + new_md)
                except StopIteration:
                    break
        # specific province
        else:
            md_head = '''| ID | City |Province | US AQI |
| -------- | -------- | -------- | -------- |
'''
            md = st.empty()
            i = AirQualityQuery.air_quality_by_province_country(country, province)
            new_md = ''
            for id, j in enumerate(i):
                new_md += f'''|{id + 1}|{j[0]}|{j[1]}|{j[2]}|\n'''
            md.markdown(md_head + new_md)




