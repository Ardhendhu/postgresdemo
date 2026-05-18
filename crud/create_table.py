import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(sys.path)

from db import get_db_connection


def create_user_table():
    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        if cursor is not None:
            try:
                cursor = conn.cursor()
                create_table_query = '''
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL
                );
                ''' 
                cursor.execute(create_table_query)
                conn.commit()
                print("Table 'users' created successfully.")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                cursor.close()
                conn.close()
create_user_table()
