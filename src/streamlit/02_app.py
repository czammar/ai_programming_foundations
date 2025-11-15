import pandas as pd
import streamlit as st
from numpy.random import default_rng

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

## Scatterplott
# Graficos usando pandas
# Creamos datos sintenticos con Pandas y Numpy
df = pd.DataFrame(
    default_rng(0).standard_normal((20, 3)),
    columns=["col1", "col2", "col3"]
)
df["col4"] = default_rng(0).choice(["a", "b", "c"], 20)
st.header('Aqui va mi grafico 1 :D')

st.scatter_chart(
    df,x="col1", y="col2", color="col4", size="col3"
    )

## line_chart
# Nuevamente Creamos datos sintenticos con Pandas y Numpy
st.header('Aqui va mi grafico 2 :D')
df_1 = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": default_rng(0).standard_normal(60),
        "col3": ["a"] * 20 + ["b"] * 20 + ["c"] * 20,
    }
)
st.line_chart(df_1, x="col1", y="col2", color="col3")

# Objetos de tipo metrica
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "25 °C", "1.2 °C")
col2.metric("Velocidad del Viento", "9 kph", "-8%")
col3.metric("Humedad", "86%", "4%")
