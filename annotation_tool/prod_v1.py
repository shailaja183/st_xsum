#Author : ADISH007
from cmath import nan
import pandas as pd
import numpy as np
import streamlit as st
from math import ceil
from annotated_text import annotated_text
from streamlit_text_annotation import text_annotation

st.set_page_config(page_title='Annotation Tool', page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

lab = [ {"text": "Adjective"}, {"text": "CommonNoun"}, {"text": "Causal/Verb"},
{"text": "ExpertKnowledge"}, {"text": "Geographic"}, {"text": "Numeric"},
{"text": "Professional"}, {"text": "ProperNoun"}, {"text": "Temporal"} ]

dfd=pd.read_csv(r'https://raw.githubusercontent.com/helloadish007/prod_v1/main/demo0.csv')

st.markdown("""
<style>div[data-testid="stToolbar"] { display: none;}</style>
""", unsafe_allow_html=True)

st.header(' ANNOTATION TOOL ')
option = st.sidebar.selectbox(
    'Select the System :',
     ('BERTS2S', 'TConvS2S', 'Gold' , 'PtGen', 'TranS2S')
)


with st.sidebar.expander("Demo File"):
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(dfd)

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='demo_df.csv',
        mime='text/csv',
    )
    #st.sidebar.image("https://apaie2022.net/wp-content/uploads/2019/05/APAIE2020_header_bg_4.png")

uploaded_file = st.file_uploader("Upload File : ", type={"csv", "txt"})
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if "updated_df" not in st.session_state:
                st.session_state.updated_df = df

    row = st.session_state["updated_df"].loc[st.session_state["updated_df"]['system'] == option]
    df1= row['summary']

    page_size = 1
    page_number = st.number_input(
        label="Page Number",
        min_value=1,
        max_value=ceil(len(df1)/page_size),
        step=1,
    )
    st.write('Total Pages :',ceil(len(df1)/page_size))
    current_start = (page_number-1)*page_size
    current_end = page_number*page_size

    hsi=int(row[current_start:current_end].index[0])
    start=int(row['hallucinated_span_start'][hsi])-1
    end=int(row['hallucinated_span_end'][hsi])
    s=row['start'][hsi]
    h=row['hallucinated_span_new'][hsi]
    e=row['end'][hsi]
    hst=row['hallucinated_span'][hsi]
    tag=row['hallucination_type'][hsi]
    alp=df1[hsi]
    art = row['article'][hsi]

    st.write('**ARTICLE**')
    st.write(art)
    
    #st.write("##")
    st.write('**SUMMARY WITH HALLUCINATION ANNOTATION**')
    annotated_text(alp[:start],(alp[start:end],tag),alp[end:])

    st.write('**ANNOTATE SUMMARY BELOW**')
    if start >= 0 and end >= 0 :
        #print("0 ",alp)
        data2 = { "allowEditing": True, "tokens": [], "labels": lab }
        tok = []
        for i in alp.split(" "):
            tok.append({"text": i, "labels": []})
        data2["tokens"] = tok
        #print(data2)
        #print("***")
        data = text_annotation(data2)
        if data:
            "Annotations saved!"
        
    if st.button('Save changes to File'):
        st.session_state["updated_df"].loc[hsi,'hallucinated_span_new']=data
        st.experimental_rerun()
        
    else:
        st.caption('SUMMARY IS NOT ANNOTATED')

    agree = st.checkbox('Made Changes? Download the CSV file from here')

    if agree:
        @st.cache
        def convert_df(df):
            # Cache the conversion to prevent computation on every rerun
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df(st.session_state["updated_df"])

        st.download_button(
            label="DOWNLOAD CHANGES",
            data=csv,
            file_name='changes.csv',
            mime='text/csv',
        )

        st.info('Changes would be reflected in hallucinated_span_new column')
