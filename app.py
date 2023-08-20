import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Load and display the image
image = Image.open('eda.png')
st.image(image, use_column_width=True)

# Web App Title
st.markdown('''
This is the **EDA App** created in Streamlit using the **pandas-profiling** library.

by Evgeniia Komarova [LinkedIn](https://www.linkedin.com/in/evgeniia-komarova/) [GitHub](https://github.com/aussiekom)

---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])


# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
