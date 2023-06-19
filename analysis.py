import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Models
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Acurracy
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

with open('./data/test_products.json', 'r') as raw_test_data:
    raw = raw_test_data.read()
    test_data_json = json.loads(raw)

with open('./data/train_products.json', 'r') as raw_train_data:
    raw = raw_train_data.read()
    train_data_json = json.loads(raw)

data_test = [test_data_json[data_idx] for data_idx in test_data_json.keys()]
test_data = pd.DataFrame(data_test)

# pp(train_data_json['0'])
data_train = [train_data_json[data_idx] for data_idx in train_data_json.keys()]
train_data = pd.DataFrame(data_train)

# train_data['categories_hierarchy_len'] = train_data.categories_hierarchy.apply(
#     len)
# train_data['ingredients_len'] = train_data.ingredients.apply(len)

# Convert unknown to NA
# 'additives_count', 'calcium_100g' 'carbohydrates_100g', 'energy_kcal_100g'
# 'fat_100g', 'fiber_100g', 'proteins_100g', 'salt_100g', 'sodium_100g', 'sugars_100g', 'nutrition_grade',

# train_data['additives_count'] = np.where(train_data.additives_count == 'unknown', np.NAN, train_data.additives_count)

# Check different matirials
# 'packaging_materials'
# train_data['packaging_materials']

train_data['len_packaging'] = train_data['packaging_materials'].apply(len)
test_data['len_packaging'] = test_data['packaging_materials'].apply(len)

# for package in train_data['packaging_materials']:
#     [pack.split(':') for pack in package]
#     breakpoint()

# breakpoint()
# 0.7956667422909616 0.795392737162054
# X_train = train_data[['is_beverage', 'non_recyclable_and_non_biodegradable_materials_count',
#                       'est_co2_agriculture', 'est_co2_consumption', 'est_co2_distribution',
#                       'est_co2_packaging', 'est_co2_processing', 'est_co2_transportation',
#                       'categories_hierarchy_len', 'ingredients_len']]

# 0.8196056622444258 0.8198688209886418
# X_train = train_data[['non_recyclable_and_non_biodegradable_materials_count',
#                       'est_co2_agriculture', 'est_co2_consumption', 'est_co2_distribution',
#                       'est_co2_packaging', 'est_co2_processing', 'est_co2_transportation',
#                       ]]

# 0.8202161973094372 0.8203487442009278
# X_train = train_data[['non_recyclable_and_non_biodegradable_materials_count', 'is_beverage',
#                       'est_co2_agriculture', 'est_co2_consumption', 'est_co2_distribution',
#                       'est_co2_packaging', 'est_co2_processing', 'est_co2_transportation',
#                       ]]

# 0.8289547154695583 0.8283474644056951
# X_train = train_data[['non_recyclable_and_non_biodegradable_materials_count', 'is_beverage',
#                       'est_co2_agriculture', 'est_co2_consumption', 'est_co2_distribution',
#                       'est_co2_packaging', 'est_co2_processing', 'est_co2_transportation',
#                       'len_packaging'
#                       ]]

X_train = train_data[['non_recyclable_and_non_biodegradable_materials_count', 'is_beverage',
                      'est_co2_agriculture', 'est_co2_consumption', 'est_co2_distribution',
                      'est_co2_packaging', 'est_co2_processing', 'est_co2_transportation',
                      'len_packaging'
                      ]]
X = X_train.to_numpy()
y_train = train_data['ecoscore_grade']
y = y_train.to_numpy()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
# breakpoint()

# Inicializar modelos
decision_tree_train = DecisionTreeClassifier()
# logistic_regression = LogisticRegression()
# svm = SVC()

decision_tree_train.fit(X_train, y_train)
# logistic_regression.fit(X_train, y_train)
# svm.fit(X_train, y_train)

# Predicciones de los modelos
y_pred_decision_tree = decision_tree_train.predict(X_test)
# y_pred_logistic_regression = logistic_regression.predict(X_test)
# y_pred_svm = svm.predict(X_test)
# print(y_pred_decision_tree, y_pred_logistic_regression, y_pred_svm)

# F1-score
f1_decision_tree = f1_score(y_test, y_pred_decision_tree, average='weighted')
# f1_logistic_regression = f1_score(y_test, y_pred_logistic_regression, average='weighted')
# f1_svm = f1_score(y_test, y_pred_svm, average='weighted')
# print(f1_decision_tree, f1_logistic_regression, f1_svm)
print('F1 Score')
print(f1_decision_tree)
# Matriz de confusión
cm_decision_tree = confusion_matrix(y_test, y_pred_decision_tree)
# cm_logistic_regression = confusion_matrix(y_test, y_pred_logistic_regression)
# cm_svm = confusion_matrix(y_test, y_pred_svm)
# print(cm_decision_tree, cm_logistic_regression, cm_svm)
print('Confusion Matriz')
print(cm_decision_tree)
# Precisión
accuracy_decision_tree = accuracy_score(y_test, y_pred_decision_tree)
# accuracy_logistic_regression = accuracy_score(y_test, y_pred_logistic_regression)
# accuracy_svm = accuracy_score(y_test, y_pred_svm)
# print(accuracy_decision_tree, accuracy_logistic_regression, accuracy_svm)
print('Accuracy Score')
print(accuracy_decision_tree)
# TRAIN ALL
decision_tree = DecisionTreeClassifier()
# logistic_regression = LogisticRegression()
# svm = SVC()

# breakpoint()

X_test = test_data[['non_recyclable_and_non_biodegradable_materials_count', 'is_beverage',
                    'est_co2_agriculture', 'est_co2_consumption', 'est_co2_distribution',
                    'est_co2_packaging', 'est_co2_processing', 'est_co2_transportation',
                    'len_packaging'
                    ]]
X_test = X_test.to_numpy()

decision_tree.fit(X, y)
# logistic_regression.fit(X_train, y_train)
# svm.fit(X_train, y_train)

# Predicciones de los modelos
y_pred_decision_tree = decision_tree.predict(X_test)
data = pd.DataFrame(y_pred_decision_tree, columns=['target'])
breakpoint()
data.to_json('predictions.json')
