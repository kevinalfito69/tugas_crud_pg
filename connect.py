import psycopg2
def postgress_test():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="db",
            port="5432",
            user="postgres",
            password="admin")
        conn.close()
        return True
    except:
        return False

if postgress_test() == True :
    print('database berhasil terkoneksi')
else:
    print('databse gagal terkoneksi')

