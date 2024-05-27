# Libraries
import sqlite3

# Connector to the database and to execute the SQL statements the database cursor was created
db = sqlite3.connect ('Resources\\SIEIDB.db')
cur = db.cursor ()

# Validates the access data to the application
def loginv(user, psw):
  cur.execute ('SELECT * FROM UsersSys WHERE users=? AND psw=?', [user, psw])

# Adds computer data to the PC table
def insert_pc(id, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PC (idpc, name, model, serial, color, colormb, cpu, ram, HDDorSDD, status, dateofarrival, departuredate) VALUES(?, ? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?)', (id, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd))
  db.commit ()
  db.close ()

# IDs checker to avoid duplication
def id_exist (id):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT COUNT(*) FROM PC WHERE idpc=?', [id])
  result = cur.fetchone ()
  db.close ()
  return result [0] > 0

# Search engine for data about computers
def search_pc (val, stat):
  cur.execute ('SELECT * FROM PC WHERE idpc=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])
