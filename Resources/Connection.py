# Libraries
import sqlite3, pandas, matplotlib.pyplot as plt
from matplotlib.widgets import Button
from docx import Document
from docx.shared import Inches
from docx.enum.section import WD_ORIENT

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
def insert_pc (idpc, name, model, serial, color, modelmb, colormb, gcn, gcm, cpu, ram, disk, pcso, dp, user, stat, dfa, dtd, obs):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PC (idpc, name, model, serial, color, modelmb, colormb, graphicscardname, graphicscardmodel, cpu, ram, HDDorSDD, so, dp, users, status, dateofarrival, departuredate, observation) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (idpc, name, model, serial, color, modelmb, colormb, gcn, gcm, cpu, ram, disk, pcso, dp, user, stat, dfa, dtd, obs))
  db.commit ()
  db.close ()

## Search engine for data
def search_pc (val, stat):
  cur.execute ('SELECT * FROM PC WHERE idpc=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data editor in the database
def edit_pc (rowid, idpc, name, model, serial, color, modelmb, colormb, gcn, gcm, cpu, ram, disk, pcso, dp, user, stat, dom, dtd, obs):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PC SET idpc=:idpc, name=:name, model=:model, serial=:serial, color=:color, modelmb=:modelmb, colormb=:colormb, graphicscardname=:graphicscardname, graphicscardmodel=:graphicscardmodel, cpu=:cpu, ram=:ram, HDDorSDD=:HDDorSDD, so=:so, dp=:dp, users=:users, status=:status, dateofmodification=:dateofmodification, departuredate=:departuredate, observation=:observation WHERE idpc = {idpc}', {'idpc':idpc, 'name':name, 'model':model, 'serial':serial, 'color':color, 'modelmb':modelmb, 'colormb':colormb, 'graphicscardname':gcn, 'graphicscardmodel':gcm, 'cpu':cpu, 'ram':ram, 'HDDorSDD':disk, 'so':pcso, 'dp':dp, 'users':user, 'status':stat, 'dateofmodification':dom, 'departuredate':dtd, 'observation':obs})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pc (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PC WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

## Printing a word document with data obtained from the database
def docx_pc ():
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT * FROM PC')
  data = cur.fetchall ()

  ### Creation of the Word document and placement of the data
  docx = Document()
  section = docx.sections [-1]
  new_width, new_height = section.page_height, section.page_width
  section.orientation = WD_ORIENT.LANDSCAPE
  section.page_width = new_width
  section.page_height = new_height
  table = docx.add_table (rows=1, cols=len(data[0]))
  ### Apply a table style
  table.style = 'Table Grid'

  ### Column headings
  headings = [descripcion[0] for descripcion in cur.description]
  for i, heading in enumerate (headings):
      cell = table.cell (0, i)
      cell.text = heading

  ### Add rows of data
  for row in data:
      new_row = table.add_row().cells
      for i, column in enumerate (row):
          new_row[i].text = str (column)

  ### Adjusts the width of the table columns
  for column in table.columns:
    width = Inches (1.5)
    column.width = width

  ### Saves the document in the current folder
  docx.save ('Datos de las computadoras.docx')

  db.close ()

## Statistical graph about computers
def graph_pc ():
  ### Connect to the SQLite database
  db = sqlite3.connect ('Resources\\SIEIDB.db')

  ### Query SQL to get data
  cur1 = '''SELECT sum_idpc, status FROM (SELECT COUNT(idpc) AS sum_idpc, status FROM PC GROUP BY status HAVING sum_idpc > 0 UNION SELECT COUNT(idpc) AS total, 'Total General' FROM PC) AS combined_results ORDER BY CASE WHEN status = 'Total General' THEN 0 ELSE 1 END, sum_idpc DESC LIMIT 5'''
  datast = pandas.read_sql (cur1, db)
  cur2 = '''SELECT sum_idpc, dp FROM (SELECT COUNT(idpc) AS sum_idpc, dp FROM PC GROUP BY dp HAVING sum_idpc > 0 UNION SELECT COUNT(idpc) AS total, 'Total General' FROM PC) AS combined_results ORDER BY CASE WHEN dp = 'Total General' THEN 0 ELSE 1 END, sum_idpc DESC LIMIT 5'''
  datadp = pandas.read_sql (cur2, db)

  ### Create a figure and an axis
  fig, ax = plt.subplots ()
  plt.subplots_adjust (bottom=0.2)
  fig.canvas.manager.set_window_title ('Estadistiscas')

  ### Colors
  colors = ['blue', 'green', 'red', 'yellow']

  ### Function to draw the graph
  def draw_graphst (data, title):
    ax.clear ()
    bars = ax.bar (data.status, data.sum_idpc, color=colors[:len(data.status)], label=data.status)
    for bar, label in zip (bars, data.status):
        yval = bar.get_height ()
        ax.annotate (yval, (bar.get_x() + bar.get_width() / 2, yval), ha='center', va='bottom')
        bar.set_label (label)
    ax.legend (title='Estados')
    ax.set_ylabel ('Cantidad')
    ax.set_title (title)
    plt.draw ()

  def draw_graphdp (data, title):
      ax.clear ()
      bars = ax.bar (data.dp, data.sum_idpc, color=colors[:len(data.dp)], label=data.dp)
      for bar, label in zip (bars, data.dp):
          yval = bar.get_height ()
          ax.annotate (yval, (bar.get_x() + bar.get_width() / 2, yval), ha='center', va='bottom')
          bar.set_label (label)
      ax.legend (title='Departamentos')
      ax.set_ylabel ('Cantidad')
      ax.set_title (title)
      plt.draw ()

  ### Initialize the graph
  global current_graph
  current_graph = 1
  draw_graphst (datast, 'PC operativas')

  ### Function to update the graph
  def update_graph (event):
      global current_graph
      if event.inaxes == ax_button_next:
          if current_graph == 1:
              draw_graphdp (datadp, 'PC operativas')
              current_graph = 2
          else:
              draw_graphst (datast, 'PC operativas por departamento')
              current_graph = 1
      elif event.inaxes == ax_button_prev:
          if current_graph == 2:
              draw_graphst (datast, 'PC operativas')
              current_graph = 1
          else:
              draw_graphdp (datadp, 'PC operativas por departamento')
              current_graph = 2

  ### Buttons
  ax_button_next = plt.axes ([0.1, 0.05, 0.35, 0.075])
  ax_button_prev = plt.axes ([0.55, 0.05, 0.35, 0.075])
  button_next = Button (ax_button_next, 'Siguiente Gráfica')
  button_prev = Button (ax_button_prev, 'Gráfica Anterior')

  ### Assign the update function to the buttons
  button_next.on_clicked (update_graph)
  button_prev.on_clicked (update_graph)

  plt.show()

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
def insert_pk (idpk, name, model, serial, color, dp, user, stat, dfa, dtd, obs):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PK (idpk, name, model, serial, color, dp, users, status, dateofarrival, departuredate, observation) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (idpk, name, model, serial, color, dp, user, stat, dfa, dtd, obs))
  db.commit ()
  db.close ()

