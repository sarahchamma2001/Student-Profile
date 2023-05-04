from hydralit import HydraHeadApp
from streamlit_option_menu import option_menu
import hydralit_components as hc
import streamlit as st
from st_clickable_images import clickable_images
import streamlit_modal as modal
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image
import numpy as np
import pyodbc
import math
import os.path
from PIL import Image

##############################
img = Image.open(r'''logo.png''')
st.set_page_config(
    page_title="OSB Graduate Program Profile",
    page_icon= img,
    layout="wide",
    initial_sidebar_state="expanded",
)
#st.set_page_config(layout="wide")

#####################################

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=OSB_Faculty_Database_F1.accdb')


#####################################
a1, a2 = st.columns((10, 25))
a1.image("AUB_Logo_OSB.png", width=230)
a2.title("Graduate Program Profile")
#####################################
# sidebar
#st.sidebar.title("Search By")
# st.sidebar.markdown("Select the desired year")
#user_options = st.sidebar.radio("Select Academic Year", options=[
                                #"2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "Advanced Option", "Dashboard"])
st.sidebar.title("Search By")
user_options = st.sidebar.selectbox("Select Academic Year", options=["Advanced Option","2023","2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013"])
#####################################
# Hydralit Navbar
if user_options == "2023" or user_options == "2021" or user_options == "2022":
    menu = option_menu(None, ["MSBA",  "MFIN", "MHRM", "MBA", "OMBA"], icons=["bar-chart-line", "calculator", "building", "clipboard-check", "search"],
                       menu_icon="cast", default_index=0, orientation="horizontal",
                       styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                               "icon": {"color": "black", "font-size": "25px"},
                               "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                               "nav-link-selected": {"background-color": "rgba(128, 0, 32, 0.8)"}, })
elif user_options == "2020" or user_options == "2019" or user_options == "2018":
        menu = option_menu(None, ["MSBA",  "MFIN", "MHRM", "MBA"], icons=["bar-chart-line", "calculator", "building", "clipboard-check"],
                       menu_icon="cast", default_index=0, orientation="horizontal",
                       styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                               "icon": {"color": "black", "font-size": "25px"},
                               "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                               "nav-link-selected": {"background-color": "rgba(128, 0, 32, 0.8)"}, })
elif user_options == "2017" or user_options == "2016" or user_options == "2015" or user_options == "2014" or user_options == "2013":
    menu = option_menu(None, ["MFIN", "MHRM", "MBA"], icons=["calculator", "building", "clipboard-check"],
                       menu_icon="cast", default_index=0, orientation="horizontal",
                       styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                               "icon": {"color": "black", "font-size": "25px"},
                               "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                               "nav-link-selected": {"background-color": "rgba(128, 0, 32, 0.8)"}, })
elif user_options == "Dashboard":
    menu = option_menu(None, ["Demographics",  "Analysis", "GPA"], icons=["search", "bar-chart-line", "clipboard-check"],
                       menu_icon="cast", default_index=0, orientation="horizontal",
                       styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                               "icon": {"color": "black", "font-size": "25px"},
                               "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                               "nav-link-selected": {"background-color": "rgba(128, 0, 32, 0.8)"}, })
#2023
cursor = conn.cursor()
cursor.execute('select * from Studentprofile')
df_main = pd.read_sql('select * from Studentprofile', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_search = pd.read_sql('select * from Studentprofile', conn)
df_search= df_search.drop_duplicates(subset="Id Number")
#####################################
df_search["Full Name"] = df_search["First Name"]+" "+df_search["Last Name"]
df_search = df_search.set_index("Full Name")

# df_search_2023=df_search[df_search["Yearofenrollment"]=="202310"]
# df_search_2023=df_search_2023.set_index("Full Name")
#####################################
df_2023 = df_main[df_main["Yearofenrollment"] == "202310"]
#####################################
df_2023_MSBA = df_2023[df_2023["student Type"] == "MSBA"]
df_2023_MSBA["Full Name"] = df_2023_MSBA["First Name"] +" "+df_2023_MSBA["Last Name"]
#####################################
df_2023_MFIN = df_2023[df_2023["student Type"] == "MF"]
df_2023_MFIN["Full Name"] = df_2023_MFIN["First Name"] +" "+df_2023_MFIN["Last Name"]
#####################################
df_2023_MHRM = df_2023[df_2023["student Type"] == "MHRM"]
df_2023_MHRM["Full Name"] = df_2023_MHRM["First Name"] +" "+df_2023_MHRM["Last Name"]
#####################################
df_2023_MSBA_FT = df_2023[df_2023["category"] == "FT"]
df_2023_MSBA_PT = df_2023[df_2023["category"] == "PT"]
#####################################
df_2023_MFIN_FT = df_2023_MFIN[df_2023_MFIN["category"] == "FT"]
df_2023_MFIN_PT = df_2023_MFIN[df_2023_MFIN["category"] == "PT"]
#####################################
df_2023_MHRM_FT = df_2023_MHRM[df_2023_MHRM["category"] == "FT"]
df_2023_MHRM_PT = df_2023_MHRM[df_2023_MHRM["category"] == "PT"]

df_2023_MSBA_FT["Full Name"] = df_2023_MSBA_FT["First Name"] +" "+df_2023_MSBA_FT["Last Name"]
df_2023_MSBA_PT["Full Name"] = df_2023_MSBA_PT["First Name"] +" "+df_2023_MSBA_PT["Last Name"]
#####################################
df_2023_MFIN_FT["Full Name"] = df_2023_MFIN_FT["First Name"] +" "+df_2023_MFIN_FT["Last Name"]
df_2023_MFIN_PT["Full Name"] = df_2023_MFIN_PT["First Name"] +" "+df_2023_MFIN_PT["Last Name"]
#####################################
df_2023_MHRM_FT["Full Name"] = df_2023_MHRM_FT["First Name"] + " "+df_2023_MHRM_FT["Last Name"]
df_2023_MHRM_PT["Full Name"] = df_2023_MHRM_PT["First Name"] +" "+df_2023_MHRM_PT["Last Name"]
#####################################
p = "missing.jpg"

# table 1
def table1(dataframe):
    l = math.ceil(len(dataframe)/3)
    x = 0

    for i in range(l):
        col1, col2, col3, = st.columns((1, 1, 1))

        with col1:
            if x < len(dataframe):
                if os.path.isfile(rf"MSBA _Photos_Folder\{dataframe.iloc[x,1]}.jpg"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x,1]}.jpg")
                    st.image(image, output_format="JPEG", width=165)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{dataframe.iloc[x,1]}.jpeg"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x,1]}.jpeg")
                    st.image(image, output_format="JPEG", width=165)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{dataframe.iloc[x,1]}.png"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x,1]}.png")
                    st.image(image, output_format="JPEG", width=165)
                elif os.path.isfile(rf"New folder\MSBA _Photos_Folder\{dataframe.iloc[x,1]}.jfif"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x,1]}.jfif")
                    st.image(image, output_format="JPEG", width=165)
                else:
                    backup = Image.open(rf"MSBA _Photos_Folder\{p}")
                    st.image(backup, output_format="JPEG", width=165)

                with st.expander(dataframe.iloc[x, 25]):
                    st.write(f"**ID:** {dataframe.iloc[x,1]}")
                    st.write(f"**Status:** {dataframe.iloc[x,18]}")
                    st.write(f"**E-mail:** {dataframe.iloc[x,6]}")
                    st.write(f"**LinkedIn:** {dataframe.iloc[x,24]}")
                    st.write(f"**Bio:** {dataframe.iloc[x,17]}")

        with col2:
            if x+1 < len(dataframe):
                if os.path.isfile(rf"MSBA _Photos_Folder\{dataframe.iloc[x+1,1]}.jpg"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x+1,1]}.jpg")
                    st.image(image, output_format="JPEG", width=165)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{dataframe.iloc[x+1,1]}.jpeg"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x+1,1]}.jpeg")
                    st.image(image, output_format="JPEG", width=165)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{dataframe.iloc[x+1,1]}.png"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x+1,1]}.png")
                    st.image(image, output_format="JPEG", width=165)
                elif os.path.isfile(rf"New folder\MSBA _Photos_Folder\{dataframe.iloc[x+1,1]}.jfif"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x+1,1]}.jfif")
                    st.image(image, output_format="JPEG", width=165)
                else:
                    backup = Image.open(rf"MSBA _Photos_Folder\{p}")
                    st.image(backup, output_format="JPEG", width=165)
  
                with st.expander(dataframe.iloc[x+1, 25]):
                    st.write(f"**ID:** {dataframe.iloc[x+1,1]}")
                    st.write(f"**Status:** {dataframe.iloc[x+1,18]}")
                    st.write(f"**E-mail:** {dataframe.iloc[x+1,6]}")
                    st.write(f"**LinkedIn:** {dataframe.iloc[x+1,24]}")
                    st.write(f"**Bio:** {dataframe.iloc[x+1,17]}")

        with col3:
            if x+2 < len(dataframe):
                if os.path.isfile(rf"MSBA _Photos_Folder\{dataframe.iloc[x+2,1]}.jpg"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x+2,1]}.jpg")
                    st.image(image, output_format="JPEG", width=165)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{dataframe.iloc[x+2,1]}.jpeg"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x+2,1]}.jpeg")
                    st.image(image, output_format="JPEG", width=165)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{dataframe.iloc[x+2,1]}.png"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x+2,1]}.png")
                    st.image(image, output_format="JPEG", width=165)
                elif os.path.isfile(rf"New folder\MSBA _Photos_Folder\{dataframe.iloc[x+2,1]}.jfif"):
                    image = Image.open(rf"MSBA _Photos_Folder\{dataframe.iloc[x+2,1]}.jfif")
                    st.image(image, output_format="JPEG", width=165)
                else:
                    backup = Image.open(rf"MSBA _Photos_Folder\{p}")
                    st.image(backup, output_format="JPEG", width=165)
                with st.expander(dataframe.iloc[x+2, 25]):
                    st.write(f"**ID:** {dataframe.iloc[x+2,1]}")
                    st.write(f"**Status:** {dataframe.iloc[x+2,18]}")
                    st.write(f"**E-mail:** {dataframe.iloc[x+2,6]}")
                    st.write(f"**LinkedIn:** {dataframe.iloc[x+2,24]}")
                    st.write(f"**Bio:** {dataframe.iloc[x+2,17]}")

        x = x+3
