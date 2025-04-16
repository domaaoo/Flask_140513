from flask import Flask, jsonify, request

app = Flask(__name__)  # utworzenie interfejsu serwera API

@app.route('/')  # kod podstrony z wykorzystaniem dekoratora
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')  # nowa podstrona
def mojastrona():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello')  # teraz obsługuje parametry z query string
def hello():
    name = request.args.get("name")  # pobieranie parametru z URL
    if name:
        return jsonify({"message": f"Hello {name}!"})
    else:
        return jsonify({"message": "Hello!"})

@app.route('/api/v1.0/predict')
def predict():
    try:
        num1 = float(request.args.get("num1", ""))
        num2 = float(request.args.get("num2", ""))
    except (ValueError, TypeError):
        return jsonify({"error": "Nieprawidlowe dane wejsciowe. To musza byc liczby"}), 400

    suma = num1 + num2
    score = 1 if suma > 5.8 else 0

    return jsonify({
        "prediction": score,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })

if __name__ == '__main__':
    app.run()
