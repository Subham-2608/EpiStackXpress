import streamlit as st
import pandas as pd

st.set_page_config(page_title="EpiStackXpress", initial_sidebar_state="expanded", layout="wide")

col1, col2, col3 = st.columns([1.5, 20, 2])
with col1:
    st.image("static/images/icarlogo.png", width=150)
with col2:
    st.markdown("<h1 style='text-align:center;'>EpiStackXpress: Epigenetic Stacking Ensemble for Gene eXpression</h1>", unsafe_allow_html=True)
with col3:
    st.image("static/images/iasri-logo.png", width=150)

st.markdown("---")
st.text("")

# ── Sample CSV preview ────────────────────────────────────────────────────────
sample_df = pd.read_csv("static/data/sample.csv")

st.markdown("**Sample File Preview:**")
st.dataframe(sample_df, use_container_width=True)

st.text("")

with open("static/data/sample.csv", "rb") as f:
    st.download_button(
        label="Download Sample File",
        data=f,
        file_name="sample.csv",
        mime="text/csv",
        icon=":material/download:",
    )

st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2026 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)