#2023 MBA & OMBA
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_s_23 = pd.read_sql('select * from Student', conn)
df_s_23= df_s_23.drop_duplicates(subset="Id Number")
df_ss_2023 = df_main[df_main["yearofadmission"].isin(["202310", "202320"])]
df_s_23["Full Name"] = df_s_23["First Name"] +" "+df_s_23["Last Name"]
df_s_23 = df_s_23.set_index("Full Name")

df_s_23 = df_s_23[df_s_23["yearofadmission"].isin(["202310", "202320"])]
#####################################
df_2023_MBA = df_ss_2023[df_ss_2023["student Type"] == "MBA"]
df_2023_MBA["Full Name"] = df_2023_MBA["First Name"] +" "+df_2023_MBA["Last Name"]
#####################################
df_2023_OMBA = df_ss_2023[df_ss_2023["student Type"] == "OMBA"]
df_2023_OMBA["Full Name"] = df_2023_OMBA["First Name"] +" "+df_2023_OMBA["Last Name"]
#####################################
df_2023_OMBA_FT = df_2023_OMBA[df_2023_OMBA["category"] == "FT"]
df_2023_OMBA_PT = df_2023_OMBA[df_2023_OMBA["category"] == "PT"]
#####################################
df_2023_MBA_FT = df_2023_MBA[df_2023_MBA["category"] == "FT"]
df_2023_MBA_PT = df_2023_MBA[df_2023_MBA["category"] == "PT"]
####################################
df_2023_MBA_FT["Full Name"] = df_2023_MBA_FT["First Name"] + " "+df_2023_MBA_FT["Last Name"]
df_2023_MBA_PT["Full Name"] = df_2023_MBA_PT["First Name"] +" "+df_2023_MBA_PT["Last Name"]
#####################################
df_2023_OMBA_FT["Full Name"] = df_2023_OMBA_FT["First Name"] + " "+df_2023_OMBA_FT["Last Name"]
df_2023_OMBA_PT["Full Name"] = df_2023_OMBA_PT["First Name"] +" "+df_2023_OMBA_PT["Last Name"]

#2022
# FT or PT 2022
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_search_22 = pd.read_sql('select * from Student', conn)
df_search_22= df_search_22.drop_duplicates(subset="Id Number")
df_2022 = df_main[df_main["yearofadmission"].isin(["202210", "202220"])]
df_search_22["Full Name"] = df_search_22["First Name"] +" "+df_search_22["Last Name"]
df_search_22 = df_search_22.set_index("Full Name")

df_search_2022 = df_search_22[df_search_22["yearofadmission"].isin(["202210", "202220"])]
#####################################
df_2022_MSBA = df_2022[df_2022["student Type"] == "MSBA"]
df_2022_MSBA["Full Name"] = df_2022_MSBA["First Name"] +" "+df_2022_MSBA["Last Name"]
#####################################
df_2022_MFIN = df_2022[df_2022["student Type"] == "MF"]
df_2022_MFIN["Full Name"] = df_2022_MFIN["First Name"] +" "+df_2022_MFIN["Last Name"]
#####################################
df_2022_MHRM = df_2022[df_2022["student Type"] == "MHRM"]
df_2022_MHRM["Full Name"] = df_2022_MHRM["First Name"] +" "+df_2022_MHRM["Last Name"]
#####################################
df_2022_MBA = df_2022[df_2022["student Type"] == "MBA"]
df_2022_MBA["Full Name"] = df_2022_MBA["First Name"] +" "+df_2022_MBA["Last Name"]
#####################################
df_2022_OMBA = df_2022[df_2022["student Type"] == "OMBA"]
df_2022_OMBA["Full Name"] = df_2022_OMBA["First Name"] +" "+df_2022_OMBA["Last Name"]

