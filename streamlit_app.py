import streamlit as st
import pandas as pd

#define data
d = {'id': ['a', 'b', 'c'], 'data': [3, 4,6]}
df = pd.DataFrame(data=d)

@st.cache(suppress_st_warning=True)
def run_calc():
    df['result'] = df['data'] + a 
    st.write(df)
    st.write("gets run")

#create sidebar input
with st.sidebar.form("my_form"):
    a = st.slider('sidebar for testing', 5, 10, 9)
    calculate = st.form_submit_button('Calculate') 

if calculate:
    run_calc()

    #no issues up to this point. When I move the slider in 10 the output in 16 stays on the web page

    ########debug############
    # I am trying to select an 'id' from the dropdown and use that to filter df, but when I select a value from the dropdown, 
    # the script runs again and the output disappears
    
filter = st.selectbox('filter data', df['id'].unique())
st.write(df[df['id'] == filter])
