# Libraries
from customtkinter import *
from tkinter import messagebox, filedialog
import shutil
from PIL import Image
import webbrowser
import Main
import Dataview
import UsersSys

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection

# I define the view so I can call it
def menuview (mainlogin):

  ## Defined appearance
  set_appearance_mode ('dark')
  set_default_color_theme ('blue')

  ## Format of the window interface
  mainmenu = CTkToplevel ()
  mainmenu.iconbitmap ('Resources\\Img\\Ico.ico')
  mainmenu.title ('Menu')
  mainmenu.geometry ('600x500')
  mainmenu.resizable (False, False)

  ## Code to center the application window
  ### Refresh the window to make sure the size of it
  mainmenu.update_idletasks ()
  ### Get the screen size
  screen_width = mainmenu.winfo_screenwidth ()
  screen_height = mainmenu.winfo_screenheight ()
  ### Get the size of the window
  win_width = mainmenu.winfo_width ()
  win_height = mainmenu.winfo_height ()
  ### Calculate the centered position
  x = (screen_width // 2) - (win_width // 2)
  y = (screen_height // 2) - (win_height // 2)
  ### Set the new position
  mainmenu.geometry(f"+{x}+{y}")

  ## Format to create the background of the application
  bg_image = CTkImage (Image.open('Resources\\Img\\InventoryMenu.jpg'), size=(600, 500))
  bg_image_label = CTkLabel (mainmenu, text='', image=bg_image)
  bg_image_label.place (x=0, y=0)

  ## Images for menu icons
  image1 = CTkImage (Image.open('Resources\\Img\\Fileadd.png'), size=(30, 30))
  image2 = CTkImage (Image.open('Resources\\Img\\Filefind.png'), size=(30, 30))
  image3 = CTkImage (Image.open('Resources\\Img\\Userpin.png'), size=(30, 30))
  image4 = CTkImage (Image.open('Resources\\Img\\Exit.png'), size=(30, 30))
  image5 = CTkImage (Image.open('Resources\\Img\\DB.png'), size=(30, 30))
  image6 = CTkImage (Image.open('Resources\\Img\\About.png'), size=(30, 30))

  ## Functions to move between the system windows
  def m1 ():
    mainmenu.withdraw  ()
    Main.mainview (mainmenu)

  def m2 ():
    mainmenu.withdraw  ()
    Dataview.dataviewview (mainmenu)

  def m3 ():
    mainmenu.withdraw  ()
    UsersSys.userssysview (mainmenu)

  def m4 ():
    mainmenu.destroy ()
    mainlogin.deiconify ()

  ### Protocol that when you hit the 'X' in the window, it returns you to the login
  mainmenu.protocol('WM_DELETE_WINDOW', m4)

  ### Function to open the database options window
  def m5 ():
    #### Format of the window interface
    options_database = CTkToplevel ()
    options_database.title ('Opciones para la base de datos')
    options_database.geometry ('500x400')
    options_database.resizable (False, False)

    #### Code to center the application window
    ##### Refresh the window to make sure the size of it
    options_database.update_idletasks ()
    ##### Get the screen size
    screen_width = options_database.winfo_screenwidth ()
    screen_height = options_database.winfo_screenheight ()
    ##### Get the size of the window
    win_width = options_database.winfo_width ()
    win_height = options_database.winfo_height ()
    ##### Calculate the centered position
    x = (screen_width // 2) - (win_width // 2)
    y = (screen_height // 2) - (win_height // 2)
    ##### Set the new position
    options_database.geometry (f"+{x}+{y}")

    #### Function that when the secondary window will be opened, the main one is blocked until the secondary one is closed, this with the aim of not being able to interact with the main window
    options_database.grab_set ()

    #### Function to show how much the database weighs
    def show_size_DB ():
      ##### Original path of the database
      original_DB = 'Resources\\SIEIDB.db'

      ##### Get the file size
      if os.path.exists (original_DB):
        size = os.path.getsize (original_DB) # Size in bytes
        size_MB = size / (1024 * 1024) # Convert to megabytes
        return f'Tamaño de la base de datos es: {size_MB:.2f} MB'
      else:
        return 'Base de datos no encontrada.'

    #### Function for creating a backup of the database
    def create_backup ():
      try:
        ##### Original path of the database
        original_DB = 'Resources\\SIEIDB.db'

        ##### Opens a 'Save As' window to select the location where the backup will be saved
        copy_route = filedialog.asksaveasfilename (defaultextension='.db', filetypes=[('Base de Datos SQLite', '*.db'), ('Todos los archivos', '*.*')])
        if not copy_route: # If the user cancels, do nothing
          return

        ##### Make the backup
        shutil.copyfile (original_DB, copy_route)

        ##### Show the result and finish the process
        messagebox.showinfo ('Éxito', 'Copia de seguridad creada correctamente.')
      except Exception as e:
        messagebox.showerror ('Error', f'No se pudo crear la copia de seguridad: {e}')

    #### Function to restore a backup of the database
    def restore_backup ():
      try:
        ##### Opens an 'Open' window to select the location from where the backup will be taken for restoration
        copy_route = filedialog.askopenfilename (filetypes=[('Base de Datos SQLite', '*.db'), ('Todos los archivos', '*.*')])
        if not copy_route:  # If the user cancels, do nothing
          return

        ##### Path of the original database
        original_DB = 'Resources\\SIEIDB.db'

        ##### Perform the restoration
        shutil.copyfile(copy_route, original_DB)

        ##### Show the result and finish the process
        messagebox.showinfo ('Éxito', 'Copia de seguridad restaurada correctamente.')
      except Exception as e:
        messagebox.showerror ('Error', f'No se pudo restaurar la copia de seguridad: {e}')

    #### Buttons to create the database backup and restore a copy of the database
    backup_button = CTkButton (options_database, text='Crear copia de seguridad', command=create_backup)
    backup_button.pack (pady=10)

    backup_restore_button = CTkButton (options_database, text='Restaurar copia de seguridad', command=restore_backup)
    backup_restore_button.pack (pady=10)

    #### Show the total weight of the database
    size_db_label = CTkLabel (options_database, text=show_size_DB())
    size_db_label.pack (pady=10)

    #### Show the total records in the database
    total_records_label = CTkLabel (options_database, text=Resources.Connection.number_of_DB_records())
    total_records_label.pack (pady=10)

  ### Function to open the 'about us' window, in this it shows who participated in the creation of the application, the reason for the creation of the application and other things related to the application
  def m6 ():
    #### Format of the window interface
    about = CTkToplevel ()
    about.title ('Acerca de la aplicación')
    about.geometry ('500x400')
    about.resizable (False, False)

    #### Configuration so that the grid is centered
    for i in range (10):
      about.grid_rowconfigure (i, weight=1)
    about.grid_columnconfigure (0, weight=1)
    about.grid_columnconfigure (1, weight=1)

    #### Code to center the application window
    ##### Refresh the window to make sure the size of it
    about.update_idletasks ()
    ##### Get the screen size
    screen_width = about.winfo_screenwidth ()
    screen_height = about.winfo_screenheight ()
    ##### Get the size of the window
    win_width = about.winfo_width ()
    win_height = about.winfo_height ()
    ##### Calculate the centered position
    x = (screen_width // 2) - (win_width // 2)
    y = (screen_height // 2) - (win_height // 2)
    ##### Set the new position
    about.geometry(f"+{x}+{y}")

    #### Function that when the secondary window will be opened, the main one is blocked until the secondary one is closed, this with the aim of not being able to interact with the main window
    about.grab_set ()

    #### Function for social media links
    ##### User one
    def github_ejeoxlac ():
      webbrowser.open ('https://github.com/ejeoxlac')
    def instagram_ejeoxlac ():
      webbrowser.open ('https://www.instagram.com/ejeoxlac')

    ##### User two
    def github_codeonyx_dev ():
      webbrowser.open ('https://github.com/codeonyx-dev')

    ##### Images of the icons of the social networks
    github = CTkImage (Image.open('Resources\\Img\\Github.png'), size=(30, 30))
    Instagram = CTkImage (Image.open('Resources\\Img\\Instagram.png'), size=(30, 30))

    ##### Interface objects that show what the content of the window is
    ###### Part of the developers
    CTkLabel (about, text='Creado por:', font=('Roboto', 26)).grid (row=0, column=0, columnspan=2)

    ####### User one
    CTkLabel (about, text='Bill Anthony Niño Riera', font=('Roboto', 26)).grid (row=1, column=0, columnspan=2)

    ######## Social network
    CTkButton (about, text='', image=github, fg_color='transparent', width=10, command=github_ejeoxlac).grid (row=2, column=0, pady=2, ipady=4)
    CTkButton (about, text='', image=Instagram, fg_color='transparent', width=10, command=instagram_ejeoxlac).grid (row=2, column=1, pady=2, ipady=4)

    ###### Part of the testers
    CTkLabel (about, text='Tester ocasional:', font=('Roboto', 26)).grid (row=4, column=0, columnspan=2)

    ####### User one
    CTkLabel (about, text='Raimond caldera', font=('Roboto', 26)).grid (row=5, column=0, columnspan=2)

    ######## Social network
    CTkButton (about, text='', image=github, fg_color='transparent', width=10, command=github_codeonyx_dev).grid (row=6, column=0, pady=2, ipady=4)

    ####### User two
    CTkLabel (about, text='Juan Torrealba', font=('Roboto', 26)).grid (row=7, column=0, columnspan=2)

    ###### Part about the program information
    CTkLabel (about, text='Acerca de:', font=('Roboto', 26)).grid (row=8, column=0, columnspan=2)

    ###### Part of the total members
    CTkLabel (about, text='Integrantes:', font=('Roboto', 26)).grid (row=9, column=0, columnspan=2)

  ## Format of the frame that forms the main body of the window
  frame_button = CTkFrame (mainmenu)
  frame_button.pack (expand=True, fill='both', padx=140, pady=50)

  ### Title
  CTkLabel (frame_button, text='Menu', font=('Roboto', 26)).pack (pady=10)

  ### Buttons for accessing the functions of the application
  CTkButton (frame_button, text='Registro de equipos informáticos', image=image1, corner_radius=15, command=m1).pack (pady=15)

  CTkButton (frame_button, text='Vista de registros guardados', image=image2, corner_radius=15, command=m2).pack (pady=15)

  CTkButton (frame_button, text='Administrador de usuarios', image=image3, corner_radius=15, command=m3).pack (pady=15)

  CTkButton (frame_button, text='Salir', image=image4, corner_radius=15, command=m4).pack (pady=15)

  CTkButton (frame_button, text='Opciones para la base de datos', image=image5, corner_radius=15, command=m5).pack (pady=15)

  ## Button to open the application information window
  CTkButton (mainmenu, text='', image=image6, width=50, corner_radius=0, command=m6).place (x=550, y=462)

  mainmenu.mainloop ()
