from flask import Flask, request, jsonify, render_template_string
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Shahins Praxisarbeit fürs Modul 323"

#A1G
def add(a, b):
    return a + b

@app.route('/a1g/<int:a>/<int:b>', methods=['GET'])
def enpoint_a1g(a, b):
    return f'Resultat: {add(a, b)}'

#A1F
@app.route('/a1f', methods=['GET', 'POST'])
def convert_list_to_tuple():
    if request.method == 'POST':
        try:
            data = request.form.get('listInput') # Daten aus Formular holen 
            if data:
                list_data = [int(item.strip()) for item in data.split(',')] # String in Liste umwandeln
                result_tuple = tuple(list_data) # Liste in Tupel umwandeln
                try:
                    result_tuple[0] = 'a' # Versuch, das erste Element zu ändern
                    message = "Tupel veraendert."
                except TypeError as e:
                    message = "Tupel nicht veraendert. Ist nicht moeglich"
                return jsonify({"result_tuple": result_tuple, "message": message})
            else:
                return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return render_template_string("""
            <form method="POST">
                <label for="listInput">Geben Sie Ihre Liste ein (z. B. 1, 2, 3, 4):</label>
                <input type="text" id="listInput" name="listInput">
                <input type="submit" value="In Tupel konvertieren">
            </form>""")
    
#A1E
#OO
class SquareCalculator:
    def __init__(self):
        pass
    def calculate_square(self, a):
        return a * a
    
# procedural
def calculate_square(a):
    return a * a

# functional
calculate_square = lambda a: a * a

@app.route('/a1e/<int:a>', methods=['GET'])
def endpoint_a1e(a):
    calc = SquareCalculator()
    oo_res = calc.calculate_square(a)
    proc_res = calculate_square(a)
    func_res = calculate_square(a)
    return f'Resultat: OO: {oo_res}, Procedural: {proc_res}, Functional: {func_res}'


#B1G
def gcd(a, b):
    r = a % b
    while b != 0:
        a, b = b, a % b
    return a

@app.route('/b1g/<int:a>/<int:b>', methods=['GET'])
def endpoint_b1g(a, b):
    return f'Resultat: {gcd(a, b)}'


#B1F
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/b1f/<int:n>', methods=['GET'])
def endpoint_b1f(n):
    return f'Resultat: {fibonacci(n)}'


if __name__ == '__main__':
    app.run(debug=True, port=5000)