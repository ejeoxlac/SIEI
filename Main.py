# Libraries
from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

## Model of the menu
menu_bar_colour = '#383838'

# Format of the window
app = CTk ()
app.title ('Registros para las computadoras')
app.geometry ('750x650')
app.resizable (False, False)

# Icons
pc_icon = CTkImage (Image.open('Resources\\Img\\Computer.png'), size=(20, 20))
pk_icon = CTkImage (Image.open('Resources\\Img\\Keyboard.png'), size=(20, 20))
pm_icon = CTkImage (Image.open('Resources\\Img\\Monitor.png'), size=(20, 20))
pmo_icon = CTkImage (Image.open('Resources\\Img\\Mouse.png'), size=(20, 20))
pp_icon = CTkImage (Image.open('Resources\\Img\\Printer.png'), size=(20, 20))

# Functions to display the data
## Computers data window
def pc_page ():

  ### Database manipulators
  #### Input re-initiator for data logging
  def new_bo():
    id_entry.delete (0, END)
    name_entry.delete (0, END)
    model_entry.delete (0, END)
    serial_entry.delete (0, END)
    color_entry.delete (0, END)
    colormb_entry.delete (0, END)
    cpu_entry.delete (0, END)
    ram_entry.delete (0, END)
    HDDorSDD_entry.delete (0, END)
    status.set ('Operativo')
    dateofarrival_entry.delete (0, END)
    departuredate_entry.delete (0, END)

  #### Entry that records the data in the database
  def submit_bo ():
    id = id_entry.get ()
    name = name_entry.get ()
    model = model_entry.get ()
    serial = serial_entry.get ()
    color = color_entry.get ()
    colormb = colormb_entry.get ()
    cpu = cpu_entry.get ()
    ram = ram_entry.get ()
    disk = HDDorSDD_entry.get ()
    stat = status.get ()
    dfa = dateofarrival_entry.get ()
    dtd = departuredate_entry.get ()
    try:
      if not (id and name and model and serial and color and colormb and cpu and ram and disk and stat and dfa):
        messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida')
      elif Resources.Connection.id_exist_pc (id):
        messagebox.showerror ('Error', 'El ID ya existe')
      else:
        Resources.Connection.insert_pc (id, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd)
        messagebox.showinfo ('Éxito', 'La información fue registrada')
    except:
      messagebox.showerror ('Error', 'A ocurrido un error')

  ### Fonts for the letters
  font1 = ('Roboto', 30, 'bold')
  font2 = ('Roboto', 18, 'bold')

  ### User interface objects
  title_label = CTkLabel (main_frame, font=font1, text='Datos del computador', text_color='#fff')
  title_label.place (x=25, y=0)

  #### Objects within the frame
  id_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff', bg_color='#292933')
  id_label.place (x=50, y=40)

  id_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  id_entry.place (x=50, y=70)

  name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff', bg_color='#292933')
  name_label.place (x=250, y=40)

  name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  name_entry.place (x=250, y=70)

  model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff', bg_color='#292933')
  model_label.place (x=445, y=40)

  model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  model_entry.place (x=445, y=70)

  serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff', bg_color='#292933')
  serial_label.place (x=50, y=100)

  serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  serial_entry.place (x=50, y=130)

  color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff', bg_color='#292933')
  color_label.place (x=250, y=100)

  color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  color_entry.place (x=250, y=130)

  colormb_label = CTkLabel (main_frame, font=font2, text='Color de la placa madre:', text_color='#fff', bg_color='#292933')
  colormb_label.place (x=445, y=100)

  colormb_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  colormb_entry.place (x=445, y=130)

  cpu_label = CTkLabel (main_frame, font=font2, text='CPU:', text_color='#fff', bg_color='#292933')
  cpu_label.place (x=50, y=160)

  cpu_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  cpu_entry.place (x=50, y=190)

  ram_label = CTkLabel (main_frame, font=font2, text='RAM:', text_color='#fff', bg_color='#292933')
  ram_label.place (x=250, y=160)

  ram_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  ram_entry.place (x=250, y=190)

  HDDorSDD_label = CTkLabel (main_frame, font=font2, text='Unidad de almacenamiento:', text_color='#fff', bg_color='#292933')
  HDDorSDD_label.place (x=50, y=230)

  HDDorSDD_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  HDDorSDD_entry.place (x=50, y=260)

  stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff', bg_color='#292933')
  stat_label.place (x=445, y=160)

  status = StringVar ()
  options = ['Operativo', 'Inoperativo']

  stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#7d01b2', button_color='#7d01b2', button_hover_color='#7d01b2', border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
  stat_options.set ('Operativo')
  stat_options.place (x=445, y=190)

  dateofarrival_label = CTkLabel (main_frame, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff', bg_color='#292933')
  dateofarrival_label.place (x=50, y=300)

  dateofarrival_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  dateofarrival_entry.place (x=50, y=330)

  departuredate_label = CTkLabel (main_frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff', bg_color='#292933')
  departuredate_label.place (x=50, y=360)

  departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  departuredate_entry.place (x=50, y=390)
  #### End of the frame

  submit_button = CTkButton(main_frame, command=submit_bo, font=font2, text_color='#fff', text='Guardar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
  submit_button.place (x=200, y=550)

  clear_button = CTkButton (main_frame, command=new_bo,font=font2, text_color='#fff', text='Registro nuevo', fg_color='#F45e02', hover_color='#CB4E01', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
  clear_button.place (x=330, y=550)

## Keyboards data window
def pk_page ():

  ### Database manipulators
  #### Input re-initiator for data logging
  def new_bo():
    id_entry.delete (0, END)
    name_entry.delete (0, END)
    model_entry.delete (0, END)
    serial_entry.delete (0, END)
    color_entry.delete (0, END)
    colormb_entry.delete (0, END)
    cpu_entry.delete (0, END)
    ram_entry.delete (0, END)
    HDDorSDD_entry.delete (0, END)
    status.set ('Operativo')
    dateofarrival_entry.delete (0, END)
    departuredate_entry.delete (0, END)

  #### Entry that records the data in the database
  def submit_bo ():
    id = id_entry.get ()
    name = name_entry.get ()
    model = model_entry.get ()
    serial = serial_entry.get ()
    color = color_entry.get ()
    colormb = colormb_entry.get ()
    cpu = cpu_entry.get ()
    ram = ram_entry.get ()
    disk = HDDorSDD_entry.get ()
    stat = status.get ()
    dfa = dateofarrival_entry.get ()
    dtd = departuredate_entry.get ()
    try:
      if not (id and name and model and serial and color and colormb and cpu and ram and disk and stat and dfa):
        messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida')
      elif Resources.Connection.id_exist_pc (id):
        messagebox.showerror ('Error', 'El ID ya existe')
      else:
        Resources.Connection.insert_pc (id, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd)
        messagebox.showinfo ('Éxito', 'La información fue registrada')
    except:
      messagebox.showerror ('Error', 'A ocurrido un error')

  ### Fonts for the letters
  font1 = ('Roboto', 30, 'bold')
  font2 = ('Roboto', 18, 'bold')

  ### User interface objects
  title_label = CTkLabel (main_frame, font=font1, text='Datos del teclado', text_color='#fff')
  title_label.place (x=25, y=0)

  #### Objects within the frame
  id_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff', bg_color='#292933')
  id_label.place (x=50, y=40)

  id_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  id_entry.place (x=50, y=70)

  name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff', bg_color='#292933')
  name_label.place (x=250, y=40)

  name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  name_entry.place (x=250, y=70)

  model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff', bg_color='#292933')
  model_label.place (x=445, y=40)

  model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  model_entry.place (x=445, y=70)

  serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff', bg_color='#292933')
  serial_label.place (x=50, y=100)

  serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  serial_entry.place (x=50, y=130)

  color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff', bg_color='#292933')
  color_label.place (x=250, y=100)

  color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  color_entry.place (x=250, y=130)

  colormb_label = CTkLabel (main_frame, font=font2, text='Color de la placa madre:', text_color='#fff', bg_color='#292933')
  colormb_label.place (x=445, y=100)

  colormb_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  colormb_entry.place (x=445, y=130)

  cpu_label = CTkLabel (main_frame, font=font2, text='CPU:', text_color='#fff', bg_color='#292933')
  cpu_label.place (x=50, y=160)

  cpu_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  cpu_entry.place (x=50, y=190)

  ram_label = CTkLabel (main_frame, font=font2, text='RAM:', text_color='#fff', bg_color='#292933')
  ram_label.place (x=250, y=160)

  ram_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  ram_entry.place (x=250, y=190)

  HDDorSDD_label = CTkLabel (main_frame, font=font2, text='Unidad de almacenamiento:', text_color='#fff', bg_color='#292933')
  HDDorSDD_label.place (x=50, y=230)

  HDDorSDD_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  HDDorSDD_entry.place (x=50, y=260)

  stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff', bg_color='#292933')
  stat_label.place (x=445, y=160)

  status = StringVar ()
  options = ['Operativo', 'Inoperativo']

  stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#7d01b2', button_color='#7d01b2', button_hover_color='#7d01b2', border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
  stat_options.set ('Operativo')
  stat_options.place (x=445, y=190)

  dateofarrival_label = CTkLabel (main_frame, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff', bg_color='#292933')
  dateofarrival_label.place (x=50, y=300)

  dateofarrival_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  dateofarrival_entry.place (x=50, y=330)

  departuredate_label = CTkLabel (main_frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff', bg_color='#292933')
  departuredate_label.place (x=50, y=360)

  departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  departuredate_entry.place (x=50, y=390)
  #### End of the frame

  submit_button = CTkButton(main_frame, command=submit_bo, font=font2, text_color='#fff', text='Guardar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
  submit_button.place (x=200, y=550)

  clear_button = CTkButton (main_frame, command=new_bo,font=font2, text_color='#fff', text='Registro nuevo', fg_color='#F45e02', hover_color='#CB4E01', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
  clear_button.place (x=330, y=550)

## Monitors data window
def pm_page ():

  ### Database manipulators
  #### Input re-initiator for data logging
  def new_bo():
    id_entry.delete (0, END)
    name_entry.delete (0, END)
    model_entry.delete (0, END)
    serial_entry.delete (0, END)
    color_entry.delete (0, END)
    colormb_entry.delete (0, END)
    cpu_entry.delete (0, END)
    ram_entry.delete (0, END)
    HDDorSDD_entry.delete (0, END)
    status.set ('Operativo')
    dateofarrival_entry.delete (0, END)
    departuredate_entry.delete (0, END)

  #### Entry that records the data in the database
  def submit_bo ():
    id = id_entry.get ()
    name = name_entry.get ()
    model = model_entry.get ()
    serial = serial_entry.get ()
    color = color_entry.get ()
    colormb = colormb_entry.get ()
    cpu = cpu_entry.get ()
    ram = ram_entry.get ()
    disk = HDDorSDD_entry.get ()
    stat = status.get ()
    dfa = dateofarrival_entry.get ()
    dtd = departuredate_entry.get ()
    try:
      if not (id and name and model and serial and color and colormb and cpu and ram and disk and stat and dfa):
        messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida')
      elif Resources.Connection.id_exist_pc (id):
        messagebox.showerror ('Error', 'El ID ya existe')
      else:
        Resources.Connection.insert_pc (id, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd)
        messagebox.showinfo ('Éxito', 'La información fue registrada')
    except:
      messagebox.showerror ('Error', 'A ocurrido un error')

  ### Fonts for the letters
  font1 = ('Roboto', 30, 'bold')
  font2 = ('Roboto', 18, 'bold')

  ### User interface objects
  title_label = CTkLabel (main_frame, font=font1, text='Datos del monitor', text_color='#fff')
  title_label.place (x=25, y=0)

  #### Objects within the frame
  id_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff', bg_color='#292933')
  id_label.place (x=50, y=40)

  id_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  id_entry.place (x=50, y=70)

  name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff', bg_color='#292933')
  name_label.place (x=250, y=40)

  name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  name_entry.place (x=250, y=70)

  model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff', bg_color='#292933')
  model_label.place (x=445, y=40)

  model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  model_entry.place (x=445, y=70)

  serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff', bg_color='#292933')
  serial_label.place (x=50, y=100)

  serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  serial_entry.place (x=50, y=130)

  color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff', bg_color='#292933')
  color_label.place (x=250, y=100)

  color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  color_entry.place (x=250, y=130)

  colormb_label = CTkLabel (main_frame, font=font2, text='Color de la placa madre:', text_color='#fff', bg_color='#292933')
  colormb_label.place (x=445, y=100)

  colormb_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  colormb_entry.place (x=445, y=130)

  cpu_label = CTkLabel (main_frame, font=font2, text='CPU:', text_color='#fff', bg_color='#292933')
  cpu_label.place (x=50, y=160)

  cpu_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  cpu_entry.place (x=50, y=190)

  ram_label = CTkLabel (main_frame, font=font2, text='RAM:', text_color='#fff', bg_color='#292933')
  ram_label.place (x=250, y=160)

  ram_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  ram_entry.place (x=250, y=190)

  HDDorSDD_label = CTkLabel (main_frame, font=font2, text='Unidad de almacenamiento:', text_color='#fff', bg_color='#292933')
  HDDorSDD_label.place (x=50, y=230)

  HDDorSDD_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  HDDorSDD_entry.place (x=50, y=260)

  stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff', bg_color='#292933')
  stat_label.place (x=445, y=160)

  status = StringVar ()
  options = ['Operativo', 'Inoperativo']

  stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#7d01b2', button_color='#7d01b2', button_hover_color='#7d01b2', border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
  stat_options.set ('Operativo')
  stat_options.place (x=445, y=190)

  dateofarrival_label = CTkLabel (main_frame, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff', bg_color='#292933')
  dateofarrival_label.place (x=50, y=300)

  dateofarrival_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  dateofarrival_entry.place (x=50, y=330)

  departuredate_label = CTkLabel (main_frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff', bg_color='#292933')
  departuredate_label.place (x=50, y=360)

  departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  departuredate_entry.place (x=50, y=390)
  #### End of the frame

  submit_button = CTkButton(main_frame, command=submit_bo, font=font2, text_color='#fff', text='Guardar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
  submit_button.place (x=200, y=550)

  clear_button = CTkButton (main_frame, command=new_bo,font=font2, text_color='#fff', text='Registro nuevo', fg_color='#F45e02', hover_color='#CB4E01', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
  clear_button.place (x=330, y=550)

## Mouses data window
def pmo_page ():

  ### Database manipulators
  #### Input re-initiator for data logging
  def new_bo():
    id_entry.delete (0, END)
    name_entry.delete (0, END)
    model_entry.delete (0, END)
    serial_entry.delete (0, END)
    color_entry.delete (0, END)
    colormb_entry.delete (0, END)
    cpu_entry.delete (0, END)
    ram_entry.delete (0, END)
    HDDorSDD_entry.delete (0, END)
    status.set ('Operativo')
    dateofarrival_entry.delete (0, END)
    departuredate_entry.delete (0, END)

  #### Entry that records the data in the database
  def submit_bo ():
    id = id_entry.get ()
    name = name_entry.get ()
    model = model_entry.get ()
    serial = serial_entry.get ()
    color = color_entry.get ()
    colormb = colormb_entry.get ()
    cpu = cpu_entry.get ()
    ram = ram_entry.get ()
    disk = HDDorSDD_entry.get ()
    stat = status.get ()
    dfa = dateofarrival_entry.get ()
    dtd = departuredate_entry.get ()
    try:
      if not (id and name and model and serial and color and colormb and cpu and ram and disk and stat and dfa):
        messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida')
      elif Resources.Connection.id_exist_pc (id):
        messagebox.showerror ('Error', 'El ID ya existe')
      else:
        Resources.Connection.insert_pc (id, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd)
        messagebox.showinfo ('Éxito', 'La información fue registrada')
    except:
      messagebox.showerror ('Error', 'A ocurrido un error')

  ### Fonts for the letters
  font1 = ('Roboto', 30, 'bold')
  font2 = ('Roboto', 18, 'bold')

  ### User interface objects
  title_label = CTkLabel (main_frame, font=font1, text='Datos del mouse', text_color='#fff')
  title_label.place (x=25, y=0)

  #### Objects within the frame
  id_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff', bg_color='#292933')
  id_label.place (x=50, y=40)

  id_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  id_entry.place (x=50, y=70)

  name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff', bg_color='#292933')
  name_label.place (x=250, y=40)

  name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  name_entry.place (x=250, y=70)

  model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff', bg_color='#292933')
  model_label.place (x=445, y=40)

  model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  model_entry.place (x=445, y=70)

  serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff', bg_color='#292933')
  serial_label.place (x=50, y=100)

  serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  serial_entry.place (x=50, y=130)

  color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff', bg_color='#292933')
  color_label.place (x=250, y=100)

  color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  color_entry.place (x=250, y=130)

  colormb_label = CTkLabel (main_frame, font=font2, text='Color de la placa madre:', text_color='#fff', bg_color='#292933')
  colormb_label.place (x=445, y=100)

  colormb_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  colormb_entry.place (x=445, y=130)

  cpu_label = CTkLabel (main_frame, font=font2, text='CPU:', text_color='#fff', bg_color='#292933')
  cpu_label.place (x=50, y=160)

  cpu_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  cpu_entry.place (x=50, y=190)

  ram_label = CTkLabel (main_frame, font=font2, text='RAM:', text_color='#fff', bg_color='#292933')
  ram_label.place (x=250, y=160)

  ram_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  ram_entry.place (x=250, y=190)

  HDDorSDD_label = CTkLabel (main_frame, font=font2, text='Unidad de almacenamiento:', text_color='#fff', bg_color='#292933')
  HDDorSDD_label.place (x=50, y=230)

  HDDorSDD_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  HDDorSDD_entry.place (x=50, y=260)

  stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff', bg_color='#292933')
  stat_label.place (x=445, y=160)

  status = StringVar ()
  options = ['Operativo', 'Inoperativo']

  stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#7d01b2', button_color='#7d01b2', button_hover_color='#7d01b2', border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
  stat_options.set ('Operativo')
  stat_options.place (x=445, y=190)

  dateofarrival_label = CTkLabel (main_frame, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff', bg_color='#292933')
  dateofarrival_label.place (x=50, y=300)

  dateofarrival_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  dateofarrival_entry.place (x=50, y=330)

  departuredate_label = CTkLabel (main_frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff', bg_color='#292933')
  departuredate_label.place (x=50, y=360)

  departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  departuredate_entry.place (x=50, y=390)
  #### End of the frame

  submit_button = CTkButton(main_frame, command=submit_bo, font=font2, text_color='#fff', text='Guardar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
  submit_button.place (x=200, y=550)

  clear_button = CTkButton (main_frame, command=new_bo,font=font2, text_color='#fff', text='Registro nuevo', fg_color='#F45e02', hover_color='#CB4E01', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
  clear_button.place (x=330, y=550)

## Printers data window
def pp_page ():

  ### Database manipulators
  #### Input re-initiator for data logging
  def new_bo():
    id_entry.delete (0, END)
    name_entry.delete (0, END)
    model_entry.delete (0, END)
    serial_entry.delete (0, END)
    color_entry.delete (0, END)
    colormb_entry.delete (0, END)
    cpu_entry.delete (0, END)
    ram_entry.delete (0, END)
    HDDorSDD_entry.delete (0, END)
    status.set ('Operativo')
    dateofarrival_entry.delete (0, END)
    departuredate_entry.delete (0, END)

  #### Entry that records the data in the database
  def submit_bo ():
    id = id_entry.get ()
    name = name_entry.get ()
    model = model_entry.get ()
    serial = serial_entry.get ()
    color = color_entry.get ()
    colormb = colormb_entry.get ()
    cpu = cpu_entry.get ()
    ram = ram_entry.get ()
    disk = HDDorSDD_entry.get ()
    stat = status.get ()
    dfa = dateofarrival_entry.get ()
    dtd = departuredate_entry.get ()
    try:
      if not (id and name and model and serial and color and colormb and cpu and ram and disk and stat and dfa):
        messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida')
      elif Resources.Connection.id_exist_pc (id):
        messagebox.showerror ('Error', 'El ID ya existe')
      else:
        Resources.Connection.insert_pc (id, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd)
        messagebox.showinfo ('Éxito', 'La información fue registrada')
    except:
      messagebox.showerror ('Error', 'A ocurrido un error')

  ### Fonts for the letters
  font1 = ('Roboto', 30, 'bold')
  font2 = ('Roboto', 18, 'bold')

  ### User interface objects
  title_label = CTkLabel (main_frame, font=font1, text='Datos del impresora', text_color='#fff')
  title_label.place (x=25, y=0)

  #### Objects within the frame
  id_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff', bg_color='#292933')
  id_label.place (x=50, y=40)

  id_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  id_entry.place (x=50, y=70)

  name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff', bg_color='#292933')
  name_label.place (x=250, y=40)

  name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  name_entry.place (x=250, y=70)

  model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff', bg_color='#292933')
  model_label.place (x=445, y=40)

  model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  model_entry.place (x=445, y=70)

  serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff', bg_color='#292933')
  serial_label.place (x=50, y=100)

  serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  serial_entry.place (x=50, y=130)

  color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff', bg_color='#292933')
  color_label.place (x=250, y=100)

  color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  color_entry.place (x=250, y=130)

  colormb_label = CTkLabel (main_frame, font=font2, text='Color de la placa madre:', text_color='#fff', bg_color='#292933')
  colormb_label.place (x=445, y=100)

  colormb_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  colormb_entry.place (x=445, y=130)

  cpu_label = CTkLabel (main_frame, font=font2, text='CPU:', text_color='#fff', bg_color='#292933')
  cpu_label.place (x=50, y=160)

  cpu_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  cpu_entry.place (x=50, y=190)

  ram_label = CTkLabel (main_frame, font=font2, text='RAM:', text_color='#fff', bg_color='#292933')
  ram_label.place (x=250, y=160)

  ram_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  ram_entry.place (x=250, y=190)

  HDDorSDD_label = CTkLabel (main_frame, font=font2, text='Unidad de almacenamiento:', text_color='#fff', bg_color='#292933')
  HDDorSDD_label.place (x=50, y=230)

  HDDorSDD_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  HDDorSDD_entry.place (x=50, y=260)

  stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff', bg_color='#292933')
  stat_label.place (x=445, y=160)

  status = StringVar ()
  options = ['Operativo', 'Inoperativo']

  stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#7d01b2', button_color='#7d01b2', button_hover_color='#7d01b2', border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
  stat_options.set ('Operativo')
  stat_options.place (x=445, y=190)

  dateofarrival_label = CTkLabel (main_frame, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff', bg_color='#292933')
  dateofarrival_label.place (x=50, y=300)

  dateofarrival_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  dateofarrival_entry.place (x=50, y=330)

  departuredate_label = CTkLabel (main_frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff', bg_color='#292933')
  departuredate_label.place (x=50, y=360)

  departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
  departuredate_entry.place (x=50, y=390)
  #### End of the frame

  submit_button = CTkButton(main_frame, command=submit_bo, font=font2, text_color='#fff', text='Guardar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
  submit_button.place (x=200, y=550)

  clear_button = CTkButton (main_frame, command=new_bo,font=font2, text_color='#fff', text='Registro nuevo', fg_color='#F45e02', hover_color='#CB4E01', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
  clear_button.place (x=330, y=550)

## Function to delete the window or close
def delete_pages ():
  for frame in main_frame.winfo_children ():
    frame.destroy ()

## Function to show which button and window is being selected
def hide_indicator ():

  pc_btn_indicator.config (bg=menu_bar_colour)
  pk_btn_indicator.config (bg=menu_bar_colour)
  pm_btn_indicator.config (bg=menu_bar_colour)
  pmo_btn_indicator.config (bg=menu_bar_colour)
  pp_btn_indicator.config (bg=menu_bar_colour)

## Function that shows the page and marks which is the button that is being used
def switch_indication (lb, page):

  hide_indicator ()
  lb.config (bg='white')
  delete_pages ()
  page ()

# Format of the menu
menu_bar_frame = tk.Frame (app, bg=menu_bar_colour)

## Menu buttons
## For the separation of the buttons you should always add 60 from where "Y" starts for example 130 + 60 = 190 + 60 = 250 and so on
pc_btn = CTkButton (menu_bar_frame, text='', image=pc_icon, width=10, height=10, command=lambda: switch_indication (pc_btn_indicator, pc_page))
pc_btn.place (x=9, y=130)

pk_btn = CTkButton (menu_bar_frame, text='', image=pk_icon, width=10, height=10, command=lambda: switch_indication (pk_btn_indicator, pk_page))
pk_btn.place (x=9, y=190)

pm_btn = CTkButton (menu_bar_frame, text='', image=pm_icon, width=10, height=10, command=lambda: switch_indication (pm_btn_indicator, pm_page))
pm_btn.place (x=9, y=250)

pmo_btn = CTkButton (menu_bar_frame, text='', image=pmo_icon, width=10, height=10,  command=lambda: switch_indication (pmo_btn_indicator, pmo_page))
pmo_btn.place (x=9, y=310)

pp_btn = CTkButton (menu_bar_frame, text='', image=pp_icon, width=10, height=10,  command=lambda: switch_indication (pp_btn_indicator, pp_page))
pp_btn.place (x=9, y=370)

## Usage indicator for the button
pc_btn_indicator = tk.Label (menu_bar_frame, bg='white')
pc_btn_indicator.place (x=3, y=130, width=3, height=30)

pk_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pk_btn_indicator.place (x=3, y=190, width=3, height=30)

pm_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pm_btn_indicator.place (x=3, y=250, width=3, height=30)

pmo_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pmo_btn_indicator.place (x=3, y=310, width=3, height=30)

pp_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pp_btn_indicator.place (x=3, y=370, width=3, height=30)

## Form of the menu
menu_bar_frame.pack (side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
menu_bar_frame.pack_propagate (flag=False)
menu_bar_frame.configure (width=45)

## Area where the objects that are selected in the menu will be displayed
main_frame = CTkFrame (app)
main_frame.pack (side=tk.LEFT)
main_frame.pack_propagate (False)
main_frame.configure (width=690, height=600)

app.mainloop ()
