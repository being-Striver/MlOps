import sys
import os
import pickle
from src.exceptions import CustomException

def save_object(file_path, obj):
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(obj,file_path)
    except Exception as e:
        raise CustomException(e, sys)
