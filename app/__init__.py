from flask import Flask, jsonify, request
from config import Config
from app.database import DatabaseConnection

def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)

    # 1.1. Obtener un cliente
    # GET /customers/<int:customer_id>
   
    @app.route('/customers/<int:customer_id>', methods=['GET'])
    def get_customer(customer_id):
        query = "SELECT customer_id, first_name, last_name, email, phone, street, city, state, zip_code FROM sales.customers WHERE customer_id = %s;"
        params = customer_id,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return {
            'customer_id': result[0],
            'first_name': result[1],
            'last_name': result[2],
            'email': result[3],
            'phone': result[4],
            'street': result[5],
            'city': result[6],
            'state': result[7],
            'zip_code': result[8]
            }, 200
        return {"msg": "No se encontró el actor"}, 404

    
    # 1.2. Obtener el listado de clientes
    # GET /customers

    @app.route('/customers', methods=['GET'])
    def get_customers():
        query = "SELECT customer_id, first_name, last_name, email, phone, street, city, state, zip_code FROM sales.customers"
        results = DatabaseConnection.fetch_all(query)
        customers = []
        for result in results:
            customers.append({
            'customer_id': result[0],
                'first_name': result[1],
                'last_name': result[2],
                'email': result[3],
                'phone': result[4],
                'street': result[5],
                'city': result[6],
                'state': result[7],
                'zip_code': result[8]
            })
        return customers, 200
    
        
    # 1.3. Registrar un cliente
    # POST /customers
    
    @app.route('/customers_post', methods=['POST'])
    def create_customer():
        sql = "INSERT INTO sales.customers (first_name, last_name, last_update, phone, street, city, state, zip_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,);"
        params = request.args.get('first_name', ''), request.args.get('last_name', ''), 
        request.args.get('first_name', '')
        DatabaseConnection.execute_query(sql, params)
        
        return {"msg": "Customers creado con éxito"}, 201
    
    
    # 1.4. Modificar un cliente
    # PUT /customers/<int:customer_id>
    
    @app.route('/customers_put/<int:customer_id>', methods=['PUT'])
    def update_actor(customer_id):
        query = "UPDATE sales.customers SET first_name = %s, last_name = %s, last_update = %s, phone = %s, street = %s, city = %s, state = %s, zip_code = %s WHERE customer_id = %s"
        params = request.args.get('first_name', ''), request.args.get('last_name', ''), request.args.get('last_update', ''), request.args.get('phone', ''), request.args.get('street', ''), request.args.get('city', ''), request.args.get('state', ''), request.args.get('zip_code', ''), customer_id
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Datos del cliente actualizados con éxito"}, 200
        
    
    

    # 1.5. Eliminar un cliente
    # DELETE /customers/<int:customer_id>
    
    @app.route('/customers_delete/<int:customer_id>', methods=['DELETE'])
    def delete_customer(customer_id):       
        query = "DELETE FROM sales.customers WHERE customer_id = %s"
        params = customer_id
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Cliente eliminado con éxito"}, 200
    
     
    
           
    # 2.1. Obtener un producto
    # GET /products/<int:product_id>

    
    @app.route('/products/<int:product_id>', methods=['GET'])
    def get_product(product_id):
        query = "SELECT product_id, product_name, brand_id, category_id, model_year, list_price FROM production.products WHERE product_id = %s;"
        params = product_id,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return {
            'product_id': result[0],
            'product_name': result[1],
            'brand_id': result[2],
            'category_id': result[3],
            'model_year': result[4],
            'list_price': result[5]
            }, 200
            
        return {"msg": "No se encontrón los productos"}, 404
     

    # 2.2. Obtener un listado de productos
    # GET /products

    @app.route('/products', methods=['GET'])
    def get_products():
        query = "SELECT product_id, product_name, brand_id, category_id, model_year, list_price FROM production.products;"
        results = DatabaseConnection.fetch_all(query)
        products = []
        for result in results:
            products.append({
            'product_id': result[0],
            'product_name': result[1],
            'brand_id': result[2],
            'category_id': result[3],
            'model_year': result[4],
            'list_price': result[5]
            })
        return products, 200

    # 2.3. Registrar un producto
    # POST /products
    @app.route('/products_post', methods=['POST'])
    def create_product():
        sql = "INSERT INTO production.products (product_name, brand_id, category_id, model_year, list_price) VALUES (%s,%s,%s,%s,%s);"
        params = request.args.get('product_name', ''), request.args.get('brand_id', ''), request.args.get('category_id', ''), request.args.get('model_year', ''), request.args.get('list_price', '')
        DatabaseConnection.execute_query(sql, params)
        
        return {"msg": "Producto creado con éxito"}, 201
    

    # 2.4. Modificar un producto
    # PUT /products/<int:product_id>
    @app.route('/products_put/<int:product_id>', methods=['PUT'])
    def update_product(product_id):
        sql = "UPDATE production.products SET product_name = %s, brand_id = %s, category_id = %s, model_year = %s, list_price = %s WHERE product_id = %s"
        params = request.args.get('product_name', ''), request.args.get('brand_id', ''), request.args.get('category_id', ''), request.args.get('model_year', ''), request.args.get('list_price', ''), product_id
        DatabaseConnection.execute_query(sql, params)
        return {"msg": "Datos del producto actualizados con éxito"}, 200

    # 2.5. Eliminar un producto
    # DELETE /products/<int:product_id>
    @app.route('/products_delete/<int:product_id>', methods=['DELETE'])
    def delete_product(product_id):
        sql = "DELETE FROM production.products WHERE product_id = %s"
        params = product_id
        DatabaseConnection.execute_query(sql, params)
        return {"msg": "Producto eliminado con éxito"}, 200
    

    return app