# FT or PT 2022
#####################################
df_2022_MSBA_FT = df_2022_MSBA[df_2022_MSBA["category"] == "FT"]
df_2022_MSBA_PT = df_2022_MSBA[df_2022_MSBA["category"] == "PT"]
#####################################
df_2022_MFIN_FT = df_2022_MFIN[df_2022_MFIN["category"] == "FT"]
df_2022_MFIN_PT = df_2022_MFIN[df_2022_MFIN["category"] == "PT"]
#####################################
df_2022_MBA_FT = df_2022_MBA[df_2022_MBA["category"] == "FT"]
df_2022_MBA_PT = df_2022_MBA[df_2022_MBA["category"] == "PT"]
#####################################
df_2022_MHRM_FT = df_2022_MHRM[df_2022_MHRM["category"] == "FT"]
df_2022_MHRM_PT = df_2022_MHRM[df_2022_MHRM["category"] == "PT"]
#####################################
df_2022_OMBA_FT = df_2022_OMBA[df_2022_OMBA["category"] == "FT"]
df_2022_OMBA_PT = df_2022_OMBA[df_2022_OMBA["category"] == "PT"]

df_2022_MSBA_FT["Full Name"] = df_2022_MSBA_FT["First Name"] + " "+df_2022_MSBA_FT["Last Name"]
df_2022_MSBA_PT["Full Name"] = df_2022_MSBA_PT["First Name"] +" "+df_2022_MSBA_PT["Last Name"]
#####################################
df_2022_MFIN_FT["Full Name"] = df_2022_MFIN_FT["First Name"] + " "+df_2022_MFIN_FT["Last Name"]
df_2022_MFIN_PT["Full Name"] = df_2022_MFIN_PT["First Name"] +" "+df_2022_MFIN_PT["Last Name"]
####################################
df_2022_MBA_FT["Full Name"] = df_2022_MBA_FT["First Name"] + " "+df_2022_MBA_FT["Last Name"]
df_2022_MBA_PT["Full Name"] = df_2022_MBA_PT["First Name"] +" "+df_2022_MBA_PT["Last Name"]
#####################################
df_2022_MHRM_FT["Full Name"] = df_2022_MHRM_FT["First Name"] +" "+df_2022_MHRM_FT["Last Name"]
df_2022_MHRM_PT["Full Name"] = df_2022_MHRM_PT["First Name"] +" "+df_2022_MHRM_PT["Last Name"]
#####################################
df_2022_OMBA_FT["Full Name"] = df_2022_OMBA_FT["First Name"] + " "+df_2022_OMBA_FT["Last Name"]
df_2022_OMBA_PT["Full Name"] = df_2022_OMBA_PT["First Name"] +" "+df_2022_OMBA_PT["Last Name"]
#####################################

def table2(dataframe):
    l = math.ceil(len(dataframe)/3)
    x = 0

    for i in range(l):
        col1, col2, col3, = st.columns((1, 1, 1))
        with col1:
            if x < len(dataframe):
                backup_path = rf"MSBA _Photos_Folder\{p}"
                if os.path.isfile(backup_path):
                    backup = Image.open(backup_path)
                    st.image(backup, output_format="JPEG", width=165)
                    with st.expander(dataframe.iloc[x, 55]):
                        st.write(f"**ID:** {dataframe.iloc[x,1]}")
                        st.write(f"**Status:** {dataframe.iloc[x,38]}")
                        st.write(f"**E-mail:** {dataframe.iloc[x,6]}")
                        st.write(f"**LinkedIn:** {dataframe.iloc[x,54]}")

        with col2:
            if x+1 < len(dataframe):
                backup_path = rf"MSBA _Photos_Folder\{p}"
                if os.path.isfile(backup_path):
                    backup = Image.open(backup_path)
                    st.image(backup, output_format="JPEG", width=165)
                    with st.expander(dataframe.iloc[x+1, 55]):
                        st.write(f"**ID:** {dataframe.iloc[x+1,1]}")
                        st.write(f"**Status:** {dataframe.iloc[x+1,38]}")
                        st.write(f"**E-mail:** {dataframe.iloc[x+1,6]}")
                        st.write(f"**LinkedIn:** {dataframe.iloc[x+1,54]}")
        with col3:
            if x+2 < len(dataframe):
                backup_path = rf"MSBA _Photos_Folder\{p}"
                if os.path.isfile(backup_path):
                    backup = Image.open(backup_path)
                    st.image(backup, output_format="JPEG", width=165)
                    with st.expander(dataframe.iloc[x+2, 55]):
                        st.write(f"**ID:** {dataframe.iloc[x+2,1]}")
                        st.write(f"**Status:** {dataframe.iloc[x+2,38]}")
                        st.write(f"**E-mail:** {dataframe.iloc[x+2,6]}")
                        st.write(f"**LinkedIn:** {dataframe.iloc[x+2,54]}")

        x = x+3
# 2018
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_search_18 = pd.read_sql('select * from Student', conn)
df_search_18= df_search_18.drop_duplicates(subset="Id Number")
df_2018 = df_main[df_main["yearofadmission"].isin(["201810", "201820"])]

df_search_18["Full Name"] = df_search_18["First Name"] +" "+df_search_18["Last Name"]
df_search_18 = df_search_18.set_index("Full Name")
df_search_2018 = df_search_18[df_search_18["yearofadmission"].isin(["201810", "201820"])]
#####################################
df_2018_MSBA = df_2018[df_2018["student Type"] == "MSBA"]
df_2018_MSBA["Full Name"] = df_2018_MSBA["First Name"] +" "+df_2018_MSBA["Last Name"]
#####################################
df_2018_MFIN = df_2018[df_2018["student Type"] == "MF"]
df_2018_MFIN["Full Name"] = df_2018_MFIN["First Name"] +" "+df_2018_MFIN["Last Name"]
#####################################
df_2018_MHRM = df_2018[df_2018["student Type"] == "MHRM"]
df_2018_MHRM["Full Name"] = df_2018_MHRM["First Name"] + " "+df_2018_MHRM["Last Name"]
#####################################
df_2018_MBA = df_2018[df_2018["student Type"] == "MBA"]
df_2018_MBA["Full Name"] = df_2018_MBA["First Name"] +" "+df_2018_MBA["Last Name"]

# FT or PT 2018
#####################################
df_2018_MSBA_FT = df_2018_MSBA[df_2018_MSBA["category"] == "FT"]
df_2018_MSBA_PT = df_2018_MSBA[df_2018_MSBA["category"] == "PT"]
#####################################
df_2018_MFIN_FT = df_2018_MFIN[df_2018_MFIN["category"] == "FT"]
df_2018_MFIN_PT = df_2018_MFIN[df_2018_MFIN["category"] == "PT"]
#####################################
df_2018_MHRM_FT = df_2018_MHRM[df_2018_MHRM["category"] == "FT"]
df_2018_MHRM_PT = df_2018_MHRM[df_2018_MHRM["category"] == "PT"]
#####################################
df_2018_MBA_FT = df_2018_MBA[df_2018_MBA["category"] == "FT"]
df_2018_MBA_PT = df_2018_MBA[df_2018_MBA["category"] == "PT"]

