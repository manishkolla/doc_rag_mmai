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

json_path = '../sample_data/child1.json'

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=database,
        user=user,
        password=password
    )
    cur = conn.cursor()

    insert_query = """
        INSERT INTO cognitive_profiles (profile_data)
        VALUES (%s::jsonb)
    """
    cur.execute(insert_query, (json.dumps(data),))
    conn.commit()
    print("✅ Data inserted successfully.")

except Exception as e:
    print("❌ Error inserting data:", e)

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()