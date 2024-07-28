import os
import pandas as pd
import mysql.connector
from mysql.connector import Error
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load database configuration from environment variables
#PRIOR TO RUNNING MYSQLCONNECTOR.PY YOU MUST SET YOUR ENVIRONMENT VARIABLES:
#export DB_USER='your_db_user'
#export DB_PASSWORD='your_db_password'
#export DB_HOST='your_db_host'
#export DB_DATABASE='your_db_name'
#export CSV_FILE_PATH='path_to_your_csv_file'
#FOR WINDOWS USERS:
#set DB_USER=your_db_user
#set DB_PASSWORD=your_db_password
#set DB_HOST=your_db_host
#set DB_DATABASE=your_db_name
#set CSV_FILE_PATH=path_to_your_csv_file


db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_DATABASE')
}

def create_connection(config):
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            logging.info("Successfully connected to the database")
            return conn
    except Error as e:
        logging.error(f"Error: {e}")
        return None

def close_connection(conn, cursor):
    if conn.is_connected():
        cursor.close()
        conn.close()
        logging.info("MySQL connection is closed.")

def load_csv_to_db(csv_path, conn):
    try:
        cursor = conn.cursor()
        df = pd.read_csv(csv_path)
        insert_query = """
            INSERT INTO dish (dish_id, name, description, price, restaurant_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        data = [tuple(row) for row in df.itertuples(index=False, name=None)]
        cursor.executemany(insert_query, data)
        conn.commit()
        logging.info("Data loaded successfully.")
    except Error as e:
        logging.error(f"Error: {e}")
        conn.rollback()
    finally:
        close_connection(conn, cursor)

def test_transactions():
    conn = create_connection(db_config)
    if conn:
        # Test data
        test_data = [
            (5000, 'Dish3', 'Description1', 10.0, 1),
            (5001, 'Dish4', 'Description2', 12.0, 1)
        ]
        try:
            cursor = conn.cursor()
            insert_query = "INSERT INTO dish (dish_id, name, description, price, restaurant_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.executemany(insert_query, test_data)
            conn.commit()
            logging.info("Test transaction completed successfully.")
        except Error as e:
            logging.error(f"Transaction Error: {e}")
            conn.rollback()
        finally:
            close_connection(conn, cursor)

if __name__ == "__main__":
    csv_file_path = os.getenv('CSV_FILE_PATH', '~/Downloads/updated_ubereats_restaurant_menu_items.csv')
    conn = create_connection(db_config)
    if conn:
        load_csv_to_db(csv_file_path, conn)
        test_transactions()

