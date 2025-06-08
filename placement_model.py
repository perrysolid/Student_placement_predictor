import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox, ttk
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score, roc_curve
from imblearn.over_sampling import SMOTE
import webbrowser
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

feature_weights = {
    'CGPA': 3.0,
    'Internships': 5.5,
    'Projects': 0.5,
    'Workshops/Certifications': 1.5,
    'SSC_Marks': 0.004,
    'HSC_Marks': 0.008
}
fields = list(feature_weights.keys())


X = data[fields]
y = data['PlacementStatus']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


X_train_weighted = X_train.copy()
X_test_weighted = X_test.copy()
for column, weight in feature_weights.items():
    X_train_weighted[column] *= weight
    X_test_weighted[column] *= weight


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_weighted)
X_test_scaled = scaler.transform(X_test_weighted)


poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)


log_model = LogisticRegression(solver='liblinear')
log_model.fit(X_train_poly, y_train)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_poly, y_train)


y_pred_rf = rf_model.predict(X_test_poly)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
f1_rf = f1_score(y_test, y_pred_rf)
precision_rf = precision_score(y_test, y_pred_rf)
recall_rf = recall_score(y_test, y_pred_rf)
roc_auc_rf = roc_auc_score(y_test, rf_model.predict_proba(X_test_poly)[:, 1])


y_pred = log_model.predict(X_test_poly)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, log_model.predict_proba(X_test_poly)[:, 1])


if accuracy_rf > accuracy:
    model = rf_model
    best_model_name = "Random Forest"
    accuracy = accuracy_rf
    f1 = f1_rf
    precision = precision_rf
    recall = recall_rf
    roc_auc = roc_auc_rf
else:
    model = log_model
    best_model_name = "Logistic Regression"
