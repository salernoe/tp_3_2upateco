import mysql.connector

class Config:
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"
    
    
    
    
    
    
    
    
    
    
    
    
    """DATABASE_CONFIG = {
        'user': 'juan',
        'password': 'Upateco12345678@',
        'host': 'localhost',
        'port': '3306',
        'database': 'sales',
        
    }

    #TEMPLATE_FOLDER = "templates/"
    #STATIC_FOLDER = "static_folder/"

    try:
        connection = mysql.connector.connect(**DATABASE_CONFIG)
        print("Conexión exitosa")
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        
    """