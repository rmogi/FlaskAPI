import pandas as pd
import numpy as np
import pickle
# scikit-learnをインポート
from sklearn import tree


with open("C:/FlaskAPI/flaskapidir/x_traub.pickle", mode="rb") as f:
    my_tree_one = pickle.load(f)

test_data = pd.read_csv('flaskapidir/uploads/test_data.csv')
print(test_data)
"""
# 「train」の目的変数と説明変数の値を取得
target = train["Survived"].values
features_one = train[["Pclass", "Sex", "Age", "Fare"]].values
# 決定木の作成
my_tree_one = tree.DecisionTreeClassifier()
my_tree_one = my_tree_one.fit(features_one, target)
"""
# 「test」の説明変数の値を取得
test_features = test_data[["Pclass", "Sex", "Age", "Fare"]].values
# 「test」の説明変数を使って「my_tree_one」のモデルで予測
my_prediction = my_tree_one.predict(test_features)

print(my_prediction)