# Crop Prediction using Machine Learning


## Overview

This project aims to develop a machine learning based crop-prediction model to support farmers in making informed decisions about crop selection, planting, and harvesting. The model was trained on a large dataset of historical crop and weather data, using deep learning techniques. The results of the model showed high accuracy in predicting crop yield, surpassing the performance of traditional crop prediction methods. The model has been deployed with user-friendly interface, thus enabling farmers to input a few values and obtain informed decisions about when and what to plant. This project represents a significant step forward in using ML to improve the efficiency and profitability of agriculture.

## Data

The data used to train the model was collected from the `crop_prediction` dataset. The dataset consists of 22 different crops whose predictions are made using 7 features: nitrogen, phosphorus, potassium, and pH content of the soil, temperature, humidity and rainfall.The  `data` datset is used to cross reference geolocations to corresponding rainfall values. The data was pre-processed to ensure consistency and cleaned to remove any missing values. The data includes information on various crop types, weather patterns, and soil types.


## Model

The model is built using Deep Neural Networks(DNNs). The architecture we have chosen consists of 3 hidden layers with 64, 128 and 64 neurons respectively, and an output layer of 22 neurons, each corresponding to one type of crop. The algorithm was trained on the data with a 80:20 train-test split ratio. The performance metric used to evaluate the model is accuracy.

## Results
The model achieved an accuracy of 99% on the train data, and an accuracy of about 98% on the test data, indicating a high level of accuracy in its predictions. The vizualization of the performance is shown as follows:

## Testing
The following data is collected from the end-user to make predictions:

1. N, P, K, pH content of the soil.
2. Geolocation (State and District)
3. Month(Season) of cultivation

The geolocation is used to obtain the temperature and humidity values of the place, using appropriate API calls to weather forecasting sites. The following sites were accessed through API calls for climate data:

1. [Open Weather](http://api.openweathermap.org/)
2. [Latitude and Logitude Finder](https://www.latlong.net)

We have created an interactive interface for users to enter relevant data to get predictions for their crop.

![Preview](preview.jpeg)