import time  

import plotly.express as px  
import streamlit as st  

st.set_page_config(
    page_title="Streamlit Live Counter",
    layout="wide",
)

st.title("Streamlit Live Counter")

placeholder = st.empty()

for seconds in range(200):
    with placeholder.container():

        st.metric(
            label="Count ⏳",
            value=seconds,
            delta=seconds - 5,
        )
          
        time.sleep(0.5)