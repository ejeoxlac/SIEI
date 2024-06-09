# Libraries
import customtkinter
from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

## Model of the menu
menu_bar_colour = '#383838'

# Format of the window interface
app = customtkinter.CTk ()
app.title ('Datos de los ordenadores')
app.geometry ('1000x650')

# Icons
reg_icon = CTkImage (Image.open('Resources\\Img\\User.png'), size=(20, 20))
view_icon = CTkImage (Image.open('Resources\\Img\\Userdetail.png'), size=(20, 20))

# Functions to display the windows
## Window where the user's data can be registered
def reg_page ():

    ### Database manipulators
    #### Input re-initiator for data logging
    def new_bo():
        id_entry.delete (0, END)
        name_entry.delete (0, END)
        model_entry.delete (0, END)
        serial_entry.delete (0, END)
        color_entry.delete (0, END)
        colormb_entry.delete (0, END)

    #### Entry that records the data in the database
    def submit_bo ():
        id = id_entry.get ()
        name = name_entry.get ()
        model = model_entry.get ()
        serial = serial_entry.get ()
        color = color_entry.get ()
        colormb = colormb_entry.get ()
        try:
            if not (id and name and model and serial and color and colormb):
                messagebox.showerror ('Error', 'Se deben llenar las celdas')
            elif Resources.Connection.id_exist_users (id):
                messagebox.showerror ('Error', 'El ID ya existe')
            else:
                Resources.Connection.insert_users (id, name, model, serial, color, colormb)
                messagebox.showinfo ('Éxito', 'La información fue registrada')
        except:
            messagebox.showerror ('Error', 'A ocurrido un error')

    ### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')

    ### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos del usuario', text_color='#fff')
    title_label.place (x=25, y=0)

    #### Objects within the frame
    id_label = CTkLabel (main_frame, font=font2, text='ID:', text_color='#fff', bg_color='#292933')
    id_label.place (x=50, y=40)

    id_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
    id_entry.place (x=50, y=70)

    name_label = CTkLabel (main_frame, font=font2, text='Nombre:', text_color='#fff', bg_color='#292933')
    name_label.place (x=250, y=40)

    name_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
    name_entry.place (x=250, y=70)

    model_label = CTkLabel (main_frame, font=font2, text='Modelo:', text_color='#fff', bg_color='#292933')
    model_label.place (x=445, y=40)

    model_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
    model_entry.place (x=445, y=70)

    serial_label = CTkLabel (main_frame, font=font2, text='Serial:', text_color='#fff', bg_color='#292933')
    serial_label.place (x=50, y=100)

    serial_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
    serial_entry.place (x=50, y=130)

    color_label = CTkLabel (main_frame, font=font2, text='Color:', text_color='#fff', bg_color='#292933')
    color_label.place (x=250, y=100)

    color_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
    color_entry.place (x=250, y=130)

    colormb_label = CTkLabel (main_frame, font=font2, text='Color de la placa madre:', text_color='#fff', bg_color='#292933')
    colormb_label.place (x=445, y=100)

    colormb_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
    colormb_entry.place (x=445, y=130)
    #### End of the frame

    submit_button = CTkButton(main_frame, command=submit_bo, font=font2, text_color='#fff', text='Guardar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    submit_button.place (x=200, y=450)

    clear_button = CTkButton (main_frame, command=new_bo,font=font2, text_color='#fff', text='Registro nuevo', fg_color='#F45e02', hover_color='#CB4E01', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    clear_button.place (x=330, y=450)

## Window to register the data of new users
def view_page ():

    ### Search function within the database to get user data
    def find ():

        #### Clear treeview
        for item in trv.get_children ():
            trv.delete (item)
        Resources.Connection.search_users ()
        PC = Resources.Connection.cur.fetchall ()
        for row in PC:
            trv.insert ('', END, values=row)

    ### Table where the data will be displayed
    trv = ttk.Treeview(main_frame, height=22, show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))

    trv.column (1, stretch=NO, width=20)
    trv.column (2, stretch=NO, width=100)
    trv.column (3, stretch=NO, width=100)
    trv.column (4, stretch=NO, width=100)
    trv.column (5, stretch=NO, width=100)
    trv.column (6, stretch=NO, width=100)
    trv.column (7, stretch=NO, width=100)
    trv.column (8, stretch=NO, width=100)
    trv.column (9, stretch=NO, width=100)
    trv.column (10, stretch=NO, width=100)
    trv.column (11, stretch=NO, width=100)

    trv.heading (1, text='ID', anchor=tk.CENTER)
    trv.heading (2, text='Nombre', anchor=tk.CENTER)
    trv.heading (3, text='Modelo', anchor=tk.CENTER)
    trv.heading (4, text='Serial', anchor=tk.CENTER)
    trv.heading (5, text='Color', anchor=tk.CENTER)
    trv.heading (6, text='Color-MB', anchor=tk.CENTER)
    trv.heading (7, text='CPU', anchor=tk.CENTER)
    trv.heading (8, text='RAM', anchor=tk.CENTER)
    trv.heading (9, text='HDDvsSSD', anchor=tk.CENTER)
    trv.heading (10, text='Estado', anchor=tk.CENTER)
    trv.heading (11, text='Usuario', anchor=tk.CENTER)

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=tk.HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=5, y=462, width=779, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=782, y=5, width=20, height=477)

    trv.place (x=5, y=5, width=775, height=455)

    ### Function to display the data automatically after opening the window
    find ()

# Function to delete the window or close
def delete_pages ():
    for frame in main_frame.winfo_children ():
        frame.destroy ()

# Function to show which button and window is being selected
def hide_indicator ():

    reg_btn_indicator.config (bg=menu_bar_colour)
    view_btn_indicator.config (bg=menu_bar_colour)

# Function that shows the page and marks which is the button that is being used
def switch_indication (lb, page):

    hide_indicator ()
    lb.config (bg='white')
    delete_pages ()
    page ()

# Format of the menu
menu_bar_frame = tk.Frame (app, bg=menu_bar_colour)

## Menu buttons
## For the separation of the buttons you should always add 60 from where "Y" starts for example 130 + 60 = 190 + 60 = 250 and so on
reg_btn = CTkButton (menu_bar_frame, text='', image=reg_icon, width=10, height=10, command=lambda: switch_indication (reg_btn_indicator, reg_page))
reg_btn.place (x=9, y=130)

view_btn = CTkButton (menu_bar_frame, text='', image=view_icon, width=10, height=10, command=lambda: switch_indication (view_btn_indicator, view_page))
view_btn.place (x=9, y=190)

## Usage indicator for the button
reg_btn_indicator = tk.Label (menu_bar_frame, bg='white')
reg_btn_indicator.place (x=3, y=130, width=3, height=30)

view_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
view_btn_indicator.place (x=3, y=190, width=3, height=30)

## Form of the menu
menu_bar_frame.pack (side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
menu_bar_frame.pack_propagate (flag=False)
menu_bar_frame.configure (width=45)

## Area where the objects that are selected in the menu will be displayed
main_frame = CTkFrame (app)
main_frame.pack (side=tk.LEFT)
main_frame.pack_propagate (False)
main_frame.configure (width=800, height=500)

# Point to create the framework that works in the app
frame = tk.Frame(app)

app.mainloop ()