## Search engine for data
def search_pk (val, stat):
  cur.execute ('SELECT * FROM PK WHERE idpk=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data editor in the database
def edit_pk (rowid, idpk, name, model, serial, color, dp, user, stat, dom, dtd, obs):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PK SET idpk=:idpk, name=:name, model=:model, serial=:serial, color=:color, dp=:dp, users=:users, status=:status, dateofmodification=:dateofmodification, departuredate=:departuredate, observation=:observation WHERE idpk = {idpk}', {'idpk':idpk, 'name':name, 'model':model, 'serial':serial, 'color':color, 'dp':dp, 'users':user, 'status':stat, 'dateofmodification':dom, 'departuredate':dtd, 'observation':obs})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pk (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PK WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

## Printing a word document with data obtained from the database
def docx_pk ():
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT * FROM PK')
  data = cur.fetchall ()

  ### Creation of the Word document and placement of the data
  docx = Document()
  section = docx.sections [-1]
  new_width, new_height = section.page_height, section.page_width
  section.orientation = WD_ORIENT.LANDSCAPE
  section.page_width = new_width
  section.page_height = new_height
  table = docx.add_table (rows=1, cols=len(data[0]))
  ### Apply a table style
  table.style = 'Table Grid'

  ### Column headings
  headings = [descripcion[0] for descripcion in cur.description]
  for i, heading in enumerate (headings):
      cell = table.cell (0, i)
      cell.text = heading

  ### Add rows of data
  for row in data:
      new_row = table.add_row().cells
      for i, column in enumerate (row):
          new_row[i].text = str (column)

  ### Adjusts the width of the table columns
  for column in table.columns:
    width = Inches (1.5)
    column.width = width

  ### Saves the document in the current folder
  docx.save ('Datos de los teclados.docx')

  db.close ()

## Statistical graph about the keyboards
def graph_pk ():
  ### Connect to the SQLite database
  db = sqlite3.connect ('Resources\\SIEIDB.db')

  ### Query SQL to get data
  cur1 = '''SELECT sum_idpk, status FROM (SELECT COUNT(idpk) AS sum_idpk, status FROM PK GROUP BY status HAVING sum_idpk > 0 UNION SELECT COUNT(idpk) AS total, 'Total General' FROM PK) AS combined_results ORDER BY CASE WHEN status = 'Total General' THEN 0 ELSE 1 END, sum_idpk DESC LIMIT 5'''
  datast = pandas.read_sql (cur1, db)
  cur2 = '''SELECT sum_idpk, dp FROM (SELECT COUNT(idpk) AS sum_idpk, dp FROM PK GROUP BY dp HAVING sum_idpk > 0 UNION SELECT COUNT(idpk) AS total, 'Total General' FROM PK) AS combined_results ORDER BY CASE WHEN dp = 'Total General' THEN 0 ELSE 1 END, sum_idpk DESC LIMIT 5'''
  datadp = pandas.read_sql (cur2, db)

  ### Create a figure and an axis
  fig, ax = plt.subplots ()
  plt.subplots_adjust (bottom=0.2)
  fig.canvas.manager.set_window_title ('Estadistiscas')

  ### Colors
  colors = ['blue', 'green', 'red', 'yellow']

  ### Function to draw the graph
  def draw_graphst (data, title):
    ax.clear ()
    bars = ax.bar (data.status, data.sum_idpk, color=colors[:len(data.status)], label=data.status)
    for bar, label in zip (bars, data.status):
        yval = bar.get_height ()
        ax.annotate (yval, (bar.get_x() + bar.get_width() / 2, yval), ha='center', va='bottom')
        bar.set_label (label)
    ax.legend (title='Estados')
    ax.set_ylabel ('Cantidad')
    ax.set_title (title)
    plt.draw ()

  def draw_graphdp (data, title):
      ax.clear ()
      bars = ax.bar (data.dp, data.sum_idpk, color=colors[:len(data.dp)], label=data.dp)
      for bar, label in zip (bars, data.dp):
          yval = bar.get_height ()
          ax.annotate (yval, (bar.get_x() + bar.get_width() / 2, yval), ha='center', va='bottom')
          bar.set_label (label)
      ax.legend (title='Departamentos')
      ax.set_ylabel ('Cantidad')
      ax.set_title (title)
      plt.draw ()

  ### Initialize the graph
  global current_graph
  current_graph = 1
  draw_graphst (datast, 'Teclados operativos')

  ### Function to update the graph
  def update_graph (event):
      global current_graph
      if event.inaxes == ax_button_next:
          if current_graph == 1:
              draw_graphdp (datadp, 'Teclados operativos')
              current_graph = 2
          else:
              draw_graphst (datast, 'Teclados operativos por departamento')
              current_graph = 1
      elif event.inaxes == ax_button_prev:
          if current_graph == 2:
              draw_graphst (datast, 'Teclados operativos')
              current_graph = 1
          else:
              draw_graphdp (datadp, 'Teclados operativos por departamento')
              current_graph = 2

  ### Buttons
  ax_button_next = plt.axes ([0.1, 0.05, 0.35, 0.075])
  ax_button_prev = plt.axes ([0.55, 0.05, 0.35, 0.075])
  button_next = Button (ax_button_next, 'Siguiente Gráfica')
  button_prev = Button (ax_button_prev, 'Gráfica Anterior')

  ### Assign the update function to the buttons
  button_next.on_clicked (update_graph)
  button_prev.on_clicked (update_graph)

  plt.show()

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
def insert_pm (idpm, name, model, serial, color, tsi, tcp, dp, user, stat, dfa, dtd, obs):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PM (idpm, name, model, serial, color, typescreeninch, typeconnectorport, dp, users, status, dateofarrival, departuredate, observation) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (idpm, name, model, serial, color, tsi, tcp, dp, user, stat, dfa, dtd, obs))
  db.commit ()
  db.close ()

