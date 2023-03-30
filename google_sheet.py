# streamlit_app.py
import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
conn = connect(credentials=(service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)))

# Perform SQL query on the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def run_query(query):
    cursor = login_to_google()
    sheet_url = st.secrets["private_gsheets_url"]
    query = query.replace('SHEET',sheet_url)
    print(query)
    dataset = cursor.execute(query)
    return dataset



def login_to_google():
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

# def get_whole_dataset():
#     cursor = login_to_google()
#     query = f'SELECT * FROM "{APIs["essay_gsheets_url"]}"'
#     dataset = cursor.execute(query)
#     return dataset

# rows = run_query(f'''SELECT * FROM SHEET''')

# Print results.
# for row in rows:
#     st.write(f"{row.name} has a :{row.pet}:")

login_to_google()