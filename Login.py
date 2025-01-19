# Libraries
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
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
      ### This deletes the data entered when making a mistake
      name.delete (0, END)
      password.delete (0, END)

  ## Defined appearance
  set_appearance_mode ('dark')
  set_default_color_theme ('blue')

  ## Format of the window interface
  mainlogin = CTk ()
  mainlogin.iconbitmap ('Resources\\Img\\Ico.ico')
  mainlogin.title ('Inicio de sesión al sistema SIEI')
  mainlogin.geometry ('540x500')
  mainlogin.resizable (False, False)

  ## Code to center the application window
  ### Refresh the window to make sure the size of it
  mainlogin.update_idletasks ()
  ### Get the screen size
  screen_width = mainlogin.winfo_screenwidth ()
  screen_height = mainlogin.winfo_screenheight ()
  ### Get the size of the window
  win_width = mainlogin.winfo_width ()
  win_height = mainlogin.winfo_height ()
  ### Calculate the centered position
  x = (screen_width // 2) - (win_width // 2)
  y = (screen_height // 2) - (win_height // 2)
  ### Set the new position
  mainlogin.geometry(f"+{x}+{y}")

  ## The format of the frames that make up the main body of the window
  frame_right = CTkFrame (mainlogin)
  frame_right.pack (side=RIGHT, expand=False, fill='both', padx=(0, 0))

  frame_left = CTkCanvas (mainlogin, highlightthickness=0) 
  frame_left.pack (side=LEFT, expand=True, fill='both', padx=(0, 0))

  ## Backgraund image
  image_path = 'Resources\\Img\\Login_SIEI_img_background.png'
  image = Image.open (image_path)

  ### Automatically resizes the image to the size of the left frame to avoid problems if the screen is scaled to other percentages
  def resized_img (event):
    canvas_width = frame_left.winfo_width ()
    canvas_height = frame_left.winfo_height ()
    resized_image = image.resize ((canvas_width, canvas_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage (resized_image)
    frame_left.create_image (0, 0, image=photo, anchor='nw')
    frame_left.image = photo

  frame_left.bind ('<Configure>', resized_img)
  resized_img (None)

  ## Objects in the right window
  ### Title
  CTkLabel (frame_right, text='Iniciar sesión', font=('Roboto', 22)).pack (padx=(10, 0),pady=(140, 0))

  ### Data entry for the login
  name = CTkEntry (frame_right, placeholder_text='Usuario 👤', width=250, height=40)
  name.pack (padx=10, pady=(60, 0))

  password = CTkEntry (frame_right, placeholder_text='Contraseña 🔑', show='*', width=250, height=40)
  password.pack (padx=10, pady=10)

  ### login button
  #### Bind the Enter key to the login function
  password.bind('<Return>', lambda event: login())
  
  CTkButton (frame_right, text='Acceder', command=login, corner_radius=15).pack (pady=20)

  CTkLabel (frame_right, text='Versión - v4.0.0', font=('Roboto', 10)).pack (pady=30)

  mainlogin.mainloop ()
