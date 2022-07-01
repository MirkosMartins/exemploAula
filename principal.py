import streamlit as st

contador = 0

st.text('APLICAÇÃO CONTADOR')
st.input_text('Insira seu nome: ')
if st.button('Incrementar'):
    contador+=1
    st.text('contador'+str(contador))
if st.button('Decrementar'):
    contador-=1
    st.text('contador'+str(contador))