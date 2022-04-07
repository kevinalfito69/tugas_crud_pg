import psycopg2
import os
# koneksi database
db = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            database="toko_sembako",
            password="admin")

# input data
def insert_data(db):
  nama = input("Masukan nama barang: ")
  harga = input("Masukan harga barang: ")
  kode = input("Masukan kode barang: ")
  val = (nama, harga, kode)
  cursor = db.cursor()
  sql = "INSERT INTO toko_sembako (nama_barang, harga_barang, kode_barang) VALUES (%s, %s, %s)"
  cursor.execute(sql,val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))

# tampil data?
def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM toko_sembako"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

# update data
def update_data(db):
  cursor = db.cursor()
  show_data(db)
  id_barang = input("pilih id barang ")
  nama = input("Nama baru: ")
  harga = input("harga baru: ")
  kode = input("Kode baru: ")


  sql = "UPDATE toko_sembako SET nama_barang=%s, harga_barang=%s,kode_barang=%s WHERE id=%s"
  val = (nama, harga,kode, id_barang)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))

# hapusdata
def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  id_barang = input("pilih id toko_sembako ")
  sql = "DELETE FROM toko_sembako WHERE id=%s"
  val = (id_barang)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))

#Cari data
def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM toko_sembako WHERE nama_barang LIKE %s OR harga_barang LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI TOKO SEMBAKO PYTHON ===")
  print("1. Masukan Data")
  print("2. Menampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("cls")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)