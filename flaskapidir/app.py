#!/usr/bin/env python3
from flask import Flask
from upload import _upload_file
from titanic import decision_tree

# ファイルアップロード先のディレクトリ
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return _upload_file(app.config['UPLOAD_FOLDER'])


@app.route('/result', methods=['GET', 'POST'])
def result():
    return decision_tree()


if __name__ == '__main__':
    app.run(host='172.31.5.100', port=8080, debug=True)
