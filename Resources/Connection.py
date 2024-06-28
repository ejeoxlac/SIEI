# Libraries
import sqlite3

# Connector to the database and to execute the SQL statements the database cursor was created
db = sqlite3.connect ('Resources\\SIEIDB.db')
cur = db.cursor ()

# Validates the access data to the application
def loginv (user, psw):
  cur.execute ('SELECT * FROM UsersSys WHERE users=? AND psw=?', [user, psw])

# Functions to work with the data from the computers that are registered
## Check if the ID is already registered
def id_exist_pc (idpc):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT COUNT(*) FROM PC WHERE idpc=?', [idpc])
  result = cur.fetchone ()
  db.close ()
  return result [0] > 0

## Inserting data to the database
def insert_pc (idpc, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PC (idpc, name, model, serial, color, colormb, cpu, ram, HDDorSDD, status, dateofarrival, departuredate) VALUES(?, ? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?)', (idpc, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd))
  db.commit ()
  db.close ()

## Search engine for data
def search_pc (val, stat):
  cur.execute ('SELECT * FROM PC WHERE idpc=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data editor in the database
def edit_pc (rowid, idpc, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PC SET idpc=:idpc, name=:name, model=:model, serial=:serial, color=:color, colormb=:colormb, cpu=:cpu, ram=:ram, HDDorSDD=:HDDorSDD, status=:status, dateofarrival=:dateofarrival, departuredate=:departuredate WHERE rowid = {rowid}', {'idpc':idpc, 'name':name, 'model':model, 'serial':serial, 'color':color, 'colormb':colormb, 'cpu':cpu, 'ram':ram, 'HDDorSDD':disk, 'status':stat, 'dateofarrival':dfa, 'departuredate':dtd})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pc (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PC WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

# Functions to work with the data of the keyboards that are registered
## Check if the ID is already registered
def id_exist_pk (idpk):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT COUNT(*) FROM PK WHERE idpk=?', [idpk])
  result = cur.fetchone ()
  db.close ()
  return result [0] > 0

## Inserting data to the database
def insert_pk (idpk, name, model, serial, color, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PK (idpk, name, model, serial, color, status, dateofarrival, departuredate) VALUES(?, ? ,? ,? ,? ,? ,? ,?)', (idpk, name, model, serial, color, stat, dfa, dtd))
  db.commit ()
  db.close ()

## Search engine for data
def search_pk (val, stat):
  cur.execute ('SELECT * FROM PK WHERE idpk=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data editor in the database
def edit_pk (rowid, idpk, name, model, serial, color, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PK SET idpk=:idpk, name=:name, model=:model, serial=:serial, color=:color, status=:status, dateofarrival=:dateofarrival, departuredate=:departuredate WHERE rowid = {rowid}', {'idpk':idpk, 'name':name, 'model':model, 'serial':serial, 'color':color, 'status':stat, 'dateofarrival':dfa, 'departuredate':dtd})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pk (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PK WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

# Functions to work with the data of the monitors that are registered
## Check if the ID is already registered
def id_exist_pm (idpm):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT COUNT(*) FROM PM WHERE idpm=?', [idpm])
  result = cur.fetchone ()
  db.close ()
  return result [0] > 0

## Inserting data to the database
def insert_pm (idpm, name, model, serial, color, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PM (idpm, name, model, serial, color, status, dateofarrival, departuredate) VALUES(?, ? ,? ,? ,? ,? ,? ,?)', (idpm, name, model, serial, color, stat, dfa, dtd))
  db.commit ()
  db.close ()

## Search engine for data
def search_pm (val, stat):
  cur.execute ('SELECT * FROM PM WHERE idpm=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data editor in the database
def edit_pm (rowid, idpm, name, model, serial, color, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PM SET idpm=:idpm, name=:name, model=:model, serial=:serial, color=:color, status=:status, dateofarrival=:dateofarrival, departuredate=:departuredate WHERE rowid = {rowid}', {'idpm':idpm, 'name':name, 'model':model, 'serial':serial, 'color':color, 'status':stat, 'dateofarrival':dfa, 'departuredate':dtd})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pm (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PM WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

# Functions to work with the data of the mouses that are registered
## Check if the ID is already registered
def id_exist_pmo (idpmo):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT COUNT(*) FROM PMO WHERE idpmo=?', [idpmo])
  result = cur.fetchone ()
  db.close ()
  return result [0] > 0

## Inserting data to the database
def insert_pmo (idpmo, name, model, serial, color, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PMO (idpmo, name, model, serial, color, status, dateofarrival, departuredate) VALUES(?, ? ,? ,? ,? ,? ,? ,?)', (idpmo, name, model, serial, color, stat, dfa, dtd))
  db.commit ()
  db.close ()

## Search engine for data
def search_pmo (val, stat):
  cur.execute ('SELECT * FROM PMO WHERE idpmo=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data editor in the database
def edit_pmo (rowid, idpmo, name, model, serial, color, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PMO SET idpmo=:idpmo, name=:name, model=:model, serial=:serial, color=:color, status=:status, dateofarrival=:dateofarrival, departuredate=:departuredate WHERE rowid = {rowid}', {'idpmo':idpmo, 'name':name, 'model':model, 'serial':serial, 'color':color, 'status':stat, 'dateofarrival':dfa, 'departuredate':dtd})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pmo (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PMO WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

# Functions to work with the data from the printers that are registered
## Check if the ID is already registered
def id_exist_pp (idpp):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT COUNT(*) FROM PP WHERE idpp=?', [idpp])
  result = cur.fetchone ()
  db.close ()
  return result [0] > 0

## Inserting data to the database
def insert_pp (idpp, name, model, serial, color, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PP (idpp, name, model, serial, color, status, dateofarrival, departuredate) VALUES(?, ? ,? ,? ,? ,? ,? ,?)', (idpp, name, model, serial, color, stat, dfa, dtd))
  db.commit ()
  db.close ()

## Search engine for data
def search_pp (val, stat):
  cur.execute ('SELECT * FROM PP WHERE idpp=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data editor in the database
def edit_pp (rowid, idpp, name, model, serial, color, stat, dfa, dtd):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PP SET idpp=:idpp, name=:name, model=:model, serial=:serial, color=:color, status=:status, dateofarrival=:dateofarrival, departuredate=:departuredate WHERE rowid = {rowid}', {'idpp':idpp, 'name':name, 'model':model, 'serial':serial, 'color':color, 'status':stat, 'dateofarrival':dfa, 'departuredate':dtd})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pp (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PP WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

# Functions to work with the data of users who are registered
## Check if the ID is already registered
def id_exist_users (idus):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT COUNT(*) FROM UsersSys WHERE idus=?', [idus])
  result = cur.fetchone ()
  db.close ()
  return result [0] > 0

## Inserting data to the database
def insert_users (idus, user, psw, firstnameperson, lastnameperson, idcardperson):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO UsersSys (idus, users, psw, firstnameperson, lastnameperson, idcardperson) VALUES(?, ?, ?, ?, ?, ?)', (idus, user, psw, firstnameperson, lastnameperson, idcardperson))
  db.commit ()
  db.close ()

## Search engine for data
def search_users ():
  cur.execute ('SELECT * FROM UsersSys')

## Data editor in the database
def edit_users (rowid, idus, user, psw, firstnameperson, lastnameperson, idcardperson):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE UsersSys SET idus=:idus, users=:user, psw=:psw, firstnameperson=:firstnameperson, lastnameperson=:lastnameperson, idcardperson=:idcardperson WHERE rowid = {rowid}', {'idus':idus, 'user':user, 'psw':psw, 'firstnameperson':firstnameperson, 'lastnameperson':lastnameperson, 'idcardperson':idcardperson})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_users (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM UsersSys WHERE rowid = {rowid}')
  db.commit ()
  db.close ()
