import streamlit as st
import requests
import json

st.title("House predictor")

district = None
subtype = None
province = None
sale_type = None

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        proprety_type = st.radio('Type of property', ['House', 'Apartment'], index=None)
    with col2:
        if proprety_type:
            sale_type = st.radio('Type of sale', ['Sale', 'Rental'], index=None)
    if proprety_type == 'House':
        subtype = st.selectbox('Subtype of property', ['House', 'Villa', 'Apartment Block', 'Mixed Used Building', 'Mansion' ,'Town House', 'Bungalow', 'Exceptional Property', 'Country Cottage', 'Farmhouse', 'Chalet', 'Other Property', 'Manor House', 'Castle', 'Pavilion'], index=None)
    elif proprety_type == 'Apartment':
        subtype = st.selectbox('Subtype of property', ['Apartment', 'Ground Floor', 'Duplex', 'Flat Studio', 'Penthouse', 'Service Flat', 'Kot', 'Loft', 'Triplex','Show House'], index=None)

if subtype and sale_type:
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
        if province == 'Antwerp':
            district = st.selectbox('District', ['Antwerp', 'Mechelen', 'Turnhout'], index=None)
        elif province == 'Flemish Brabant':
            district = st.selectbox('District', ['Halle-Vilvoorde', 'Leuven'], index=None)
        elif province == 'Limburg':
            district = st.selectbox('District', ['Hasselt', 'Maaseik', 'Tongeren'], index=None)
        elif province == 'East Flanders':
            district = st.selectbox('District', ['Aalst', 'Dendermonde', 'Eeklo', 'Gent', 'Oudenaarde', 'Sint-Niklaas'], index=None)
        elif province == 'West Flanders':
            district = st.selectbox('District', ['Brugge', 'Diksmuide', 'Ieper', 'Kortrijk', 'Oostend', 'Roeselare', 'Tielt', 'Veurne'], index=None)
        elif province == 'Hainaut':
            district = st.selectbox('District', ['Ath', 'Charleroi', 'Mouscron', 'Soignies', 'Thuin', 'Tournai', 'Mons'], index=None)
        elif province == 'Liège':
            district = st.selectbox('District', ['Huy', 'Liège', 'Verviers', 'Waremme'], index=None)
        elif province == 'Luxembourg':
            district = st.selectbox('District', ['Arlon', 'Bastogne', 'Marche-en-Famenne', 'Neufchâteau', 'Virton'], index=None)
        elif province == 'Namur':
            district = st.selectbox('District', ['Dinant', 'Namur', 'Philippeville'], index=None)
        elif province == 'Walloon Brabant':
            district = st.selectbox('District', ['Nivelles'])
        elif province == 'Brussels':
            district = st.selectbox('District', ['Brussels'])

if district:
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
    if subtype == 'Villa':
        facade_count = col2.slider('Number of facades', min_value=2, max_value=4, value=4)
    else:
        facade_count = col2.slider('Number of facades', min_value=2, max_value=4, value=2)
    col1, col2 = st.columns(2)
    kitchen = col1.selectbox('Kitchen', ['Installed', 'Hyper-equipped', 'Semi-equipped', 'Not installed', 'USA Hyper-equipped', 'USA Installed', 'USA Semi-Equipped', 'USA Uninstalled'], index=0)
    state = col2.selectbox('State of building', ['As new', 'Good', 'Just renovated', 'To renovate', 'To be done up', 'To restore'], index=1)
    peb = st.select_slider('Energy performance', ['G','F','E','D','C','B','A','A+','A++'], value=('B'))

    if st.button('Calculate'):
        inputs = {
            'TypeOfProperty': proprety_type,
            'TypeOfSale': sale_type,
            'SubtypeOfProperty': subtype,
            'Region': region,
            'Province': province,
            'District': district,
            'BedroomCount': bedroom_count,
            'BathroomCount': bathroom_count,
            'ToiletCount': toilet_count,
            'ShowerCount': shower_count,
            'LivingArea': living_area,
            'Garden': garden,
            'GardenArea': garden_area,
            'SurfaceOfPlot': plot_area,
            'SwimmingPool': pool,
            'Fireplace': fireplace,
            'Furnished': furnished,
            'Terrace': terrace,
            'ConstructionYear': construction_year,
            'NumberOfFacades': facade_count,
            'Kitchen': kitchen,
            'StateOfBuilding': state,
            'PEB': peb
            }
        res = requests.post(url='http://127.0.0.1:8000/predict', data=json.dumps(inputs))
        st.subheader(f'We estimate this good at around : {float(res.text):.2f} €')