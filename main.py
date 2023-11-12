from flask import Flask, request, jsonify, render_template
from functools import reduce
import timeit

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

@app.route('/a1g', methods=['POST'])
def endpoint_a1g():
    data = request.get_json()
    operation = data['operation']
    num1 = data['num1']
    num2 = data['num2']
    match operation:
        case 'add':
            sum = add(num1, num2)
        case 'sub':
            sum = sub(num1, num2)
        case 'mul':
            sum = mul(num1, num2)
    return jsonify({"result": sum}), 200

#A1F
@app.route('/a1f', methods=['POST'])
def endpoint_a1f():
        data = request.get_json()
        if data:
            result_tuple = tuple(data) # Liste in Tupel umwandeln
            try:
                result_tuple[0] = 'a' # Versuch, das erste Element zu ändern
                message = "Tupel veraendert."
            except TypeError as e:
                message = "Tupel nicht verändert. Ist nicht möglich 💀"
            return jsonify({"result_tuple": result_tuple, "message": message}), 200
        else:
            return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
    
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

def measure_execution_time(func, *args):
    start_time = timeit.default_timer()
    result = func(*args)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time

@app.route('/a1e', methods=['POST'])
def endpoint_a1e():
    data = request.get_json()
    calc = SquareCalculator()
    oo_res, oo_time = measure_execution_time(calc.calculate_square, data)
    proc_res, proc_time = measure_execution_time(calculate_square, data)
    func_res, func_time = measure_execution_time(calculate_square, data)
    # Sortierung und Formatierung der Ergebnisse für den Vergleich
    results = [
        {"type": "Object Oriented", "result": oo_res, "executiontime": oo_time},
        {"type": "Procedural", "result": proc_res, "executiontime": proc_time},
        {"type": "Functional", "result": func_res, "executiontime": func_time}
    ]
    return jsonify({"sorted_results": results}), 200


#B1G
def gcd(a, b):
    """
    Berechnet den größten gemeinsamen Teiler von a und b mithilfe des Euklidischen Algorithmus. 
    Der Algorithmus wiederholt die Division, bis der Rest 0 ist. 
    Der GCD ist dann die nicht-0-letzte Restzahl.
    """
    while b != 0:
        a, b = b, a % b
    return a

@app.route('/b1g', methods=['POST'])
def endpoint_b1g():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = gcd(a, b)
    return jsonify({"result": result}), 200


#B1F
def fibonacci(n):
    """
    berechnet die Fibonacci-Zahl für die gegebene Position n in der Fibonacci-Folge. 
    Die Fibonacci-Folge beginnt mit den Zahlen 0 und 1, und jede nachfolgende Zahl 
    ist die Summe der beiden vorherigen Zahlen.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/b1f', methods=['POST'])
def endpoint_b1f():
    data = request.get_json()
    n = data['n']
    result = fibonacci(n)
    return jsonify({"result": result}), 200

#B1E
def bubble_sort(arr):
    """
    Sortiert eine Liste arr mithilfe des Bubble-Sort-Algorithmus.
    Der Bubble-Sort-Algorithmus vergleicht benachbarte Elemente und tauscht sie, wenn sie in der falschen Reihenfolge sind.
    Dieser Prozess wird so lange wiederholt, bis die gesamte Liste sortiert ist.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tausche die benachbarten Elemente, wenn sie in der falschen Reihenfolge sind.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def format_nums(numbers):
    if numbers is not None:
        return ' '.join(map(str, numbers))
    return None

@app.route('/b1e', methods=['POST'])
def endpoint_b1e():
        data = request.get_json()
        if data:
            bubble_sort(data)
            formatted_nums = format_nums(data)
            return jsonify({"result": data, "formatted_result": formatted_nums}), 200
        else:
            return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste"}), 400
    
#B2G
@app.route('/b2g', methods=['POST'])
def endpoint_b2g():
    data = request.get_json()
    a = data['a']
    b = data['b']
    sum = add(a, b)
    return jsonify({"result": sum}), 200

