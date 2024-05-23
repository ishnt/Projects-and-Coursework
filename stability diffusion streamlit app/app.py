import streamlit as st
# Add a title to your app
st.title('My Streamlit App')

# Add some text
st.write('Welcome to my first Streamlit app!')

# Add a slider widget
age = st.slider('Select your age', 0, 100, 25)

# Display a chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate some example data
df = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

# Plot the data
fig, ax = plt.subplots()
ax.scatter(df['x'], df['y'])
st.pyplot(fig) 