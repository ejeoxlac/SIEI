# Libraries
from customtkinter import *
from tkinter import messagebox

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

# Format of the window interface
main = CTk ()
main.title ('Menu')
main.geometry ('500x500')

# Format of the frame that forms the main body of the window
frame = CTkFrame (main)
frame.pack (expand=True, fill='both', padx=20, pady=60)

# Title
CTkLabel (frame, text='Menu', font=('Roboto', 26)).pack (pady=20)

# Buttons for accessing the functions of the application
CTkButton (frame, text='Registro de equipos informáticos').pack (pady=20)

CTkButton (frame, text='Vista de registros guardados').pack (pady=20)

CTkButton (frame, text='Administrador de usuarios').pack (pady=20)

CTkButton (frame, text='Salir').pack (pady=20)

main.mainloop ()
