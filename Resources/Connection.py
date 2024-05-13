import sqlite3

db = sqlite3.connect("Resources\SIEIDB.db")
cur = db.cursor()

def insert_course(id, name, op, format, xx, yy):
  db = sqlite3.connect("Resources\SIEIDB.db")
  cur = db.cursor()
  cur.execute('INSERT INTO Courses (id, name, duration, format, languaje, price) VALUES(?,?,?,?,?,?)',
              (id, name, op, format, xx, yy))
  db.commit()
  db.close()
  

def id_exist(id):
  db = sqlite3.connect("Resources\SIEIDB.db")
  cur = db.cursor()
  cur.execute('SELECT COUNT(*) FROM Courses WHERE id = ?', (id,))
  result = cur.fetchone()
  db.close()
  return result[0] > 0