## Search engine for data
def search_pm (val, stat):
  cur.execute ('SELECT * FROM PM WHERE idpm=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data editor in the database
def edit_pm (rowid, idpm, name, model, serial, color, tsi, tcp, dp, user, stat, dom, dtd, obs):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PM SET idpm=:idpm, name=:name, model=:model, serial=:serial, color=:color, typescreeninch=:typescreeninch, typeconnectorport=:typeconnectorport, dp=:dp, users=:users, status=:status, dateofmodification=:dateofmodification, departuredate=:departuredate, observation=:observation WHERE idpm = {idpm}', {'idpm':idpm, 'name':name, 'model':model, 'serial':serial, 'color':color, 'typescreeninch':tsi, 'typeconnectorport':tcp, 'dp':dp, 'users':user, 'status':stat, 'dateofmodification':dom, 'departuredate':dtd, 'observation':obs})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pm (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PM WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

## Printing a word document with data obtained from the database
def docx_pm ():
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT * FROM PM')
  data = cur.fetchall ()

  ### Creation of the Word document and placement of the data
  docx = Document()
  section = docx.sections [-1]
  new_width, new_height = section.page_height, section.page_width
  section.orientation = WD_ORIENT.LANDSCAPE
  section.page_width = new_width
  section.page_height = new_height
  table = docx.add_table (rows=1, cols=len(data[0]))
  ### Apply a table style
  table.style = 'Table Grid'

  ### Column headings
  headings = [descripcion[0] for descripcion in cur.description]
  for i, heading in enumerate (headings):
      cell = table.cell (0, i)
      cell.text = heading

  ### Add rows of data
  for row in data:
      new_row = table.add_row().cells
      for i, column in enumerate (row):
          new_row[i].text = str (column)

  ### Adjusts the width of the table columns
  for column in table.columns:
    width = Inches (1.5)
    column.width = width

  ### Saves the document in the current folder
  docx.save ('Datos de los monitores.docx')

  db.close ()

## Statistical graph about the monitors
def graph_pm ():
  ### Connect to the SQLite database
  db = sqlite3.connect ('Resources\\SIEIDB.db')

  ### Query SQL to get data
  cur1 = '''SELECT sum_idpm, status FROM (SELECT COUNT(idpm) AS sum_idpm, status FROM PM GROUP BY status HAVING sum_idpm > 0 UNION SELECT COUNT(idpm) AS total, 'Total General' FROM PM) AS combined_results ORDER BY CASE WHEN status = 'Total General' THEN 0 ELSE 1 END, sum_idpm DESC LIMIT 5'''
  datast = pandas.read_sql (cur1, db)
  cur2 = '''SELECT sum_idpm, dp FROM (SELECT COUNT(idpm) AS sum_idpm, dp FROM PM GROUP BY dp HAVING sum_idpm > 0 UNION SELECT COUNT(idpm) AS total, 'Total General' FROM PM) AS combined_results ORDER BY CASE WHEN dp = 'Total General' THEN 0 ELSE 1 END, sum_idpm DESC LIMIT 5'''
  datadp = pandas.read_sql (cur2, db)

  ### Create a figure and an axis
  fig, ax = plt.subplots ()
  plt.subplots_adjust (bottom=0.2)
  fig.canvas.manager.set_window_title ('Estadistiscas')

  ### Colors
  colors = ['blue', 'green', 'red', 'yellow']

  ### Function to draw the graph
  def draw_graphst (data, title):
    ax.clear ()
    bars = ax.bar (data.status, data.sum_idpm, color=colors[:len(data.status)], label=data.status)
    for bar, label in zip (bars, data.status):
        yval = bar.get_height ()
        ax.annotate (yval, (bar.get_x() + bar.get_width() / 2, yval), ha='center', va='bottom')
        bar.set_label (label)
    ax.legend (title='Estados')
    ax.set_ylabel ('Cantidad')
    ax.set_title (title)
    plt.draw ()

  def draw_graphdp (data, title):
      ax.clear ()
      bars = ax.bar (data.dp, data.sum_idpm, color=colors[:len(data.dp)], label=data.dp)
      for bar, label in zip (bars, data.dp):
          yval = bar.get_height ()
          ax.annotate (yval, (bar.get_x() + bar.get_width() / 2, yval), ha='center', va='bottom')
          bar.set_label (label)
      ax.legend (title='Departamentos')
      ax.set_ylabel ('Cantidad')
      ax.set_title (title)
      plt.draw ()

  ### Initialize the graph
  global current_graph
  current_graph = 1
  draw_graphst (datast, 'Monitores operativos')

  ### Function to update the graph
  def update_graph (event):
      global current_graph
      if event.inaxes == ax_button_next:
          if current_graph == 1:
              draw_graphdp (datadp, 'Monitores operativos')
              current_graph = 2
          else:
              draw_graphst (datast, 'Monitores operativos por departamento')
              current_graph = 1
      elif event.inaxes == ax_button_prev:
          if current_graph == 2:
              draw_graphst (datast, 'Monitores operativos')
              current_graph = 1
          else:
              draw_graphdp (datadp, 'Monitores operativos por departamento')
              current_graph = 2

  ### Buttons
  ax_button_next = plt.axes ([0.1, 0.05, 0.35, 0.075])
  ax_button_prev = plt.axes ([0.55, 0.05, 0.35, 0.075])
  button_next = Button (ax_button_next, 'Siguiente Gráfica')
  button_prev = Button (ax_button_prev, 'Gráfica Anterior')

  ### Assign the update function to the buttons
  button_next.on_clicked (update_graph)
  button_prev.on_clicked (update_graph)

  plt.show()

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
def insert_pmo (idpmo, name, model, serial, color, dp, user, stat, dfa, dtd, obs):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PMO (idpmo, name, model, serial, color, dp, users, status, dateofarrival, departuredate, observation) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (idpmo, name, model, serial, color, dp, user, stat, dfa, dtd, obs))
  db.commit ()
  db.close ()

