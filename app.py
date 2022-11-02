from requests_toolkit import exchange_rate_cn
import streamlit as st
import time

st.markdown("# 中国实时汇率")
with st.spinner():
    try:
        results = exchange_rate_cn()
    except:
        st.info('Connection Failed. Retry in 3 seconds...')
        time.sleep(3)
        st.experimental_rerun()
    st.dataframe(results)