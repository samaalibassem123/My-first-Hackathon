import streamlit as st

st.write('# Predict Oil prices in china')


date = st.date_input("Date :")
pch = st.number_input('Indice des actions : ')
tch = st.number_input('Température : ')
co2ch = st.number_input('CO2CH exprimés en Millions : ')
chus = st.number_input('Chinese Yuan to US $ : ')
ich = st.number_input("Taux d'intérêt : ")

def clicked():
    print(date, pch)
    if date == '' or pch == 0 or tch == 0 or co2ch == 0 or ich == 0:
        st.warning('fileds are required')
        return
    st.session_state['res'] = 6

st.button('predict', on_click=clicked())

#check if the button is clicked or not
if 'res' in st.session_state:
    res = st.session_state['res']
    st.write(res) 