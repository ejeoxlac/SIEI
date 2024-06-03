# Libraries
from customtkinter import *
from tkinter import messagebox
from PIL import Image

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

# Format of the window interface
main = CTk ()
main.title ('Menu')
main.geometry ('500x500')
main.resizable (False, False)

# Format to create the background of the application
bg_image = CTkImage (Image.open('Resources\\Img\\Bggradient.jpg'), size=(500, 500))
bg_image_label = CTkLabel (main, text='', image=bg_image)
bg_image_label.place (x=0, y=0)

# Format of the frame that forms the main body of the window
frame = CTkFrame (main)
frame.pack (expand=True, fill=Y, padx=20, ipadx=20)

# Images for menu icons
image1 = CTkImage (Image.open('Resources\\Img\\Fileadd.png'), size=(30, 30))
image2 = CTkImage (Image.open('Resources\\Img\\Filefind.png'), size=(30, 30))
image3 = CTkImage (Image.open('Resources\\Img\\Userpin.png'), size=(30, 30))
image4 = CTkImage (Image.open('Resources\\Img\\Exit.png'), size=(30, 30))

# Title
CTkLabel (frame, text='Menu', font=('Roboto', 26)).pack (pady=20)

# Buttons for accessing the functions of the application
CTkButton (frame, text='Registro de equipos informáticos', image=image1).pack (pady=20)

CTkButton (frame, text='Vista de registros guardados', image=image2).pack (pady=20)

CTkButton (frame, text='Administrador de usuarios', image=image3).pack (pady=20)

CTkButton (frame, text='Salir', image=image4).pack (pady=20)

main.mainloop ()
