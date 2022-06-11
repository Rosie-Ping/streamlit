import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.title('Hello World. Hello Git. Hello Branch')
# Text
st.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum.')
# Using st.write
st.write('This is can be used for text and other features.')

df = pd.read_csv('C:/Users/pingy/Documents/kaggle_data.csv')
df1 = df[['team_1','team_2','Winner_toss','Toss_descision','time','venue','target_achieved','Winner']]
table = df1.pivot_table(index=['Toss_descision','time'],columns=['venue'],aggfunc = 'count',fill_value=0)
st.dataframe(table)
st.dataframe(df1.head())

st.markdown("** You can select specific time duration **")
df_sliced = df

col1, col2 = st.columns(2)

with col1:
    st.write('Select the Initial Date')
    init_dt = st.date_input('Initial Date',min_value= datetime.date(2022,1,1),max_value=datetime.date(2022,12,31),value=datetime.date(2022,1,1))

with col2:
    st.write('Select the Final Date')
    final_dt = st.date_input('Final Date',min_value=datetime.date(2022,1,1),max_value=datetime.date(2022,12,31),value=datetime.datetime.now())

'''
if(init_dt != None or final_dt != None):
    if(init_dt < final_dt):
        df_sliced = df[init_dt:final_dt]
    else:
        st.warning("Entered the Date in Correct Order")
'''
