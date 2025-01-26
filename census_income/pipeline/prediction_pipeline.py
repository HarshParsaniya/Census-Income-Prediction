import os
import sys

from census_income.exception.exception import CustomException
from census_income.utils.utils import load_object

import pandas as pd


class PredictPipeline:
    """
    This class is used to create a pipeline for prediction.
    """
    def __init__(self):
        pass

    def predict(self,features):
        try:
            # Load the preprocessor file path from the pickle file
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            # Load the model file path from the pickle file
            model_path=os.path.join('artifacts','model.pkl')

            # Load the preprocessor object from the pickle file
            preprocessor=load_object(preprocessor_path)
            # Load the model object from the pickle file
            model=load_object(model_path)

            # Transform the features according to preprocessor object
            data_scaled=preprocessor.transform(features)

            # Predict the value using model object
            pred=model.predict(data_scaled)

            return pred
            

        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    """
    This class is used to create a custom data object.
    """
    def __init__(self,
                 age:int,
                 workclass:str,
                 final_weight:int,
                 educationNum:int,
                 occupation:str,
                 capital_gain:int,
                 capital_loss:int,
                 hours_per_week:int,
                 native_country:str):
        
        self.age=age
        self.workclass=workclass
        self.final_weight=final_weight
        self.educationNum=educationNum
        self.occupation=occupation
        self.capital_gain=capital_gain
        self.capital_loss = capital_loss
        self.hours_per_week = hours_per_week
        self.native_country = native_country

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'age':[self.age],
                'workclass':[self.workclass],
                'final_weight':[self.final_weight],
                'educationNum':[self.educationNum],
                'occupation':[self.occupation],
                'capital_gain':[self.capital_gain],
                'capital_loss':[self.capital_loss],
                'hours_per_week':[self.hours_per_week],
                'native_country	':[self.native_country]
            }
            df = pd.DataFrame(custom_data_input_dict)
            return df
        
        
        except Exception as e:
            raise CustomException(e,sys)