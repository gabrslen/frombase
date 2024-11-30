from flask import Flask, jsonify, request
from flask_cors import CORS
from control.names_control import NamesControl

app = Flask(__name__)
CORS(app)

@app.route('/login_validation', methods=['GET'])
def login_validation():
    try:
        retorno = ''
        login = request.args.get('login')
        if login:
            login_list = NamesControl.get_names_in_table(login)
            print(login_list)
        else:
            raise RuntimeError('Digite o login.')
        return jsonify(retorno)
    except Exception as e:
        app.logger.error(f"Erro ao fazer login: {e}")
        return jsonify({'data':{'error':'Erro ao logst.','details': str(e)}}), 500

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
        app.logger.error(f"Error fetching data: {e}")
        return jsonify({"error": "Error fetching data.", "details": str(e)}), 500

@app.route('/set_name', methods=['POST'])
def set_name():
    data = request.get_json()
    try:
        NamesControl.set_name_in_table(data)
        return jsonify({"message": "Successful inputted name!"}), 201
    except ValueError as e:
        app.logger.error(f"Validation Error: {e}")
        return jsonify({"error": "Validation Error.", "details": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Error saving name: {e}")
        return jsonify({"error": "Error saving name.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
