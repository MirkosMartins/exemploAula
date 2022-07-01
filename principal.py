import streamlit as st

contador = 0

st.text('APLICAÇÃO CONTADOR')
if st.button('Incrementar'):
    contador+=1
    st.text('contador'+str(contador))