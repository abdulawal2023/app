import os
path= os.getcwd()
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

date=datetime.now()

#st.title('SCIL Power data')
st.text('SCIL live data')
st.text(date)
os.chdir('//OS01//Energy_Report')
excel_file='EMS.xlsx'
sheet_name='Template'
df=pd.read_excel(excel_file,
                 sheet_name=sheet_name,
                 usecols='c:e',
                 header=2,
                 )

backgroundColor = "#F0F0F0"
st.backgroundColor = "#0FFFFF"
st.dataframe(
    df,
    hide_index=True,
    )
os.chdir('C:/Users/800xAService/Desktop')            
