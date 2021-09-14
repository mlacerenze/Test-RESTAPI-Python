from flask import Flask, jsonify, request
app = Flask(__name__)

from products import products

# Testing server
@app.route('/test')
def test():
  return jsonify({'message': 'Hello world!'})

# Show all products
@app.route('/prod')
def getProducts():
  return jsonify({'products': products, 'message': 'List of products'})

# See a element of the list
@app.route('/prod/<string:product_name>')
def getProduct(product_name):
  # Create a for looop to find the product, if product match, return the product
  productsFound = [product for product in products if product['name'] == product_name] 
  if (len(productsFound) > 0):
    return jsonify({'product': productsFound[0]})
  return jsonify({'message': 'Product not found'})

@app.route('/prod', methods=['POST'])
def addProducts():
  newProduct = {
    # Add product in insomnia
    'name': request.json['name'],
    'model': request.json['model'],
    'price': request.json['price'],
    'quantity': request.json['quantity']
  }
  products.append(newProduct)
  return jsonify({'products': products, 'message': 'Product added'})

# Update a product
@app.route('/prod/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
  productsFound = [product for product in products if product['name'] == product_name]
  if (len(productsFound) > 0):
    productsFound[0]['name'] = request.json['name']
    productsFound[0]['model'] = request.json['model']
    productsFound[0]['price'] = request.json['price']
    productsFound[0]['quantity'] = request.json['quantity']
    return jsonify({'products': productsFound[0], 'message': 'Product Updated'})
  return jsonify({'message': 'Product not found'})

# Delete a product
@app.route('/prod/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
  productsFound = [product for product in products if product['name'] == product_name]
  if (len(productsFound) > 0):
    products.remove(productsFound[0])
    return jsonify({'products': products,  'message': 'Product deleted'})
  return jsonify({'message': 'Product not found'})

# @app.route('/prod/<string:model>')
# def getModel(model):
#   modelFound = [product for product in products if product['model'] == model]

if __name__ == '__main__':
  app.run(debug=True, port=8000)