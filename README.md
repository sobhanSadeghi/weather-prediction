# Weather Prediction

A machine learning project for weather prediction using `scikit-learn` to create a predictive model, along with a simple user interface built using `Streamlit`.

This project demonstrates a full pipeline for predicting weather conditions based on historical data. The `model.py` script is used to train and save a machine learning model, and `app.py` provides a web-based interface where users can input data and get predictions.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Project Description

This project builds a machine learning model to predict weather conditions based on various environmental parameters. Using historical weather data, we apply data preprocessing, train a model with `scikit-learn`, and then create a simple UI with `Streamlit` for easy interaction. The goal is to provide a tool that can make predictions on future weather conditions based on user-inputted parameters.

### Model

The `model.py` script contains code to load data, preprocess it, and train a machine learning model using `scikit-learn`. This trained model can predict weather conditions like temperature, humidity, and wind speed.

### User Interface

The `app.py` script uses `Streamlit` to provide a user-friendly interface where users can input relevant weather parameters and get predictions from the trained model.

---

## Features

- **Data Loading and Preprocessing**: Loads and preprocesses weather data for model training.
- **Model Training**: Trains a weather prediction model using `scikit-learn`.
- **Streamlit Interface**: A simple UI for inputting parameters and viewing predictions.
- **Virtual Environment Support**: A virtual environment setup to manage dependencies.

---

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sobhanSadeghi/weather-prediction.git