df_2018_MSBA_FT["Full Name"] = df_2018_MSBA_FT["First Name"] +" "+df_2018_MSBA_FT["Last Name"]
df_2018_MSBA_PT["Full Name"] = df_2018_MSBA_PT["First Name"] +" "+df_2018_MSBA_PT["Last Name"]
#####################################
df_2018_MFIN_FT["Full Name"] = df_2018_MFIN_FT["First Name"] +" "+df_2018_MFIN_FT["Last Name"]
df_2018_MFIN_PT["Full Name"] = df_2018_MFIN_PT["First Name"] + " "+df_2018_MFIN_PT["Last Name"]
#####################################
df_2018_MHRM_FT["Full Name"] = df_2018_MHRM_FT["First Name"] + " "+df_2018_MHRM_FT["Last Name"]
df_2018_MHRM_PT["Full Name"] = df_2018_MHRM_PT["First Name"] + " "+df_2018_MHRM_PT["Last Name"]
#####################################
df_2018_MBA_FT["Full Name"] = df_2018_MBA_FT["First Name"] + " "+df_2018_MBA_FT["Last Name"]
df_2018_MBA_PT["Full Name"] = df_2018_MBA_PT["First Name"] + " "+df_2018_MBA_PT["Last Name"]

# 2019
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_search_19 = pd.read_sql('select * from Student', conn)
df_search_19= df_search_19.drop_duplicates(subset="Id Number")
df_2019 = df_main[df_main["yearofadmission"].isin(["201910", "201920"])]
df_search_19["Full Name"] = df_search_19["First Name"] +" "+df_search_19["Last Name"]
df_search_19 = df_search_19.set_index("Full Name")
df_search_2019 = df_search_19[df_search_19["yearofadmission"].isin(["201910", "201920"])]
#####################################
df_2019_MSBA = df_2019[df_2019["student Type"] == "MSBA"]
df_2019_MSBA["Full Name"] = df_2019_MSBA["First Name"] +" "+df_2019_MSBA["Last Name"]
#####################################
df_2019_MFIN = df_2019[df_2019["student Type"] == "MF"]
df_2019_MFIN["Full Name"] = df_2019_MFIN["First Name"] +" "+df_2019_MFIN["Last Name"]
#####################################
df_2019_MHRM = df_2019[df_2019["student Type"] == "MHRM"]
df_2019_MHRM["Full Name"] = df_2019_MHRM["First Name"] +" "+df_2019_MHRM["Last Name"]
#####################################
df_2019_MBA = df_2019[df_2019["student Type"] == "MBA"]
df_2019_MBA["Full Name"] = df_2019_MBA["First Name"] +" "+df_2019_MBA["Last Name"]

# FT or PT 2019
#####################################
df_2019_MSBA_FT = df_2019_MSBA[df_2019_MSBA["category"].isin(["FT", "FT-GA", "FT-MC"])]
df_2019_MSBA_PT = df_2019_MSBA[df_2019_MSBA["category"] == "PT"]
#####################################
df_2019_MFIN_FT = df_2019_MFIN[df_2019_MFIN["category"].isin(["FT", "FT-GA", "FT-MC"])]
df_2019_MFIN_PT = df_2019_MFIN[df_2019_MFIN["category"] == "PT"]
#####################################
df_2019_MBA_FT = df_2019_MBA[df_2019_MBA["category"].isin(["FT", "FT-GA"])]
df_2019_MBA_PT = df_2019_MBA[df_2019_MBA["category"].isin(["PT", "PT-GA"])]

df_2019_MSBA_FT["Full Name"] = df_2019_MSBA_FT["First Name"] + " "+df_2019_MSBA_FT["Last Name"]
df_2019_MSBA_PT["Full Name"] = df_2019_MSBA_PT["First Name"] + " "+df_2019_MSBA_PT["Last Name"]
#####################################
df_2019_MFIN_FT["Full Name"] = df_2019_MFIN_FT["First Name"] + " "+df_2019_MFIN_FT["Last Name"]
df_2019_MFIN_PT["Full Name"] = df_2019_MFIN_PT["First Name"] + " "+df_2019_MFIN_PT["Last Name"]
#####################################
df_2019_MBA_FT["Full Name"] = df_2019_MBA_FT["First Name"] + " "+df_2019_MBA_FT["Last Name"]
df_2019_MBA_PT["Full Name"] = df_2019_MBA_PT["First Name"] +" "+df_2019_MBA_PT["Last Name"]

# 2020
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")

df_search_20 = pd.read_sql('select * from Student', conn)
df_search_20= df_search_20.drop_duplicates(subset="Id Number")

df_2020 = df_main[df_main["yearofadmission"].isin(["202010", "202020"])]

df_search_20["Full Name"] = df_search_20["First Name"] +  " "+df_search_20["Last Name"]
df_search_20 = df_search_20.set_index("Full Name")
df_search_2020 = df_search_20[df_search_20["yearofadmission"].isin(["202010", "202020"])]
#####################################
df_2020_MSBA = df_2020[df_2020["student Type"] == "MSBA"]
df_2020_MSBA["Full Name"] = df_2020_MSBA["First Name"] + " "+df_2020_MSBA["Last Name"]
#####################################
df_2020_MFIN = df_2020[df_2020["student Type"] == "MF"]
df_2020_MFIN["Full Name"] = df_2020_MFIN["First Name"] + " "+df_2020_MFIN["Last Name"]
#####################################
df_2020_MHRM = df_2020[df_2020["student Type"] == "MHRM"]
df_2020_MHRM["Full Name"] = df_2020_MHRM["First Name"] +" "+df_2020_MHRM["Last Name"]
#####################################
df_2020_MBA = df_2020[df_2020["student Type"] == "MBA"]
df_2020_MBA["Full Name"] = df_2020_MBA["First Name"] +" "+df_2020_MBA["Last Name"]

# FT or PT 2020
#####################################
df_2020_MSBA_FT = df_2020_MSBA[df_2020_MSBA["category"] == "FT"]
df_2020_MSBA_PT = df_2020_MSBA[df_2020_MSBA["category"] == "PT"]
#####################################
df_2020_MFIN_FT = df_2020_MFIN[df_2020_MFIN["category"] == "FT"]
df_2020_MFIN_PT = df_2020_MFIN[df_2020_MFIN["category"] == "PT"]
#####################################
df_2020_MBA_FT = df_2020_MBA[df_2020_MBA["category"] == "FT"]
df_2020_MBA_PT = df_2020_MBA[df_2020_MBA["category"] == "PT"]

