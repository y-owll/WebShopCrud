from products import *


@app.route('/api/v1/products', methods=['GET'])
def get_products():
    return jsonify({'products': products.get_all_products()})


@app.route('/api/v1/products/<int:id>', methods=['GET'])
def get_products_by_id(id):
    return_value = products.get_products(id)
    return jsonify(return_value)


@app.route('/api/v1/products', methods=['POST'])
def add_products():
    request_data = request.get_json()
    products.add_products(request_data["name"], request_data["price"],
                    request_data["quantity"], request_data["quantityOfBuys"])
    response = Response("products added", 201, mimetype='application/json')
    return response


@app.route('/api/v1/products/<int:id>', methods=['PUT'])
def update_products(id):
    request_data = request.get_json()
    products.update_products(id, request_data['name'], request_data['price'], request_data["quantity"], request_data["quantityOfBuys"])
    response = Response("products Updated", status=200, mimetype='application/json')
    return response


@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def remove_products(id):
    products.delete_products(id)
    response = Response("products Deleted", status=200, mimetype='application/json')
    return response


@app.route('/api/v1/register', methods=['POST'])
def register ():
    response = Response("register successful", status=200, mimetype='application/json')
    return response


@app.route('/api/v1/login', methods=['POST'])
def login():
    response = Response("login successful", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=4000, debug=True)