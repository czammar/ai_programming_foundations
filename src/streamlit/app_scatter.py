import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng


st.title('Dashboard de prueba')
st.header('Header text')
st.subheader('Sub-header text')


multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
df = pd.DataFrame(
    rng(0).standard_normal((20, 3)), columns=["col1", "col2", "col3"]
)
df["col4"] = rng(0).choice(["a", "b", "c"], 20)

st.scatter_chart(
    df,
    x="col1",
    y="col2",
    color="col4",
    size="col3",
)

st.subheader('Sub-header text')
df_1 = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": rng(0).standard_normal(60),
        "col3": ["a"] * 20 + ["b"] * 20 + ["c"] * 20,
    }
)
st.line_chart(df_1, x="col1", y="col2", color="col3")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")