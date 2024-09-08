# Libraries
import customtkinter
from customtkinter import *
import tkinter as tk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
from PIL import Image
from datetime import datetime

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection

# I define the view so I can call it
def mainview (mainmenu):

  ## Defined appearance
  set_appearance_mode ('dark')
  set_default_color_theme ('blue')

  ### Model of the menu
  menu_bar_colour = '#383838'

  ## Format of the window
  mainmain = customtkinter.CTkToplevel ()
  mainmain.iconbitmap ('Resources\\Img\\Ico.ico')
  mainmain.title ('Registros de los equipos informaticos')
  mainmain.geometry ('750x650')
  mainmain.resizable (False, False)

  ## Icons
  exit_icon = CTkImage (Image.open('Resources\\Img\\ExitWhite.png'), size=(20, 20))
  pc_icon = CTkImage (Image.open('Resources\\Img\\Computer.png'), size=(20, 20))
  pk_icon = CTkImage (Image.open('Resources\\Img\\Keyboard.png'), size=(20, 20))
  pm_icon = CTkImage (Image.open('Resources\\Img\\Monitor.png'), size=(20, 20))
  pmo_icon = CTkImage (Image.open('Resources\\Img\\Mouse.png'), size=(20, 20))
  pp_icon = CTkImage (Image.open('Resources\\Img\\Printer.png'), size=(20, 20))

  ## Functions to show the windows
  ### Computers data window
  def pc_page ():

    #### Database manipulators
    ##### Input re-initiator for data logging
    def new_dt ():
      idpc_entry.delete (0, END)
      name_entry.delete (0, END)
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      color_entry.delete (0, END)
      colormb_entry.delete (0, END)
      cpu_entry.delete (0, END)
      memory.set ('1 GB DDR2')
      HDDorSDD_entry.delete (0, END)
      status.set ('Operativo')
      departuredate_entry.delete (0, END)

    ##### Entry that records the data in the database
    def submit_dt ():
      idpc = idpc_entry.get ()
      name = name_entry.get ()
      model = model_entry.get ()
      serial = serial_entry.get ()
      color = color_entry.get ()
      colormb = colormb_entry.get ()
      cpu = cpu_entry.get ()
      ram = memory.get ()
      disk = HDDorSDD_entry.get ()
      stat = status.get ()
      dfa = datetime.now().strftime("%d-%m-%Y")
      dtd = departuredate_entry.get ()
      dp = department_entry.get ()
      user = user_entry.get ()
      obs = observation_entry. get ()
      try:
        if not (idpc and name and model and serial and color and colormb and cpu and ram and disk and stat and dfa):
          messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida de la entidad')
        elif Resources.Connection.id_exist_pc (idpc):
          messagebox.showerror ('Error', 'El ID ya existe')
        else:
          Resources.Connection.insert_pc (idpc, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd, dp, user, obs)
          messagebox.showinfo ('Éxito', 'La información fue registrada')
      except:
        messagebox.showerror ('Error', 'A ocurrido un error')

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del computador', text_color='#fff')
    title_label.place (x=25, y=0)

    ##### Objects within the frame
    ###### Front row
    idpc_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpc_label.place (x=50, y=60)

    idpc_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idpc_entry.place (x=50, y=90)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff')
    name_label.place (x=250, y=60)

    name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    name_entry.place (x=250, y=90)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.place (x=445, y=60)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.place (x=445, y=90)

    ###### Second row
    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.place (x=50, y=140)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.place (x=50, y=170)

    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.place (x=250, y=140)

    color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    color_entry.place (x=250, y=170)

    colormb_label = CTkLabel (main_frame, font=font2, text='Color de la placa madre:', text_color='#fff')
    colormb_label.place (x=445, y=140)

    colormb_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    colormb_entry.place (x=445, y=170)

    ###### Third row
    cpu_label = CTkLabel (main_frame, font=font2, text='CPU:', text_color='#fff')
    cpu_label.place (x=50, y=220)

    cpu_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    cpu_entry.place (x=50, y=250)

    ram_label = CTkLabel (main_frame, font=font2, text='RAM:', text_color='#fff')
    ram_label.place (x=250, y=220)

    memory = StringVar ()
    options = ['1 GB DDR2', '2 GB DDR2', '4 GB DDR2', '8 GB DDR2', '16 GB DDR2', '1 GB DDR3', '2 GB DDR3', '4 GB DDR3', '8 GB DDR3', '16 GB DDR3']

    ram_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=memory, values=options, state='readonly')
    ram_options.set ('1 GB DDR2')
    ram_options.place (x=250, y=250)

    HDDorSDD_label = CTkLabel (main_frame, font=font2, text='Unidad de almacenamiento:', text_color='#fff')
    HDDorSDD_label.place (x=445, y=220)

    HDDorSDD_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    HDDorSDD_entry.place (x=445, y=250)

    ###### Fourth row
    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.place (x=50, y=300)

    department_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    department_entry.place (x=50, y=330)

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.place (x=250, y=300)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=250, y=330)

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.place (x=445, y=300)

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=445, y=330)

    ###### Fifth row
    departuredate_label = CTkLabel (main_frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.place (x=50, y=380)

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    departuredate_entry.place (x=50, y=410)

    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.place (x=445, y=380)

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=200, height=100, corner_radius=10, wrap=WORD)
    observation_entry.place (x=445, y=410)

    ###### Button area
    submit_button = CTkButton(main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.place (x=180, y=550)

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.place (x=360, y=550)
    ##### End of the frame

  ### Keyboards data window
  def pk_page ():

    #### Database manipulators
    ##### Input re-initiator for data logging
    def new_dt ():
      idpk_entry.delete (0, END)
      name_entry.delete (0, END)
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      color_entry.delete (0, END)
      status.set ('Operativo')
      departuredate_entry.delete (0, END)

    ##### Entry that records the data in the database
    def submit_dt ():
      idpk = idpk_entry.get ()
      name = name_entry.get ()
      model = model_entry.get ()
      serial = serial_entry.get ()
      color = color_entry.get ()
      stat = status.get ()
      dfa = dfa = datetime.now().strftime("%d-%m-%Y")
      dtd = departuredate_entry.get ()
      dp = department_entry.get ()
      user = user_entry.get ()
      obs = observation_entry. get ()
      try:
        if not (idpk and name and model and serial and color and stat and dfa):
          messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida de la entidad')
        elif Resources.Connection.id_exist_pk (idpk):
          messagebox.showerror ('Error', 'El ID ya existe')
        else:
          Resources.Connection.insert_pk (idpk, name, model, serial, color, stat, dfa, dtd, dp, user, obs)
          messagebox.showinfo ('Éxito', 'La información fue registrada')
      except:
        messagebox.showerror ('Error', 'A ocurrido un error')

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del teclado', text_color='#fff')
    title_label.place (x=25, y=0)

    ##### Objects within the frame
    ###### Front row
    idpk_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpk_label.place (x=50, y=60)

    idpk_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idpk_entry.place (x=50, y=90)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff')
    name_label.place (x=250, y=60)

    name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    name_entry.place (x=250, y=90)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.place (x=445, y=60)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.place (x=445, y=90)

    ###### Second row
    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.place (x=50, y=140)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.place (x=50, y=170)

    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.place (x=250, y=140)

    color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    color_entry.place (x=250, y=170)

    ###### Third row

    ###### Fourth row
    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.place (x=50, y=300)

    department_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    department_entry.place (x=50, y=330)

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.place (x=250, y=300)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=250, y=330)

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.place (x=445, y=300)

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=445, y=330)

    ###### Fifth row
    departuredate_label = CTkLabel (main_frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.place (x=50, y=380)

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    departuredate_entry.place (x=50, y=410)

    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.place (x=445, y=380)

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=200, height=100, corner_radius=10)
    observation_entry.place (x=445, y=410)

    ###### Button area
    submit_button = CTkButton(main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.place (x=180, y=550)

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.place (x=360, y=550)
    ##### End of the frame

  ### Monitors data window
  def pm_page ():

    #### Database manipulators
    ##### Input re-initiator for data logging
    def new_dt ():
      idpm_entry.delete (0, END)
      name_entry.delete (0, END)
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      color_entry.delete (0, END)
      status.set ('Operativo')
      departuredate_entry.delete (0, END)

    ##### Entry that records the data in the database
    def submit_dt ():
      idpm = idpm_entry.get ()
      name = name_entry.get ()
      model = model_entry.get ()
      serial = serial_entry.get ()
      color = color_entry.get ()
      stat = status.get ()
      dfa = datetime.now().strftime("%d-%m-%Y")
      dtd = departuredate_entry.get ()
      dp = department_entry.get ()
      user = user_entry.get ()
      obs = observation_entry. get ()
      try:
        if not (idpm and name and model and serial and color and stat and dfa):
          messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida de la entidad')
        elif Resources.Connection.id_exist_pm (idpm):
          messagebox.showerror ('Error', 'El ID ya existe')
        else:
          Resources.Connection.insert_pm (idpm, name, model, serial, color, stat, dfa, dtd, dp, user, obs)
          messagebox.showinfo ('Éxito', 'La información fue registrada')
      except:
        messagebox.showerror ('Error', 'A ocurrido un error')

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del monitor', text_color='#fff')
    title_label.place (x=25, y=0)

    ##### Objects within the frame
    ###### Front row
    idpm_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpm_label.place (x=50, y=60)

    idpm_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idpm_entry.place (x=50, y=90)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff')
    name_label.place (x=250, y=60)

    name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    name_entry.place (x=250, y=90)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.place (x=445, y=60)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.place (x=445, y=90)

    ###### Second row
    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.place (x=50, y=140)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.place (x=50, y=170)

    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.place (x=250, y=140)

    color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    color_entry.place (x=250, y=170)

    ###### Third row

    ###### Fourth row
    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.place (x=50, y=300)

    department_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    department_entry.place (x=50, y=330)

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.place (x=250, y=300)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=250, y=330)

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.place (x=445, y=300)

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=445, y=330)

    ###### Fifth row
    departuredate_label = CTkLabel (main_frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.place (x=50, y=380)

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    departuredate_entry.place (x=50, y=410)

    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.place (x=445, y=380)

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=200, height=100, corner_radius=10)
    observation_entry.place (x=445, y=410)

    ###### Button area
    submit_button = CTkButton(main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.place (x=180, y=550)

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.place (x=360, y=550)
    ##### End of the frame

  ### Mouses data window
  def pmo_page ():

    #### Database manipulators
    ##### Input re-initiator for data logging
    def new_dt ():
      idpmo_entry.delete (0, END)
      name_entry.delete (0, END)
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      color_entry.delete (0, END)
      status.set ('Operativo')
      departuredate_entry.delete (0, END)

    ##### Entry that records the data in the database
    def submit_dt ():
      idpmo = idpmo_entry.get ()
      name = name_entry.get ()
      model = model_entry.get ()
      serial = serial_entry.get ()
      color = color_entry.get ()
      stat = status.get ()
      dfa = datetime.now().strftime("%d-%m-%Y")
      dtd = departuredate_entry.get ()
      dp = department_entry.get ()
      user = user_entry.get ()
      obs = observation_entry. get ()
      try:
        if not (idpmo and name and model and serial and color and stat and dfa):
          messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida de la entidad')
        elif Resources.Connection.id_exist_pmo (idpmo):
          messagebox.showerror ('Error', 'El ID ya existe')
        else:
          Resources.Connection.insert_pmo (idpmo, name, model, serial, color, stat, dfa, dtd, dp, user, obs)
          messagebox.showinfo ('Éxito', 'La información fue registrada')
      except:
        messagebox.showerror ('Error', 'A ocurrido un error')

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del mouse', text_color='#fff')
    title_label.place (x=25, y=0)

    ##### Objects within the frame
    ###### Front row
    idpmo_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpmo_label.place (x=50, y=60)

    idpmo_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idpmo_entry.place (x=50, y=90)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff')
    name_label.place (x=250, y=60)

    name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    name_entry.place (x=250, y=90)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.place (x=445, y=60)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.place (x=445, y=90)

    ###### Second row
    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.place (x=50, y=140)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.place (x=50, y=170)

    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.place (x=250, y=140)

    color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    color_entry.place (x=250, y=170)

    ###### Third row

    ###### Fourth row
    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.place (x=50, y=300)

    department_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    department_entry.place (x=50, y=330)

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.place (x=250, y=300)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=250, y=330)

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.place (x=445, y=300)

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=445, y=330)

    ###### Fifth row
    departuredate_label = CTkLabel (main_frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.place (x=50, y=380)

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    departuredate_entry.place (x=50, y=410)

    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.place (x=445, y=380)

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=200, height=100, corner_radius=10)
    observation_entry.place (x=445, y=410)

    ###### Button area
    submit_button = CTkButton(main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.place (x=180, y=550)

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.place (x=360, y=550)
    ##### End of the frame

  ### Printers data window
  def pp_page ():

    #### Database manipulators
    ##### Input re-initiator for data logging
    def new_dt ():
      idpp_entry.delete (0, END)
      name_entry.delete (0, END)
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      color_entry.delete (0, END)
      status.set ('Operativo')
      departuredate_entry.delete (0, END)

    ##### Entry that records the data in the database
    def submit_dt ():
      idpp = idpp_entry.get ()
      name = name_entry.get ()
      model = model_entry.get ()
      serial = serial_entry.get ()
      color = color_entry.get ()
      stat = status.get ()
      dfa = datetime.now().strftime("%d-%m-%Y")
      dtd = departuredate_entry.get ()
      dp = department_entry.get ()
      user = user_entry.get ()
      obs = observation_entry. get ()
      try:
        if not (idpp and name and model and serial and color and stat and dfa):
          messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida de la entidad')
        elif Resources.Connection.id_exist_pp (idpp):
          messagebox.showerror ('Error', 'El ID ya existe')
        else:
          Resources.Connection.insert_pp (idpp, name, model, serial, color, stat, dfa, dtd, dp, user, obs)
          messagebox.showinfo ('Éxito', 'La información fue registrada')
      except:
        messagebox.showerror ('Error', 'A ocurrido un error')

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos de la impresora', text_color='#fff')
    title_label.place (x=25, y=0)

    ##### Objects within the frame
    ###### Front row
    idpp_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpp_label.place (x=50, y=60)

    idpp_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idpp_entry.place (x=50, y=90)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff')
    name_label.place (x=250, y=60)

    name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    name_entry.place (x=250, y=90)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.place (x=445, y=60)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.place (x=445, y=90)

    ###### Second row
    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.place (x=50, y=140)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.place (x=50, y=170)

    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.place (x=250, y=140)

    color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    color_entry.place (x=250, y=170)

    ###### Third row

    ###### Fourth row
    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.place (x=50, y=300)

    department_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    department_entry.place (x=50, y=330)

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.place (x=250, y=300)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=250, y=330)

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.place (x=445, y=300)

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=445, y=330)

    ###### Fifth row
    departuredate_label = CTkLabel (main_frame, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.place (x=50, y=380)

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    departuredate_entry.place (x=50, y=410)

    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.place (x=445, y=380)

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=200, height=100, corner_radius=10)
    observation_entry.place (x=445, y=410)

    ###### Button area
    submit_button = CTkButton(main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.place (x=180, y=550)

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.place (x=360, y=550)
    ##### End of the frame

  ### Function to delete the window or close
  def delete_pages ():
    
    for frame in main_frame.winfo_children ():
      frame.destroy ()

  ### Function to return to the menu window
  def menu_page ():
    if messagebox.askyesno ('Confirmación', '¿Está seguro que desea salir?'):
      mainmain.destroy ()
      mainmenu.deiconify ()

  mainmain.protocol("WM_DELETE_WINDOW", menu_page) 

  ## Function to show which button and window is being selected
  def hide_indicator ():

    exit_btn_indicator.config (bg=menu_bar_colour)
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

  ## Generator of help message for objects in which the cursor is needed to be positioned to know more about the object
  class CustomHovertip (Hovertip):
    def showcontents (main):
      label = tk.Label (main.tipwindow, text=f'''{main.text}''', justify=tk.LEFT, bg='#151515', fg='#ffffff', relief=tk.SOLID, borderwidth=1, font=('Roboto', 12))
      label.pack ()

  ## Format of the menu
  menu_bar_frame = tk.Frame (mainmain, bg=menu_bar_colour)

  ### Menu buttons
  exit_btn = CTkButton (menu_bar_frame, text='', image=exit_icon, width=10, height=10, command=lambda: switch_indication (exit_btn_indicator, menu_page))
  exit_btn.place (x=9, y=20)
  CustomHovertip (exit_btn, text='Ir al menu', hover_delay=500)

  ### For the separation of the buttons you should always add 60 from where "Y" starts for example 130 + 60 = 190 + 60 = 250 and so on
  pc_btn = CTkButton (menu_bar_frame, text='', image=pc_icon, width=10, height=10, command=lambda: switch_indication (pc_btn_indicator, pc_page))
  pc_btn.place (x=9, y=130)
  CustomHovertip (pc_btn, text='Registrar computadoras', hover_delay=500)

  pk_btn = CTkButton (menu_bar_frame, text='', image=pk_icon, width=10, height=10, command=lambda: switch_indication (pk_btn_indicator, pk_page))
  pk_btn.place (x=9, y=190)
  CustomHovertip (pk_btn, text='Registrar teclados', hover_delay=500)

  pm_btn = CTkButton (menu_bar_frame, text='', image=pm_icon, width=10, height=10, command=lambda: switch_indication (pm_btn_indicator, pm_page))
  pm_btn.place (x=9, y=250)
  CustomHovertip (pm_btn, text='Registrar monitores', hover_delay=500)

  pmo_btn = CTkButton (menu_bar_frame, text='', image=pmo_icon, width=10, height=10,  command=lambda: switch_indication (pmo_btn_indicator, pmo_page))
  pmo_btn.place (x=9, y=310)
  CustomHovertip (pmo_btn, text='Registrar mouses', hover_delay=500)

  pp_btn = CTkButton (menu_bar_frame, text='', image=pp_icon, width=10, height=10,  command=lambda: switch_indication (pp_btn_indicator, pp_page))
  pp_btn.place (x=9, y=370)
  CustomHovertip (pp_btn, text='Registrar impresoras', hover_delay=500)

  ### Usage indicator for the button
  exit_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
  exit_btn_indicator.place (x=3, y=20, width=2, height=28)

  pc_btn_indicator = tk.Label (menu_bar_frame, bg='white')
  pc_btn_indicator.place (x=3, y=130, width=2, height=28)

  pk_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
  pk_btn_indicator.place (x=3, y=190, width=2, height=28)

  pm_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
  pm_btn_indicator.place (x=3, y=250, width=2, height=28)

  pmo_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
  pmo_btn_indicator.place (x=3, y=310, width=2, height=28)

  pp_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
  pp_btn_indicator.place (x=3, y=370, width=2, height=28)

  ### Form of the menu
  menu_bar_frame.pack (side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
  menu_bar_frame.pack_propagate (flag=False)
  menu_bar_frame.configure (width=45)

  ### Area where the objects that are selected in the menu will be displayed
  main_frame = CTkFrame (mainmain)
  main_frame.pack (side=tk.LEFT)
  main_frame.pack_propagate (False)
  main_frame.configure (width=690, height=600)

  ## To display one of the pages
  pc_page ()

  mainmain.mainloop ()
