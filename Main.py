
# Libraries
from customtkinter import *
from tkinter import *
from tkinter import messagebox

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection 

# Database manipulators
def new_course():
  id_entry.delete(0,END)
  name_entry.delete(0,END)
  model_entry.delete(0,END)
  serial_entry.delete(0,END)
  status.set('Operativo')

def submit_course():
  id = id_entry.get()
  name = name_entry.get()
  model = model_entry.get()
  serial = serial_entry.get()
  stat = status.get()
  try:
    if not (id and name and model and serial and stat):
      messagebox.showerror('Error', 'Se debe llenar las celdas.')
    elif Resources.Connection.id_exist(id):
      messagebox.showerror('Error', 'ID ya existe.')
    else:
      Resources.Connection.insert_course(id, name, model, serial, stat)
      messagebox.showinfo('Success', 'La información fue registrado')
  except:
    messagebox.showerror('Error','Ocurrio un error.')

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

app = CTk ()
app.title ('CTK - SQLTool')
app.geometry ('700x600')
app.resizable(False,False)

font1 = ('Roboto',30, 'bold')
font2 = ('Roboto',20, 'bold')

title_label = CTkLabel(app, font=font1, text='Datos del computador',text_color='#fff',bg_color='#292933')
title_label.place(x=25, y=20)

frame1 = CTkFrame(app,bg_color='#131314',fg_color='#292933',corner_radius=10,border_width=2,border_color='#0f0',width=650,height=520)
frame1.place(x=25, y=70)

id_label = CTkLabel(frame1, font=font2, text='ID:',text_color='#fff', bg_color='#292933')
id_label.place(x=50, y=15)

id_entry = CTkEntry(frame1, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
id_entry.place(x=50, y=45)

name_label = CTkLabel(frame1, font=font2, text='Nombre:',text_color='#fff',bg_color='#292933')
name_label.place(x=50, y=90)

name_entry = CTkEntry(frame1, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
name_entry.place(x=50, y=120)

stat_label = CTkLabel(frame1, font=font2, text='Estado:',text_color='#fff',bg_color='#292933')
stat_label.place(x=445, y=15)

status = StringVar()
options = ['Operativo', 'Inoperativo']

stat_options = CTkComboBox(frame1,font=font2,text_color='#000', fg_color='#fff',dropdown_hover_color='#7d01b2', button_color='#7d01b2',button_hover_color='#7d01b2',border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
stat_options.set('Operativo')
stat_options.place(x=445, y=45)

serial_label = CTkLabel(frame1, font=font2, text='Serial:',text_color='#fff',bg_color='#292933')
serial_label.place(x=50, y=160)

serial_entry = CTkEntry(frame1, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
serial_entry.place(x=50, y=190)

model_label = CTkLabel(frame1, font=font2, text='Modelo:',text_color='#fff',bg_color='#292933')
model_label.place(x=50, y=220)

model_entry = CTkEntry(frame1, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
model_entry.place(x=50, y=250)

submit_button = CTkButton(app, command=submit_course ,font=font2, text_color='#fff', text='Guardar',fg_color='#02ab10',hover_color='#02920D', bg_color='#292933', cursor='hand2',corner_radius=5, width=100)
submit_button.place(x=200, y=550)

clear_button = CTkButton(app, command=new_course,font=font2, text_color='#fff', text='Registro nuevo',fg_color='#F45e02',hover_color='#CB4E01', bg_color='#292933', cursor='hand2',corner_radius=5, width=100)
clear_button.place(x=330, y=550)



app.mainloop ()
