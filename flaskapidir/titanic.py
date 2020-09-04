import pandas as pd
import pickle
# scikit-learnをインポート
from sklearn import tree
from flask import request, redirect, url_for, render_template


def decision_tree():
    with open("x_traub.pickle", mode="rb") as f:
        tree = pickle.load(f)

        test_data = pd.read_csv('uploads/test_data.csv')
        print(test_data)

        # 「test」の説明変数の値を取得
        test_features = test_data[["Pclass", "Sex", "Age", "Fare"]].values
        # 「test」の説明変数を使って「tree」のモデルで予測
        prediction = tree.predict(test_features)

        if prediction == 1:
            Survived = "生存"
        elif prediction == 0:
            Survived = "死亡"

    return render_template('result.html', prediction=Survived)