df_2020_MSBA_FT["Full Name"] = df_2020_MSBA_FT["First Name"] +" "+df_2020_MSBA_FT["Last Name"]
df_2020_MSBA_PT["Full Name"] = df_2020_MSBA_PT["First Name"] + " "+df_2020_MSBA_PT["Last Name"]
#####################################
df_2020_MFIN_FT["Full Name"] = df_2020_MFIN_FT["First Name"] + " "+df_2020_MFIN_FT["Last Name"]
df_2020_MFIN_PT["Full Name"] = df_2020_MFIN_PT["First Name"] + " "+df_2020_MFIN_PT["Last Name"]
#####################################
df_2020_MBA_FT["Full Name"] = df_2020_MBA_FT["First Name"] + " "+df_2020_MBA_FT["Last Name"]
df_2020_MBA_PT["Full Name"] = df_2020_MBA_PT["First Name"] +" "+df_2020_MBA_PT["Last Name"]

# 2021
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_search_21 = pd.read_sql('select * from Student', conn)
df_search_21= df_search_21.drop_duplicates(subset="Id Number")
df_2021 = df_main[df_main["yearofadmission"].isin(["202110", "202120"])]
df_search_21["Full Name"] = df_search_21["First Name"] +" "+df_search_21["Last Name"]
df_search_21 = df_search_21.set_index("Full Name")
df_search_2021 = df_search_21[df_search_21["yearofadmission"].isin(["202110", "202120"])]
#####################################
df_2021_MSBA = df_2021[df_2021["student Type"] == "MSBA"]
df_2021_MSBA["Full Name"] = df_2021_MSBA["First Name"] +" "+df_2021_MSBA["Last Name"]
#####################################
df_2021_MFIN = df_2021[df_2021["student Type"] == "MF"]
df_2021_MFIN["Full Name"] = df_2021_MFIN["First Name"] +" "+df_2021_MFIN["Last Name"]
#####################################
df_2021_MHRM = df_2021[df_2021["student Type"] == "MHRM"]
df_2021_MHRM["Full Name"] = df_2021_MHRM["First Name"] +" "+df_2021_MHRM["Last Name"]
#####################################
df_2021_MBA = df_2021[df_2021["student Type"] == "MBA"]
df_2021_MBA["Full Name"] = df_2021_MBA["First Name"] +" "+df_2021_MBA["Last Name"]
#####################################
df_2021_OMBA = df_2021[df_2021["student Type"] == "OMBA"]
df_2021_OMBA["Full Name"] = df_2021_OMBA["First Name"] +" "+df_2021_OMBA["Last Name"]

# FT or PT 2021
#####################################
df_2021_MSBA_FT = df_2021_MSBA[df_2021_MSBA["category"] == "FT"]
df_2021_MSBA_PT = df_2021_MSBA[df_2021_MSBA["category"] == "PT"]
#####################################
df_2021_MFIN_FT = df_2021_MFIN[df_2021_MFIN["category"] == "FT"]
df_2021_MFIN_PT = df_2021_MFIN[df_2021_MFIN["category"] == "PT"]
#####################################
df_2021_MBA_FT = df_2021_MBA[df_2021_MBA["category"] == "FT"]
df_2021_MBA_PT = df_2021_MBA[df_2021_MBA["category"] == "PT"]
#####################################
df_2021_MHRM_FT = df_2021_MHRM[df_2021_MHRM["category"] == "FT"]
df_2021_MHRM_PT = df_2021_MHRM[df_2021_MHRM["category"] == "PT"]
#####################################
df_2021_OMBA_FT = df_2021_OMBA[df_2021_OMBA["category"] == "FT"]
df_2021_OMBA_PT = df_2021_OMBA[df_2021_OMBA["category"] == "PT"]

df_2021_MSBA_FT["Full Name"] = df_2021_MSBA_FT["First Name"] + " "+df_2021_MSBA_FT["Last Name"]
df_2021_MSBA_PT["Full Name"] = df_2021_MSBA_PT["First Name"] +" "+df_2021_MSBA_PT["Last Name"]
#####################################
df_2021_MFIN_FT["Full Name"] = df_2021_MFIN_FT["First Name"] + " "+df_2021_MFIN_FT["Last Name"]
df_2021_MFIN_PT["Full Name"] = df_2021_MFIN_PT["First Name"] +" "+df_2021_MFIN_PT["Last Name"]
#####################################
df_2021_MBA_FT["Full Name"] = df_2021_MBA_FT["First Name"] + " "+df_2021_MBA_FT["Last Name"]
df_2021_MBA_PT["Full Name"] = df_2021_MBA_PT["First Name"] +" "+df_2021_MBA_PT["Last Name"]
#####################################
df_2021_MHRM_FT["Full Name"] = df_2021_MHRM_FT["First Name"] +" "+df_2021_MHRM_FT["Last Name"]
df_2021_MHRM_PT["Full Name"] = df_2021_MHRM_PT["First Name"] +" "+df_2021_MHRM_PT["Last Name"]
#####################################
df_2021_OMBA_FT["Full Name"] = df_2021_OMBA_FT["First Name"] + " "+df_2021_OMBA_FT["Last Name"]
df_2021_OMBA_PT["Full Name"] = df_2021_OMBA_PT["First Name"] +" "+df_2021_OMBA_PT["Last Name"]

# 2017
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_search_17 = pd.read_sql('select * from Student', conn)
df_search_17= df_search_17.drop_duplicates(subset="Id Number")
df_2017 = df_main[df_main["yearofadmission"].isin(["201710", "201720"])]
df_search_17["Full Name"] = df_search_17["First Name"] +" "+df_search_17["Last Name"]
df_search_17 = df_search_17.set_index("Full Name")
df_search_2017 = df_search_17[df_search_17["yearofadmission"].isin(["201710", "201720"])]
#####################################
df_2017_MFIN = df_2017[df_2017["student Type"] == "MF"]
df_2017_MFIN["Full Name"] = df_2017_MFIN["First Name"] + " "+df_2017_MFIN["Last Name"]
#####################################
df_2017_MHRM = df_2017[df_2017["student Type"] == "MHRM"]
df_2017_MHRM["Full Name"] = df_2017_MHRM["First Name"] +" "+df_2017_MHRM["Last Name"]
#####################################
df_2017_MBA = df_2017[df_2017["student Type"] == "MBA"]
df_2017_MBA["Full Name"] = df_2017_MBA["First Name"] +" "+df_2017_MBA["Last Name"]
# table3
def table3(dataframe):
    l = math.ceil(len(dataframe)/3)
    x = 0

    for i in range(l):
        col1, col2, col3, = st.columns((1, 1, 1))
        with col1:
            if x < len(dataframe):
                backup_path = rf"MSBA _Photos_Folder\{p}"
                if os.path.isfile(backup_path):
                    backup = Image.open(backup_path)
                    st.image(backup, output_format="JPEG", width=165)
                    with st.expander(dataframe.iloc[x, 55]):
                        st.write(f"**ID:** {dataframe.iloc[x,1]}")
                        st.write(f"**E-mail:** {dataframe.iloc[x,6]}")
                        st.write(f"**LinkedIn:** {dataframe.iloc[x,54]}")

        with col2:
            if x+1 < len(dataframe):
                backup_path = rf"MSBA _Photos_Folder\{p}"
                if os.path.isfile(backup_path):
                    backup = Image.open(backup_path)
                    st.image(backup, output_format="JPEG", width=165)
                    with st.expander(dataframe.iloc[x+1, 55]):
                        st.write(f"**ID:** {dataframe.iloc[x+1,1]}")
                        st.write(f"**E-mail:** {dataframe.iloc[x+1,6]}")
                        st.write(f"**LinkedIn:** {dataframe.iloc[x+1,54]}")

        with col3:
            if x+2 < len(dataframe):
                backup_path = rf"MSBA _Photos_Folder\{p}"
                if os.path.isfile(backup_path):
                    backup = Image.open(backup_path)
                    st.image(backup, output_format="JPEG", width=165)
                    with st.expander(dataframe.iloc[x+2, 55]):
                        st.write(f"**ID:** {dataframe.iloc[x+2,1]}")
                        st.write(f"**E-mail:** {dataframe.iloc[x+2,6]}")
                        st.write(f"**LinkedIn:** {dataframe.iloc[x+2,54]}")

        x = x+3

