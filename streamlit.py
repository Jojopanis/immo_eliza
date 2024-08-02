import streamlit as st

st.title("House predictor")

province = None
sale = None

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        proprety_type = st.radio('Type of property', ['House', 'Apartment'], index=None)
    with col2:
        if proprety_type:
            sale = st.radio('Type of sale', ['Sale', 'Rental'], index=None)
    if proprety_type == 'House':
        subtype = st.selectbox('Subtype of property', ['House', 'Villa', 'Mansion', 'Farmhouse', 'Town house', 'Cottage', 'Bungalow', 'Chalet', 'Castle', 'Country house', 'Exceptional property', 'Other'], index=None)
    elif proprety_type == 'Apartment':
        subtype = st.selectbox('Subtype of property', ['Apartment', 'Duplex', 'Triplex', 'Studio', 'Loft', 'Ground floor', 'Penthouse', 'Service flat', 'Exceptional property', 'Other'], index=None)

if sale:
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            region = st.selectbox('Region', ['Brussels', 'Flanders', 'Wallonia'], index=None)
        with col2:
            if region == 'Flanders':
                province = st.selectbox('Province', ['Antwerp', 'Flemish Brabant','Limburg','East Flanders','West Flanders'], index=None)
            elif region == 'Wallonia':
                province = st.selectbox('Province', ['Hainaut', 'Liège','Luxembourg','Namur','Walloon Brabant'], index=None)
            elif region == 'Brussels':
                province = st.selectbox('Province', ['Brussels'])

if province:
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        col1.number_input('Number of bedrooms', min_value=0, max_value=10, value=1)
        col2.number_input('Number of bathroom', min_value=0, max_value=10, value=1)
        col3.number_input('Number of toilets', min_value=0, max_value=10, value=1)
        col4.number_input('Number of showers', min_value=0, max_value=10, value=1)
        with st.expander('Areas'):
            with st.container():
                col1, col2 = st.columns(2)
                col1.write('Living area')
                col2.number_input('Living area', min_value=0, max_value=1000, value=100)
            with st.container():
                col1, col2 = st.columns(2)
                garden = col1.checkbox('Garden')
                if garden:
                    garden_area = col2.number_input('Garden area', min_value=0, max_value=1000, value=100)
            with st.container():
                col1, col2 = st.columns(2)
                plot = col1.checkbox('Plot area')
                if plot:
                    plot_area = col2.number_input('Plot area', min_value=0, max_value=1000, value=600)
        with st.expander('Characteristics'):
            with st.container():
                col1, col2 = st.columns(2)
                col1.checkbox('Swimming pool')
                col2.checkbox('Fireplace')
                col1.checkbox('Terrace')
                col2.checkbox('Furnished')
    col1, col2 = st.columns(2)
    col1.number_input('Construction year', min_value=0, max_value=2032, value=2000)
    col2.slider('Number of facades', min_value=2, max_value=4, value=2)
    col1, col2 = st.columns(2)
    col1.selectbox('Kitchen', ['Installed', 'Hyper-equipped', 'Semi-equipped', 'Not installed'], index=None)
    col2.selectbox('State of building', ['New', 'Good', 'To be renovated', 'Just renovated', 'To renovate'], index=None)
    st.select_slider('Energy performance', ['G','F','E','D','C','B','A'], value=('B'))


