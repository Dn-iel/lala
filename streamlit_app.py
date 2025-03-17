import streamlit as st
import joblib

def main():
  st.title('🎈 Dermatology Machine Learning')
  st.write('This app using machine learning')

  # input by user
  erythema = st.slider('Erythema', min_value=0, max_value=3, value=2)


if_name_=="_main":
  main()
