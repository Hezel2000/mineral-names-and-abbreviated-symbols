import streamlit as st
import mag4 as mg
import matplotlib.pyplot as plt


st.title('Hello Katharina')

df = mg.get_data('Banda Arc')

el1 = st.selectbox('sel x', df.columns.tolist()[27:])
el2 = st.selectbox('sel y', df.columns.tolist()[27:])
fig, ax = plt.subplots()
ax.scatter(df[el1], df[el2])
st.pyplot(fig)


st.dataframe(mg.get_data('abminsym'))