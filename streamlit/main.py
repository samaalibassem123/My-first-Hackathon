import streamlit as st
import pandas as pd
import joblib

#get the model
model = joblib.load('model.joblib')


st.write('# Stock price prediction for China')
st.image('2024-08-02_dqevqgf3r0.webp')

#upload the file


date = st.date_input("Date :")
pch = st.number_input('Prix de petrole : ')
tch = st.number_input('Température : ')
co2ch = st.number_input('CO2CH exprimés en Millions : ')
chus = st.number_input('Chinese Yuan to US $ : ')
ich = st.number_input("Taux d'intérêt : ")

#split the date to year-month-day
date = str(date)
year = int(date[:date.find('-')])
date = date[date.find('-')+1:]
month = int(date[:date.find('-')])
day = int(date[date.find('-')+1:])



def clicked():

    if pch == 0 or tch == 0 or co2ch == 0 or chus == 0 or ich == 0:
        st.session_state['error'] = True
    else:
        st.session_state['error'] = False
        #create the dataframe
        columns = ['Prix de petrole', 'Température', 'Emission CO2',
            'Chinese Yuan to US $', "Taux d'intérêt", 'month',
            'year', 'day']
        print(pch, tch, co2ch,chus,ich, month, year, day)
        cdf = pd.DataFrame(data=[[pch, tch, co2ch,chus,ich, month, year, day]], columns=columns)
       
        #predict the result from the given inputs
        res = model.predict(cdf)
        st.session_state['res'] = res
    

st.button('predict', on_click=clicked)

#check if the button is clicked or not
if 'res' in st.session_state:
    res = st.session_state['res']
    st.write(res) 


#errors Handlers
if 'error' in st.session_state and st.session_state['error'] == True:
    st.warning('fileds are required')