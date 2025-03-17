import streamlit as st
import joblib

def load_model(filename):
  model = joblib.load(filename)
  return model
  
def predict_with_model(model, user_input):
  prediction = model.predict([user_input])
  return prediction[0]

def main():
  st.title('🎈 Dermatology Machine Learning')
  st.write('This app using machine learning')

  # input by user
  erythema = st.slider('Erythema', min_value=0, max_value=3, value=2)
  age = st.slider('Age', min_value=0, max_value=3, value=2)

  user_input = [erythema, age]

  model_filename = "trained_model.pkl"
  model = load_model(model_filename)
  prediction = predict_with_model(model, user_input)
  st.write("Model Prediction is : ", prediction)

if  __name__ == "__main__" :
  main()
