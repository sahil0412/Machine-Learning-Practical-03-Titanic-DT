import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            
            ## DO Preprocessig of I/P features before passing for Imputing
            
            features["Has_Cabin"] = (features["Cabin"].notnull().astype('int'))
            features = features.drop(['Cabin'], axis=1)
            
            features["no_of_persons"] = features["SibSp"] + features["Parch"]
            features = features.drop(labels=["SibSp", "Parch"], axis=1)
            
            
            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 Pclass:float,
                 Sex:str,
                 Age:float,
                 SibSp:float,
                 Parch:float,
                 Fare:float,
                 Cabin:str,
                 Embarked:str):
        
        self.Pclass=Pclass
        self.Sex=Sex
        self.Age=Age
        self.SibSp=SibSp
        self.Parch=Parch
        self.Fare=Fare
        self.Cabin = Cabin
        self.Embarked = Embarked

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Pclass':[self.Pclass],
                'Sex':[self.Sex],
                'Age':[self.Age],
                'SibSp':[self.SibSp],
                'Parch':[self.Parch],
                'Fare':[self.Fare],
                'Cabin':[self.Cabin],
                'Embarked':[self.Embarked]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)