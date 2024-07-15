import streamlit as st  
from streamlit_option_menu import option_menu

#! https://icons.getbootstrap.com


# with st.sidebar:
#     selecao = option_menu(
#         menu_title='app',
#         options=['Inicio', 'Projetos', 'Contato']
#     )
    
    
selecao = option_menu(
        menu_title='app',
        options=['Inicio', 'Projetos', 'Contato'],
        icons=['house', 'book', 'envelope'],
        menu_icon='cast',
        orientation='horizontal'
    )
    
if selecao == 'Inicio':
    st.title(f'Você selecionou o menu {selecao}')

if selecao == 'Projetos':
    st.title(f'Você selecionou o menu {selecao}')
    
if selecao == 'Contato':
    st.title(f'Você selecionou o menu {selecao}')