# Libraries
import customtkinter
from customtkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
from PIL import Image

# Communication with SQLite3 to get the data from the database
import Resources.Connection

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

## Model of the menu
menu_bar_colour = '#383838'

# Format of the window interface
main = customtkinter.CTk ()
main.iconbitmap ('Resources\\Img\\Ico.ico')
main.title ('Datos de los usuarios')
main.geometry ('860x580')
main.resizable (False, False)

# Icons
exit_icon = CTkImage (Image.open('Resources\\Img\\ExitWhite.png'), size=(20, 20))
reg_icon = CTkImage (Image.open('Resources\\Img\\User.png'), size=(20, 20))
view_icon = CTkImage (Image.open('Resources\\Img\\Userdetail.png'), size=(20, 20))

# Functions to display the windows
## Window where the user's data can be registered
def reg_page ():

    ### Database manipulators
    #### Input re-initiator for data logging
    def new_dt ():
        idus_entry.delete (0, END)
        user_entry.delete (0, END)
        psw_entry.delete (0, END)
        firstnameperson_entry.delete (0, END)
        lastnameperson_entry.delete (0, END)
        idcardperson_entry.delete (0, END)

    #### Entry that records the data in the database
    def submit_dt ():
        idus = idus_entry.get ()
        user = user_entry.get ()
        psw = psw_entry.get ()
        firstnameperson = firstnameperson_entry.get ()
        lastnameperson = lastnameperson_entry.get ()
        idcardperson = idcardperson_entry.get ()
        try:
            if not (idus and user and psw and firstnameperson and lastnameperson and idcardperson):
                messagebox.showerror ('Error', 'Se deben llenar las celdas')
            elif Resources.Connection.id_exist_users (idus):
                messagebox.showerror ('Error', 'El ID ya existe')
            else:
                Resources.Connection.insert_users (idus, user, psw, firstnameperson, lastnameperson, idcardperson)
                messagebox.showinfo ('Éxito', 'La información fue registrada')
        except:
            messagebox.showerror ('Error', 'A ocurrido un error')

    ### Fonts for the letters
    font1 = ('Roboto', 30, 'bold')
    font2 = ('Roboto', 18, 'bold')

    ### User interface objects
    title_label = CTkLabel (main_frame, font=font1, text='Datos de registro del usuario', text_color='#fff')
    title_label.place (x=25, y=0)

    #### Objects to register the users that is inside the frame
    ##### Front row
    idus_label = CTkLabel (main_frame, font=font2, text='ID del usuario:', text_color='#fff')
    idus_label.place (x=50, y=60)

    idus_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idus_entry.place (x=50, y=90)

    user_label = CTkLabel (main_frame, font=font2, text='Nombre de usuario:', text_color='#fff')
    user_label.place (x=280, y=60)

    user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    user_entry.place (x=280, y=90)

    psw_label = CTkLabel (main_frame, font=font2, text='Contraseña del usuario:', text_color='#fff')
    psw_label.place (x=520, y=60)

    psw_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    psw_entry.place (x=520, y=90)

    ##### Second row
    firstnameperson_label = CTkLabel (main_frame, font=font2, text='Nombre real del usuario:', text_color='#fff')
    firstnameperson_label.place (x=50, y=140)

    firstnameperson_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    firstnameperson_entry.place (x=50, y=170)

    lastnameperson_label = CTkLabel (main_frame, font=font2, text='Apellido del usuario:', text_color='#fff')
    lastnameperson_label.place (x=280, y=140)

    lastnameperson_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    lastnameperson_entry.place (x=280, y=170)

    idcardperson_label = CTkLabel (main_frame, font=font2, text='Cedula de identidad del usuario:', text_color='#fff')
    idcardperson_label.place (x=520, y=140)

    idcardperson_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
    idcardperson_entry.place (x=520, y=170)

    ##### Button area
    submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
    submit_button.place (x=240, y=450)

    clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
    clear_button.place (x=420, y=450)
    #### The end of the frame objects

