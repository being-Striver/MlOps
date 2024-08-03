import sys
import os
import dill
from src.exceptions import CustomException
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def save_object(file_path, obj):
    try:
        with open(file_path, 'wb') as file:
            dill.dump(obj,file)
    except Exception as e:
        raise CustomException(e, sys)

def evaluation_model(X_train, X_test,y_train,y_test, models):
    report={}
    for i in range(len(list(models))):
        model=list(models.values())[i]
        #train model
        model.fit(X_train, y_train)

        #make prediction
        y_train_pred=model.predict(X_train)
        y_test_pred=model.predict(X_test)

        train_model_score=r2_score(y_train,y_train_pred)
        test_model_score=r2_score(y_test, y_test_pred)
        report[(list(models.keys())[i])]=test_model_score
    return report
    
