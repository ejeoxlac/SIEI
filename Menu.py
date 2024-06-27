# Libraries
from customtkinter import *
from PIL import Image
import subprocess

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

# Format of the window interface
main = CTk ()
main.iconbitmap ('Resources\\Img\\Ico.ico')
main.title ('Menu')
main.geometry ('500x400')
main.resizable (False, False)

# Format to create the background of the application
bg_image = CTkImage (Image.open('Resources\\Img\\Bggradient.jpg'), size=(500, 400))
bg_image_label = CTkLabel (main, text='', image=bg_image)
bg_image_label.place (x=0, y=0)

# Format of the frame that forms the main body of the window
frame = CTkFrame (main)
frame.pack (expand=True, fill=Y, padx=20, ipadx=50)

# Images for menu icons
image1 = CTkImage (Image.open('Resources\\Img\\Fileadd.png'), size=(30, 30))
image2 = CTkImage (Image.open('Resources\\Img\\Filefind.png'), size=(30, 30))
image3 = CTkImage (Image.open('Resources\\Img\\Userpin.png'), size=(30, 30))
image4 = CTkImage (Image.open('Resources\\Img\\Exit.png'), size=(30, 30))

# Functions to move between the system windows
def m1 ():
  main.destroy ()
  subprocess.run (['python', 'Main.py'])

def m2 ():
  main.destroy ()
  subprocess.run (['python', 'Dataview.py'])
  
def m3 ():
  main.destroy ()
  subprocess.run (['python', 'UsersSys.py'])

def m4 ():
  main.destroy ()
  subprocess.run (['python', 'Login.py'])

# Title
CTkLabel (frame, text='Menu', font=('Roboto', 26)).pack (pady=10)

# Buttons for accessing the functions of the application
CTkButton (frame, text='Registro de equipos informáticos', image=image1, corner_radius=15, command=m1).pack (pady=15)

# Window that could possibly be created
# CTkButton (frame, text='Asignación de los equipos', image=image1, corner_radius=15).pack (pady=15)

CTkButton (frame, text='Vista de registros guardados', image=image2, corner_radius=15, command=m2).pack (pady=15)

CTkButton (frame, text='Administrador de usuarios', image=image3, corner_radius=15, command=m3).pack (pady=15)

CTkButton (frame, text='Salir', image=image4, corner_radius=15, command=m4).pack (pady=15)

main.mainloop ()
