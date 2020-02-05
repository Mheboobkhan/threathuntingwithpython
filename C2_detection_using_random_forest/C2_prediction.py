# Detecting the C2 Using random forest algorith 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('/home/wh/my_project_dir/http.csv')
X = df.drop(['ip.src','ip.dst','tcp.dstport','Satus'],axis=1)
Y = df.iloc[:,5]
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

classifier = RandomForestClassifier(n_estimators=12,criterion = 'entropy',random_state=0)
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
print (cm)
print (accuracy_score(y_test, y_pred))