# 2016
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_search_16 = pd.read_sql('select * from Student', conn)
df_search_16= df_search_16.drop_duplicates(subset="Id Number")
df_2016 = df_main[df_main["yearofadmission"].isin(["201610", "201620"])]
df_search_16["Full Name"] = df_search_16["First Name"] +" "+df_search_16["Last Name"]
df_search_16 = df_search_16.set_index("Full Name")
df_search_2016 = df_search_16[df_search_16["yearofadmission"].isin(["201610", "201620"])]
#####################################
df_2016_MFIN = df_2016[df_2016["student Type"] == "MF"]
df_2016_MFIN["Full Name"] = df_2016_MFIN["First Name"] +" "+df_2016_MFIN["Last Name"]
#####################################
df_2016_MHRM = df_2016[df_2016["student Type"] == "MHRM"]
df_2016_MHRM["Full Name"] = df_2016_MHRM["First Name"] +" "+df_2016_MHRM["Last Name"]
#####################################
df_2016_MBA = df_2016[df_2016["student Type"] == "MBA"]
df_2016_MBA["Full Name"] = df_2016_MBA["First Name"] +" "+df_2016_MBA["Last Name"]

# 2015
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_search_15 = pd.read_sql('select * from Student', conn)
df_search_15= df_search_15.drop_duplicates(subset="Id Number")
df_2015 = df_main[df_main["yearofadmission"].isin(["201510", "201520"])]
df_search_15["Full Name"] = df_search_15["First Name"] +" "+df_search_15["Last Name"]
df_search_15 = df_search_15.set_index("Full Name")
df_search_2015 = df_search_15[df_search_15["yearofadmission"].isin(["201510", "201520"])]
#####################################
df_2015_MFIN = df_2015[df_2015["student Type"] == "MF"]
df_2015_MFIN["Full Name"] = df_2015_MFIN["First Name"] +" "+df_2015_MFIN["Last Name"]
#####################################
df_2015_MHRM = df_2015[df_2015["student Type"] == "MHRM"]
df_2015_MHRM["Full Name"] = df_2015_MHRM["First Name"] +" "+df_2015_MHRM["Last Name"]
#####################################
df_2015_MBA = df_2015[df_2015["student Type"] == "MBA"]
df_2015_MBA["Full Name"] = df_2015_MBA["First Name"] +" "+df_2015_MBA["Last Name"]

# 2014
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_search_14 = pd.read_sql('select * from Student', conn)
df_search_14 = df_search_14 .drop_duplicates(subset="Id Number")
df_2014 = df_main[df_main["yearofadmission"].isin(["201410", "201420"])]
df_search_14["Full Name"] = df_search_14["First Name"] +" "+df_search_14["Last Name"]
df_search_14 = df_search_14.set_index("Full Name")
df_search_2014 = df_search_14[df_search_14["yearofadmission"].isin(["201410", "201420"])]
#####################################
df_2014_MFIN = df_2014[df_2014["student Type"] == "MF"]
df_2014_MFIN["Full Name"] = df_2014_MFIN["First Name"] + " "+df_2014_MFIN["Last Name"]
#####################################
df_2014_MHRM = df_2014[df_2014["student Type"] == "MHRM"]
df_2014_MHRM["Full Name"] = df_2014_MHRM["First Name"] +" "+df_2014_MHRM["Last Name"]
#####################################
df_2014_MBA = df_2014[df_2014["student Type"] == "MBA"]
df_2014_MBA["Full Name"] = df_2014_MBA["First Name"] + " "+df_2014_MBA["Last Name"]

# 2013
cursor = conn.cursor()
cursor.execute('select * from Student')
df_main = pd.read_sql('select * from Student', conn)
df_main= df_main.drop_duplicates(subset="Id Number")
df_search_13 = pd.read_sql('select * from Student', conn)
df_search_13=df_search_13.drop_duplicates(subset="Id Number")
df_2013 = df_main[df_main["yearofadmission"].isin(["201310", "201320"])]
df_search_13["Full Name"] = df_search_13["First Name"] +" "+df_search_13["Last Name"]
df_search_13 = df_search_13.set_index("Full Name")
df_search_2013 = df_search_13[df_search_13["yearofadmission"].isin(["201310", "201320"])]
#####################################
df_2013_MFIN = df_2013[df_2013["student Type"] == "MF"]
df_2013_MFIN["Full Name"] = df_2013_MFIN["First Name"] +" "+df_2013_MFIN["Last Name"]
#####################################
df_2013_MHRM = df_2013[df_2013["student Type"] == "MHRM"]
df_2013_MHRM["Full Name"] = df_2013_MHRM["First Name"] +" "+df_2013_MHRM["Last Name"]
#####################################
df_2013_MBA = df_2013[df_2013["student Type"] == "MBA"]
df_2013_MBA["Full Name"] = df_2013_MBA["First Name"] +" "+df_2013_MBA["Last Name"]


# Checkbox
d1, d2, d3 = st.columns((0.5, 1, 1))
if user_options == "2023" or user_options == "2022" or user_options == "2021" :
    if menu == "MSBA":
        Full_Time = d1.checkbox('Full-Time')
        Part_Time = d2.checkbox('Part-Time')
    elif menu == "MFIN":
        Full_Time = d1.checkbox('Full-Time')
        Part_Time = d2.checkbox('Part-Time')
    elif menu == "MHRM":
        Full_Time = d1.checkbox('Full-Time')
        Part_Time = d2.checkbox('Part-Time')
    elif menu == "MBA":
        Full_Time = d1.checkbox('Full-Time')
        Part_Time = d2.checkbox('Part-Time')
    elif menu == "OMBA":
        Full_Time = d1.checkbox('Full-Time')
        Part_Time = d2.checkbox('Part-Time')

elif user_options == "2020" or user_options == "2019" or user_options == "2018":
    if menu == "MSBA":
        Full_Time = d1.checkbox('Full-Time')
        Part_Time = d2.checkbox('Part-Time')
    elif menu == "MFIN":
        Full_Time = d1.checkbox('Full-Time')
        Part_Time = d2.checkbox('Part-Time')
    elif menu == "MBA":
        Full_Time = d1.checkbox('Full-Time')
        Part_Time = d2.checkbox('Part-Time')

