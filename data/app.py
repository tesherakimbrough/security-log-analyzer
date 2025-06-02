import streamlit as st
import pandas as pd

st.title("Security Log Analyzer")

uploaded_file = st.file_uploader("Upload Log File (CSV)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
else:
    st.info("Please upload a CSV log file to get started.")

