import streamlit as st 
import pandas as pd 
import numpy as np

st.header('usando dataframe')

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(df)


st.header('usando tabela')

df2 = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(df2)

st.header('utilizando metric')

st.metric(label='Temperature', value='70 °F', delta='1.2 °F')


st.header(' utilizando json')

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stu':[
        'stu1',
        'stu2',
        'stu3'
    ]
})