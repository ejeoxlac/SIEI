from customtkinter import *
from tkinter import *
from tkinter import messagebox

# from sqlite3 import Communication
import Resources.Connection 

set_appearance_mode ('dark')
set_default_color_theme ('blue')

app = CTk ()
app.title ('CTK - SQLTool')
app.geometry ('700x600')
app.resizable(False,False)

font1 = ('Roboto',30, 'bold')
font2 = ('Roboto',20, 'bold')

def new_course():
  id_entry.delete(0,END)
  name_entry.delete(0,END)
  variable1.set('Operativo')
  xx_entry.delete(0,END)
  yy_entry.delete(0,END)

def submit_course():
  id = id_entry.get()
  name = name_entry.get()
  op = variable1.get()
  xx = xx_entry.get()
  yy = yy_entry.get()
  try:
    if not (id and name and op and xx and yy):
      messagebox.showerror('Error', 'Se debe llenar las celdas.')
    elif Resources.Connection.id_exists(id):
      messagebox.showerror('Error', 'ID ya existe.')
    else:
      price_value = int(price)
      Resources.Connection.insert_course(id,name,op,xx,yy_value)
      messagebox.showinfo('Success', 'La información fue registrado')
  except ValueError:
    messagebox.showerror('Error','Price no es entero')
  except:
    messagebox.showerror('Error','Ocurrio un error.')

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

op_label = CTkLabel(frame1, font=font2, text='Estado:',text_color='#fff',bg_color='#292933')
op_label.place(x=445, y=15)

variable1 = StringVar()
options = ['Operativo', 'Inoperativo']

op_options = CTkComboBox(frame1,font=font2,text_color='#000', fg_color='#fff',dropdown_hover_color='#7d01b2', button_color='#7d01b2',button_hover_color='#7d01b2',border_color="#7d01b2", width=150, variable=variable1, values=options, state='readonly')
op_options.set('Operativo')
op_options.place(x=445, y=45)

xx_label = CTkLabel(frame1, font=font2, text='Serial:',text_color='#fff',bg_color='#292933')
xx_label.place(x=50, y=160)

xx_entry = CTkEntry(frame1, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
xx_entry.place(x=50, y=190)

yy_label = CTkLabel(frame1, font=font2, text='Color:',text_color='#fff',bg_color='#292933')
yy_label.place(x=50, y=220)

yy_entry = CTkEntry(frame1, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
yy_entry.place(x=50, y=250)

submit_button = CTkButton(app, command=submit_course ,font=font2, text_color='#fff', text='Guardar',fg_color='#02ab10',hover_color='#02920D', bg_color='#292933', cursor='hand2',corner_radius=5, width=100)
submit_button.place(x=200, y=550)

clear_button = CTkButton(app, command=new_course,font=font2, text_color='#fff', text='Registro nuevo',fg_color='#F45e02',hover_color='#CB4E01', bg_color='#292933', cursor='hand2',corner_radius=5, width=100)
clear_button.place(x=330, y=550)



app.mainloop ()
