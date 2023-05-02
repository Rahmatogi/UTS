import pickle
import streamlit as st 
import setuptools
# membaca model
house_model = pickle.load(open('estimmasi_harga_rumah_india_fix.sav','rb'))

#judul web
st.title('Aplikasi Prediksi Harga Rumah')

col1, col2,col3=st.columns(3)
with col1:
    Storage = st.number_input('number of bedrooms:')
with col2:
    BatteryCapacity  = st.number_input('number of bathrooms :')
with col3:
    ScreenSize  = st.number_input('living area :')
with col1:
    RAM = st.number_input('number of floors:')
with col2:
    JumlahKamera = st.number_input('waterfront present :')
with col3:
    cam1 = st.number_input('number of views :')
with col1:
    cam2 = st.number_input('grade of the house :')
with col2:
    cam3 = st.number_input('Area of the house(excluding basement) :')
with col3:
    cam4 = st.number_input('Area of the basement :')
with col1:
    idBrand = st.number_input('Lattitude')
with col2:
    cam4 = st.number_input('living_area_renov :')

#code untuk estimasi
house_est=''

#membuat button
with col1:
    if st.button('Estimasi Harga'):
        house_pred = house_model.predict([[number_of_bedrooms,number_of_bathroom,living_area,number_of_floors,waterfront_present,number_of_views,grade_of_the_house,Area_of_the_house_excluding_basement,Area_of_the_basement,Lattitude,living_area_renov]])

        st.success(f'Estimasi Harga : {house_pred[0]:.2f}')