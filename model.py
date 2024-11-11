import pandas as pd 
import numpy as np
import sklearn
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#data loader the data
def load_data(filepath='weather.csv'):
    df=pd.read_csv(filepath)
    df=df.drop(["Date","Wind Direction (°)"],axis=1)
    return df

# Preprocess data and split
def preprocess_data(df):
    X=df.drop(['Weather Condition'],axis=1)
    y=df['Weather Condition']
    encoder=LabelEncoder()
    y_encode=encoder.fit_transform(y.values.reshape(-1,1))
    X_train, X_test, y_train, y_test = train_test_split(X, y_encode, test_size=0.10, random_state=101)

    return X_train, X_test, y_train, y_test, encoder


# Logistic Regression Model
def train_model(X_train,y_train):
    log_model=LogisticRegression()

    log_model.fit(X_train,y_train)

    return log_model


