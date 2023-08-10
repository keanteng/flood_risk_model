import streamlit as st
import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim
import math

st.set_page_config(layout="wide")

st.sidebar.title("Resources:")
st.sidebar.info(
    """
    - GitHub repository: [streamlit_flood](https://github.com/keanteng/flood_risk_model)
    - Data sources: [Flood Data](https://www.water.gov.my/)
    """
)

st.sidebar.title("Created By:")
st.sidebar.info(
    """
  Khor Kean Teng | Intern, DGA, JPS, Bank Negara Malaysia | [GitHub](https://github.com/keanteng) | [LinkedIn](https://www.linkedin.com/in/khorkeanteng/)
    """
)

# Customize page title
st.title("Flood Risk Prediction Service")

st.markdown("""
            This is a flood risk prediction service that predicts the flood risk of a location in Malaysia. The result is not 100% accurate and should not be used as a basis for any decision making. 
            The result is only for reference purposes.
            """)

your_address = st.text_input("Enter your address here:")
your_state = st.selectbox("Select your state here:", ["Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", "Pahang", "Perak", "Penang", "Sabah", "Sarawak", "Selangor", "Terengganu", "Kuala Lumpur", "Labuan"])
submitted = st.button("Submit For Prediction")

#####################################
# geocoding function
@st.cache_data
def my_geocoder(address):
            try:
                point = geolocator.geocode(address).point
                return pd.Series({'Latitude': point.latitude, 'Longitude': point.longitude})
            except:
                return pd.Series({'Latitude': None, 'Longitude': None})

# distance function
def distance_to_nearest_flood_point(data):
    flood_points = pd.read_csv('data/all_states_all_years_geocoded.csv')
    data = gpd.GeoDataFrame(data, geometry = gpd.points_from_xy(data.Longitude, data.Latitude), crs = "EPSG:4326").to_crs('EPSG:3857')
    flood_points_data = gpd.GeoDataFrame(flood_points, geometry = gpd.points_from_xy(flood_points.Longitude, flood_points.Latitude), crs = "EPSG:4326").to_crs('EPSG:3857')
    
    # write a function to compute for the minimum distances from any flood point
    for i in range(0, len(data)):
        distances = flood_points_data.geometry.distance(data.iloc[i].geometry)
        data.loc[i, 'distance'] = distances.min()

    return data

@st.cache_data
def determineCoefficient(your_address):
    new =  [4.77941620e-01, 1.22460645e-01, 1.37677540e-03,
            1.52185371e+00, 5.30927351e-02, 9.10748035e-01, 5.44494671e-01,
            8.31631218e-01, 6.50728294e-01, 2.67305790e-01, 1.99053696e-01,
            1.45960340e+00, 1.12335137e+00, 1.95290287e-02] 
    
    if your_address == "Kuala Lumpur":
        return new[0]
    elif your_address == "Johor":
        return new[1]
    elif your_address == "Selangor":
        return new[2]
    elif your_address == "Penang":
        return new[3]
    elif your_address == "Perak":
        return new[4]
    elif your_address == "Sarawak":
        return new[5]
    elif your_address == "Sabah":
        return new[6]
    elif your_address == "Pahang":
        return new[7]
    elif your_address == "Negeri Sembilan":
        return new[8]
    elif your_address == "Terengganu":
        return new[9]
    elif your_address == "Melaka":
        return new[10]
    elif your_address == "Kedah":
        return new[11]
    elif your_address == "Kelantan":
        return new[12]
    elif your_address == "Labuan":
        return new[13]
        

#####################################

if submitted:
    with st.spinner("Computing ... Please Wait ..."):
        data = pd.DataFrame({'Location': [your_address],})
        geolocator = Nominatim(user_agent="u2004763@siswa.um.edu.my")
        data[['Latitude', 'Longitude']] = data.apply(lambda x: my_geocoder(x['Location']), axis=1)
        
        if data['Latitude'][0] == None:
            st.error("Please enter a new address. The address you entered is not valid.")
        else:
            data = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.Longitude, data.Latitude))
            data.crs = {'init': 'epsg:4326'}
            
            new_data = distance_to_nearest_flood_point(data)
            temp = determineCoefficient(your_state)
            flood_risk = 1/(1 + math.exp(-1.89407693e-02*new_data['distance'][0] + 8.18317099 + temp))
            
            st.write("The flood risk for your location is: ", flood_risk)
            
            if flood_risk < 0.5:
                st.markdown("Your location is at a low risk of flooding.")
            else:
                st.markdown("Your location is at a high risk of flooding. Please be careful and take precautions.")
            
            


