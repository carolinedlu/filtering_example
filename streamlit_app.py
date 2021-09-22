import streamlit as st
import pandas as pd

#define data
d = {'id': ['a', 'b', 'c'], 'data': [3, 4,6]}
df = pd.DataFrame(data=d)

#create sidebar input
with st.sidebar.form("my_form"):
    a = st.slider('sidebar for testing', 5, 10, 9)
    calculate = st.form_submit_button('Calculate') 
 

if calculate:
    df['result'] = df['data'] + a 
    st.write(df)
    #no issues up to this point. When I move the slider in 10 the output in 16 stays on the web page

    ########debug############
    # I am trying to select an 'id' from the dropdown and use that to filter df, but when I select a value from the dropdown, 
    # the script runs again and the output disappears
    
with st.sidebar.form("filter_form")
    filter = st.selectbox('filter data', df['id'].unique())
    filter = st.form_submit_button('Filter')
    
if filter
      st.write(df[df['id'] == filter])
