import numpy as np
import pandas as pd

import json
import pickle

import warnings
warnings.filterwarnings("ignore")
import config

class PredictionData():
    def __init__(self, Age ,Gender,Location,Subscription_Length_Months,
                 Monthly_Bill,Total_Usage_GB ):

        self.Age                         = Age
        self.Gender                      = Gender
        self.Subscription_Length_Months  = Subscription_Length_Months
        self.Monthly_Bill                = Monthly_Bill
        self.Total_Usage_GB              = Total_Usage_GB

        # # input for one-hot encoding
        self.Location = "Location_" + Location
        

    def load_models(self):
        #fitted model
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

        with open(config.SCALLING_FILE_PATH, "rb") as f:
            self.StandardScaler = pickle.load(f)


    def get_prediction(self):

        self.load_models()   # Creating instance function of model and json_data

        # # input for label encoding
        self.Gender   = self.json_data['Gender'][self.Gender]

        # index of one-hot encodded columns
        Location_index = self.json_data['columns'].index(self.Location)

        # Creating array of user input values
        test_array = np.zeros(len(self.json_data['columns']))

        # Note: put feature values in front of correct feature index
        test_array[0] = self.Age
        test_array[1] = self.Gender    #label encodded
        test_array[2] = self.Subscription_Length_Months
        test_array[3] = self.Monthly_Bill
        test_array[4] = self.Total_Usage_GB
        test_array[Location_index] = 1   # one-hot encodded

        prediction = self.model.predict([test_array])[0]

        return prediction