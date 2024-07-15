import streamlit as st
import time


st.header('Usando barra de progresso')
progress_text = "Operação em andamento. Por favor, aguarde."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)
    
    if percent_complete == 99:
        st.write('Download completo')
    
    
st.header('usando spinner')
with st.spinner('Espere por isso...'):
    time.sleep(5)
st.success('pronto!')


st.header('Usando o ballons')
st.balloons()


st.header('Usando o snowflake')
st.snow()

st.header('Usando mensagens de error, warning, info, sucess, exception')

st.error('This is an error', icon="🚨")
st.warning('This is a warning', icon="⚠️")
st.info('This is a purely informational message', icon="ℹ️")
st.success('This is a success message!', icon="✅")
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)