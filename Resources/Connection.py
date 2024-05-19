import sqlite3

db = sqlite3.connect("Resources\SIEIDB.db")
cur = db.cursor()

def loginc(user, psw):
  db = sqlite3.connect("Resources\SIEIDB.db")
  cur = db.cursor()
  cur.execute ('SELECT * FROM "Usuarios-Sis" WHERE Usuario = ? AND PSW = ?', [user, psw])

def insert_course(id, name, model, serial, stat):
  db = sqlite3.connect("Resources\SIEIDB.db")
  cur = db.cursor()
  cur.execute('INSERT INTO "BO" (id, Nombre, Modelo, Serial, Estado) VALUES(?,?,?,?,?)',
              (id, name, model, serial, stat))
  db.commit()
  db.close()
  
def id_exist(id):
  db = sqlite3.connect("Resources\SIEIDB.db")
  cur = db.cursor()
  cur.execute('SELECT COUNT(*) FROM BO WHERE id = ?', [id])
  result = cur.fetchone()
  db.close()
  return result[0] > 0

def search(val, stat):
  cur.execute('SELECT * FROM BO WHERE id = ? OR Nombre LIKE ? AND Estado = ?', [val, '%'+val+'%', stat])

