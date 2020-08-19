from flask import Flask
from upload import _upload_file


UPLOAD_FOLDER = './flaskapidir/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return _upload_file(app.config['UPLOAD_FOLDER'])


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
