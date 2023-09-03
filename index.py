import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Audit Recommendations Tracker')
# st.header('AUDIT RECOMMENDATIONS TRACKING TOOL DASHBOARD - SAI NAURU')
# st.subheader('Supreme Audit Institution of Nauru')

## --- LOAD DATAFRAME
excel_file1 = 'Database_2_web_app.xlsx'
sheet_name1 = 'Database'
sheet_name2 = 'Summary'
sheet_name3 = 'Fully Implemented Reports'
sheet_name4 = 'Not Implemented Recommendations'
sheet_name5 = 'Partially Implemented'
sheet_name6 = 'Ongoing'

df_tracking_tool2 = pd.read_excel(excel_file1,
                                sheet_name= sheet_name2,
                                usecols='K:O',
                                header=6)

df_tracking_tool1 = pd.read_excel(excel_file1,
                                sheet_name= sheet_name2,
                                usecols='B:G',
                                header=6)


df1 = pd.read_excel(excel_file1,
                   sheet_name=sheet_name1,
                   usecols='B:R',
                   header=5)

df2 = pd.read_excel(excel_file1,
                   sheet_name=sheet_name3,
                   usecols='B:N',
                   header=7)

df3 = pd.read_excel(excel_file1,
                   sheet_name=sheet_name4,
                   usecols='C:P',
                   header=6)

df4 = pd.read_excel(excel_file1,
                   sheet_name=sheet_name6,
                   usecols='C:P',
                   header=6)

df5 = pd.read_excel(excel_file1,
                   sheet_name=sheet_name5,
                   usecols='C:P',
                   header=6)
# Define function for the Home page
def home():
    # st.title("Home Page")
    st.markdown(
    """
    <h1 style='text-align: center;'>AUDIT RECOMMENDATIONS TRACKING TOOL DASHBOARD</h1>
    """,
    unsafe_allow_html=True)

    # st.write("IMPLEMENTATION STATUS SUMMARY")
    # assuming df_participants has columns 'Departments', 'Total Participants', and 'Actual Participants'
    pie_chart = px.pie(df_tracking_tool2, 
                    # title='IMPLEMENTATION STATUS SUMMARY',
                    names='Implementation Status',
                    values='Sub Totals'
                    )

    # pie_chart.update_layout(title_x=0.25)
    # display the chart using Streamlit
    st.plotly_chart(pie_chart)


# Define function for the About page
def charts():
    st.title("Charts")

    # FULLY IMPLEMENTED RECOMMENDATIONS
    bar_chart = px.bar(df_tracking_tool1, 
                    title='FULLY IMPLEMENTED RECOMMENDATIONS',
                    barmode='group',
                    x='Lead Body', 
                    y=['Total Recommendations','Fully Implemented'])
    bar_chart.update_layout(title_x=0.25)
    # display the chart using Streamlit
    st.plotly_chart(bar_chart)

    # NOT IMPLEMENTED RECOMMENDATIONS
    bar_chart = px.bar(df_tracking_tool1, 
                    title='NOT IMPLEMENTED RECOMMENDAATIONS',
                    barmode='group',
                    x='Lead Body', 
                    y=['Total Recommendations','Not Implemented'])

    bar_chart.update_layout(title_x=0.25)
    # display the chart using Streamlit
    st.plotly_chart(bar_chart)

    # PARTIALLY IMPLEMENTED RECOMMENDATIONS
    bar_chart = px.bar(df_tracking_tool1, 
                    title='PARTIALLY IMPLEMENTED RECOMMENDATIONS',
                    barmode='group',
                    x='Lead Body', 
                    y=['Total Recommendations','Partially Implemented'])
    # display the chart using Streamlit
    bar_chart.update_layout(title_x=0.25)
    st.plotly_chart(bar_chart)

    # ONGOING IMPLEMENTIONS
    bar_chart = px.bar(df_tracking_tool1, 
                    title='ONGOING IMPLEMENTATION',
                    barmode='group',
                    x='Lead Body', 
                    y=['Total Recommendations','Ongoing'])

    bar_chart.update_layout(title_x=0.25)
    # display the chart using Streamlit
    st.plotly_chart(bar_chart)

    # SUMMARY CHART
    bar_chart = px.bar(df_tracking_tool1, 
                    title='IMPLEMENTATION STATUS SUMMARY',
                    barmode='group',
                    x='Lead Body', 
                    y=['Total Recommendations','Fully Implemented', 'Partially Implemented', 'Not Implemented', 'Ongoing'])
    bar_chart.update_layout(title_x=0.25)
    # display the chart using Streamlit
    st.plotly_chart(bar_chart)

# Define function for the Contact page
def tables():
    st.title("Tables")
    # st.subheader('NOT IMPLEMENTED RECOMMENDATIONS')
    st.markdown(
        """
        <h2 style='text-align: center;'>NOT IMPLEMENTED RECOMMENDATIONS</h2>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(df3)

    # st.subheader('FULLY IMPLEMENTED RECOMMENDATIONS')
    st.markdown(
        """
        <h2 style='text-align: center;'>FULLY IMPLEMENTED RECOMMENDATIONS</h2>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(df2)

    # st.subheader('FULLY IMPLEMENTED RECOMMENDATIONS')
    st.markdown(
        """
        <h2 style='text-align: center;'>ONGOING IMPLEMENTATIONS</h2>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(df4)

    # st.subheader('FULLY IMPLEMENTED RECOMMENDATIONS')
    st.markdown(
        """
        <h2 style='text-align: center;'>PARTIALLY IMPLEMENTED RECOMMENDATIONS</h2>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(df5)


    # st.subheader('RECOMMENDATIONS TABLE')
    st.markdown(
        """
        <h2 style='text-align: center;'>RECOMMENDATIONS TABLE</h2>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(df1)

# Create a dictionary with the page names and their corresponding functions
pages = {
    "Home": home,
    "Charts": charts,
    "Tables": tables
}

# Create a sidebar with navigation links
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Call the appropriate function based on the user's selection
page = pages[selection]
page()

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
