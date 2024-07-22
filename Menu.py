# Libraries
from customtkinter import *
from PIL import Image
import Main
import Dataview
import UsersSys

# I define the view so I can call it
def menuview (mainlogin):

  ## Defined appearance
  set_appearance_mode ('dark')
  set_default_color_theme ('blue')

  ## Format of the window interface
  mainmenu = CTkToplevel ()
  mainmenu.iconbitmap ('Resources\\Img\\Ico.ico')
  mainmenu.title ('Menu')
  mainmenu.geometry ('500x400')
  mainmenu.resizable (False, False)

  ## Format to create the background of the application
  bg_image = CTkImage (Image.open('Resources\\Img\\Bggradient.jpg'), size=(500, 400))
  bg_image_label = CTkLabel (mainmenu, text='', image=bg_image)
  bg_image_label.place (x=0, y=0)

  ## Images for menu icons
  image1 = CTkImage (Image.open('Resources\\Img\\Fileadd.png'), size=(30, 30))
  image2 = CTkImage (Image.open('Resources\\Img\\Filefind.png'), size=(30, 30))
  image3 = CTkImage (Image.open('Resources\\Img\\Userpin.png'), size=(30, 30))
  image4 = CTkImage (Image.open('Resources\\Img\\Exit.png'), size=(30, 30))

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

  mainmenu.protocol('WM_DELETE_WINDOW', m4)

  ## Format of the frame that forms the main body of the window
  frame = CTkFrame (mainmenu)
  frame.pack (expand=True, fill=Y, padx=20, ipadx=50)

  ### Title
  CTkLabel (frame, text='Menu', font=('Roboto', 26)).pack (pady=10)

  ### Buttons for accessing the functions of the application
  CTkButton (frame, text='Registro de equipos informáticos', image=image1, corner_radius=15, command=m1).pack (pady=15)

  CTkButton (frame, text='Vista de registros guardados', image=image2, corner_radius=15, command=m2).pack (pady=15)

  CTkButton (frame, text='Administrador de usuarios', image=image3, corner_radius=15, command=m3).pack (pady=15)

  CTkButton (frame, text='Salir', image=image4, corner_radius=15, command=m4).pack (pady=15)

  mainmenu.mainloop ()
