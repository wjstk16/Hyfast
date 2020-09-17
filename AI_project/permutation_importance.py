from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import time
from matplotlib import pyplot as plt
import sys
import eli5
from eli5.sklearn import PermutationImportance

data = pd.read_csv("./network-2020_08_18_07_15_AM_metrics.csv")
col = list(map(str, data.columns))
x = data[col[:-1]]
y = data[col[-1]]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.4)
x_test, x_val, y_test, y_val = train_test_split(x_test,y_test, test_size=0.5)

model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(x_train, y_train)
perm = PermutationImportance(model, scoring = "f1", random_state = 42).fit(x_train, y_train)
eli5.show_weights(perm, top = 80, feature_names = x_train.columns.tolist())
