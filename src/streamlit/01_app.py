import streamlit as st

# Objetos titulo, header y sub header
st.title('Hola :D! Soy Dashboard de prueba')
st.header('Este es un titulo')
st.subheader('Soy un subtitulo coqueto :D')

# Texto en Markdown https://www.markdownguide.org/getting-started/
# \n significa salto de linea
message = '''Soy un texto
que pueder dar informacion
en muchas lineas :D \n
holaaaa  \n
aprendedores!!
'''

st.markdown(message)