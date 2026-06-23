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

col1_1, col2_1 =st.columns([1, 1])

with col1_1:
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/Subham.jpg")
        with colInCon_2:
            st.markdown('''**Subham Ghosh**  
                        Ph.D. Scholar  
                        Discipline of Bioinformatics, The Graduate School  
                        ICAR-Indian Agricultural Research Institute  
                        Pusa, New Delhi-110012, India.  
                        Contact mail: search4aghosh@gmail.com''')
    
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/dipro.jpg")
        with colInCon_2:
            st.markdown('''**Dr. Dipro Sinha**  
                        Post Doctoral Fellow  
                        South Dakota State University  
                        1451 Stadium Rd, Brookings,   
                        SD 57007, USA.  
                        Contact mail: diprosinha@gmail.com''')
            
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/yeasin.jpg")
        with colInCon_2:
            st.markdown('''**Dr. Md Yeasin**  
                        Scientist  
                        Division of Statistical Genetics  
                        ICAR-Indian Agricultural Statistics Research Institute,  
                        Pusa, New Delhi-110012, India.  
                        Contact mail: yeasin.iasri@gmail.com''')
            
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/UBAngadi.jpg")
        with colInCon_2:
            st.markdown('''**Dr. U.B.Angadi**  
                        Principal Scientist  
                        Division of Agricultural Bioinformatics  
                        ICAR-Indian Agricultural Statistics Research Institute,  
                        Pusa, New Delhi-110012, India.  
                        Contact mail: angadiub@gmail.com''')

with col2_1:
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/Abhik_Sarkar.jpg")
        with colInCon_2:
            st.markdown('''  
                        **Abhik Sarkar**  
                        Ph.D. Scholar  
                        Discipline of Bioinformatics  
                        The Graduate School  
                        ICAR-Indian Agricultural Research Institute  
                        Pusa, New Delhi-110012, India.  
                        Contact mail: abhik.iasri@gmail.com''')
            
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/Sneha_murmu.png")
        with colInCon_2:
            st.markdown('''**Dr. Sneha Murmu**  
                        Scientist  
                        Division of Agricultural Bioinformatics  
                        ICAR-Indian Agricultural Statistics Research Institute  
                        Pusa, New Delhi-110012, India.  
                        Contact mail: murmu.sneha22@gmail.com''')
            
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/dcmishra.jpg")
        with colInCon_2:
            st.markdown('''**Dr. Dwijesh Chandra Mishra**  
                        Senior Scientist  
                        Division of Agricultural Bioinformatics  
                        ICAR-Indian Agricultural Statistics Research Institute  
                        Pusa, New Delhi-110012, India.  
                        Contact mail: dwij.mishra@gmail.com''')
            
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/Monendra_grover.jpeg")
        with colInCon_2:
            st.markdown('''**Dr. Monendra Grover**  
                        Principal Scientist  
                        Division of Agricultural Bioinformatics  
                        ICAR-Indian Agricultural Statistics Research Institute  
                        Pusa, New Delhi-110012, India.  
                        Contact mail: monendra.grover@icar.gov.in''')


st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2026 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)