## Window where users' data can be viewed
def view_page ():

    ### Search function within the database to get user data
    def find ():

        #### Clear treeview
        for item in trv.get_children ():
            trv.delete (item)
        Resources.Connection.search_users ()
        users = Resources.Connection.cur.fetchall ()
        for row in users:
            trv.insert (parent='', index='end', iid=row[0], text='', values=row)

    ### Fonts for the letters
    font1 = ('Roboto', 18, 'bold')

    ### Table where the data will be displayed
    trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6))

    trv.column (1, stretch=NO, minwidth=20,width=20)
    trv.column (2, stretch=NO, minwidth=100,width=100)
    trv.column (3, stretch=NO, minwidth=100,width=100)
    trv.column (4, stretch=NO, minwidth=150,width=150)
    trv.column (5, stretch=NO, minwidth=150,width=150)
    trv.column (6, stretch=NO, minwidth=200,width=200)

    trv.heading (1, text='ID', anchor=CENTER)
    trv.heading (2, text='Usuario', anchor=CENTER)
    trv.heading (3, text='Contraseña', anchor=CENTER)
    trv.heading (4, text='Nombre real del usuario', anchor=CENTER)
    trv.heading (5, text='Apellido del usuario', anchor=CENTER)
    trv.heading (6, text='Cedula de identidad del usuario', anchor=CENTER)

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=5, y=405, width=778, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=782, y=5, width=20, height=420)

    trv.place (x=5, y=5, width=777, height=400)

    ### Function to delete users
    def button_del ():

        selected = trv.selection ()
        if selected:
            rowid = selected [0]
            Resources.Connection.del_user (rowid)
            trv.delete (rowid)
        else:
            messagebox.showerror ('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

    ### Function to edit users
    def button_dem ():

        #### Format of the window interface
        data_editing_menu = customtkinter.CTkToplevel ()
        data_editing_menu.title ('Menu de edición de datos')
        data_editing_menu.geometry ('800x500')
        data_editing_menu.resizable (False, False)

        #### Fonts for the letters
        font1 = ('Roboto', 30, 'bold')
        font2 = ('Roboto', 18, 'bold')

        #### User interface objects
        title_label = CTkLabel (data_editing_menu, font=font1, text='Datos del usuario', text_color='#fff')
        title_label.place (x=25, y=0)

        ##### Objects to register the users that is inside the frame
        ###### Front row
        idus_label = CTkLabel (data_editing_menu, font=font2, text='ID del usuario:', text_color='#fff')
        idus_label.place (x=50, y=60)

        idus_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        idus_entry.place (x=50, y=90)

        user_label = CTkLabel (data_editing_menu, font=font2, text='Nombre de usuario:', text_color='#fff')
        user_label.place (x=280, y=60)

        user_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        user_entry.place (x=280, y=90)

        psw_label = CTkLabel (data_editing_menu, font=font2, text='Contraseña del usuario:', text_color='#fff')
        psw_label.place (x=520, y=60)

        psw_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        psw_entry.place (x=520, y=90)

        ###### Second row
        firstnameperson_label = CTkLabel (data_editing_menu, font=font2, text='Nombre real del usuario:', text_color='#fff')
        firstnameperson_label.place (x=50, y=140)

        firstnameperson_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        firstnameperson_entry.place (x=50, y=170)

        lastnameperson_label = CTkLabel (data_editing_menu, font=font2, text='Apellido del usuario:', text_color='#fff')
        lastnameperson_label.place (x=280, y=140)

        lastnameperson_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        lastnameperson_entry.place (x=280, y=170)

        idcardperson_label = CTkLabel (data_editing_menu, font=font2, text='Cedula de identidad del usuario:', text_color='#fff')
        idcardperson_label.place (x=520, y=140)

        idcardperson_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        idcardperson_entry.place (x=520, y=170)
        ##### The end of the frame objects

        #### Data verification input
        def check_input ():
            selected = trv.focus ()
            rowid = selected [0]
            idus = idus_entry.get ()
            user = user_entry.get ()
            psw = psw_entry.get ()
            firstnameperson = firstnameperson_entry.get ()
            lastnameperson = lastnameperson_entry.get ()
            idcardperson = idcardperson_entry.get ()
            if not (idus and user and psw and firstnameperson and lastnameperson and idcardperson):
                messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
            else:
                Resources.Connection.edit_user (rowid, idus, user, psw, firstnameperson, lastnameperson, idcardperson)
                for item in trv.get_children ():
                    trv.delete (item)
                Resources.Connection.search_users ()
                users = Resources.Connection.cur.fetchall ()
                for row in users:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row)
                data_editing_menu.destroy ()
                messagebox.showinfo ('Elemento editado correctamente', 'El usuario fue editado correctamente')

        #### Button area
        button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
        button_dem.place (x=300, y=450)

        #### Returns selected item for editing
        try:
            selected = trv.focus ()
            values = trv.item (selected, 'values')
            idus_entry.insert (0, values[0])
            user_entry.insert (0, values[1])
            psw_entry.insert (0, values[2])
            firstnameperson_entry.insert (0, values[3])
            lastnameperson_entry.insert (0, values[4])
            idcardperson_entry.insert (0, values[5])
        except IndexError:
            data_editing_menu.destroy ()
            messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

    ### Button area
    button_del = CTkButton (main_frame, font=font1, text='Borrar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
    button_del.place (x=240, y=450)
    
    button_edi = CTkButton (main_frame, font=font1, text='Editar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
    button_edi.place (x=420, y=450)

    ### Function to display the data automatically after opening the window
    find ()

# Function to delete the window or close
def delete_pages ():
    
    for frame in main_frame.winfo_children ():
        frame.destroy ()

# Function to show which button and window is being selected
def hide_indicator ():

    exit_btn_indicator.config (bg=menu_bar_colour)
    reg_btn_indicator.config (bg=menu_bar_colour)
    view_btn_indicator.config (bg=menu_bar_colour)

# Function that shows the page and marks which is the button that is being used
def switch_indication (lb, page):

    hide_indicator ()
    lb.config (bg='white')
    delete_pages ()
    page ()

# Generator of help message for objects in which the cursor is needed to be positioned to know more about the object
class CustomHovertip (Hovertip):
    def showcontents (main):
        label = tk.Label (main.tipwindow, text=f'"{main.text}"', justify=tk.LEFT, bg='#151515', fg='#ffffff', relief=tk.SOLID, borderwidth=1, font=('Roboto', 12))
        label.pack ()

# Format of the menu
menu_bar_frame = tk.Frame (main, bg=menu_bar_colour)

## Menu buttons
exit_btn = CTkButton (menu_bar_frame, text='', image=exit_icon, width=10, height=10, command=lambda: switch_indication (exit_btn_indicator, delete_pages))
exit_btn.place (x=9, y=20)
CustomHovertip (exit_btn, text='Ir al menu', hover_delay=500)

## For the separation of the buttons you should always add 60 from where "Y" starts for example 130 + 60 = 190 + 60 = 250 and so on
reg_btn = CTkButton (menu_bar_frame, text='', image=reg_icon, width=10, height=10, command=lambda: switch_indication (reg_btn_indicator, reg_page))
reg_btn.place (x=9, y=130)
CustomHovertip (reg_btn, text='Ventana para añadir datos de usuarios', hover_delay=500)

view_btn = CTkButton (menu_bar_frame, text='', image=view_icon, width=10, height=10, command=lambda: switch_indication (view_btn_indicator, view_page))
view_btn.place (x=9, y=190)
CustomHovertip (view_btn, text='Ventana para ver los datos de usuarios', hover_delay=500)

## Usage indicator for the button
exit_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
exit_btn_indicator.place (x=3, y=20, width=2, height=28)

reg_btn_indicator = tk.Label (menu_bar_frame, bg='white')
reg_btn_indicator.place (x=3, y=130, width=2, height=28)

view_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
view_btn_indicator.place (x=3, y=190, width=2, height=28)

## Form of the menu
menu_bar_frame.pack (side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
menu_bar_frame.pack_propagate (flag=False)
menu_bar_frame.configure (width=45)

## Area where the objects that are selected in the menu will be displayed
main_frame = CTkFrame (main)
main_frame.pack (side=tk.LEFT)
main_frame.pack_propagate (False)
main_frame.configure (width=800, height=500)

# To display one of the pages
reg_page ()

main.mainloop ()
