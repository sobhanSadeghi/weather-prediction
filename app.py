import numpy as np
import streamlit as st
from model import load_data, preprocess_data, train_model


@st.cache_data
def get_data():
    df=load_data()
    X_train, X_test, y_train, y_test, encoder = preprocess_data(df)
    model=train_model(X_train,y_train)
    return df,model,encoder

df,model,encoder=get_data()


# Streamlit UI
st.title('Weather Prediction for Tehran')
st.header('Predict the weather based on input parameters')

# Streamlit form for user input
with st.form('user-input'):
    temp = st.slider('Temperature (°C)', df['Temperature (°C)'].min(), df['Temperature (°C)'].max())
    humidity = st.slider('Humidity (%)', df['Humidity (%)'].min(), df['Humidity (%)'].max(), 80, 5)
    wind_speed = st.slider('Wind Speed (km/h)', df['Wind Speed (km/h)'].min(), df['Wind Speed (km/h)'].max(), 10)
    pressure = st.slider('Pressure (hPa)', df['Pressure (hPa)'].min(), df['Pressure (hPa)'].max(), 1010)

    submitted = st.form_submit_button('Predict', type='primary')

# Prediction
if submitted:
    input_array = np.array([[temp, humidity, wind_speed, pressure]])
    prediction = model.predict(input_array)
    pred_label = encoder.inverse_transform(prediction)
    st.header(f"Based on your input parameters, the predicted weather is: {pred_label.item()}")