## Search engine for data
def search_pmo (val, stat):
  cur.execute ('SELECT * FROM PMO WHERE idpmo=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data editor in the database
def edit_pmo (rowid, idpmo, name, model, serial, color, dp, user, stat, dom, dtd, obs):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PMO SET idpmo=:idpmo, name=:name, model=:model, serial=:serial, color=:color, dp=:dp, users=:users, status=:status, dateofmodification=:dateofmodification, departuredate=:departuredate, observation=:observation WHERE idpmo = {idpmo}', {'idpmo':idpmo, 'name':name, 'model':model, 'serial':serial, 'color':color, 'dp':dp, 'users':user, 'status':stat, 'dateofmodification':dom, 'departuredate':dtd, 'observation':obs})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pmo (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PMO WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

## Printing a word document with data obtained from the database
def docx_pmo ():
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT * FROM PMO')
  data = cur.fetchall ()

  ### Creation of the Word document and placement of the data
  docx = Document()
  section = docx.sections [-1]
  new_width, new_height = section.page_height, section.page_width
  section.orientation = WD_ORIENT.LANDSCAPE
  section.page_width = new_width
  section.page_height = new_height
  table = docx.add_table (rows=1, cols=len(data[0]))
  ### Apply a table style
  table.style = 'Table Grid'

  ### Column headings
  headings = [descripcion[0] for descripcion in cur.description]
  for i, heading in enumerate (headings):
      cell = table.cell (0, i)
      cell.text = heading

  ### Add rows of data
  for row in data:
      new_row = table.add_row().cells
      for i, column in enumerate (row):
          new_row[i].text = str (column)

  ### Adjusts the width of the table columns
  for column in table.columns:
    width = Inches (1.5)
    column.width = width

  ### Saves the document in the current folder
  docx.save ('Datos de los mouses.docx')

  db.close ()

## Statistical graph about mouses
def graph_pmo ():
  ### Connect to the SQLite database
  db = sqlite3.connect ('Resources\\SIEIDB.db')

  ### Query SQL to get data
  cur1 = '''SELECT sum_idpmo, status FROM (SELECT COUNT(idpmo) AS sum_idpmo, status FROM PMO GROUP BY status HAVING sum_idpmo > 0 UNION SELECT COUNT(idpmo) AS total, 'Total General' FROM PMO) AS combined_results ORDER BY CASE WHEN status = 'Total General' THEN 0 ELSE 1 END, sum_idpmo DESC LIMIT 5'''
  datast = pandas.read_sql (cur1, db)
  cur2 = '''SELECT sum_idpmo, dp FROM (SELECT COUNT(idpmo) AS sum_idpmo, dp FROM PMO GROUP BY dp HAVING sum_idpmo > 0 UNION SELECT COUNT(idpmo) AS total, 'Total General' FROM PMO) AS combined_results ORDER BY CASE WHEN dp = 'Total General' THEN 0 ELSE 1 END, sum_idpmo DESC LIMIT 5'''
  datadp = pandas.read_sql (cur2, db)

  ### Create a figure and an axis
  fig, ax = plt.subplots ()
  plt.subplots_adjust (bottom=0.2)
  fig.canvas.manager.set_window_title ('Estadistiscas')

  ### Colors
  colors = ['blue', 'green', 'red', 'yellow']

  ### Function to draw the graph
  def draw_graphst (data, title):
    ax.clear ()
    bars = ax.bar (data.status, data.sum_idpmo, color=colors[:len(data.status)], label=data.status)
    for bar, label in zip (bars, data.status):
        yval = bar.get_height ()
        ax.annotate (yval, (bar.get_x() + bar.get_width() / 2, yval), ha='center', va='bottom')
        bar.set_label (label)
    ax.legend (title='Estados')
    ax.set_ylabel ('Cantidad')
    ax.set_title (title)
    plt.draw ()

  def draw_graphdp (data, title):
      ax.clear ()
      bars = ax.bar (data.dp, data.sum_idpmo, color=colors[:len(data.dp)], label=data.dp)
      for bar, label in zip (bars, data.dp):
          yval = bar.get_height ()
          ax.annotate (yval, (bar.get_x() + bar.get_width() / 2, yval), ha='center', va='bottom')
          bar.set_label (label)
      ax.legend (title='Departamentos')
      ax.set_ylabel ('Cantidad')
      ax.set_title (title)
      plt.draw ()

  ### Initialize the graph
  global current_graph
  current_graph = 1
  draw_graphst (datast, 'Mouses operativos')

  ### Function to update the graph
  def update_graph (event):
      global current_graph
      if event.inaxes == ax_button_next:
          if current_graph == 1:
              draw_graphdp (datadp, 'Mouses operativos')
              current_graph = 2
          else:
              draw_graphst (datast, 'Mouses operativos por departamento')
              current_graph = 1
      elif event.inaxes == ax_button_prev:
          if current_graph == 2:
              draw_graphst (datast, 'Mouses operativos')
              current_graph = 1
          else:
              draw_graphdp (datadp, 'Mouses operativos por departamento')
              current_graph = 2

  ### Buttons
  ax_button_next = plt.axes ([0.1, 0.05, 0.35, 0.075])
  ax_button_prev = plt.axes ([0.55, 0.05, 0.35, 0.075])
  button_next = Button (ax_button_next, 'Siguiente Gráfica')
  button_prev = Button (ax_button_prev, 'Gráfica Anterior')

  ### Assign the update function to the buttons
  button_next.on_clicked (update_graph)
  button_prev.on_clicked (update_graph)

  plt.show()

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
def insert_pp (idpp, name, model, serial, color, tp, dp, user, stat, dfa, dtd, obs):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('INSERT INTO PP (idpp, name, model, serial, color, typeprinting, dp, users, status, dateofarrival, departuredate, observation) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (idpp, name, model, serial, color, tp, dp, user, stat, dfa, dtd, obs))
  db.commit ()
  db.close ()

## Search engine for data
def search_pp (val, stat):
  cur.execute ('SELECT * FROM PP WHERE idpp=? OR name LIKE ? AND status=?', [val, '%'+val+'%', stat])

## Data editor in the database
def edit_pp (rowid, idpp, name, model, serial, color, tp, dp, user, stat, dom, dtd, obs):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE PP SET idpp=:idpp, name=:name, model=:model, serial=:serial, color=:color, typeprinting=:typeprinting, dp=:dp, users=:users, status=:status, dateofmodification=:dateofmodification, departuredate=:departuredate, observation=:observation WHERE idpp = {idpp}', {'idpp':idpp, 'name':name, 'model':model, 'serial':serial, 'color':color, 'typeprinting':tp, 'dp':dp, 'users':user, 'status':stat, 'dateofmodification':dom, 'departuredate':dtd, 'observation':obs})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_pp (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM PP WHERE rowid = {rowid}')
  db.commit ()
  db.close ()

## Printing a word document with data obtained from the database
def docx_pp ():
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute ('SELECT * FROM PP')
  data = cur.fetchall ()

  ### Creation of the Word document and placement of the data
  docx = Document()
  section = docx.sections [-1]
  new_width, new_height = section.page_height, section.page_width
  section.orientation = WD_ORIENT.LANDSCAPE
  section.page_width = new_width
  section.page_height = new_height
  table = docx.add_table (rows=1, cols=len(data[0]))
  ### Apply a table style
  table.style = 'Table Grid'

  ### Column headings
  headings = [descripcion[0] for descripcion in cur.description]
  for i, heading in enumerate (headings):
      cell = table.cell (0, i)
      cell.text = heading

  ### Add rows of data
  for row in data:
      new_row = table.add_row().cells
      for i, column in enumerate (row):
          new_row[i].text = str (column)

  ### Adjusts the width of the table columns
  for column in table.columns:
    width = Inches (1.5)
    column.width = width

  ### Saves the document in the current folder
  docx.save ('Datos de las impresoras.docx')

  db.close ()

## Statistical graph about printers
def graph_pp ():
  ### Connect to the SQLite database
  db = sqlite3.connect ('Resources\\SIEIDB.db')

  ### Query SQL to get data
  cur1 = '''SELECT sum_idpp, status FROM (SELECT COUNT(idpp) AS sum_idpp, status FROM PP GROUP BY status HAVING sum_idpp > 0 UNION SELECT COUNT(idpp) AS total, 'Total General' FROM PP) AS combined_results ORDER BY CASE WHEN status = 'Total General' THEN 0 ELSE 1 END, sum_idpp DESC LIMIT 5'''
  datast = pandas.read_sql (cur1, db)
  cur2 = '''SELECT sum_idpp, dp FROM (SELECT COUNT(idpp) AS sum_idpp, dp FROM PP GROUP BY dp HAVING sum_idpp > 0 UNION SELECT COUNT(idpp) AS total, 'Total General' FROM PP) AS combined_results ORDER BY CASE WHEN dp = 'Total General' THEN 0 ELSE 1 END, sum_idpp DESC LIMIT 5'''
  datadp = pandas.read_sql (cur2, db)

  ### Create a figure and an axis
  fig, ax = plt.subplots ()
  plt.subplots_adjust (bottom=0.2)
  fig.canvas.manager.set_window_title ('Estadistiscas')

  ### Colors
  colors = ['blue', 'green', 'red', 'yellow']

  ### Function to draw the graph
  def draw_graphst (data, title):
    ax.clear ()
    bars = ax.bar (data.status, data.sum_idpp, color=colors[:len(data.status)], label=data.status)
    for bar, label in zip (bars, data.status):
        yval = bar.get_height ()
        ax.annotate (yval, (bar.get_x() + bar.get_width() / 2, yval), ha='center', va='bottom')
        bar.set_label (label)
    ax.legend (title='Estados')
    ax.set_ylabel ('Cantidad')
    ax.set_title (title)
    plt.draw ()

  def draw_graphdp (data, title):
      ax.clear ()
      bars = ax.bar (data.dp, data.sum_idpp, color=colors[:len(data.dp)], label=data.dp)
      for bar, label in zip (bars, data.dp):
          yval = bar.get_height ()
          ax.annotate (yval, (bar.get_x() + bar.get_width() / 2, yval), ha='center', va='bottom')
          bar.set_label (label)
      ax.legend (title='Departamentos')
      ax.set_ylabel ('Cantidad')
      ax.set_title (title)
      plt.draw ()

  ### Initialize the graph
  global current_graph
  current_graph = 1
  draw_graphst (datast, 'Impresoras operativas')

  ### Function to update the graph
  def update_graph (event):
      global current_graph
      if event.inaxes == ax_button_next:
          if current_graph == 1:
              draw_graphdp (datadp, 'Impresoras operativas')
              current_graph = 2
          else:
              draw_graphst (datast, 'Impresoras operativas por departamento')
              current_graph = 1
      elif event.inaxes == ax_button_prev:
          if current_graph == 2:
              draw_graphst (datast, 'Impresoras operativas')
              current_graph = 1
          else:
              draw_graphdp (datadp, 'Impresoras operativas por departamento')
              current_graph = 2

  ### Buttons
  ax_button_next = plt.axes ([0.1, 0.05, 0.35, 0.075])
  ax_button_prev = plt.axes ([0.55, 0.05, 0.35, 0.075])
  button_next = Button (ax_button_next, 'Siguiente Gráfica')
  button_prev = Button (ax_button_prev, 'Gráfica Anterior')

  ### Assign the update function to the buttons
  button_next.on_clicked (update_graph)
  button_prev.on_clicked (update_graph)

  plt.show()

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
  cur.execute ('INSERT INTO UsersSys (idus, users, psw, firstnameperson, lastnameperson, idcardperson) VALUES(?, ?, ? ,? ,? ,?)', (idus, user, psw, firstnameperson, lastnameperson, idcardperson))
  db.commit ()
  db.close ()

## Search engine for data
def search_users ():
  cur.execute ('SELECT * FROM UsersSys')

## Data editor in the database
def edit_users (rowid, idus, user, psw, firstnameperson, lastnameperson, idcardperson):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'UPDATE UsersSys SET idus=:idus, users=:user, psw=:psw, firstnameperson=:firstnameperson, lastnameperson=:lastnameperson, idcardperson=:idcardperson WHERE idus = {idus}', {'idus':idus, 'user':user, 'psw':psw, 'firstnameperson':firstnameperson, 'lastnameperson':lastnameperson, 'idcardperson':idcardperson})
  db.commit ()
  db.close ()

## Deletion of data from the database
def del_users (rowid):
  db = sqlite3.connect ('Resources\\SIEIDB.db')
  cur = db.cursor ()
  cur.execute (f'DELETE FROM UsersSys WHERE rowid = {rowid}')
  db.commit ()
  db.close ()
