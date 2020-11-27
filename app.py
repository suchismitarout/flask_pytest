from flask import Flask, jsonify
from service.registry_service import RegistryService
from flask import request

app = Flask(__name__)

# create service object
service = RegistryService()


@app.route('/students', methods=['GET'])
def get_all_data():
    """
        it'll call get_all_data from service module
        and return all students data
    :return:
    """
    return jsonify(service.get_all_data())


@app.route('/students/bynames', methods=['GET'])
def get_all_by_name():
    """
         it'll call get_all_by_name from service module
        and return student's data by name
    :return:
    """
    name = request.args['name']
    return jsonify(service.get_all_data_by_name(name))


@app.route('/students/byid', methods=['GET'])
def get_all_by_id():
    """
         it'll call get_all_by_id from service module
         and return student's data by id
    :return:
    """
    id = request.args['id']
    return jsonify(service.get_all_data_by_id(id))


if __name__ == '__main__':
    app.run(debug=True)
