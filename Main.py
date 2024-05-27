# Libraries
from customtkinter import *
from tkinter import *
from tkinter import messagebox

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection

# Database manipulators
## Input re-initiator for data logging
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

## Entry that records the data in the database
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
    elif Resources.Connection.id_exist (id):
      messagebox.showerror ('Error', 'El ID ya existe')
    else:
      Resources.Connection.insert_pc (id, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd)
      messagebox.showinfo ('Éxito', 'La información fue registrada')
  except:
    messagebox.showerror ('Error', 'A ocurrido un error')

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

# Format of the window
app = CTk ()
app.title ('Registros para las computadoras')
app.geometry ('700x600')
app.resizable (False, False)

# Fonts for the letters
font1 = ('Roboto', 30, 'bold')
font2 = ('Roboto', 20, 'bold')

# User interface objects
title_label = CTkLabel (app, font=font1, text='Datos del computador', text_color='#fff', bg_color='#292933')
title_label.place (x=25, y=20)

## Frame that will contain the objects that will record the data
frame = CTkFrame (app, bg_color='#131314', fg_color='#292933', corner_radius=10, border_width=2, border_color='#0f0', width=650, height=520)
frame.place (x=25, y=70)

### Objects within the frame
id_label = CTkLabel (frame, font=font2, text='ID:', text_color='#fff', bg_color='#292933')
id_label.place (x=50, y=15)

id_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
id_entry.place (x=50, y=45)

name_label = CTkLabel (frame, font=font2, text='Nombre:', text_color='#fff', bg_color='#292933')
name_label.place (x=250, y=15)

name_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
name_entry.place (x=250, y=45)

model_label = CTkLabel (frame, font=font2, text='Modelo:', text_color='#fff', bg_color='#292933')
model_label.place (x=50, y=90)

model_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
model_entry.place (x=50, y=115)

serial_label = CTkLabel (frame, font=font2, text='Serial:', text_color='#fff', bg_color='#292933')
serial_label.place (x=445, y=15)

serial_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
serial_entry.place (x=445, y=45)

color_label = CTkLabel (frame, font=font2, text='Color:', text_color='#fff', bg_color='#292933')
color_label.place (x=250, y=90)

color_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
color_entry.place (x=250, y=115)

colormb_label = CTkLabel (frame, font=font2, text='Color de la placa madre:', text_color='#fff', bg_color='#292933')
colormb_label.place (x=445, y=90)

colormb_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
colormb_entry.place (x=445, y=115)

cpu_label = CTkLabel (frame, font=font2, text='CPU:', text_color='#fff', bg_color='#292933')
cpu_label.place (x=50, y=160)

cpu_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
cpu_entry.place (x=50, y=190)

ram_label = CTkLabel (frame, font=font2, text='RAM:', text_color='#fff', bg_color='#292933')
ram_label.place (x=250, y=160)

ram_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
ram_entry.place (x=250, y=190)

HDDorSDD_label = CTkLabel (frame, font=font2, text='Unidad de almacenamiento:', text_color='#fff', bg_color='#292933')
HDDorSDD_label.place (x=50, y=230)

HDDorSDD_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
HDDorSDD_entry.place (x=50, y=260)

stat_label = CTkLabel (frame, font=font2, text='Estado:', text_color='#fff', bg_color='#292933')
stat_label.place (x=445, y=160)

status = StringVar ()
options = ['Operativo', 'Inoperativo']

stat_options = CTkComboBox (frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#7d01b2', button_color='#7d01b2', button_hover_color='#7d01b2', border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
stat_options.set ('Operativo')
stat_options.place (x=445, y=190)

dateofarrival_label = CTkLabel (frame, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff', bg_color='#292933')
dateofarrival_label.place (x=50, y=300)

dateofarrival_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
dateofarrival_entry.place (x=50, y=330)

departuredate_label = CTkLabel (frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff', bg_color='#292933')
departuredate_label.place (x=50, y=360)

departuredate_entry = CTkEntry (frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
departuredate_entry.place (x=50, y=390)
### End of the frame

submit_button = CTkButton(app, command=submit_bo, font=font2, text_color='#fff', text='Guardar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
submit_button.place (x=200, y=550)

clear_button = CTkButton (app, command=new_bo,font=font2, text_color='#fff', text='Registro nuevo', fg_color='#F45e02', hover_color='#CB4E01', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
clear_button.place (x=330, y=550)

app.mainloop ()
