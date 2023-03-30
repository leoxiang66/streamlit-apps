import sthelper as sth
import streamlit as st

sth.widgets.build_TOC([])

def homepage():
    st.markdown("# Homepage")
    st.button('to test', on_click=lambda : session.go_to_page('test'))

def testpage():
    st.markdown("# Test page")



session = sth.OpenSession(dict(
    home = homepage,
    test = testpage
),
    current_page='home'
)

session.render()

print(session.get_current_page())


