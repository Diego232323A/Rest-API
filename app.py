from flask import Flask, jsonify

app = Flask(__name__)

# Ruta raíz que devuelve un mensaje de "Hola Mundo"
@app.route('/', methods=['GET'])
def hello_world():
    return "Hola Mundo desde una REST API con Flask"
    # return jsonify({"message": "Hola Mundo desde una REST API con Flask"})

# Ejecutar la aplicación en modo de depuración
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)