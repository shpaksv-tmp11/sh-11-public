import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
     np.random.randn(20, 1),
     columns=['normal distribution'])

st.line_chart(chart_data)
