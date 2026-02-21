import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

cancer=pd.read_csv("global_cancer_patients_2015_2024.xls")


from sklearn.preprocessing import LabelEncoder
ol= LabelEncoder()
stage = ol.fit_transform(cancer[["Cancer_Stage"]])


clf = tree.DecisionTreeClassifier()

X=cancer[["Genetic_Risk","Air_Pollution","Alcohol_Use","Smoking","Obesity_Level"]]
y= stage


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.02, random_state=0
)


clf.fit(X_train,y_train)


y_pred = clf.predict(X)

joblib.dump(clf, 'cancermodel.pkl')
joblib.dump(ol, 'LabelEncoder.pkl')
print("cancer model is saved in cancermodel.pkl file")
