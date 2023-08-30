"""from flask import render_template, request,Flask,jsonify, current_app, Blueprint
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app.database import DatabaseConnection
from config import Config
import re
import json
import os"""
from flask import Flask, jsonify
from config import Config
from app.database import DatabaseConnection

def init_app():
        
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
   
   
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