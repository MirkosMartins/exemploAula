import streamlit as st
import pandas as pd

valor = pd.read_csv('./data.csv',sep=';')#lê o valor de um csv

contador = valor[0]

st.text('APLICAÇÃO CONTADOR')
st.text_input('Insira seu nome: ',key='nome')
nome = st.session_state.nome
if st.button('Incrementar'):
    contador+=1
if st.button('Decrementar'):
    contador-=1
st.text(nome+' contador'+str(contador))
df= pd.DataFrame([contador],columns=['valor'])
df.to_csv('./data.csv',sep=';')#salva o valor num csv