import streamlit as st
import joblib
model=joblib.load('Fuel-Detector')
st.title('Fuel Detection')
ip=st.text_input('Enter the fuel type')
op=model.predict([ip])
if st.button('Predict')
  st.title(op[0])