#user otion
if user_options == "2023":
    if menu == "MSBA":
        if Full_Time and Part_Time:
            table1(df_2023_MSBA)
            st.markdown("-----")
        elif Full_Time:
            table1(df_2023_MSBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table1(df_2023_MSBA_PT)
            st.markdown("-----")
        else:
            table1(df_2023_MSBA)
            st.markdown("-----")
    elif menu == "MFIN":
        if Full_Time and Part_Time:
            table1(df_2023_MFIN)
            st.markdown("-----")
        elif Full_Time:
            table1(df_2023_MFIN_FT)
            st.markdown("-----")
        elif Part_Time:
            table1(df_2023_MFIN_PT)
            st.markdown("-----")
        else:
            table1(df_2023_MFIN)
            st.markdown("-----")
    elif menu == "MHRM":
        if Full_Time and Part_Time:
            table1(df_2023_MHRM)
            st.markdown("-----")
        elif Full_Time:
            table1(df_2023_MHRM_FT)
            st.markdown("-----")
        elif Part_Time:
            table1(df_2023_MHRM_PT)
            st.markdown("-----")
        else:
            table1(df_2023_MHRM)
            st.markdown("-----")
    elif menu == "MBA":
        if Full_Time and Part_Time:
            table2(df_2023_MBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2023_MBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2023_MBA_PT)
            st.markdown("-----")
        else:
            table2(df_2023_MBA)
            st.markdown("-----")
    elif menu == "OMBA":
        if Full_Time and Part_Time:
            table2(df_2023_OMBA)
            st.markdown("-----")
        if Full_Time:
            table2(df_2023_OMBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2023_OMBA_PT)
            st.markdown("-----")
        else:
            table2(df_2023_OMBA)
            st.markdown("-----")
    #if user_options == "2024":
        #st.title("Coming Soon :)")

elif user_options == "2022":
    if menu == "MSBA":
        if Full_Time and Part_Time:
            table2(df_2022_MSBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2022_MSBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2022_MSBA_PT)
            st.markdown("-----")
        else:
            table2(df_2022_MSBA)
            st.markdown("-----")
    elif menu == "MFIN":
        if Full_Time and Part_Time:
            table2(df_2022_MFIN)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2022_MFIN_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2022_MFIN_PT)
            st.markdown("-----")
        else:
            table2(df_2022_MFIN)
            st.markdown("-----")
    elif menu == "MHRM":
        if Full_Time and Part_Time:
            table2(df_2022_MHRM)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2022_MHRM_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2022_MHRM_PT)
            st.markdown("-----")
        else:
            table2(df_2022_MHRM)
            st.markdown("-----")
    elif menu == "MBA":
        if Full_Time and Part_Time:
            table2(df_2022_MBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2022_MBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2022_MBA_PT)
            st.markdown("-----")
        else:
            table2(df_2022_MBA)
            st.markdown("-----")
    elif menu == "OMBA":
        if Full_Time and Part_Time:
            table2(df_2022_OMBA)
            st.markdown("-----")
        if Full_Time:
            table2(df_2022_OMBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2022_OMBA_PT)
            st.markdown("-----")
        else:
            table2(df_2022_OMBA)
            st.markdown("-----")

elif user_options == "2021":
    if menu == "MSBA":
        if Full_Time and Part_Time:
            table2(df_2021_MSBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2021_MSBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2021_MSBA_PT)
            st.markdown("-----")
        else:
            table2(df_2021_MSBA)
            st.markdown("-----")
    elif menu == "MFIN":
        if Full_Time and Part_Time:
            table2(df_2021_MFIN)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2021_MFIN_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2021_MFIN_PT)
            st.markdown("-----")
        else:
            table2(df_2021_MFIN)
            st.markdown("-----")
    elif menu == "MHRM":
        if Full_Time and Part_Time:
            table2(df_2021_MHRM)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2021_MHRM_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2021_MHRM_PT)
            st.markdown("-----")
        else:
            table2(df_2021_MHRM)
            st.markdown("-----")
    elif menu == "MBA":
        if Full_Time and Part_Time:
            table2(df_2021_MBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2021_MBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2021_MBA_PT)
            st.markdown("-----")
        else:
            table2(df_2021_MBA)
            st.markdown("-----")
    elif menu == "OMBA":
        if Full_Time and Part_Time:
            table2(df_2021_OMBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2021_OMBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2021_OMBA_PT)
            st.markdown("-----")
        else:
            table2(df_2021_OMBA)
            st.markdown("-----")

elif user_options == "2020":
    if menu == "MSBA":
        if Full_Time and Part_Time:
            table2(df_2020_MSBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2020_MSBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2020_MSBA_PT)
            st.markdown("-----")
        else:
            table2(df_2020_MSBA)
            st.markdown("-----")
    elif menu == "MFIN":
        if Full_Time and Part_Time:
            table2(df_2020_MFIN)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2020_MFIN_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2020_MFIN_PT)
            st.markdown("-----")
        else:
            table2(df_2020_MFIN)
            st.markdown("-----")
    elif menu == "MHRM":
        table2(df_2020_MHRM)
        st.markdown("-----")
    elif menu == "MBA":
        if Full_Time and Part_Time:
            table2(df_2020_MBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2020_MBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2020_MBA_PT)
            st.markdown("-----")
        else:
            table2(df_2020_MBA)
            st.markdown("-----")

elif user_options == "2019":
    if menu == "MSBA":
        if Full_Time and Part_Time:
            table2(df_2019_MSBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2019_MSBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2019_MSBA_PT)
            st.markdown("-----")
        else:
            table2(df_2019_MSBA)
            st.markdown("-----")
    elif menu == "MFIN":
        if Full_Time and Part_Time:
            table2(df_2019_MFIN)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2019_MFIN_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2019_MFIN_PT)
            st.markdown("-----")
        else:
            table2(df_2019_MFIN)
            st.markdown("-----")
    elif menu == "MHRM":
        table2(df_2019_MHRM)
        st.markdown("-----")
    elif menu == "MBA":
        if Full_Time and Part_Time:
            table2(df_2019_MBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2019_MBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2019_MBA_PT)
            st.markdown("-----")
        else:
            table2(df_2019_MBA)
            st.markdown("-----")

elif user_options == "2018":
    if menu == "MSBA":
        if Full_Time and Part_Time:
            table2(df_2018_MSBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2018_MSBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2018_MSBA_PT)
            st.markdown("-----")
        else:
            table2(df_2018_MSBA)
            st.markdown("-----")
    elif menu == "MFIN":
        if Full_Time and Part_Time:
            table2(df_2018_MFIN)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2018_MFIN_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2018_MFIN_PT)
            st.markdown("-----")
        else:
            table2(df_2018_MFIN)
            st.markdown("-----")
    elif menu == "MHRM":
        table2(df_2018_MHRM)
        st.markdown("-----")
    elif menu == "MBA":
        if Full_Time and Part_Time:
            table2(df_2018_MBA)
            st.markdown("-----")
        elif Full_Time:
            table2(df_2018_MBA_FT)
            st.markdown("-----")
        elif Part_Time:
            table2(df_2018_MBA_PT)
            st.markdown("-----")
        else:
            table2(df_2018_MBA)
            st.markdown("-----")

