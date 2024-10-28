# Libraries
from customtkinter import *
from tkinter import messagebox
from PIL import Image
import Menu

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection

# I define the view so I can call it
def loginview ():

  ## User validator to enter the system
  def login():
    user = name.get ()
    psw = password.get ()
    Resources.Connection.loginv (user, psw)
    if Resources.Connection.cur.fetchall ():
      messagebox.showinfo ('Login', 'Acceso permitido')
      mainlogin.withdraw ()
      Menu.menuview (mainlogin)
    elif not (user and psw):
      messagebox.showerror ('Error', 'Debes llenar las celdas')
    else:
      messagebox.showerror ('Error','Acceso denegado')

  ## Defined appearance
  set_appearance_mode ('dark')
  set_default_color_theme ('blue')

  ## Format of the window interface
  mainlogin = CTk ()
  mainlogin.iconbitmap ('Resources\\Img\\Ico.ico')
  mainlogin.title ('Inicio de sesión al sistema SIEI')
  mainlogin.geometry ('500x400')
  mainlogin.resizable (False, False)

  ## Format to create the background of the application
  bg_image = CTkImage (Image.open('Resources\\Img\\Bggradient.jpg'), size=(500, 400))
  bg_image_label = CTkLabel (mainlogin, text='', image=bg_image)
  bg_image_label.place (x=0, y=0)

  ## Format of the frame that forms the main body of the window
  frame = CTkFrame (mainlogin)
  frame.pack (side=RIGHT, expand=True, fill='both', padx=(150, 0), pady=30)

  # ## Logos
  # logo_image1 = CTkImage (Image.open('Resources\\Img\\Logo.png'), size=(60, 60))
  # logo_image1_label = CTkLabel (frame, text='', image=logo_image1, fg_color=None, bg_color='transparent')
  # logo_image1_label.place (x=50, y=5)

  logo_image_central = CTkImage (Image.open('Resources\\Img\\LogoLogin.png'), size=(60, 60))
  logo_image_central_label = CTkLabel (frame, text='', image=logo_image_central, fg_color=None, bg_color='transparent')
  logo_image_central_label.place (x=145, y=5)

  # logo_image2 = CTkImage (Image.open('Resources\\Img\\Logo.png'), size=(60, 60))
  # logo_image2_label = CTkLabel (frame, text='', image=logo_image2, fg_color=None, bg_color='transparent')
  # logo_image2_label.place (x=212, y=5)

  login_image3 = CTkImage (Image.open('Resources\\Img\\Inventario.jpg'), size=(150, 340))
  login_image3_label = CTkLabel (mainlogin, text='', image=login_image3)
  login_image3_label.place (x=0, y=30)

  ### Title
  CTkLabel (frame, text='Sistema de inventario', font=('Roboto', 22)).pack (pady=(80, 0))
  CTkLabel (frame, text='para', font=('Roboto', 22)).pack (pady=2)
  CTkLabel (frame, text='equipos informáticos', font=('Roboto', 21)).pack (pady=2)

  ### Data entry for the login
  name = CTkEntry (frame, placeholder_text='Usuario 👤', show='*', width=250, height=40)
  name.pack (pady=5)

  password = CTkEntry (frame, placeholder_text='Contraseña 🔑', show='*', width=250, height=40)
  password.pack (pady=10)

  ### login button
  CTkButton (frame, text='Acceder', command=login, corner_radius=15).pack (pady=5)

  mainlogin.mainloop ()
