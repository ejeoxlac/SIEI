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
def id_exist_pc (id):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT COUNT(*) FROM PC WHERE idpc=?', [id])
  result = cur.fetchone ()
  db.close ()
  return result [0] > 0

# Search Engines
## Search engine for data about computers
def search_pc (val, stat):
  cur.execute ('SELECT * FROM PC WHERE idpc=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data finder about keyboards
def search_pk (val, stat):
  cur.execute ('SELECT * FROM Pk WHERE idpk=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data finder about monitors
def search_pm (val, stat):
  cur.execute ('SELECT * FROM PM WHERE idpm=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Search for data about mouses
def search_pmo (val, stat):
  cur.execute ('SELECT * FROM PMO WHERE idpmo=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Search for data about printers
def search_pp (val, stat):
  cur.execute ('SELECT * FROM PP WHERE idpp=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])
