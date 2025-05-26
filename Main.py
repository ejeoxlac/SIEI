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
  mainmain.after(250, lambda:  mainmain.iconbitmap('Resources\\Img\\Ico.ico'))
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


  ## Generator of help message for objects in which the cursor is needed to be positioned to know more about the object
  class CustomHovertip (Hovertip):
    def showcontents (main):
      label = tk.Label (main.tipwindow, text=f'''{main.text}''', justify=tk.LEFT, bg='#151515', fg='#ffffff', relief=tk.SOLID, borderwidth=1, font=('Roboto', 12))
      label.pack ()

  ## Format of the menu
  menu_bar_frame = tk.Frame (mainmain, bg=menu_bar_colour)

  ### Menu buttons
  exit_btn = CTkButton (menu_bar_frame, text='', image=exit_icon, width=10, height=10, command=lambda: switch_indication (exit_btn_indicator, menu_page))
  exit_btn.grid (row=0, column=0, padx=(5, 0), pady=(13.2, 0))
  CustomHovertip (exit_btn, text='Ir al menu', hover_delay=500)

  ### For the separation of the buttons you should always add 60 from where "Y" starts for example 130 + 60 = 190 + 60 = 250 and so on
  pc_btn = CTkButton (menu_bar_frame, text='', image=pc_icon, width=10, height=10, command=lambda: switch_indication (pc_btn_indicator, pc_page))
  pc_btn.grid (row=1, column=0, padx=(5, 0), pady=(60, 0))
  CustomHovertip (pc_btn, text='Registrar computadoras', hover_delay=500)

  pk_btn = CTkButton (menu_bar_frame, text='', image=pk_icon, width=10, height=10, command=lambda: switch_indication (pk_btn_indicator, pk_page))
  pk_btn.grid (row=2, column=0, padx=(5, 0), pady=(20, 0))
  CustomHovertip (pk_btn, text='Registrar teclados', hover_delay=500)

  pm_btn = CTkButton (menu_bar_frame, text='', image=pm_icon, width=10, height=10, command=lambda: switch_indication (pm_btn_indicator, pm_page))
  pm_btn.grid (row=3, column=0, padx=(6, 0), pady=(20, 0))
  CustomHovertip (pm_btn, text='Registrar monitores', hover_delay=500)

  pmo_btn = CTkButton (menu_bar_frame, text='', image=pmo_icon, width=10, height=10,  command=lambda: switch_indication (pmo_btn_indicator, pmo_page))
  pmo_btn.grid (row=4, column=0, padx=(6, 0), pady=(20, 0))
  CustomHovertip (pmo_btn, text='Registrar mouses', hover_delay=500)

  pp_btn = CTkButton (menu_bar_frame, text='', image=pp_icon, width=10, height=10,  command=lambda: switch_indication (pp_btn_indicator, pp_page))
  pp_btn.grid (row=5, column=0, padx=(6, 0), pady=(20, 0))
  CustomHovertip (pp_btn, text='Registrar impresoras', hover_delay=500)

  ### Usage indicator for the button
  exit_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
  exit_btn_indicator.grid(row=0, column=1, padx=(2, 0), pady=(15, 0), sticky='n')

  pc_btn_indicator = tk.Label (menu_bar_frame, bg='white', width=0, height=3)
  pc_btn_indicator.grid(row=1, column=1, padx=(2, 0), pady=(72, 0), sticky='n')

  pk_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
  pk_btn_indicator.grid(row=2, column=1, padx=(2, 0), pady=(23, 0), sticky='n')

  pm_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
  pm_btn_indicator.grid(row=3, column=1, padx=(2, 0), pady=(23, 0), sticky='n')

  pmo_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
  pmo_btn_indicator.grid(row=4, column=1, padx=(2, 0), pady=(23, 0), sticky='n')

  pp_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
  pp_btn_indicator.grid(row=5, column=1, padx=(2, 0), pady=(23, 0), sticky='n')

  ### Form of the menu
  menu_bar_frame.pack (side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
  menu_bar_frame.pack_propagate (flag=False)
  menu_bar_frame.configure (width=45)

  ### Area where the objects that are selected in the menu will be displayed
  main_frame = CTkFrame (mainmain)
  main_frame.pack (fill='both', side=tk.LEFT, padx=(0,20), pady=20)
  main_frame.pack_propagate (False)
  main_frame.configure (width=900, height=600)

  ## Functions to show the windows
  ### Computers data window
  def pc_page ():

    #### The window that is open is saved in the variable
    global current_page
    current_page = 'pc_page'

    #### Database manipulators
    ##### Input re-initiator for data logging
    def new_dt ():
      idpc_entry.delete (0, END)
      name.set ('Vit')
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      color.set ('Negro')
      modelmb_entry.delete (0, END)
      colormb.set ('Verde')
      graphicscardname.set ('NVIDIA')
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

    def validate_only_number_input (char):
      if char == '' or all (c.isdigit() for c in char):
        return True
      else:
        return False

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')
    font3 = ('Roboto', 16, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del computador', text_color='#fff')
    title_label.grid (row=0, column=0, columnspan=3, padx=(20, 0), pady=5, sticky='w')

    ##### Objects within the frame
    ###### Front row
    idpc_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpc_label.grid (row=1, column=0, padx=(40, 5), pady=(5, 5), sticky='w')

    idpc_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_only_number_input), '%S'))
    idpc_entry.grid (row=2, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    name_label = CTkLabel (main_frame, font=font2, text='Nombre de la marca:', text_color='#fff')
    name_label.grid (row=1, column=1, padx=5, pady=(5, 5), sticky='w')

    namepc = StringVar ()
    options = ['Vit', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Microsoft', 'Google', 'Apple']

    name = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepc, values=options, state='readonly')
    name.set ('Vit')
    name.grid (row=2, column=1, padx=5, pady=(0, 5), sticky='w')

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.grid (row=1, column=2, padx=5, pady=(5, 5), sticky='w')

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.grid (row=2, column=2, padx=5, pady=(0, 5), sticky='w')

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.grid (row=1, column=3, pady=(5, 5), sticky='w')

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.grid (row=2, column=3, pady=(0, 5), sticky='w')

    ###### Second row
    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.grid  (row=3, column=0, padx=(40, 5), pady=(5, 5), sticky='w')

    colorpc = StringVar ()
    options = ['Negro', 'Plata', 'Gris', 'Azul', 'Blanco']

    color = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpc, values=options, state='readonly')
    color.set ('Negro')
    color.grid (row=4, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    modelmb_label = CTkLabel (main_frame, font=font3, text='Modelo de la placa madre:', text_color='#fff')
    modelmb_label.grid (row=3, column=1, padx=5, pady=(5, 5), sticky='w')

    modelmb_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    modelmb_entry.grid (row=4, column=1, padx=5, pady=(0, 5), sticky='w')

    colormb_label = CTkLabel (main_frame, font=font3, text='Color de la placa madre:', text_color='#fff')
    colormb_label.grid (row=3, column=2, padx=5, pady=(5, 5), sticky='w')

    colormbpc = StringVar ()
    options = ['Verde', 'Negro', 'Azul', 'Rojo', 'Blanco']

    colormb = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colormbpc, values=options, state='readonly')
    colormb.set ('Verde')
    colormb.grid (row=4, column=2, padx=5, pady=(0, 5), sticky='w')

    graphicscardname_label = CTkLabel (main_frame, font=font3, text='Marca de la grafica:', text_color='#fff')
    graphicscardname_label.grid (row=3, column=3, pady=(5, 5), sticky='w')

    graphicscard = StringVar ()
    options = ['NVIDIA', 'AMD', 'Intel', 'ASUS', 'EVGA', 'MSI', 'Zotac']

    graphicscardname = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=graphicscard, values=options, state='readonly')
    graphicscardname.set ('NVIDIA')
    graphicscardname.grid (row=4, column=3, pady=(0, 5), sticky='w')

    ###### Third row
    graphicscardmodel_label = CTkLabel (main_frame, font=font3, text='Modelo de la grafica:', text_color='#fff')
    graphicscardmodel_label.grid (row=5, column=0, padx=(40, 5), pady=(5, 5), sticky='w')

    graphicscardmodel_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    graphicscardmodel_entry.grid (row=6, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    cpu_label = CTkLabel (main_frame, font=font2, text='CPU:', text_color='#fff')
    cpu_label.grid (row=5, column=1, padx=5, pady=(5, 5), sticky='w')

    cpu_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    cpu_entry.grid (row=6, column=1, padx=5, pady=(0, 5), sticky='w')

    ram_label = CTkLabel (main_frame, font=font2, text='RAM:', text_color='#fff')
    ram_label.grid (row=5, column=2, padx=5, pady=(5, 5), sticky='w')

    memory = StringVar ()
    options = ['1 GB DDR2', '2 GB DDR2', '4 GB DDR2', '8 GB DDR2', '16 GB DDR2', '32 GB DDR2', '1 GB DDR3', '2 GB DDR3', '4 GB DDR3', '8 GB DDR3', '16 GB DDR3', '32 GB DDR3']

    ram_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=memory, values=options, state='readonly')
    ram_options.set ('1 GB DDR2')
    ram_options.grid (row=6, column=2, padx=5, pady=(0, 5), sticky='w')

    HDDorSDD_label = CTkLabel (main_frame, font=font3, text='Unidad de almacenamiento:', text_color='#fff')
    HDDorSDD_label.grid (row=5, column=3, pady=(5, 5), sticky='w')

    HDDorSDD_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    HDDorSDD_entry.grid (row=6, column=3, pady=(0, 5), sticky='w')

    ###### Fourth row
    win_label = CTkLabel (main_frame, font=font2, text='Sistema operativo:', text_color='#fff')
    win_label.grid (row=7, column=0, padx=(40, 5), pady=(5, 5), sticky='w')

    so = StringVar ()
    options = ['Windows 11', 'Windows 10', 'Windows 8', 'Windows 7', 'Windows XP', 'GNU/Linux', 'iOS']

    win_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=so, values=options, state='readonly')
    win_options.set ('Windows 11')
    win_options.grid (row=8, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.grid (row=7, column=1, padx=5, pady=(5, 5), sticky='w')

    departments = StringVar ()
    options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo']

    department_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Informática')
    department_options.grid (row=8, column=1, padx=5, pady=(0, 5), sticky='w')

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.grid (row=7, column=2, padx=5, pady=(5, 5), sticky='w')

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.grid (row=8, column=2, padx=5, pady=(0, 5), sticky='w')

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.grid (row=7, column=3, pady=(5, 5), sticky='w')

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.grid (row=8, column=3, pady=(0, 5), sticky='w')

    ###### Fifth row
    departuredate_label = CTkLabel (main_frame, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.grid (row=9, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
    departuredate_entry.grid (row=10, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

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
    calendar_button.grid (row=11, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    def delete_date ():
      departuredate_entry.configure (state='normal')
      departuredate_entry.delete (0, tk.END)
      departuredate_entry.configure (state='readonly')

    date_delete_button = CTkButton (main_frame, text='Borrar Fecha', command=delete_date)
    date_delete_button.grid (row=12, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    ####### Settings to avoid manually modifying the date
    departuredate_entry.configure (state='readonly')

    ###### Sixth row

    ###### Fifth and sixth row
    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.grid (row=9, column=1, columnspan=3, padx=(15, 45), pady=(5, 5), sticky='e')

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
    observation_entry.grid (row=10, column=1, rowspan=3,  columnspan=3, padx=(15, 45), pady=(0, 5), sticky='e')

    ###### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.grid (row=13, column=0, columnspan=4, padx=(0, 200), pady=(10, 0))

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.grid (row=13, column=0, columnspan=4, padx=(200, 0), pady=(10, 0))
    ##### End of the frame

  ### Keyboards data window
  def pk_page ():

    #### The window that is open is saved in the variable
    global current_page
    current_page = 'pk_page'

    #### Database manipulators
    ##### Input re-initiator for data logging
    def new_dt ():
      idpk_entry.delete (0, END)
      name.set ('Vit')
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      color.set ('Negro')
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

    def validate_only_number_input (char):
      if char == '' or all (c.isdigit() for c in char):
        return True
      else:
        return False

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')
    font3 = ('Roboto', 16, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del teclado', text_color='#fff')
    title_label.grid (row=0, column=0, columnspan=3, padx=(20, 0), pady=5, sticky='w')

    ##### Objects within the frame
    ###### Front row
    idpk_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpk_label.grid (row=1, column=0, padx=(40, 5), pady=(5, 5), sticky='w')

    idpk_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_only_number_input), '%S'))
    idpk_entry.grid (row=2, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    name_label = CTkLabel (main_frame, font=font2, text='Nombre de la marca:', text_color='#fff')
    name_label.grid (row=1, column=1, padx=5, pady=(5, 5), sticky='w')

    namepk = StringVar ()
    options = ['Vit', 'Dell', 'Logitech', 'Corsair']

    name = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepk, values=options, state='readonly')
    name.set ('Vit')
    name.grid (row=2, column=1, padx=5, pady=(0, 5), sticky='w')

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.grid (row=1, column=2, padx=15, pady=(5, 5), sticky='w')


    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.grid (row=2, column=2, padx=15, pady=(0, 5), sticky='w')

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.grid (row=1, column=3, padx=(40, 5), pady=(5, 5), sticky='w')

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.grid (row=2, column=3,  padx=(40, 5), pady=(0, 5), sticky='w')

    ###### Second row
    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.grid  (row=3, column=0, padx=(40, 5), pady=(5, 5), sticky='w')

    colorpk = StringVar ()
    options = ['Negro', 'Plata', 'Gris', 'Blanco', 'Verde', 'Amarillo', 'Rojo']

    color = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpk, values=options, state='readonly')
    color.set ('Negro')
    color.grid (row=4, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.grid (row=3, column=1, padx=5, pady=(5, 5), sticky='w')

    departments = StringVar ()
    options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo']

    department_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Informática')
    department_options.grid (row=4, column=1, padx=5, pady=(0, 5), sticky='w')

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.grid (row=3, column=2, padx=15, pady=(5, 5), sticky='w')

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.grid (row=4, column=2, padx=15, pady=(0, 5), sticky='w')

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.grid (row=3, column=3, padx=(40, 5), pady=(5, 5), sticky='w')

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.grid (row=4, column=3, padx=(40, 5), pady=(0, 5), sticky='w')

    ###### Third row
    departuredate_label = CTkLabel (main_frame, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.grid (row=5, column=0, padx=(40, 5), pady=(5, 5), sticky='w')

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
    departuredate_entry.grid (row=6, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

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
    calendar_button.grid (row=7, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    def delete_date ():
      departuredate_entry.configure (state='normal')
      departuredate_entry.delete (0, tk.END)
      departuredate_entry.configure (state='readonly')

    date_delete_button = CTkButton (main_frame, text='Borrar Fecha', command=delete_date)
    date_delete_button.grid (row=8, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    ####### Settings to avoid manually modifying the date
    departuredate_entry.configure (state='readonly')

    ###### Fourth row

    ###### Fifth row

    ###### Sixth row

    ###### Fifth and sixth row
    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.grid (row=5, column=1, columnspan=3, padx=(40, 5), pady=(5, 5), sticky='e')

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
    observation_entry.grid (row=6, column=1, rowspan=3,  columnspan=3, padx=(40, 5), pady=(0, 5), sticky='e')

    ###### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.grid (row=9, column=0, columnspan=4, padx=(0, 200), pady=(70, 0))

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.grid (row=9, column=0, columnspan=4, padx=(200, 0), pady=(70, 0))
    ##### End of the frame

  ### Monitors data window
  def pm_page ():

    #### The window that is open is saved in the variable
    global current_page
    current_page = 'pp_page'

    #### Database manipulators
    ##### Input re-initiator for data logging
    def new_dt ():
      idpm_entry.delete (0, END)
      name.set ('Vit')
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      color.set ('Negro')
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

    def validate_only_number_input (char):
      if char == '' or all (c.isdigit() for c in char):
        return True
      else:
        return False

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')
    font3 = ('Roboto', 16, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del monitor', text_color='#fff')
    title_label.grid (row=0, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    ##### Objects within the frame
    ###### Front row
    idpm_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpm_label.grid (row=1, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

    idpm_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_only_number_input), '%S'))
    idpm_entry.grid (row=2, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    name_label = CTkLabel (main_frame, font=font2, text='Nombre de la marca:', text_color='#fff')
    name_label.grid (row=1, column=1, padx=20, pady=(10, 5), sticky='w')

    namepm = StringVar ()
    options = ['Vit', 'Dell', 'Samsung', 'Asus', 'LG', 'Acer', 'Dahua', 'BenQ', 'HP']

    name = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepm, values=options, state='readonly')
    name.set ('Vit')
    name.grid (row=2, column=1, padx=20, pady=(0, 10), sticky='w')

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.grid (row=1, column=2, padx=20, pady=(10, 5), sticky='w')

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.grid (row=2, column=2, padx=20, pady=(0, 10), sticky='w')

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.grid (row=1, column=3, padx=20, pady=(10, 5), sticky='w')

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.grid (row=2, column=3, padx=20, pady=(0, 10), sticky='w')

    ###### Second row
    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.grid  (row=3, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

    colorpm = StringVar ()
    options = ['Negro', 'Plata', 'Gris', 'Blanco']

    color = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpm, values=options, state='readonly')
    color.set ('Negro')
    color.grid (row=4, column=0, padx=(40, 20), pady=(5, 5), sticky='w')

    typescreen_label = CTkLabel (main_frame, font=font2, text='Tipo de pantalla:', text_color='#fff')
    typescreen_label.grid (row=3, column=1, padx=20, pady=(10, 5), sticky='w')

    typescreeninch = StringVar ()
    options = ['18 pulgadas', '19 pulgadas', '22 pulgadas', '24 pulgadas', '28 pulgadas', '32 pulgadas', '40 pulgadas', '42 pulgadas', '43 pulgadas', '48 pulgadas', '49 pulgadas', '50 pulgadas', '55 pulgadas', '60 pulgadas', '65 pulgadas', '70 pulgadas', '75 pulgadas', '77 pulgadas', '85 pulgadas']

    typescreen_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=typescreeninch, values=options, state='readonly')
    typescreen_options.set ('18 pulgadas')
    typescreen_options.grid (row=4, column=1, padx=20, pady=(5, 5), sticky='w')

    typeconnector_label = CTkLabel (main_frame, font=font2, text='Tipo de conector:', text_color='#fff')
    typeconnector_label.grid (row=3, column=2, padx=20, pady=(10, 5), sticky='w')

    typeconnectorport = StringVar ()
    options = ['VGA', 'HDMI', 'DisplayPort', 'DVI']

    typeconnector_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=typeconnectorport, values=options, state='readonly')
    typeconnector_options.set ('VGA')
    typeconnector_options.grid (row=4, column=2, padx=20, pady=(5, 5), sticky='w')

    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.grid (row=3, column=3, padx=20, pady=(10, 5), sticky='w')

    departments = StringVar ()
    options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo']

    department_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Informática')
    department_options.grid (row=4, column=3, padx=20, pady=(5, 5), sticky='w')

    ###### Third row
    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.grid (row=5, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.grid (row=6, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.grid (row=5, column=1, padx=20, pady=(10, 5), sticky='w')

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.grid (row=6, column=1, padx=20, pady=(5, 5), sticky='w')

    ###### Fourth row
    departuredate_label = CTkLabel (main_frame, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.grid (row=7, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
    departuredate_entry.grid (row=8, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

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
    calendar_button.grid (row=9, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    def delete_date ():
      departuredate_entry.configure (state='normal')
      departuredate_entry.delete (0, tk.END)
      departuredate_entry.configure (state='readonly')

    date_delete_button = CTkButton (main_frame, text='Borrar Fecha', command=delete_date)
    date_delete_button.grid (row=10, column=0, padx=(40, 5), pady=(0, 5), sticky='w')

    ####### Settings to avoid manually modifying the date
    departuredate_entry.configure (state='readonly')

    ###### Fifth row

    ###### Sixth row

    ###### Fifth and sixth row
    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.grid (row=7, column=1, columnspan=3, padx=(15, 45), pady=(5, 5), sticky='e')

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
    observation_entry.grid (row=8, column=1, rowspan=3,  columnspan=3, padx=(15, 45), pady=(0, 5), sticky='e')

    ###### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.grid (row=11, column=0, columnspan=4, padx=(0, 200), pady=(10, 0))

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.grid (row=11, column=0, columnspan=4, padx=(200, 0), pady=(10, 0))
    ##### End of the frame

  ### Mouses data window
  def pmo_page ():

    #### The window that is open is saved in the variable
    global current_page
    current_page = 'pmo_page'

    #### Database manipulators
    ##### Input re-initiator for data logging
    def new_dt ():
      idpmo_entry.delete (0, END)
      name.set ('Vit')
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      color.set ('Negro')
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

    def validate_only_number_input (char):
      if char == '' or all (c.isdigit() for c in char):
        return True
      else:
        return False

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')
    font3 = ('Roboto', 16, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del mouse', text_color='#fff')
    title_label.grid (row=0, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    ##### Objects within the frame
    ###### Front row
    idpmo_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpmo_label.grid (row=1, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

    idpmo_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_only_number_input), '%S'))
    idpmo_entry.grid (row=2, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    name_label = CTkLabel (main_frame, font=font2, text='Nombre de la marca:', text_color='#fff')
    name_label.grid (row=1, column=1, padx=20, pady=(10, 5), sticky='w')

    namepmo = StringVar ()
    options = ['Vit', 'Logitech', 'Corsair', 'Genius', 'Argom', 'Lenovo', 'HP']

    name = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepmo, values=options, state='readonly')
    name.set ('Vit')
    name.grid (row=2, column=1, padx=20, pady=(0, 10), sticky='w')

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.grid (row=1, column=2, padx=20, pady=(10, 5), sticky='w')

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.grid (row=2, column=2, padx=20, pady=(0, 10), sticky='w')

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.grid (row=1, column=3, padx=20, pady=(10, 5), sticky='w')

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.grid (row=2, column=3, padx=20, pady=(0, 10), sticky='w')

    ###### Second row
    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.grid  (row=3, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

    colorpmo = StringVar ()
    options = ['Negro', 'Plata', 'Gris', 'Blanco']

    color = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpmo, values=options, state='readonly')
    color.set ('Negro')
    color.grid (row=4, column=0, padx=(40, 20), pady=(5, 5), sticky='w')

    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.grid (row=3, column=1, padx=20, pady=(10, 5), sticky='w')

    departments = StringVar ()
    options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo']

    department_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Informática')
    department_options.grid (row=4, column=1, padx=20, pady=(5, 5), sticky='w')

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.grid (row=3, column=2, padx=20, pady=(10, 5), sticky='w')

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.grid (row=4, column=2, padx=20, pady=(5, 5), sticky='w')

    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.grid (row=3, column=3, padx=20, pady=(10, 5), sticky='w')

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.grid (row=4, column=3, padx=20, pady=(5, 5), sticky='w')

    ###### Third row
    departuredate_label = CTkLabel (main_frame, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.grid (row=5, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
    departuredate_entry.grid (row=6, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    ####### Displays a calendar to facilitate the selection of the date
    def calendar ():
        ######## Create a new window for the calendar
        window_callendary = tk.Toplevel (main_frame)
        window_callendary.after(250, lambda:  window_callendary.iconbitmap('Resources\\Img\\Ico.ico'))
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
    calendar_button.grid (row=7, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    def delete_date ():
      departuredate_entry.configure (state='normal')
      departuredate_entry.delete (0, tk.END)
      departuredate_entry.configure (state='readonly')

    date_delete_button = CTkButton (main_frame, text='Borrar Fecha', command=delete_date)
    date_delete_button.grid (row=8, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    ####### Settings to avoid manually modifying the date
    departuredate_entry.configure (state='readonly')

    ###### Fourth row

    ###### Fifth row

    ###### Sixth row

    ###### Fifth and sixth row
    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.grid (row=5, column=1, columnspan=3, padx=(40, 20), pady=(10, 5), sticky='e')

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
    observation_entry.grid (row=6, column=1, rowspan=3, columnspan=3, padx=(40, 20), pady=(10, 5), sticky='e')

    ###### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.grid (row=9, column=0, columnspan=4, padx=(0, 200), pady=(70, 0))

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.grid (row=9, column=0, columnspan=4, padx=(200, 0), pady=(70, 0))
    ##### End of the frame

  ### Printers data window
  def pp_page ():

    #### The window that is open is saved in the variable
    global current_page
    current_page = 'pp_page'

    #### Database manipulators
    ##### Input re-initiator for data logging
    def new_dt ():
      idpp_entry.delete (0, END)
      name.set ('HP')
      model_entry.delete (0, END)
      serial_entry.delete (0, END)
      color.set ('Negro')
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

    def validate_only_number_input (char):
      if char == '' or all (c.isdigit() for c in char):
        return True
      else:
        return False

    #### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')
    font3 = ('Roboto', 16, 'bold')

    #### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos de la impresora', text_color='#fff')
    title_label.grid (row=0, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    ##### Objects within the frame
    ###### Front row
    idpp_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff')
    idpp_label.grid (row=1, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

    idpp_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_only_number_input), '%S'))
    idpp_entry.grid (row=2, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    name_label = CTkLabel (main_frame, font=font2, text='Nombre de la marca:', text_color='#fff')
    name_label.grid (row=1, column=1, padx=20, pady=(10, 5), sticky='w')

    namepp = StringVar ()
    options = ['HP', 'Canon', 'Epson', 'Samsung', 'Brother', 'Lexmark', 'Xerox']

    name = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepp, values=options, state='readonly')
    name.set ('HP')
    name.grid (row=2, column=1, padx=20, pady=(0, 10), sticky='w')

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff')
    model_label.grid (row=1, column=2, padx=20, pady=(10, 5), sticky='w')

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    model_entry.grid (row=2, column=2, padx=20, pady=(0, 10), sticky='w')

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff')
    serial_label.grid (row=1, column=3, padx=20, pady=(10, 5), sticky='w')

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    serial_entry.grid (row=2, column=3, padx=20, pady=(0, 10), sticky='w')

    ###### Second row
    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff')
    color_label.grid  (row=3, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

    colorpp = StringVar ()
    options = ['Negro', 'Plata', 'Gris', 'Blanco']

    color = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpp, values=options, state='readonly')
    color.set ('Negro')
    color.grid (row=4, column=0, padx=(40, 20), pady=(5, 5), sticky='w')

    type_label = CTkLabel (main_frame, font=font2, text='Tipo de impresión:', text_color='#fff')
    type_label.grid (row=3, column=1, padx=20, pady=(10, 5), sticky='w')

    typeprinting = StringVar ()
    options = ['Tóner', 'Cartucho']

    type_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=typeprinting, values=options, state='readonly')
    type_options.set ('Tóner')
    type_options.grid (row=4, column=1, padx=20, pady=(5, 5), sticky='w')

    department_label = CTkLabel (main_frame, font=font2, text='Departamento:', text_color='#fff')
    department_label.grid (row=3, column=2, padx=20, pady=(10, 5), sticky='w')

    departments = StringVar ()
    options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo']

    department_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Informática')
    department_options.grid (row=4, column=2, padx=20, pady=(5, 5), sticky='w')

    user_label = CTkLabel (main_frame, font=font2, text='Usuario:', text_color='#fff')
    user_label.grid (row=3, column=3, padx=20, pady=(10, 5), sticky='w')

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.grid (row=4, column=3, padx=20, pady=(5, 5), sticky='w')

    ###### Third row
    stat_label = CTkLabel (main_frame, font=font2, text='Estado:', text_color='#fff')
    stat_label.grid (row=5, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (main_frame, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.grid (row=6, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    ###### Fourth row
    departuredate_label = CTkLabel (main_frame, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
    departuredate_label.grid (row=7, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

    departuredate_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
    departuredate_entry.grid (row=8, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    ####### Displays a calendar to facilitate the selection of the date
    def calendar ():
        ######## Create a new window for the calendar
        window_callendary = tk.Toplevel (main_frame)
        window_callendary.after(250, lambda:  window_callendary.iconbitmap('Resources\\Img\\Ico.ico'))
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
    calendar_button.grid (row=9, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    def delete_date ():
      departuredate_entry.configure (state='normal')
      departuredate_entry.delete (0, tk.END)
      departuredate_entry.configure (state='readonly')

    date_delete_button = CTkButton (main_frame, text='Borrar Fecha', command=delete_date)
    date_delete_button.grid (row=10, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

    ####### Settings to avoid manually modifying the date
    departuredate_entry.configure (state='readonly')

    ###### Fifth row

    ###### Sixth row

    ###### Fifth and sixth row
    observation_label = CTkLabel (main_frame, font=font2, text='Observación:', text_color='#fff')
    observation_label.grid (row=7, column=1, columnspan=3, padx=(40, 20), pady=(10, 5), sticky='e')

    observation_entry = CTkTextbox (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
    observation_entry.grid (row=8, column=1, rowspan=3,  columnspan=3, padx=(40, 20), pady=(0, 10), sticky='e')

    ###### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.grid (row=11, column=0, columnspan=4, padx=(0, 200), pady=(30, 0))

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.grid (row=11, column=0, columnspan=4, padx=(200, 0), pady=(30, 0))
    ##### End of the frame

  ### Function to delete the window or close
  def delete_pages ():
    
    for frame in main_frame.winfo_children ():
      frame.destroy ()

  ### Function to return to the menu window
  def menu_page ():

    #### Calls the variable to find out what its previous state was
    global current_page

    #### Fonts for the letters
    font1 = ('Roboto', 22, 'bold')

    #### Format for the background of the output page
    CTkLabel (main_frame, text='Sistema de inventario', font=font1).pack (pady=(80, 0))
    CTkLabel (main_frame, text='para', font=font1).pack (pady=2)
    CTkLabel (main_frame, text='equipos informáticos', font=font1).pack (pady=2)
    logo_image_central = CTkImage (Image.open('Resources\\Img\\Logo_SIEI_icon.png'), size=(150, 150))
    logo_image_central_label = CTkLabel (main_frame, text='', image=logo_image_central, fg_color=None, bg_color='transparent')
    logo_image_central_label.pack (pady=20)

    #### Exit confirmation message, also if the exit is rejected it will return to the window that was open
    if messagebox.askyesno ('Confirmación', '¿Está seguro que desea salir?'):
      mainmain.destroy ()
      mainmenu.deiconify ()
    else:
      if current_page == 'pc_page':
        delete_pages ()
        pc_page ()
        pc_btn_indicator.config (bg='white')
        exit_btn_indicator.config (bg=menu_bar_colour)
      elif current_page == 'pk_page':
        delete_pages ()
        pk_page ()
        pk_btn_indicator.config (bg='white')
        exit_btn_indicator.config (bg=menu_bar_colour)
      elif current_page == 'pm_page':
        delete_pages ()
        pm_page ()
        pm_btn_indicator.config (bg='white')
        exit_btn_indicator.config (bg=menu_bar_colour)
      elif current_page == 'pmo_page':
        delete_pages ()
        pmo_page ()
        pmo_btn_indicator.config (bg='white')
        exit_btn_indicator.config (bg=menu_bar_colour)
      elif current_page == 'pp_page':
        delete_pages ()
        pp_page ()
        pp_btn_indicator.config (bg='white')
        exit_btn_indicator.config (bg=menu_bar_colour)

  ## Function to detect when I want to leave the window
  def closing ():
      switch_indication (exit_btn_indicator, menu_page)

  ## Detector of whether I want to close the window
  mainmain.protocol ("WM_DELETE_WINDOW", closing) 

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

  ## To display one of the pages
  pc_page ()

  mainmain.mainloop ()
