import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.title('Hello World. This is a Title')
# Using st.write
st.write('This is can be used for text and other features.')

st.markdown("** You can select specific time duration **")
col1, col2 = st.columns(2)

with col1:
    st.write('Select the Initial Date')
    init_dt = st.date_input('Initial Date',min_value= datetime.date(2022,1,1),max_value=datetime.date(2022,12,31),value=datetime.date(2022,1,1))

with col2:
    st.write('Select the Final Date')
    final_dt = st.date_input('Final Date',min_value=datetime.date(2022,1,1),max_value=datetime.date(2022,12,31),value=datetime.datetime.now())
