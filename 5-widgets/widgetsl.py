# https://docs.streamlit.io/library/api-reference/widgets
import pandas as pd
import streamlit as st
import datetime
from io import StringIO


st.header('botão')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    
    

st.header('botão de download')
#https://docs.streamlit.io/library/api-reference/widgets/st.download_button


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

# Suponhamos que você tenha um DataFrame chamado large_df
# Aqui, usarei um exemplo fictício para demonstração
large_df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})

csv = convert_df(large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)


st.header('utilizando checkbox')

aceito = st.checkbox('eu aceito o termo de uso')

if aceito:
    st.write('Parabéns por ter lido os nossos termos')
else:
    st.write('Por favor, leia nossos termos de uso')
    


st.header('Utilizando radiobox')
#https://docs.streamlit.io/library/api-reference/widgets/st.radio

genero = st.radio(
    "Qual é o seu gênero de filme favorito? ",
    ('Comédia', 'Ficção', 'Terror'))

if genero == 'Comédia':
    st.write('Você selecionou gênero Comédia')
else:
    st.write("Você não gosta de comédia?")
    
    
    
st.header('Utilizando SelectBox')
opcao = st.selectbox(
    'Escolha a opção de contato?',
    ('Email', 'Whatsapp', 'Mobile phone'))

st.write('Você selecionou:', opcao)


st.header('Utilizando Multiselect')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)


st.header('Utilizando Select Slider')

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)


st.header(' Usando slider')
age = st.slider('quantos anos vc tem?', 0, 130, 18)
st.write("Eu tenho ", age, 'anos')


st.header('Usando Input Text')
title = st.text_input('Nome do filme:', 'Ex: Invocação do mal')
st.write('Seu filme Favorito é: ', title)


st.header('Usando Number Input')
number = st.number_input('Insert a number')
st.write('The current number is ', number)


st.header('Usando text área')
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Texto:', txt)

st.header('Usando date input')
d = st.date_input("que dia você faz aniversário? ", datetime.date(2023, 1, 1))
st.write('Seu aniversário é :', d)


st.header('Utilizando o time input')
t = st.time_input('Set an alarm for', datetime.time(10, 45))
st.write('Alarm is set for', t)

st.header('Usando o file upload')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
    
st.header('Usando a camera input')

foto = st.camera_input('Tirando Foto')

if foto:
    st.image(foto)
    
st.header('Usando color pick')
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)