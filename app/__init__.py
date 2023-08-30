from flask import Flask, jsonify, request
from config import Config
from app.database import DatabaseConnection

def init_app():
        
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
   
   
    # 1.1. Obtener un cliente
    #GET /customers/<int:customer_id>
   
    @app.route('/customers/<int:customer_id>', methods=['GET'])
    def get_customer(customer_id):
        sql = "SELECT customer_id, first_name, last_name, email, phone, street, city, state, zip_code FROM sail.customer WHERE customer_id = %s;"
        #customer = Customer.query.get(customer_id)
        params = customer_id,
        result = DatabaseConnection.fetch_one(sql, params)
       
       
        if result is None:
            return jsonify({'error': 'Customer not found'}), 404
        
        customer_data = {
            'customer_id': result[0],
            'first_name': result[1],
            'last_name': result[2],
            'email': result[3],
            'phone': result[4],
            'street': result[5],
            'city': result[6],
            'state': result[7],
            'zip_code': result[8]
        },200
        #return {"msg": "No se encontró el actor"}, 404
        return customer_data
    
    
    
    #1.2. Obtener el listado de clientes
    #GET /customers
    
    @app.route('/customers', methods=['GET'])
    def get_customers():
        state = request.args.get('state', default=None, type=str)

        sql = "SELECT customer_id, first_name, last_name, email, phone, street, city, state, zip_code FROM sales.customer"
        params = ()

        if state:
            sql += " WHERE state = %s"
            params = (state,)

        results = DatabaseConnection.fetch_all(sql, params)
        total = len(results)

        customers = []
        for result in results:
            customer_data = {
                'customer_id': result[0],
                'first_name': result[1],
                'last_name': result[2],
                'email': result[3],
                'phone': result[4],
                'street': result[5],
                'city': result[6],
                'state': result[7],
                'zip_code': result[8]
            }
            customers.append(customer_data)

        response = {
            'customers': customers,
            'total': total
        }

        return jsonify(response)
    
   
    #1.3. Registrar un cliente
    #POST /customers
    @app.route('/customers', methods=['POST'])
    def create_customer():
        data = request.get_json()

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone = data.get('phone')
        street = data.get('street')
        city = data.get('city')
        state = data.get('state')
        zip_code = data.get('zip_code')

        if not first_name or not last_name or not email:
            return jsonify({'error': 'Missing required fields'}), 400

        sql = "INSERT INTO sales.customer (first_name, last_name, email, phone, street, city, state, zip_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (first_name, last_name, email, phone, street, city, state, zip_code)

        DatabaseConnection.execute(sql, params)

        return jsonify({}), 201
    
    #1.4. Modificar un cliente
   # PUT /customers/<int:customer_id>
   
    @app.route('/customers/<int:customer_id>', methods=['PUT'])
    def update_customer(customer_id):
        data = request.get_json()

        email = data.get('email')
        phone = data.get('phone')
        street = data.get('street')
        city = data.get('city')
        state = data.get('state')
        zip_code = data.get('zip_code')

        sql = "UPDATE sales.customer SET email = %s, phone = %s, street = %s, city = %s, state = %s, zip_code = %s WHERE customer_id = %s"
        params = (email, phone, street, city, state, zip_code, customer_id)

        DatabaseConnection.execute(sql, params)

        return jsonify({}), 200
    
    
    #1.5. Eliminar un cliente
    #DELETE /customers/<int:customer_id>
    
    @app.route('/customers/<int:customer_id>', methods=['DELETE'])
    def delete_customer(customer_id):
        sql = "DELETE FROM sales.customer WHERE customer_id = %s"
        params = (customer_id,)

        DatabaseConnection.execute(sql, params)

        return jsonify({}), 204
    