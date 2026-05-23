import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db import get_db_connection


def delete_user(user_id):
    conn = get_db_connection()

    if conn:
        try:
            cursor = conn.cursor()

            query = "DELETE FROM users WHERE id = %s;"
            cursor.execute(query, (user_id,))

            conn.commit()

            if cursor.rowcount > 0:
                print(f"User with id {user_id} deleted successfully.")
            else:
                print(f"No user found with id {user_id}.")

            cursor.close()

        except Exception as e:
            print(f"Error deleting user: {e}")

        finally:
            conn.close()


delete_user(1)