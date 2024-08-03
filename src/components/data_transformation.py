import sys 
import os 
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = "C:/Users/shudh/OneDrive/Desktop/ML_OPS/artifacts/preprocessor.pkl"


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_objects(self):
        ''' 
        This function is responsible for data transformation 
        '''
        try:
            numerical_columns=['reading score','writing score']
            categorical_columns=["gender", 
                                 "race/ethnicity",
                                 "parental level of education",
                                "lunch", 
                                "test preparation course"
                                ]
            
            numerical_pipeline=Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy="median")),
                    ('scalar', StandardScaler())
                ]
            )
            categorical_pipeline=Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder', OneHotEncoder()),
                    # ('scalar', StandardScaler())
                ]
            )
            logging.info("numerical columns standard scaling completed")
            logging.info("Categorical columns encoding completed")

            preprocessor=ColumnTransformer(
                [
                    ("numerical_pipeline",numerical_pipeline, numerical_columns),
                    ("categorical_pipeline", categorical_pipeline, categorical_columns)
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
        

    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Reading train and test data completed..!")

            logging.info("Obtaining preprocessing object...")

            preprocessing_obj=self.get_data_transformer_objects()

            target_column_names="math score"
            numerical_columns=["reading score","writing score"]
            #for test dataset 
            input_feature_test_df=test_df.drop(columns=[target_column_names], axis=1)
            target_feature_test_df=test_df[target_column_names]

            #for train dataset
            input_feature_train_df=train_df.drop(columns=[target_column_names],axis=1)
            target_feature_train_df=train_df[target_column_names]

            

            logging.info("Applying preprocessing object on training dataframe and testing dataframe...")
            
            input_feature_train_arr= preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr=np.c_[ 
                input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr=np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]

            logging.info("saved preprocessing obejct.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            return (
                train_arr, 
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path

            )

        except Exception as e:
            raise CustomException(e, sys)
        


