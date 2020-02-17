from flask import Flask, jsonify, request 

app = Flask(__name__) 

from products import products

@app.route('/ping', methods=['GET'])
def ping():
    return 'Pong'


@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message":"Lista de Productos"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    print(product_name)
    productsFound=[product for product in products if product['name']==product_name]
    if (len(productsFound)>0):
        return jsonify({"products":productsFound[0]})
    return jsonify({"message":"producto no encontrado"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product={
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    print (request.json) 
    return jsonify({"message":"Producto agregado con exito","productos":products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    producto_found= [product for product in products if product['name']==product_name]
    if(len(producto_found)>0):
        producto_found[0]['price']=request.json['price']
        producto_found[0]['quantity']=request.json['quantity']
        return jsonify({
            "message": "Producto actulizado",
            "productos": producto_found[0]
        })
    return jsonify({"message": "producto no encontrado"})


@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound=[product for product in products if product['name']==product_name]
    if(len(productFound)>0):
        products.remove(productFound[0])
        return jsonify({
            "message": "Producto eliminado",
            "productos": products
            })
    return jsonify({"message": "Producto no encontrado"})



if __name__ == '__main__':
    app.run(debug=True, port=4000)