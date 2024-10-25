
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

db = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password
)
cursor = db.cursor()

def perform_insert(selected_table, data_to_insert):
    columns = ", ".join(data_to_insert.keys())
    values = ", ".join(["%s"] * len(data_to_insert))
    query = f"INSERT INTO {selected_table} ({columns}) VALUES ({values})"
    values_tuple = tuple(data_to_insert.values())
    cursor.execute(query, values_tuple)
    db.commit()

def perform_delete(selected_table, selected_column, selected_column_value):
    try:
        cursor = db.cursor()
        delete_query = 'DELETE FROM {} WHERE {} = %s'.format(selected_table, selected_column)
        cursor.execute(delete_query, (selected_column_value,))
        db.commit()
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        cursor.close()

def perform_select(selected_table, selected_column):
    try:
        select_query = f'SELECT {selected_column} FROM {selected_table}'
        cursor.execute(select_query)
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return None
    
def perform_full_select(selected_table):
    select_query = f'SELECT * FROM {selected_table}'
    cursor.execute(select_query)
    result = cursor.fetchall()
    return result

def perform_search(search_key, selected_table, selected_column):
    try:
        cursor = db.cursor()
        search_query = f'SELECT * FROM {selected_table} WHERE {selected_column} = %s'
        cursor.execute(search_query, (search_key,))
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()