elif user_options == "2017":
    if menu == "MFIN":
        table3(df_2017_MFIN)
        st.markdown("-----")
    elif menu == "MHRM":
        table3(df_2017_MHRM)
        st.markdown("-----")
    elif menu == "MBA":
        table3(df_2017_MBA)
        st.markdown("-----")

elif user_options == "2016":
    if menu == "MFIN":
        table3(df_2016_MFIN)
        st.markdown("-----")
    elif menu == "MHRM":
        table3(df_2016_MHRM)
        st.markdown("-----")
    elif menu == "MBA":
        table3(df_2016_MBA)
        st.markdown("-----")

elif user_options == "2015":
    if menu == "MFIN":
        table3(df_2015_MFIN)
        st.markdown("-----")
    elif menu == "MHRM":
        table3(df_2015_MHRM)
        st.markdown("-----")
    elif menu == "MBA":
        table3(df_2015_MBA)
        st.markdown("-----")

elif user_options == "2014":
    if menu == "MFIN":
        table3(df_2014_MFIN)
        st.markdown("-----")
    elif menu == "MHRM":
        table3(df_2014_MHRM)
        st.markdown("-----")
    elif menu == "MBA":
        table3(df_2014_MBA)
        st.markdown("-----")

elif user_options == "2013":
    if menu == "MFIN":
        table3(df_2013_MFIN)
        st.markdown("-----")
    elif menu == "MHRM":
        table3(df_2013_MHRM)
        st.markdown("-----")
    elif menu == "MBA":
        table3(df_2013_MBA)
        st.markdown("-----")   
#search
d = pd.read_sql('select * from Student', conn)
d= d.drop_duplicates(subset="Id Number")
d["Full Name"] = d["First Name"] +" "+d["Last Name"]
d = d.set_index("Full Name")
df_search_all = d[d["yearofadmission"].isin(["201310", "201320","201410", "201420","201510", "201520","201610", "201620","201710", "201720","201810", "201820","201910", "201920","202010", "202020","202110", "202120","202210", "202220","202310","202320"])]

if user_options == "Advanced Option":
    Years = st.selectbox("Years", options=["All Years", "2023", "2022", "2021","2020","2019", "2018", "2017", "2016", "2015","2014","2013"])
    if Years == "2023":
        def search(dataframe):
            name = st.selectbox(
                "Please select who you are looking for:", options=dataframe.index)
            id = dataframe.loc[name, "Id Number"]
            with st.container():
                if os.path.isfile(rf"MSBA _Photos_Folder\{id}.jpg"):
                    image = Image.open(rf"MSBA _Photos_Folder\{id}.jpg")
                    st.image(image, output_format="JPEG", width=200)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{id}.jpeg"):
                    image = Image.open(rf"MSBA _Photos_Folder\{id}.jpeg")
                    st.image(image, output_format="JPEG", width=200)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{id}.png"):
                    image = Image.open(rf"MSBA _Photos_Folder\{id}.png")
                    st.image(image, output_format="JPEG", width=200)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{id}.jfif"):
                    image = Image.open(rf"MSBA _Photos_Folder\{id}.jfif")
                    st.image(image, output_format="JPEG", width=200)
                else:
                    backup = Image.open(
                        rf"MSBA _Photos_Folder\{p}")
                    st.image(backup, output_format="JPEG", width=165)

            with st.container():
                L1, L2, L3= st.columns((1.5, 1, 1))
                v1, v2= st.columns((1, 1))
                L1.metric("Name", name)
                L2.metric('ID Number', dataframe.loc[name, "Id Number"])
                L3.metric("Program", dataframe.loc[name, "student Type"])
                v1.metric("Email:", dataframe.loc[name, "AUBEmail"])
                v1.metric("Linkedin:", dataframe.loc[name, "Linkedin"])
            with st.container():
                st.subheader(dataframe.loc[name, "Notes"])
        search(df_search)

    def search(dataframe):
            name = st.selectbox(
                "Please select who you are looking for:", options=dataframe.index)
            id = dataframe.loc[name, "Id Number"]
            backup = Image.open(rf"MSBA _Photos_Folder\{p}")
            st.image(backup, output_format="JPEG", width=165)

            with st.container():
                L1, L2, L3= st.columns((1.5, 1, 1))
                v1, v2= st.columns((1, 1))
                L1.metric("Name", name)
                L2.metric('ID Number', dataframe.loc[name, "Id Number"])
                L3.metric("Program", dataframe.loc[name, "student Type"])
                v1.metric("Email:", dataframe.loc[name, "AUBEmail"])
                v1.metric("Linkedin:", dataframe.loc[name, "Linkedin"])
    if Years == "2022":
        search(df_search_2022)
    elif Years == "2021":
        search(df_search_2021)
    elif Years == "2020":
        search(df_search_2020)
    elif Years == "2019":
        search(df_search_2019)
    elif Years == "2018":
        search(df_search_2018)
    elif Years == "2017":
        search(df_search_2017)
    elif Years == "2016":
        search(df_search_2016)
    elif Years == "2015":
        search(df_search_2015)
    elif Years == "2014":
        search(df_search_2014)
    elif Years == "2013":
        search(df_search_2013)
    elif Years == "All Years":
        def search(dataframe):
            name = st.selectbox(
                "Please select who you are looking for:", options=dataframe.index)
            id = dataframe.loc[name, "Id Number"]
            with st.container():
                if os.path.isfile(rf"MSBA _Photos_Folder\{id}.jpg"):
                    image = Image.open(rf"MSBA _Photos_Folder\{id}.jpg")
                    st.image(image, output_format="JPEG", width=200)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{id}.jpeg"):
                    image = Image.open(rf"MSBA _Photos_Folder\{id}.jpeg")
                    st.image(image, output_format="JPEG", width=200)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{id}.png"):
                    image = Image.open(rf"MSBA _Photos_Folder\{id}.png")
                    st.image(image, output_format="JPEG", width=200)
                elif os.path.isfile(rf"MSBA _Photos_Folder\{id}.jfif"):
                    image = Image.open(rf"MSBA _Photos_Folder\{id}.jfif")
                    st.image(image, output_format="JPEG", width=200)
                else:
                    backup = Image.open(
                        rf"MSBA _Photos_Folder\{p}")
                    st.image(backup, output_format="JPEG", width=165)

            with st.container():
                L1, L2, L3= st.columns((1.5, 1, 1))
                v1, V2= st.columns((1, 0.02))
                L1.metric("Name", name)
                L2.metric('ID Number', dataframe.loc[name, "Id Number"])
                L3.metric("Program", dataframe.loc[name, "student Type"])
                v1.metric("Email:", dataframe.loc[name, "AUBEmail"])
                v1.metric("Linkedin:", dataframe.loc[name, "Linkedin"])
            with st.container():
                st.subheader(dataframe.loc[name, "Notes"])
        search(df_search_all)


