import psycopg2
import os
from dotenv import load_dotenv
import json

load_dotenv()

host = 'profiles-db.c9qoeaqo4o0n.us-east-2.rds.amazonaws.com'
port = 5432
database = 'postgres'
user = os.getenv('PROFILE_RDS_USERNAME')
password = os.getenv('PROFILE_RDS_PASSWORD')

try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=database,
        user=user,
        password=password
    )
    cur = conn.cursor()

    cur.execute("SELECT id, profile_data, created_at FROM cognitive_profiles;")
    rows = cur.fetchall()

    print(rows)

except Exception as e:
    print("❌ Error fetching data:", e)

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()