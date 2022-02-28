import streamlit as st
import matplotlib.pylab as plt
import numpy as np

fig, ax = plt.subplots()
x1 = np.arange(0.00, 10*np.pi, 0.01)
x2 = np.arange(0.00, 10*np.pi, 0.1)
y1 = np.sin(x1) * np.exp(-x1 / (2*np.pi))
y2 = np.sin(x2)
y3 = np.sin(x1) * np.exp(-x1 / (10*np.pi))
ax.plot(x1, y1, 'b-', x2, y2, 'r.', x1, y3, 'k-',)

st.pyplot(fig)
