from flask import Flask, request, jsonify, render_template_string, render_template
from functools import reduce
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#A1G
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

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

#B1E
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def print_nums(numbers):
    for num in numbers:
        print(num, end=" ")
    print()

@app.route('/b1e', methods=['GET', 'POST'])
def endpoint_b1e():
    if request.method == 'POST':
        try:
            data = request.form.get('listInput') # Daten aus Formular holen 
            if data:
                list_data = [int(item.strip()) for item in data.split(',')] # String in Liste umwandeln
                bubble_sort(list_data)
                return jsonify({"result": list_data})
            else:
                return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return render_template_string("""
            <form method="POST">
                <label for="listInput">Geben Sie Ihre Liste ein (z. B. 29, 2, 1, 40):</label>
                <input type="text" id="listInput" name="listInput">
                <input type="submit" value="Sortieren">
            </form>""")
    
#B2G
@app.route('/b2g/<int:a>/<int:b>', methods=['GET'])
def enpoint_b2g(a, b):
    sum = add(a, b)
    return jsonify({"result": sum})

#B2F
def power_of(func, a, b):
    b = func(a, b)
    return a ** b

@app.route('/b2f', methods=['GET', 'POST'])
def endpoint_b2f():
    if request.method == 'POST':
        try:
            num1 = request.form.get('num1') # Daten aus Formular holen 
            num2 = request.form.get('num2') # Daten aus Formular holen
            operation = request.form.get('operation') # Daten aus Formular holen
            if num1 and num2:
                num1 = int(num1)
                num2 = int(num2)
                match operation:
                    case 'add':
                        operation = add
                    case 'sub':
                        operation = sub
                    case 'mul':
                        operation = mul
                result = power_of(operation, num1, num2)
                return jsonify({"result": result})
            else:
                return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return render_template_string("""
            <form method="POST">
                <p>Die Basis ist die erste Zahl, der Exponent wird von den zwei Zahlen und der ausgewählten Operation bestummen</p>
                <label for="num1">Geben Sie Ihre erste Zahl ein:</label>
                <input type="number" id="num1" name="num1">
                <label for="num2">Geben Sie Ihre zweite Zahl ein:</label>
                <input type="number" id="num2" name="num2">
                <label for="operation">Wählen Sie Ihre Operation:</label>
                <select name="operation" id="operation">
                    <option value="add">Addieren</option>
                    <option value="sub">Subtrahieren</option>
                    <option value="mul">Multiplizieren</option>
                <input type="submit" value="Potenzieren">
            </form>""")

#B2E    
def greet(greeting_text):
    def display_name(name):
        return f'{greeting_text} {name}!'
    return display_name

@app.route('/b2e', methods=['GET', 'POST'])
def endpoint_b2e():
    if request.method == 'POST':
        try:
            text = request.form.get('greeting_text')  # Daten aus Formular holen
            name = request.form.get('name')  # Daten aus Formular holen
            if text and name:
                text = greet(text)
                result = text(name)
                return jsonify({"result": result})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return render_template_string("""
            <form method="POST">
                <label for="greeting_text">Geben Sie Ihren Text ein:</label>
                <input type="text" id="greeting_text" name="greeting_text">
                <label for="name">Geben Sie Ihren Namen ein:</label>
                <input type="text" id="name" name="name">
                <input type="submit" value="Ausgeben">
            </form>""")
    
#B3G
@app.route('/b3g', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        try:
            data = request.form.get('num') # Daten aus Formular holen 
            if data:
                square = lambda data: data ** 2
                return jsonify({"result": square(int(data))})
            else:
                return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return render_template_string("""
            <form method="POST">
                <label for="listInput">Geben Sie eine Zahl ein:</label>
                <input type="number" id="num" name="num">
                <input type="submit" value="Quadrieren">
            </form>""")

#B3F
@app.route('/b3f', methods=['GET', 'POST'])
def endpoint_b3f():
    if request.method == 'POST':
        try:
            list1 = request.form.get('listInput1') # Daten aus Formular holen 
            list2 = request.form.get('listInput2') # Daten aus Formular holen
            if list1 and list2:
                list1 = list1.split(",")
                list2 = list2.split(",")
                result = list(map(lambda x, y: max(int(x), int(y)), list1, list2))
                return jsonify({"result": result})
            else:
                return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return render_template_string("""
            <form method="POST">
                <label for="listInput">Geben Sie zwei gleich grosse Listen ein (z. B. 1, 2, 3, 4). Eine neue Liste mit der 
                                      jeweils grössten Zahl für jeden Index wird zurückgegeben:</label>
                <input type="text" id="listInput1" name="listInput1">
                <input type="text" id="listInput2" name="listInput2">
                <input type="submit" value="Senden">
            </form>""")
    
#B3E
@app.route('/b3e', methods=['GET', 'POST'])
def endpoint_b3e():
    if request.method == 'POST':
        try:
            list = request.form.get('list')
            sort = request.form.get('sort')
            if list:
                list = list.split(",")
                match sort:
                    case 'asc':
                        list = sorted(list, key=lambda x: len(x))
                    case 'desc':
                        list = sorted(list, key=lambda x: len(x), reverse=True)
                return jsonify({"result": list})
            else:
                return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return render_template_string("""
            <form method="POST">
                <label for="list">Geben Sie eine Liste ein. Eine sortierte Liste wird zurückgegeben:</label>
                <input type="text" id="list" name="list">
                <select name="sort" id="sort">
                    <option value="asc">Aufsteigend</option>
                    <option value="desc">Absteigend</option>
                </select>
                <input type="submit" value="Senden">
            </form>""")

#B4G
@app.route('/b4g', methods=['GET', 'POST'])
def endpoint_b4g():
    if request.method == 'POST':
        try:
            input_list = request.form.get('list')
            operation = request.form.get('operation')
            if input_list:
                input_list = json.loads(input_list)
                match operation:
                    case 'map':
                        result = list(map(lambda x: x * x, input_list))
                    case 'filter':
                        result = list(filter(lambda x: x % 2 == 0, input_list))
                    case 'reduce':
                        input_list = list(map(int, input_list))
                        result = reduce(lambda x, y: x + y, input_list)
                return jsonify({"result": result})
            else:
                return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return render_template_string("""
            <form method="POST">
                <label for="list">Geben Sie eine Zahlenliste ein (z.B. [3,4,5,2]):</label>
                <input type="text" id="list" name="list">
                <select name="operation" id="operation">
                    <option value="map">Map</option>
                    <option value="filter">Filter</option>
                    <option value="reduce">Reduce</option>
                </select>
                <input type="submit" value="Senden">
            </form>""")
    

#B4F
@app.route('/b4f', methods=['POST'])
def endpoint_b4f():
    data = request.get_json()
    result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 3, data)))
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)