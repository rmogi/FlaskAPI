import pandas as pd
import numpy as np
import pickle
# scikit-learnをインポート
from sklearn import tree


def decision_tree():
    with open("./flaskapidir/x_traub.pickle", mode="rb") as f:
        tree = pickle.load(f)

        test_data = pd.read_csv('./flaskapidir/uploads/test_data.csv')
        print(test_data)

        # 「test」の説明変数の値を取得
        test_features = test_data[["Pclass", "Sex", "Age", "Fare"]].values
        # 「test」の説明変数を使って「my_tree_one」のモデルで予測
        prediction = tree.predict(test_features)

        return prediction()

    return render_template('result.html')

    # print(prediction)
