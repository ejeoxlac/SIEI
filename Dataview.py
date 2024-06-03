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
app.geometry ('850x650')

# Icons
pc_icon = CTkImage (Image.open('Resources\\Img\\Computer.png'), size=(20, 20))
pk_icon = CTkImage (Image.open('Resources\\Img\\Keyboard.png'), size=(20, 20))
pm_icon = CTkImage (Image.open('Resources\\Img\\Monitor.png'), size=(20, 20))
pmo_icon = CTkImage (Image.open('Resources\\Img\\Mouse.png'), size=(20, 20))
pp_icon = CTkImage (Image.open('Resources\\Img\\Printer.png'), size=(20, 20))

# Functions to display the data
## Computers data window
def pc_page ():

    ### Search function within the database for obtaining data from computers
    def find ():

        #### Clear treeview
        for item in trv.get_children ():
            trv.delete (item)
        stat = status.get ()
        val = entry_search.get ()
        Resources.Connection.search_pc (val, stat)
        PC = Resources.Connection.cur.fetchall ()
        for row in PC:
            trv.insert ('', END, values=row)

    ### Search button
    button_search = CTkButton (app, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    button_search.place (x=350, y=15)

    ### Table where the data that is being searched will be displayed
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
    scrollbarx.place (x=30, y=515, width=789, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=820, y=50, width=20, height=485)

    trv.place (x=5, y=5, width=775, height=455)

    ### Function to display the data automatically after opening the window
    button_search ['command'] = find

    find ()

## Keyboards data window
def pk_page ():

    ### Search function within the database to get data from keyboards
    def find ():

        #### Clear treeview
        for item in trv.get_children ():
            trv.delete (item)
        stat = status.get ()
        val = entry_search.get ()
        Resources.Connection.search_pk (val, stat)
        Pk = Resources.Connection.cur.fetchall ()
        for row in Pk:
            trv.insert ('', END, values=row)

    ### Search button
    button_search = CTkButton (app, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    button_search.place (x=350, y=15)

    ### Table where the data that is being searched will be displayed
    trv = ttk.Treeview(main_frame, height=22, show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

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

    trv.heading (1, text='ID', anchor=tk.CENTER)
    trv.heading (2, text='Nombre', anchor=tk.CENTER)
    trv.heading (3, text='Modelo', anchor=tk.CENTER)
    trv.heading (4, text='Serial', anchor=tk.CENTER)
    trv.heading (5, text='Color', anchor=tk.CENTER)
    trv.heading (6, text='CPU', anchor=tk.CENTER)
    trv.heading (7, text='RAM', anchor=tk.CENTER)
    trv.heading (8, text='HDDvsSSD', anchor=tk.CENTER)
    trv.heading (9, text='Estado', anchor=tk.CENTER)
    trv.heading (10, text='Usuario', anchor=tk.CENTER)

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=tk.HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=30, y=515, width=789, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=820, y=50, width=20, height=485)

    trv.place (x=5, y=5, width=775, height=455)

    ### Function to display the data automatically after opening the window
    button_search ['command'] = find

    find ()

## Monitors data window
def pm_page ():

    ### Search function within the database to get data from the monitors
    def find ():

        #### Clear treeview
        for item in trv.get_children ():
            trv.delete (item)
        stat = status.get ()
        val = entry_search.get ()
        Resources.Connection.search_pm (val, stat)
        Pk = Resources.Connection.cur.fetchall ()
        for row in Pk:
            trv.insert ('', END, values=row)

    ### Search button
    button_search = CTkButton (app, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    button_search.place (x=350, y=15)

    ### Table where the data that is being searched will be displayed
    trv = ttk.Treeview(main_frame, height=22, show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

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

    trv.heading (1, text='ID', anchor=tk.CENTER)
    trv.heading (2, text='Nombre', anchor=tk.CENTER)
    trv.heading (3, text='Modelo', anchor=tk.CENTER)
    trv.heading (4, text='Serial', anchor=tk.CENTER)
    trv.heading (5, text='Color', anchor=tk.CENTER)
    trv.heading (6, text='CPU', anchor=tk.CENTER)
    trv.heading (7, text='RAM', anchor=tk.CENTER)
    trv.heading (8, text='HDDvsSSD', anchor=tk.CENTER)
    trv.heading (9, text='Estado', anchor=tk.CENTER)
    trv.heading (10, text='Usuario', anchor=tk.CENTER)

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=tk.HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=30, y=515, width=789, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=820, y=50, width=20, height=485)

    trv.place (x=5, y=5, width=775, height=455)

    ### Function to display the data automatically after opening the window
    button_search ['command'] = find

    find ()

## Mouses data window
def pmo_page ():

  ### Search function within the database for obtaining data from mouses
    def find ():

        #### Clear treeview
        for item in trv.get_children ():
            trv.delete (item)
        stat = status.get ()
        val = entry_search.get ()
        Resources.Connection.search_pmo (val, stat)
        Pk = Resources.Connection.cur.fetchall ()
        for row in Pk:
            trv.insert ('', END, values=row)

    ### Search button
    button_search = CTkButton (app, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    button_search.place (x=350, y=15)

    ### Table where the data that is being searched will be displayed
    trv = ttk.Treeview(main_frame, height=22, show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

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

    trv.heading (1, text='ID', anchor=tk.CENTER)
    trv.heading (2, text='Nombre', anchor=tk.CENTER)
    trv.heading (3, text='Modelo', anchor=tk.CENTER)
    trv.heading (4, text='Serial', anchor=tk.CENTER)
    trv.heading (5, text='Color', anchor=tk.CENTER)
    trv.heading (6, text='CPU', anchor=tk.CENTER)
    trv.heading (7, text='RAM', anchor=tk.CENTER)
    trv.heading (8, text='HDDvsSSD', anchor=tk.CENTER)
    trv.heading (9, text='Estado', anchor=tk.CENTER)
    trv.heading (10, text='Usuario', anchor=tk.CENTER)

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=tk.HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=30, y=515, width=789, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=820, y=50, width=20, height=485)

    trv.place (x=5, y=5, width=775, height=455)

    ### Function to display the data automatically after opening the window
    button_search ['command'] = find

    find ()

## Printers data window
def pp_page ():

    ### Search function within the database to get data from printers
    def find ():

        #### Clear treeview
        for item in trv.get_children ():
            trv.delete (item)
        stat = status.get ()
        val = entry_search.get ()
        Resources.Connection.search_pp (val, stat)
        Pk = Resources.Connection.cur.fetchall ()
        for row in Pk:
            trv.insert ('', END, values=row)

    ### Search button
    button_search = CTkButton (app, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    button_search.place (x=350, y=15)

    ### Table where the data that is being searched will be displayed
    trv = ttk.Treeview(main_frame, height=22, show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

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

    trv.heading (1, text='ID', anchor=tk.CENTER)
    trv.heading (2, text='Nombre', anchor=tk.CENTER)
    trv.heading (3, text='Modelo', anchor=tk.CENTER)
    trv.heading (4, text='Serial', anchor=tk.CENTER)
    trv.heading (5, text='Color', anchor=tk.CENTER)
    trv.heading (6, text='CPU', anchor=tk.CENTER)
    trv.heading (7, text='RAM', anchor=tk.CENTER)
    trv.heading (8, text='HDDvsSSD', anchor=tk.CENTER)
    trv.heading (9, text='Estado', anchor=tk.CENTER)
    trv.heading (10, text='Usuario', anchor=tk.CENTER)

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=tk.HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=30, y=515, width=789, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=820, y=50, width=20, height=485)

    trv.place (x=5, y=5, width=775, height=455)

    ### Function to display the data automatically after opening the window
    button_search ['command'] = find

    find ()

# Function to delete the window or close
def delete_pages ():
  for frame in main_frame.winfo_children ():
    frame.destroy ()

# Function to show which button and window is being selected
def hide_indicator ():

  pc_btn_indicator.config (bg=menu_bar_colour)
  pk_btn_indicator.config (bg=menu_bar_colour)
  pm_btn_indicator.config (bg=menu_bar_colour)
  pmo_btn_indicator.config (bg=menu_bar_colour)
  pp_btn_indicator.config (bg=menu_bar_colour)

# Function that shows the page and marks which is the button that is being used
def switch_indication (lb, page):

  hide_indicator ()
  lb.config (bg='white')
  delete_pages ()
  page ()

# Format of the menu
menu_bar_frame = tk.Frame (app, bg=menu_bar_colour)

## Menu buttons
### For the separation of the buttons you should always add 60 from where "Y" starts for example 130 + 60 = 190 + 60 = 250 and so on
pc_btn = CTkButton (menu_bar_frame, text='', image=pc_icon, width=10, height=10, command=lambda: switch_indication (pc_btn_indicator, pc_page))
pc_btn.place (x=9, y=130)

pk_btn = CTkButton (menu_bar_frame, text='', image=pk_icon, width=10, height=10, command=lambda: switch_indication (pk_btn_indicator, pk_page))
pk_btn.place (x=9, y=190)

pm_btn = CTkButton (menu_bar_frame, text='', image=pm_icon, width=10, height=10, command=lambda: switch_indication (pm_btn_indicator, pm_page))
pm_btn.place (x=9, y=250)

pmo_btn = CTkButton (menu_bar_frame, text='', image=pmo_icon, width=10, height=10,  command=lambda: switch_indication (pmo_btn_indicator, pmo_page))
pmo_btn.place (x=9, y=310)

pp_btn = CTkButton (menu_bar_frame, text='', image=pp_icon, width=10, height=10,  command=lambda: switch_indication (pp_btn_indicator, pp_page))
pp_btn.place (x=9, y=370)

## Usage indicator for the button
pc_btn_indicator = tk.Label (menu_bar_frame, bg='white')
pc_btn_indicator.place (x=3, y=130, width=3, height=30)

pk_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pk_btn_indicator.place (x=3, y=190, width=3, height=30)

pm_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pm_btn_indicator.place (x=3, y=250, width=3, height=30)

pmo_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pmo_btn_indicator.place (x=3, y=310, width=3, height=30)

pp_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pp_btn_indicator.place (x=3, y=370, width=3, height=30)

## Form of the menu
menu_bar_frame.pack (side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
menu_bar_frame.pack_propagate (flag=False)
menu_bar_frame.configure (width=45)

## Area where the objects that are selected in the menu will be displayed
main_frame = CTkFrame (app)
main_frame.pack (side=tk.LEFT)
main_frame.pack_propagate (False)
main_frame.configure (height=465, width=789)

# Point to create the framework that works in the app
frame = tk.Frame(app)

# Title
title_label = CTkLabel (app, text='Computadoras registradas', text_color='#fff', font=('Roboto', 20, 'bold'))
title_label.place (x=350, y=45)

# Search box and button to be used with the options box for filtering
entry_search = CTkEntry (app, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=300)
entry_search.place (x=50, y=15)

## Box of options for the search
status = StringVar ()
options = ['Operativo', 'Inoperativo']

stat_options = CTkComboBox (app, text_color='#000', fg_color='#fff', dropdown_hover_color='#7d01b2', button_color='#7d01b2', button_hover_color='#7d01b2', border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
stat_options.set ('Operativo')
stat_options.place (x=460, y=15)

app.mainloop ()
