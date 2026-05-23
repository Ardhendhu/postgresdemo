import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(sys.path)

from db import get_db_connection


def create_user(user_id, name):
    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        if cursor is not None:
            try:
                cursor = conn.cursor()
                query = '''
                INSERT INTO users (id, name) VALUES (%s, %s);  
                '''
                cursor.execute(query, (user_id, name))
                conn.commit()
                print(f"user {name} created successfully.")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                cursor.close()
                conn.close()
create_user(1, 'Ardhendhu')
