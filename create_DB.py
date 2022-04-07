import psycopg2
conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            password="admin")
conn.autocommit=True
cursor = conn.cursor()
cursor.execute("CREATE DATABASE TEST ")

print('DATABASE BERHASIL DIBUAT')
conn.close()