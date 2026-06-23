import streamlit as st

st.set_page_config( page_title="EpiStackXpress", initial_sidebar_state="expanded", layout="wide")
col1, col2, col3 = st.columns([1.5, 20, 2])

with col1:
    st.image("static/images/icarlogo.png", width=150)

with col2:
    st.markdown("<h1 style='text-align:center;'> EpiStackXpress: Epigenetic Stacking Ensemble for Gene eXpression</h1>", unsafe_allow_html=True)

with col3:
    st.image("static/images/iasri-logo.png", width=150)

st.markdown("---")
st.text("")

col1_1, col2_1, col3_1 = st.columns([1, 1, 1])

with col1_1:
    with st.container(border=True, height=160):
        st.markdown('''<div style='text-align:center'><b>Professor</b></br>  
                    Discipline of Bioinformatics, Graduate School  </br>
                    ICAR-Indian Agricultural Research Institute  </br>
                    Pusa, New Delhi-110012  </br>
                    Mail Id: sarika@icar.gov.in</div>''', unsafe_allow_html=True)

with col2_1:
     with st.container(border=True, height=160):
        st.markdown('''<div style='text-align:center'><h5>Director</h5>  
                    <p>ICAR-Indian Agricultural Statistics Research Institute  </br>
                    Pusa, New Delhi-110012  </br>
                    Mail Id: director.iasri@icar.gov.in</p></div>''', unsafe_allow_html=True)
        
with col3_1:
     with st.container(border=True, height=160):
        st.markdown('''<div style='text-align:center'><b>Head</b></br>  
                    Division of Agricultural Bioinformatics  </br>
                    ICAR-Indian Agricultural Research Institute  </br>
                    Pusa, New Delhi-110012  </br>
                    Mail Id: hd.cabin@iasri.res.in</div>''', unsafe_allow_html=True)

st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2026 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)