import streamlit as st
from pathlib import Path
from helper import *
import gzip, zlib


st.write("""
# Drug Resistance Checker
""")
uploaded_file = st.file_uploader("Choose a vcf file.", type=["vcf"])

#scheme = dr_scheme_parser('../dr_list.csv')
scheme = dr_scheme_parser('https://raw.githubusercontent.com/arupgsh/leprae_lineage_caller_test/main/dr_list.csv')
#https://raw.githubusercontent.com/arupgsh/leprae_lineage_caller_test/main/dr_list.csv

#parse byte code data from vcf
def bvcf_dict(fname,b_data)->dict:
    vd = {}
    var_l = set()
    v = b_data.decode('utf-8').splitlines() #gzip.open(b_data,'rt').readlines()
    for l in v:
        if l.startswith('#'):
            continue
        l = l.strip('\n').split('\t')
        alt = l[4].split(',')
        for al in alt:
            var_l.add(str(l[1])+'_'+l[3]+'_'+al)
    vd[fname] = var_l
    return vd

# Get the filename of the uploaded file
if uploaded_file is not None:
    fname = uploaded_file.name
    st.write("Filename:", fname)
    bytes_data = uploaded_file.getvalue()
    st.write(match_vars(bvcf_dict(fname, bytes_data), scheme))


# if uploaded_file is not None:
#     bytes_data = uploaded_file.getvalue()
#     data = uploaded_file.getvalue().decode('utf-8')


# if uploaded_file is not None:
#     bytes_data = uploaded_file.getvalue()
#     data = uploaded_file.getvalue().decode('utf-8').splitlines()         
#     st.session_state["preview"] = ''
#     for i in range(0, min(5, len(data))):
#         st.session_state["preview"] += data[i]


# preview = st.text_area("CSV Preview", "", height=150, key="preview")
# upload_state = st.text_area("Upload State", "", key="upload_state")
# def upload():
#     if uploaded_file is None:
#         st.session_state["upload_state"] = "Upload a file first!"
#     else:
#         data = uploaded_file.getvalue().decode('utf-8')
#         parent_path = pathlib.Path(__file__).parent.parent.resolve()           
#         save_path = os.path.join(parent_path, "data")
#         complete_name = os.path.join(save_path, uploaded_file.name)
#         destination_file = open(complete_name, "w")
#         destination_file.write(data)
#         destination_file.close()
#         st.session_state["upload_state"] = "Saved " + complete_name + " successfully!"
# st.button("Upload file to Sandbox", on_click=upload)