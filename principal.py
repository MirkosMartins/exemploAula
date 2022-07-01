import streamlit as st

contador = 0

st.text('APLICAÇÃO CONTADOR')
st.text_input('Insira seu nome: ',key='nome')
nome = st.session_state.nome
if st.button('Incrementar'):
    contador+=1
    st.text(nome+' contador'+str(contador))
if st.button('Decrementar'):
    contador-=1
    st.text(nome+' contador'+str(contador))