import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(sys.path)

from db import get_db_connection


def get_user(user_id):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query ="SELECT * FROM users WHERE id = %s;"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            cursor.close()
            if user:
                print(f"User found: {user}")
            else:
                print(f"No user found with id {user_id}.")
        except Exception as e:
            print(f"error reading user: {e}")
        finally:
            conn.close()
get_user(1)