#B2F
def power_of(func, a, b):
    """
    Die Funktion power_of akzeptiert eine Funktion func, sowie zwei Zahlen a und b. 
    Sie wendet die Funktion func (bis jetzt add, sub, mul) auf die Zahlen an und verwendet das Ergebnis 
    als Exponenten, um a potenziert mit b zu berechnen.
    """
    b = func(a, b)
    return a ** b

@app.route('/b2f', methods=['POST'])
def endpoint_b2f():
    try:
        data = request.get_json()
        operation = data['operation']
        num1 = data['num1']
        num2 = data['num2']
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
            return jsonify({"result": result}), 200
        else:
            return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#B2E    
def greet(greeting_text):
    def display_name(name):
        return f'{greeting_text} {name}!'
    return display_name

@app.route('/b2e', methods=['POST'])
def endpoint_b2e():
    try:
        data = request.get_json()
        text = data['text']
        name = data['name']
        if text and name:
            text = greet(text)
            result = text(name)
            return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#B3G
@app.route('/b3g', methods=['POST'])
def endpoint_b3g():
        try:
            data = request.get_json()
            if data:
                square = lambda data: data ** 2
                return jsonify({"result": square(int(data))}), 200
            else:
                return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

#B3F
@app.route('/b3f', methods=['POST'])
def endpoint_b3f():
    try:
        data = request.get_json()
        list1 = data['list1']
        list2 = data['list2']
        if list1 and list2:
            result = list(map(lambda x, y: max(x, y), list1, list2))
            return jsonify({"result": result}), 200
        else:
            return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#B3E
@app.route('/b3e', methods=['POST'])
def endpoint_b3e():
    try:
        data = request.get_json()
        list = data['list']
        sort = data['sort']
        if list:
            match sort:
                case 'asc':
                    list = sorted(list, key=lambda x: len(x))
                case 'desc':
                    list = sorted(list, key=lambda x: len(x), reverse=True)
            return jsonify({"result": list}), 200
        else:
            return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#B4G
@app.route('/b4g', methods=['POST'])
def endpoint_b4g():
    try:
        data = request.get_json()
        operation = data['operation']
        input_list = data['list']
        if data:
            match operation:
                case 'map':
                    result = list(map(lambda x: x * x, input_list))
                case 'filter':
                    result = list(filter(lambda x: x % 2 == 0, input_list))
                case 'reduce':
                    input_list = list(map(int, input_list))
                    result = reduce(lambda x, y: x + y, input_list)
            return jsonify({"result": result}), 200
        else:
            return jsonify({"error": "Ungueltige Daten. Bitte senden Sie eine Liste."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#B4F
@app.route('/b4f', methods=['POST'])
def endpoint_b4f():
    data = request.get_json()
    # Potenziert jede Zahl in der Liste mit 3
    # Filtert alle ungeraden Zahlen aus der Liste
    # Addiert alle Zahlen in der übrigen Liste zusammen
    result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 3, data)))
    return jsonify({"result": result}), 200

#B4E
def get_average_population(data):
    filtered_populations = list(map(lambda x: x['population'], filter(lambda x: x['population'] > 10000000 and x['region'] == 'Asia', data)))
    total_population = reduce(lambda x, y: x + y, filtered_populations, 0)
    return round(total_population / len(filtered_populations))

def rearange_data(data):
    filtered_populations = list(filter(lambda x: x['population'] > 10000000 and x['region'] == 'Asia', data))
    reduced_data = list(map(lambda x: {'name': x['name'], 'capital': x['capital'], 'population': x['population']}, filtered_populations))
    return sorted(reduced_data, key=lambda x: x['population'], reverse=True)


@app.route('/b4e', methods=['POST'])
def endpoint_b4e():
    data = request.get_json()
    average_population = get_average_population(data)
    rearanged_data = rearange_data(data)
    return jsonify({"average_population_asia_10": average_population, 
                    "rearanged_data": rearanged_data}), 200
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)