import streamlit as st


st.title('Isso é um título')


st.markdown('Isso é **divertido**')

st.header('isso é um cabeçalho')

st.subheader('isso é um sub cabeçãlho')

st.caption('isso esta pequeno')

st.code('streamlit run app.py')

st.text('Olá mundo')

st.latex(r'''
         a + ar + a r² + r³ + \cdots + a r^(n-1)
         ''')