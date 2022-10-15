import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import xgboost as xg

def prediction(Fcatgeory, Ftype, Fyear, Fmonth):
    
    # Read CSV
    df = pd.read_csv("./dataset.csv")
    
    # dropping unnecessary columns
    df.drop(['VORJAHRESWERT','VERAEND_VORMONAT_PROZENT','VERAEND_VORJAHRESMONAT_PROZENT','ZWOELF_MONATE_MITTELWERT'], axis=1, inplace=True)
    
    # renaming the columns
    df.rename( columns = { 
      'MONATSZAHL' : 'Category',
      'AUSPRAEGUNG': 'Accident-Type',
      'JAHR'       : 'Year',
      'MONAT'      : 'Month',
      'WERT'       : 'Value'
    }, inplace=True)

    df.dropna(inplace = True)

    # dropping records after 2020
    df_year = df[df['Year'] > 2020]     
    df.drop(df_year.index, axis=0, inplace=True)

    # Outlier removal
    upper_limit = df.Value.mean() + 3*df.Value.std()
    lower_limit = df.Value.mean() - 3*df.Value.std()
    df = df[(df.Value<upper_limit) & (df.Value>lower_limit)]

    # Converting the string variable to int using LabelEncoder
    le_category = preprocessing.LabelEncoder()
    le_category.fit(df["Category"])
    df["Category"] = le_category.transform(df["Category"])
     
    le_accident = preprocessing.LabelEncoder()
    le_accident.fit(df["Accident-Type"])
    df["Accident-Type"] = le_accident.transform(df["Accident-Type"])
    
    # Display only month numbers 
    df['Month'] = df['Month'].str[-2:]
    # Removing Summe from MONAT Column
    df = df[df['Month'] != 'me']

    # X,y values
    X = df.iloc[:,:4].values
    y = df.iloc[:,-1].values

    Fcatgeory = le_category.transform([Fcatgeory])[0]
    Ftype = le_accident.transform([Ftype])[0]

    input = np.array([Fcatgeory, Ftype, Fyear, Fmonth])
    input = np.reshape(input, (1,4))
    # Advanced Ensemble Learning Model - xGBoost 

    # Instantiation
    xgb_reg = xg.XGBRegressor(n_estimators = 10, seed = 123)
    # Fitting the model
    xgb_reg.fit(X, y)
    # Predict the model
    pred = xgb_reg.predict(input)

    return pred