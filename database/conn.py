import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    host = os.getenv('DB_HOST')
    database = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    return mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
        )

def perform_insert(selected_table, data_to_insert):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        columns = ", ".join(data_to_insert.keys())
        values = ", ".join(["%s"] * len(data_to_insert))
        query = f"INSERT INTO {selected_table} ({columns}) VALUES ({values})"
        values_tuple = tuple(data_to_insert.values())
        cursor.execute(query, values_tuple)
        db.commit()
    except Exception as e:
        db.rollback()
        print("Error during insert:", e)
        raise
    finally:
        cursor.close()
        db.close()

def perform_delete(selected_table, selected_column, selected_column_value):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        delete_query = f'DELETE FROM {selected_table} WHERE {selected_column} = %s'
        cursor.execute(delete_query, (selected_column_value,))
        db.commit()
    except Exception as e:
        db.rollback()
        print("Error during delete:", e)
    finally:
        cursor.close()
        db.close()

def perform_select(selected_table, selected_column):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        select_query = f'SELECT {selected_column} FROM {selected_table}'
        cursor.execute(select_query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Error during select: {e}")
        return None
    finally:
        cursor.close()
        db.close()

def perform_full_select(selected_table):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        select_query = f'SELECT * FROM {selected_table}'
        cursor.execute(select_query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Error during full select: {e}")
        return None
    finally:
        cursor.close()
        db.close()

def perform_search(search_key, selected_table, selected_column):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        search_query = f'SELECT * FROM {selected_table} WHERE {selected_column} = %s'
        cursor.execute(search_query, (search_key,))
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("Error during search:", e)
        return None
    finally:
        cursor.close()
        db.close()
