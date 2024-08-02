import streamlit as st
import requests
import json

st.title("House predictor")

province = None
sale = None

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        proprety_type = st.radio('Type of property', ['House', 'Apartment'], index=None)
    with col2:
        if proprety_type:
            sale_type = st.radio('Type of sale', ['Sale', 'Rental'], index=None)
    if proprety_type == 'House':
        subtype = st.selectbox('Subtype of property', ['House', 'Villa', 'Mansion', 'Farmhouse', 'Town house', 'Cottage', 'Bungalow', 'Chalet', 'Castle', 'Country house', 'Exceptional property', 'Other'], index=None)
    elif proprety_type == 'Apartment':
        subtype = st.selectbox('Subtype of property', ['Apartment', 'Duplex', 'Triplex', 'Studio', 'Loft', 'Ground floor', 'Penthouse', 'Service flat', 'Exceptional property', 'Other'], index=None)

if sale_type:
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
        bedroom_count = col1.number_input('Number of bedrooms', min_value=0, max_value=10, value=1)
        bathroom_count = col2.number_input('Number of bathroom', min_value=0, max_value=10, value=1)
        toilet_count = col3.number_input('Number of toilets', min_value=0, max_value=10, value=1)
        shower_count = col4.number_input('Number of showers', min_value=0, max_value=10, value=1)
        with st.expander('Areas'):
            with st.container():
                col1, col2 = st.columns(2)
                col1.write('Living area')
                living_area = col2.number_input('Living area', min_value=0, max_value=1000, value=100)
            with st.container():
                col1, col2 = st.columns(2)
                garden = col1.checkbox('Garden')
                if garden:
                    garden_area = col2.number_input('Garden area', min_value=0, max_value=1000, value=100)
                else:
                    garden_area = None
            with st.container():
                col1, col2 = st.columns(2)
                plot = col1.checkbox('Plot area')
                if plot:
                    plot_area = col2.number_input('Plot area', min_value=0, max_value=1000, value=600)
                else:
                    plot_area = None
        with st.expander('Characteristics'):
            with st.container():
                col1, col2 = st.columns(2)
                pool = col1.checkbox('Swimming pool')
                fireplace = col2.checkbox('Fireplace')
                terrace = col1.checkbox('Terrace')
                furnished = col2.checkbox('Furnished')
    col1, col2 = st.columns(2)
    construction_year = col1.number_input('Construction year', min_value=0, max_value=2032, value=2000)
    facade_count = col2.slider('Number of facades', min_value=2, max_value=4, value=2)
    col1, col2 = st.columns(2)
    kitchen = col1.selectbox('Kitchen', ['Installed', 'Hyper-equipped', 'Semi-equipped', 'Not installed'], index=None)
    state = col2.selectbox('State of building', ['New', 'Good', 'To be renovated', 'Just renovated', 'To renovate'], index=None)
    peb = st.select_slider('Energy performance', ['G','F','E','D','C','B','A'], value=('B'))

if st.button('Calculate'):
    inputs = {'province': province, 'sale': sale, 'proprety_type': proprety_type, 'subtype': subtype, 'region': region, 'bedroom_count': bedroom_count, 'bathroom_count': bathroom_count, 'toilet_count': toilet_count, 'shower_count': shower_count, 'living_area': living_area, 'garden': garden, 'garden_area': garden_area, 'plot': plot, 'plot_area': plot_area, 'pool': pool, 'fireplace': fireplace, 'terrace': terrace, 'furnished': furnished, 'construction_year': construction_year, 'facade_count': facade_count, 'kitchen': kitchen, 'state': state, 'peb': peb}
    # st.subheader(f'Inputs: {json.dumps(inputs)}')
    res = requests.post(url='http://127.0.0.1:8000/predict', data=json.dumps(inputs))
    st.subheader(f'Response from the API: {res.text}')