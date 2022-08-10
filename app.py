import streamlit as st
import joblib
model = joblib.load('Fuel-Detector')
st.title('Fuel-Detection_Portal')
ip=st.text_input('Enter the Fuel Used')
op=model.predict([ip])
if st.button('Predict')
  st.title(op[0])
 
   
