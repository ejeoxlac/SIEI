import sqlite3

class Communication():
  def __init__(self):
    self.connection = sqlite3.connect('SIEIDB.db')