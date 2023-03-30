# streamlit_app.py
import streamlit as st
from shillelagh.backends.apsw.db import connect

# # Create a connection object.
# conn = connect(credentials=(service_account.Credentials.from_service_account_info(
#     st.secrets["gcp_service_account"],
#     scopes=[
#         "https://www.googleapis.com/auth/spreadsheets",
#     ],
# )))

# Perform SQL query on the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def run_query(query):
    cursor = __login_to_google__()
    sheet_url = st.secrets["private_gsheets_url"]
    query = query.replace('SHEET',f'''"{sheet_url}"''')
    dataset = cursor.execute(query)
    return dataset



def __login_to_google__():
    print("\n\n##########################\n\n")
    print("Login to Google API")

    connect_args = {
        "path": ":memory:",
        "adapters": "gsheetsapi",
        "adapter_kwargs": {
        "gsheetsapi": {
                           "service_account_info": {
                               **st.secrets["gcp_service_account"]
                           }
                       }
                   }
    }

    conn = connect(**connect_args)
    cursor = conn.cursor()
    print("Login done.")
    return cursor


#########################
#                       #
#   Store essay data    #
#                       #
#########################

def get_whole_dataset():
    query = f'SELECT * FROM SHEET'
    dataset = run_query(query)
    return dataset

rows = run_query(f'''SELECT * FROM SHEET''')


print(list(rows))
