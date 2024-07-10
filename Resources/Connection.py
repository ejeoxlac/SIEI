# Libraries
import sqlite3, pandas, matplotlib.pyplot as plt

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
def edit_pc (rowid, idpc, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd, dom):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PC SET idpc=:idpc, name=:name, model=:model, serial=:serial, color=:color, colormb=:colormb, cpu=:cpu, ram=:ram, HDDorSDD=:HDDorSDD, status=:status, dateofarrival=:dateofarrival, departuredate=:departuredate, dateofmodification=:dateofmodification WHERE rowid = {rowid}', {'idpc':idpc, 'name':name, 'model':model, 'serial':serial, 'color':color, 'colormb':colormb, 'cpu':cpu, 'ram':ram, 'HDDorSDD':disk, 'status':stat, 'dateofarrival':dfa, 'departuredate':dtd, 'dateofmodification':dom})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pc (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PC WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

## Statistical graph showing which computers are operational or not
def graph_pc ():
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = '''SELECT COUNT(idpc) sum_idpc, status FROM PC GROUP BY status HAVING sum_idpc > 0 UNION SELECT COUNT(idpc) AS total, 'Total General' FROM PC ORDER BY sum_idpc DESC LIMIT 5'''
  
  data = pandas.read_sql (cur, db)

  plt.figure (num='Registro de las PC')
  colors = ['blue', 'green', 'red']
  plt.bar (data.status, data.sum_idpc, color=colors)
  for i in range (len(data.status)):
      plt.bar (0, 0, color=colors[i], label=data.status[i])
  plt.legend ()
  plt.ylabel ('Cantidad')
  plt.title ('PC operativas')
  plt.show ()

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
def edit_pk (rowid, idpk, name, model, serial, color, stat, dfa, dtd, dom):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PK SET idpk=:idpk, name=:name, model=:model, serial=:serial, color=:color, status=:status, dateofarrival=:dateofarrival, departuredate=:departuredate, dateofmodification=:dateofmodification WHERE rowid = {rowid}', {'idpk':idpk, 'name':name, 'model':model, 'serial':serial, 'color':color, 'status':stat, 'dateofarrival':dfa, 'departuredate':dtd, 'dateofmodification':dom})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pk (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PK WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

## Statistical graph showing which keyboards are operational or not
def graph_pk ():
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = '''SELECT COUNT(idpk) sum_idpk, status FROM PK GROUP BY status HAVING sum_idpk > 0 UNION SELECT COUNT(idpk) AS total, 'Total General' FROM PK ORDER BY sum_idpk DESC LIMIT 5'''

  data = pandas.read_sql (cur, db)

  plt.figure (num='Registro de los teclados')
  colors = ['blue', 'green', 'red']
  plt.bar (data.status, data.sum_idpk, color=colors)
  for i in range (len(data.status)):
      plt.bar (0, 0, color=colors[i], label=data.status[i])
  plt.legend ()
  plt.ylabel ('Cantidad')
  plt.title ('Teclados operativos')
  plt.show ()

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
def edit_pm (rowid, idpm, name, model, serial, color, stat, dfa, dtd, dom):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PM SET idpm=:idpm, name=:name, model=:model, serial=:serial, color=:color, status=:status, dateofarrival=:dateofarrival, departuredate=:departuredate, dateofmodification=:dateofmodification WHERE rowid = {rowid}', {'idpm':idpm, 'name':name, 'model':model, 'serial':serial, 'color':color, 'status':stat, 'dateofarrival':dfa, 'departuredate':dtd, 'dateofmodification':dom})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pm (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PM WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

## Statistical graph showing which monitors are operational or not
def graph_pm ():
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = '''SELECT COUNT(idpm) sum_idpm, status FROM PM GROUP BY status HAVING sum_idpm > 0 UNION SELECT COUNT(idpm) AS total, 'Total General' FROM PM ORDER BY sum_idpm DESC LIMIT 5'''
  
  data = pandas.read_sql (cur, db)

  plt.figure (num='Registro de los monitores')
  colors = ['blue', 'green', 'red']
  plt.bar (data.status, data.sum_idpm, color=colors)
  for i in range (len(data.status)):
      plt.bar (0, 0, color=colors[i], label=data.status[i])
  plt.legend ()
  plt.ylabel ('Cantidad')
  plt.title ('Monitores operativos')
  plt.show ()

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
def edit_pmo (rowid, idpmo, name, model, serial, color, stat, dfa, dtd, dom):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PMO SET idpmo=:idpmo, name=:name, model=:model, serial=:serial, color=:color, status=:status, dateofarrival=:dateofarrival, departuredate=:departuredate, dateofmodification=:dateofmodification WHERE rowid = {rowid}', {'idpmo':idpmo, 'name':name, 'model':model, 'serial':serial, 'color':color, 'status':stat, 'dateofarrival':dfa, 'departuredate':dtd, 'dateofmodification':dom})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pmo (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PMO WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

## Statistical graph showing which monitors are operational or not
def graph_pmo ():
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = '''SELECT COUNT(idpmo) sum_idpmo, status FROM PMO GROUP BY status HAVING sum_idpmo > 0 UNION SELECT COUNT(idpmo) AS total, 'Total General' FROM PMO ORDER BY sum_idpmo DESC LIMIT 5'''
  
  data = pandas.read_sql (cur, db)

  plt.figure (num='Registro de los mouses')
  colors = ['blue', 'green', 'red']
  plt.bar (data.status, data.sum_idpmo, color=colors)
  for i in range (len(data.status)):
      plt.bar (0, 0, color=colors[i], label=data.status[i])
  plt.legend ()
  plt.ylabel ('Cantidad')
  plt.title ('Mouses operativos')
  plt.show ()

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
def edit_pp (rowid, idpp, name, model, serial, color, stat, dfa, dtd, dom):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PP SET idpp=:idpp, name=:name, model=:model, serial=:serial, color=:color, status=:status, dateofarrival=:dateofarrival, departuredate=:departuredate, dateofmodification=:dateofmodification WHERE rowid = {rowid}', {'idpp':idpp, 'name':name, 'model':model, 'serial':serial, 'color':color, 'status':stat, 'dateofarrival':dfa, 'departuredate':dtd, 'dateofmodification':dom})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pp (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PP WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

## Statistical graph showing which printers are operational or not
def graph_pp ():
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = '''SELECT COUNT(idpp) sum_idpp, status FROM PP GROUP BY status HAVING sum_idpp > 0 UNION SELECT COUNT(idpp) AS total, 'Total General' FROM PP ORDER BY sum_idpp DESC LIMIT 5'''
  
  data = pandas.read_sql (cur, db)

  plt.figure (num='Registro de las impresoras')
  colors = ['blue', 'green', 'red']
  plt.bar (data.status, data.sum_idpp, color=colors)
  for i in range (len(data.status)):
      plt.bar (0, 0, color=colors[i], label=data.status[i])
  plt.legend ()
  plt.ylabel ('Cantidad')
  plt.title ('Impresoras operativas')
  plt.show ()

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
