import streamlit as st
import numpy as np
import time



# Using object notation
st.header('<-- Usando sidebar')
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
    
    
    
st.header('Usando colunas')
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("cat.jpg")

with col2:
   st.header("A dog")
   st.image("dog.jpg")

with col3:
   st.header("An owl")
   st.image("owl.jpg")



st.header('Usando expander')
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")


st.header('Usando Container')
with st.container():
   st.write("Isso está dentro do contêiner")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("Isso está fora do contêiner")


st.header('Usando empty')
with st.empty():
    for seconds in range(60):
        st.write(f"⏳ {seconds} segundos se passaram")
        time.sleep(1)
    st.write("✔️ 1 minuto acabou!")
