import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import request
import pickle

model_url ="https://raw.github.com/rajkumarp984/machine_learning/master/model_pickle2"

response = requests.get(model_url, stream = True)
response.raise_for_status()

model = pickle.load(response.content)


def predict_house_price(area, bathrooms, age):
    input_data = [[area, bathrooms, age]]
    predict_price = model.predict(input_data)
    return predicted_price[0]
