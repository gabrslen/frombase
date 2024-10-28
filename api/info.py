# info.py

from flask import Flask, jsonify, request
from control.names_control import NamesControl

app = Flask(__name__)

@app.route('/get_names', methods=['GET'])
def get_names():
    try:
        name_to_find = request.args.get('name')
        if name_to_find:
            names = NamesControl.get_names_in_table(name_to_find)
        else:
            names = NamesControl.get_full_names_table()
        return jsonify(names), 200
    except Exception as e:
        app.logger.error(f"Erro ao buscar dados: {e}")
        return jsonify({"error": "Erro ao buscar dados", "details": str(e)}), 500

@app.route('/set_name', methods=['POST'])
def set_name():
    data = request.get_json()
    try:
        NamesControl.set_name_in_table(data)
        return jsonify({"message": "Nome inserido com sucesso!"}), 201
    except ValueError as e:
        app.logger.error(f"Erro de Validação: {e}")
        return jsonify({"error": "Erro de Validação", "details": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Erro ao inserir nome: {e}")
        return jsonify({"error": "Erro ao inserir nome", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
