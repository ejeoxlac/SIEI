# Libraries
import customtkinter
from customtkinter import *
import tkinter as tk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
from PIL import Image
from tkcalendar import *
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
  mainmain.geometry ('960x600')
  mainmain.resizable (False, False)

  ## Code to center the application window
  ### Refresh the window to make sure the size of it
  mainmain.update_idletasks ()
  ### Get the screen size
  screen_width = mainmain.winfo_screenwidth ()
  screen_height = mainmain.winfo_screenheight ()
  ### Get the size of the window
  win_width = mainmain.winfo_width ()
  win_height = mainmain.winfo_height ()
  ### Calculate the centered position
  x = (screen_width // 2) - (win_width // 2)
  y = (screen_height // 2) - (win_height // 2)
  ### Set the new position
  mainmain.geometry(f"+{x}+{y}")

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
      namepc.set ('Vit')
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      colorpc.set ('Negro')
      modelmb_entry.delete (0, END)
      colormbpc.set ('Verde')
      graphicscard.set ('NVIDIA')
      graphicscardmodel_entry.delete (0, END)
      cpu_entry.delete (0, END)
      memory.set ('1 GB DDR2')
      HDDorSDD_entry.delete (0, END)
      so.set ('Windows 11')
      departments.set ('Informática')
      user_entry.delete (0, END)
      status.set ('Operativo')
      departuredate_entry.delete (0, END)
      observation_entry.delete ('1.0', 'end-1c')

    ##### Entry that records the data in the database
    def submit_dt ():
      idpc = idpc_entry.get ()
      name = namepc.get ()
      model = model_entry.get ()
      serial = serial_entry.get ()
      color = colorpc.get ()
      modelmb = modelmb_entry.get ()
      colormb = colormbpc.get ()
      gcn = graphicscard.get ()
      gcm = graphicscardmodel_entry.get ()
      cpu = cpu_entry.get ()
      ram = memory.get ()
      disk = HDDorSDD_entry.get ()
      pcso = so.get ()
      dp = departments.get ()
      user = user_entry.get ()
      stat = status.get ()
      dfa = datetime.now().strftime ('%d-%m-%Y')
      dtd = departuredate_entry.get ()
      obs = observation_entry.get ('1.0', 'end-1c')
      try:
        if not (idpc and name and model and serial and color and modelmb and colormb and cpu and ram and disk and pcso and dp and stat and dfa):
          messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida de la entidad')
        elif Resources.Connection.id_exist_pc (idpc):
          messagebox.showerror ('Error', 'El ID ya existe')
        else:
          Resources.Connection.insert_pc (idpc, name, model, serial, color, modelmb, colormb, gcn, gcm, cpu, ram, disk, pcso, dp, user, stat, dfa, dtd, obs)
          messagebox.showinfo ('Éxito', 'La información fue registrada')
      except:
        messagebox.showerror ('Error', 'A ocurrido un error')

    #### Validates if they are only numbers and dashes
    def validate_numbers_entry (char):
      if char == '' or all (c.isdigit() or c == '-' for c in char):
        return True
      else:
        return False

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')
    font3 = ('Roboto', 16, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del computador', text_color='#fff')
    title_label.place (x=25, y=5)

    ##### Objects within the frame
    ###### Front row
    idpc_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpc_label.place (x=50, y=60)

    idpc_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idpc_entry.place (x=50, y=90)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre de la marca:', text_color='#fff')
    name_label.place (x=280, y=60)

    namepc = StringVar ()
    options = ['Vit', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Microsoft', 'Google', 'Apple']

    name = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepc, values=options, state='readonly')
    name.set ('Vit')
    name.place (x=280, y=90)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.place (x=485, y=60)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.place (x=485, y=90)

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.place (x=680, y=60)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.place (x=680, y=90)

    ###### Second row
    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.place (x=50, y=140)

    colorpc = StringVar ()
    options = ['Negro', 'Plata', 'Gris', 'Azul', 'Blanco']

    color = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpc, values=options, state='readonly')
    color.set ('Negro')
    color.place (x=50, y=170)

    modelmb_label = CTkLabel (main_frame, font=font3, text='Modelo de la placa madre:', text_color='#fff')
    modelmb_label.place (x=280, y=140)

    modelmb_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    modelmb_entry.place (x=280, y=170)

    colormb_label = CTkLabel (main_frame, font=font3, text='Color de la placa madre:', text_color='#fff')
    colormb_label.place (x=485, y=140)

    colormbpc = StringVar ()
    options = ['Verde', 'Negro', 'Azul', 'Rojo', 'Blanco']

    colormb = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colormbpc, values=options, state='readonly')
    colormb.set ('Verde')
    colormb.place (x=485, y=170)

    graphicscardname_label = CTkLabel (main_frame, font=font3, text='Marca de la grafica:', text_color='#fff')
    graphicscardname_label.place (x=680, y=140)

    graphicscard = StringVar ()
    options = ['NVIDIA', 'AMD', 'Intel', 'ASUS', 'EVGA', 'MSI', 'Zotac']

    graphicscardmodel = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=graphicscard, values=options, state='readonly')
    graphicscardmodel.set ('NVIDIA')
    graphicscardmodel.place (x=680, y=170)

    ###### Third row
    graphicscardmodel_label = CTkLabel (main_frame, font=font3, text='Modelo de la grafica:', text_color='#fff')
    graphicscardmodel_label.place (x=50, y=220)

    graphicscardmodel_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    graphicscardmodel_entry.place (x=50, y=250)

    cpu_label = CTkLabel (main_frame, font=font2, text='CPU:', text_color='#fff')
    cpu_label.place (x=280, y=220)

    cpu_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    cpu_entry.place (x=280, y=250)

    ram_label = CTkLabel (main_frame, font=font2, text='RAM:', text_color='#fff')
    ram_label.place (x=485, y=220)

    memory = StringVar ()
    options = ['1 GB DDR2', '2 GB DDR2', '4 GB DDR2', '8 GB DDR2', '16 GB DDR2', '32 GB DDR2', '1 GB DDR3', '2 GB DDR3', '4 GB DDR3', '8 GB DDR3', '16 GB DDR3', '32 GB DDR3']

    ram_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=memory, values=options, state='readonly')
    ram_options.set ('1 GB DDR2')
    ram_options.place (x=485, y=250)

    HDDorSDD_label = CTkLabel (main_frame, font=font3, text='Unidad de almacenamiento:', text_color='#fff')
    HDDorSDD_label.place (x=680, y=220)

    HDDorSDD_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    HDDorSDD_entry.place (x=680, y=250)

    ###### Fourth row
    win_label = CTkLabel (main_frame, font=font2, text='Sistema operativo:', text_color='#fff')
    win_label.place (x=50, y=300)

    so = StringVar ()
    options = ['Windows 11', 'Windows 10', 'Windows 8', 'Windows 7', 'Windows XP', 'GNU/Linux', 'iOS']

    win_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=so, values=options, state='readonly')
    win_options.set ('Windows 11')
    win_options.place (x=50, y=330)

    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.place (x=280, y=300)

    departments = StringVar ()
    options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo']

    department_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Informática')
    department_options.place (x=280, y=330)

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.place (x=485, y=300)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=485, y=330)

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.place (x=680, y=300)

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=680, y=330)

    ###### Fifth row
    departuredate_label = CTkLabel (main_frame, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.place (x=50, y=380)

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
    departuredate_entry.place (x=50, y=410)

    ####### Displays a calendar to facilitate the selection of the date
    def calendar ():
        ######## Create a new window for the calendar
        window_callendary = tk.Toplevel (main_frame)
        window_callendary.title ('Calendario seleccionable')

        ######## Create a calendar widget
        calendar = Calendar (window_callendary, date_pattern='dd-mm-y', selectmode='day')
        calendar.pack (pady=20)

        ######## Function to show the selected date in the Entry of the main window
        def show_calendar_date ():
          date_selected = calendar.get_date ()
          departuredate_entry.configure (state='normal')
          departuredate_entry.delete (0, tk.END)
          departuredate_entry.insert (0, date_selected)
          departuredate_entry.configure (state='readonly')

        ######## button to show the selected date
        date_button = tk.Button (window_callendary, text='Mostrar fecha', command=show_calendar_date)
        date_button.pack (pady=10)

    calendar_button = CTkButton (main_frame, text='Abrir Calendario', command=calendar)
    calendar_button.place (x=54, y=460)

    def delete_date ():
      departuredate_entry.configure (state='normal')
      departuredate_entry.delete (0, tk.END)
      departuredate_entry.configure (state='readonly')

    date_delete_button = CTkButton (main_frame, text='Borrar Fecha', command=delete_date)
    date_delete_button.place (x=54, y=510)

    ####### Settings to avoid manually modifying the date
    departuredate_entry.configure (state='readonly')

    ###### Sixth row

    ###### Fifth and sixth row
    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.place (x=485, y=380)

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
    observation_entry.place (x=485, y=410)

    ###### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
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
      namepk.set ('Vit')
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      colorpk.set ('Negro')
      departments.set ('Informática')
      user_entry.delete (0, END)
      status.set ('Operativo')
      departuredate_entry.delete (0, END)
      observation_entry.delete ('1.0', 'end-1c')

    ##### Entry that records the data in the database
    def submit_dt ():
      idpk = idpk_entry.get ()
      name = namepk.get ()
      model = model_entry.get ()
      serial = serial_entry.get ()
      color = colorpk.get ()
      dp = departments.get ()
      user = user_entry.get ()
      stat = status.get ()
      dfa = datetime.now().strftime ('%d-%m-%Y')
      dtd = departuredate_entry.get ()
      obs = observation_entry.get ('1.0', 'end-1c')
      try:
        if not (idpk and name and model and serial and color and dp and stat and dfa):
          messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida de la entidad')
        elif Resources.Connection.id_exist_pk (idpk):
          messagebox.showerror ('Error', 'El ID ya existe')
        else:
          Resources.Connection.insert_pk (idpk, name, model, serial, color, dp, user, stat, dfa, dtd, obs)
          messagebox.showinfo ('Éxito', 'La información fue registrada')
      except:
        messagebox.showerror ('Error', 'A ocurrido un error')

    #### Validates if they are only numbers and dashes
    def validate_numbers_entry (char):
      if char == '' or all (c.isdigit() or c == '-' for c in char):
        return True
      else:
        return False

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')
    font3 = ('Roboto', 16, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del teclado', text_color='#fff')
    title_label.place (x=25, y=5)

    ##### Objects within the frame
    ###### Front row
    idpk_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpk_label.place (x=50, y=60)

    idpk_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idpk_entry.place (x=50, y=90)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre de la marca:', text_color='#fff')
    name_label.place (x=280, y=60)

    namepk = StringVar ()
    options = ['Vit', 'Dell', 'Logitech', 'Corsair']

    name = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepk, values=options, state='readonly')
    name.set ('Vit')
    name.place (x=280, y=90)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.place (x=485, y=60)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.place (x=485, y=90)

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.place (x=680, y=60)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.place (x=680, y=90)

    ###### Second row
    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.place (x=50, y=140)

    colorpk = StringVar ()
    options = ['Negro', 'Plata', 'Gris', 'Blanco', 'Verde', 'Amarillo', 'Rojo']

    color = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpk, values=options, state='readonly')
    color.set ('Negro')
    color.place (x=50, y=170)

    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.place (x=280, y=140)

    departments = StringVar ()
    options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo']

    department_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Informática')
    department_options.place (x=280, y=170)

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.place (x=485, y=140)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=485, y=170)

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.place (x=680, y=140)

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=680, y=170)

    ###### Third row
    departuredate_label = CTkLabel (main_frame, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.place (x=50, y=220)

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
    departuredate_entry.place (x=50, y=250)

    ####### Displays a calendar to facilitate the selection of the date
    def calendar ():
        ######## Create a new window for the calendar
        window_callendary = tk.Toplevel (main_frame)
        window_callendary.title ('Calendario seleccionable')

        ######## Create a calendar widget
        calendar = Calendar (window_callendary, date_pattern='dd-mm-y', selectmode='day')
        calendar.pack (pady=20)

        ######## Function to show the selected date in the Entry of the main window
        def show_calendar_date ():
          date_selected = calendar.get_date ()
          departuredate_entry.configure (state='normal')
          departuredate_entry.delete (0, tk.END)
          departuredate_entry.insert (0, date_selected)
          departuredate_entry.configure (state='readonly')

        ######## button to show the selected date
        date_button = tk.Button (window_callendary, text='Mostrar fecha', command=show_calendar_date)
        date_button.pack (pady=10)

    calendar_button = CTkButton (main_frame, text='Abrir Calendario', command=calendar)
    calendar_button.place (x=54, y=300)

    def delete_date ():
      departuredate_entry.configure (state='normal')
      departuredate_entry.delete (0, tk.END)
      departuredate_entry.configure (state='readonly')

    date_delete_button = CTkButton (main_frame, text='Borrar Fecha', command=delete_date)
    date_delete_button.place (x=54, y=350)

    ####### Settings to avoid manually modifying the date
    departuredate_entry.configure (state='readonly')

    ###### Fourth row

    ###### Fifth row

    ###### Sixth row

    ###### Fifth and sixth row
    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.place (x=485, y=380)

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
    observation_entry.place (x=485, y=410)

    ###### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
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
      namepm.set ('Vit')
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      colorpm.set ('Negro')
      typescreeninch.set ('18 pulgadas')
      typeconnectorport.set ('VGA')
      departments.set ('Informática')
      user_entry.delete (0, END)
      status.set ('Operativo')
      departuredate_entry.delete (0, END)
      observation_entry.delete ('1.0', 'end-1c')

    ##### Entry that records the data in the database
    def submit_dt ():
      idpm = idpm_entry.get ()
      name = namepm.get ()
      model = model_entry.get ()
      serial = serial_entry.get ()
      color = colorpm.get ()
      tsi = typescreeninch.get ()
      tcp = typeconnectorport.get ()
      dp = departments.get ()
      user = user_entry.get ()
      stat = status.get ()
      dfa = datetime.now().strftime ('%d-%m-%Y')
      dtd = departuredate_entry.get ()
      obs = observation_entry.get ('1.0', 'end-1c')
      try:
        if not (idpm and name and model and serial and color and tsi and tcp and dp and stat and dfa):
          messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida de la entidad')
        elif Resources.Connection.id_exist_pm (idpm):
          messagebox.showerror ('Error', 'El ID ya existe')
        else:
          Resources.Connection.insert_pm (idpm, name, model, serial, color, tsi, tcp, dp, user, stat, dfa, dtd, obs)
          messagebox.showinfo ('Éxito', 'La información fue registrada')
      except:
        messagebox.showerror ('Error', 'A ocurrido un error')

    #### Validates if they are only numbers and dashes
    def validate_numbers_entry (char):
      if char == '' or all (c.isdigit() or c == '-' for c in char):
        return True
      else:
        return False

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')
    font3 = ('Roboto', 16, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del monitor', text_color='#fff')
    title_label.place (x=25, y=5)

    ##### Objects within the frame
    ###### Front row
    idpm_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpm_label.place (x=50, y=60)

    idpm_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idpm_entry.place (x=50, y=90)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre de la marca:', text_color='#fff')
    name_label.place (x=280, y=60)

    namepm = StringVar ()
    options = ['Vit', 'Dell', 'Samsung', 'Asus', 'LG', 'Acer', 'Dahua', 'BenQ', 'HP']

    name = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepm, values=options, state='readonly')
    name.set ('Vit')
    name.place (x=280, y=90)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.place (x=485, y=60)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.place (x=485, y=90)

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.place (x=680, y=60)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.place (x=680, y=90)

    ###### Second row
    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.place (x=50, y=140)

    colorpm = StringVar ()
    options = ['Negro', 'Plata', 'Gris', 'Blanco']

    color = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpm, values=options, state='readonly')
    color.set ('Negro')
    color.place (x=50, y=170)

    typescreen_label = CTkLabel (main_frame, font=font2, text='Tipo de pantalla:', text_color='#fff')
    typescreen_label.place (x=280, y=140)

    typescreeninch = StringVar ()
    options = ['18 pulgadas', '19 pulgadas', '22 pulgadas', '24 pulgadas', '28 pulgadas', '32 pulgadas', '40 pulgadas', '42 pulgadas', '43 pulgadas', '48 pulgadas', '49 pulgadas', '50 pulgadas', '55 pulgadas', '60 pulgadas', '65 pulgadas', '70 pulgadas', '75 pulgadas', '77 pulgadas', '85 pulgadas']

    typescreen_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=typescreeninch, values=options, state='readonly')
    typescreen_options.set ('18 pulgadas')
    typescreen_options.place (x=280, y=170)

    typeconnector_label = CTkLabel (main_frame, font=font2, text='Tipo de conector:', text_color='#fff')
    typeconnector_label.place (x=485, y=140)

    typeconnectorport = StringVar ()
    options = ['VGA', 'HDMI', 'DisplayPort', 'DVI']

    typeconnector_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=typeconnectorport, values=options, state='readonly')
    typeconnector_options.set ('VGA')
    typeconnector_options.place (x=485, y=170)

    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.place (x=680, y=140)

    departments = StringVar ()
    options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo']

    department_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Informática')
    department_options.place (x=680, y=170)

    ###### Third row
    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.place (x=50, y=220)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=50, y=250)

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.place (x=280, y=220)

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=280, y=250)

    ###### Fourth row
    departuredate_label = CTkLabel (main_frame, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.place (x=50, y=300)

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
    departuredate_entry.place (x=50, y=330)

    ####### Displays a calendar to facilitate the selection of the date
    def calendar ():
        ######## Create a new window for the calendar
        window_callendary = tk.Toplevel (main_frame)
        window_callendary.title ('Calendario seleccionable')

        ######## Create a calendar widget
        calendar = Calendar (window_callendary, date_pattern='dd-mm-y', selectmode='day')
        calendar.pack (pady=20)

        ######## Function to show the selected date in the Entry of the main window
        def show_calendar_date ():
          date_selected = calendar.get_date ()
          departuredate_entry.configure (state='normal')
          departuredate_entry.delete (0, tk.END)
          departuredate_entry.insert (0, date_selected)
          departuredate_entry.configure (state='readonly')

        ######## button to show the selected date
        date_button = tk.Button (window_callendary, text='Mostrar fecha', command=show_calendar_date)
        date_button.pack (pady=10)

    calendar_button = CTkButton (main_frame, text='Abrir Calendario', command=calendar)
    calendar_button.place (x=54, y=380)

    def delete_date ():
      departuredate_entry.configure (state='normal')
      departuredate_entry.delete (0, tk.END)
      departuredate_entry.configure (state='readonly')

    date_delete_button = CTkButton (main_frame, text='Borrar Fecha', command=delete_date)
    date_delete_button.place (x=54, y=430)

    ####### Settings to avoid manually modifying the date
    departuredate_entry.configure (state='readonly')

    ###### Fifth row

    ###### Sixth row

    ###### Fifth and sixth row
    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.place (x=485, y=380)

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
    observation_entry.place (x=485, y=410)

    ###### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
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
      namepmo.set ('Vit')
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      colorpmo.set ('Negro')
      departments.set ('Informática')
      user_entry.delete (0, END)
      status.set ('Operativo')
      departuredate_entry.delete (0, END)
      observation_entry.delete ('1.0', 'end-1c')

    ##### Entry that records the data in the database
    def submit_dt ():
      idpmo = idpmo_entry.get ()
      name = namepmo.get ()
      model = model_entry.get ()
      serial = serial_entry.get ()
      color = colorpmo.get ()
      dp = departments.get ()
      user = user_entry.get ()
      stat = status.get ()
      dfa = datetime.now().strftime ('%d-%m-%Y')
      dtd = departuredate_entry.get ()
      obs = observation_entry.get ('1.0', 'end-1c')
      try:
        if not (idpmo and name and model and serial and color and dp and stat and dfa):
          messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida de la entidad')
        elif Resources.Connection.id_exist_pmo (idpmo):
          messagebox.showerror ('Error', 'El ID ya existe')
        else:
          Resources.Connection.insert_pmo (idpmo, name, model, serial, color, dp, user, stat, dfa, dtd, obs)
          messagebox.showinfo ('Éxito', 'La información fue registrada')
      except:
        messagebox.showerror ('Error', 'A ocurrido un error')

    #### Validates if they are only numbers and dashes
    def validate_numbers_entry (char):
      if char == '' or all (c.isdigit() or c == '-' for c in char):
        return True
      else:
        return False

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')
    font3 = ('Roboto', 16, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del mouse', text_color='#fff')
    title_label.place (x=25, y=5)

    ##### Objects within the frame
    ###### Front row
    idpmo_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpmo_label.place (x=50, y=60)

    idpmo_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idpmo_entry.place (x=50, y=90)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre de la marca:', text_color='#fff')
    name_label.place (x=280, y=60)

    namepmo = StringVar ()
    options = ['Vit', 'Logitech', 'Corsair', 'Genius', 'Argom', 'Lenovo', 'HP']

    name = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepmo, values=options, state='readonly')
    name.set ('Vit')
    name.place (x=280, y=90)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.place (x=485, y=60)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.place (x=485, y=90)

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.place (x=680, y=60)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.place (x=680, y=90)

    ###### Second row
    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.place (x=50, y=140)

    colorpmo = StringVar ()
    options = ['Negro', 'Plata', 'Gris', 'Blanco']

    color = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpmo, values=options, state='readonly')
    color.set ('Negro')
    color.place (x=50, y=170)

    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.place (x=280, y=140)

    departments = StringVar ()
    options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo']

    department_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Informática')
    department_options.place (x=280, y=170)

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.place (x=485, y=140)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=485, y=170)

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.place (x=680, y=140)

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=680, y=170)

    ###### Third row
    departuredate_label = CTkLabel (main_frame, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.place (x=50, y=220)

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
    departuredate_entry.place (x=50, y=250)

    ####### Displays a calendar to facilitate the selection of the date
    def calendar ():
        ######## Create a new window for the calendar
        window_callendary = tk.Toplevel (main_frame)
        window_callendary.title ('Calendario seleccionable')

        ######## Create a calendar widget
        calendar = Calendar (window_callendary, date_pattern='dd-mm-y', selectmode='day')
        calendar.pack (pady=20)

        ######## Function to show the selected date in the Entry of the main window
        def show_calendar_date ():
          date_selected = calendar.get_date ()
          departuredate_entry.configure (state='normal')
          departuredate_entry.delete (0, tk.END)
          departuredate_entry.insert (0, date_selected)
          departuredate_entry.configure (state='readonly')

        ######## button to show the selected date
        date_button = tk.Button (window_callendary, text='Mostrar fecha', command=show_calendar_date)
        date_button.pack (pady=10)

    calendar_button = CTkButton (main_frame, text='Abrir Calendario', command=calendar)
    calendar_button.place (x=54, y=300)

    def delete_date ():
      departuredate_entry.configure (state='normal')
      departuredate_entry.delete (0, tk.END)
      departuredate_entry.configure (state='readonly')

    date_delete_button = CTkButton (main_frame, text='Borrar Fecha', command=delete_date)
    date_delete_button.place (x=54, y=350)

    ####### Settings to avoid manually modifying the date
    departuredate_entry.configure (state='readonly')

    ###### Fourth row

    ###### Fifth row

    ###### Sixth row

    ###### Fifth and sixth row
    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.place (x=485, y=380)

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
    observation_entry.place (x=485, y=410)

    ###### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
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
      namepp.set ('HP')
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      colorpp.set ('Negro')
      typeprinting.set ('Tóner')
      departments.set ('Informática')
      user_entry.delete (0, END)
      status.set ('Operativo')
      departuredate_entry.delete (0, END)
      observation_entry.delete ('1.0', 'end-1c')

    ##### Entry that records the data in the database
    def submit_dt ():
      idpp = idpp_entry.get ()
      name = namepp.get ()
      model = model_entry.get ()
      serial = serial_entry.get ()
      color = colorpp.get ()
      tp = typeprinting.get ()
      dp = departments.get ()
      user = user_entry.get ()
      stat = status.get ()
      dfa = datetime.now().strftime ('%d-%m-%Y')
      dtd = departuredate_entry.get ()
      obs = observation_entry.get ('1.0', 'end-1c')
      try:
        if not (idpp and name and model and serial and color and tp and dp and stat and dfa):
          messagebox.showerror ('Error', 'Se deben llenar las celdas, y si es necesario la fecha de salida de la entidad')
        elif Resources.Connection.id_exist_pp (idpp):
          messagebox.showerror ('Error', 'El ID ya existe')
        else:
          Resources.Connection.insert_pp (idpp, name, model, serial, color, tp, dp, user, stat, dfa, dtd, obs)
          messagebox.showinfo ('Éxito', 'La información fue registrada')
      except:
        messagebox.showerror ('Error', 'A ocurrido un error')

    #### Validates if they are only numbers and dashes
    def validate_numbers_entry (char):
      if char == '' or all (c.isdigit() or c == '-' for c in char):
        return True
      else:
        return False

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')
    font3 = ('Roboto', 16, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos de la impresora', text_color='#fff')
    title_label.place (x=25, y=5)

    ##### Objects within the frame
    ###### Front row
    idpp_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpp_label.place (x=50, y=60)

    idpp_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idpp_entry.place (x=50, y=90)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre de la marca:', text_color='#fff')
    name_label.place (x=280, y=60)

    namepp = StringVar ()
    options = ['HP', 'Canon', 'Epson', 'Samsung', 'Brother', 'Lexmark', 'Xerox']

    name = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepp, values=options, state='readonly')
    name.set ('HP')
    name.place (x=280, y=90)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.place (x=485, y=60)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.place (x=485, y=90)

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.place (x=680, y=60)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.place (x=680, y=90)

    ###### Second row
    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.place (x=50, y=140)

    colorpp = StringVar ()
    options = ['Negro', 'Plata', 'Gris', 'Blanco']

    color = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpp, values=options, state='readonly')
    color.set ('Negro')
    color.place (x=50, y=170)

    type_label = CTkLabel (main_frame, font=font2, text='Tipo de impresión:', text_color='#fff')
    type_label.place (x=280, y=140)

    typeprinting = StringVar ()
    options = ['Tóner', 'Cartucho']

    type_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=typeprinting, values=options, state='readonly')
    type_options.set ('Tóner')
    type_options.place (x=280, y=170)

    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.place (x=485, y=140)

    departments = StringVar ()
    options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo']

    department_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Informática')
    department_options.place (x=485, y=170)

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.place (x=680, y=140)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=680, y=170)

    ###### Third row
    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.place (x=50, y=220)

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=50, y=250)

    ###### Fourth row
    departuredate_label = CTkLabel (main_frame, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.place (x=50, y=300)

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
    departuredate_entry.place (x=50, y=330)

    ####### Displays a calendar to facilitate the selection of the date
    def calendar ():
        ######## Create a new window for the calendar
        window_callendary = tk.Toplevel (main_frame)
        window_callendary.title ('Calendario seleccionable')

        ######## Create a calendar widget
        calendar = Calendar (window_callendary, date_pattern='dd-mm-y', selectmode='day')
        calendar.pack (pady=20)

        ######## Function to show the selected date in the Entry of the main window
        def show_calendar_date ():
          date_selected = calendar.get_date ()
          departuredate_entry.configure (state='normal')
          departuredate_entry.delete (0, tk.END)
          departuredate_entry.insert (0, date_selected)
          departuredate_entry.configure (state='readonly')

        ######## button to show the selected date
        date_button = tk.Button (window_callendary, text='Mostrar fecha', command=show_calendar_date)
        date_button.pack (pady=10)

    calendar_button = CTkButton (main_frame, text='Abrir Calendario', command=calendar)
    calendar_button.place (x=54, y=380)

    def delete_date ():
      departuredate_entry.configure (state='normal')
      departuredate_entry.delete (0, tk.END)
      departuredate_entry.configure (state='readonly')

    date_delete_button = CTkButton (main_frame, text='Borrar Fecha', command=delete_date)
    date_delete_button.place (x=54, y=430)

    ####### Settings to avoid manually modifying the date
    departuredate_entry.configure (state='readonly')

    ###### Fifth row

    ###### Sixth row

    ###### Fifth and sixth row
    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.place (x=485, y=380)

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
    observation_entry.place (x=485, y=410)

    ###### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
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

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')

    #### Format for the background of the output page
    CTkLabel (main_frame, text='Sistema de inventario', font=('Roboto', 22)).pack (pady=(80, 0))
    CTkLabel (main_frame, text='para', font=('Roboto', 22)).pack (pady=2)
    CTkLabel (main_frame, text='equipos informáticos', font=('Roboto', 21)).pack (pady=2)
    logo_image_central = CTkImage (Image.open('Resources\\Img\\LogoLogin.png'), size=(150, 150))
    logo_image_central_label = CTkLabel (main_frame, text='', image=logo_image_central, fg_color=None, bg_color='transparent')
    logo_image_central_label.place (x=380, y=280)

    #### Departure confirmation message
    if messagebox.askyesno ('Confirmación', '¿Está seguro que desea salir?'):
      mainmain.destroy ()
      mainmenu.deiconify ()

  ## Function to detect when I want to leave the window
  def closing ():
    switch_indication (exit_btn_indicator, menu_page)

  ## detector of whether I want to close the window
  mainmain.protocol("WM_DELETE_WINDOW", closing) 

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
  main_frame.configure (width=900, height=600)

  ## To display one of the pages
  pc_page ()

  mainmain.mainloop ()
