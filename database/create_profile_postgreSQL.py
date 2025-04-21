import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host = 'profiles-db.c9qoeaqo4o0n.us-east-2.rds.amazonaws.com'
port = 5432
database = 'postgres'  # change to 'kid_profiles' if you created it
user = os.getenv('PROFILE_RDS_USERNAME')
password = os.getenv('PROFILE_RDS_PASSWORD')

create_table_sql = """
CREATE TABLE IF NOT EXISTS cognitive_profiles (
    id SERIAL PRIMARY KEY,
    profile_data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
"""

try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=database,
        user=user,
        password=password
    )
    cur = conn.cursor()
    
    cur.execute(create_table_sql)
    conn.commit()
    print("Table created successfully (or already exists).")
    
    print("\nTable Contents:")
    cur.execute("SELECT id, created_at FROM cognitive_profiles;")
    rows = cur.fetchall()
    
    if not rows:
        print("No data found.")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Created At: {row[1]}")
    
except Exception as e:
    print("Error:", e)
finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()