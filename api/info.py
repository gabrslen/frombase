from flask import Flask, jsonify
from control.names_control import NamesControl

app = Flask(__name__)

@app.route('/get_names', methods=['GET'])
def get_names():
    try:
        names = NamesControl.get_full_names_table()
        return jsonify(names), 200
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return jsonify({"error": "Erro ao buscar dados"}), 500

if __name__ == '__main__':
    app.run(debug=True)
