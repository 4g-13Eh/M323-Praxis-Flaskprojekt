from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Shahins Praxisarbeit fürs Modul 323"

#A1G
def add(a, b):
    return a + b

@app.route('/A1G/<int:a>/<int:b>', methods=['GET'])
def enpoint_a1g(a, b):
    return f'Resultat: {add(a, b)}'


if __name__ == '__main__':
    app.run(debug=True, port=5000)