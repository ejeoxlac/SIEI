# Libraries
import customtkinter
from customtkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
from PIL import Image

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

## Model of the menu
menu_bar_colour = '#383838'

# Format of the window interface
main = customtkinter.CTk ()
main.iconbitmap ('Resources\\Img\\ico.ico')
main.title ('Datos de los equipos')
main.geometry ('860x580')
main.resizable (False, False)

# Setting the table and scrollbar style
trv_style = ttk.Style ()
trv_style.theme_use ('default')

trv_style.configure ('Treeview', background='#2a2d2e', foreground='white', rowheight=25, fieldbackground='#343638', bordercolor='#343638', borderwidth=0)
trv_style.map ('Treeview', background=[('selected', '#22559b')])

trv_style.configure ('Treeview.Heading', background='#565b5e', foreground='white', relief='flat')
trv_style.map ('Treeview.Heading', background=[('active', '#3484F0')])

trv_style.configure('Horizontal.TScrollbar', gripcount=0, background='#343638', troughcolor='#202020', arrowcolor='#E8E8E8')
trv_style.configure('Vertical.TScrollbar', gripcount=0, background='#343638', troughcolor='#202020', arrowcolor='#E8E8E8')
trv_style.map('Horizontal.TScrollbar', background=[('disabled', '#343638')])
trv_style.map('Vertical.TScrollbar', background=[('disabled', '#343638')])

# Icons
exit_icon = CTkImage (Image.open('Resources\\Img\\ExitWhite.png'), size=(20, 20))
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
        global count
        count = 0
        stat = status.get ()
        val = entry_search.get ()
        Resources.Connection.search_pc (val, stat)
        PC = Resources.Connection.cur.fetchall ()
        for row in PC:
            ##### Format so that the divisions of the data can be created within the table
            if count % 2 == 0:
                trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
            else:
                trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
            count += 1

    ### Fonts for the letters
    font1 = ('Roboto', 18, 'bold')

    ### Variable to display the text in the window
    area = "Computadoras"
    title_label_area["text"] = area

    ### Search button
    button_search = CTkButton (main, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    button_search.place (x=540, y=10)

    ### Table where the data that is being searched will be displayed
    trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

    trv.column (1, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (2, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (3, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (4, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (5, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (6, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (7, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (8, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (9, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (10, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (11, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (12, stretch=NO, width=100, anchor=tk.CENTER)

    trv.heading (1, text='ID', anchor=tk.CENTER)
    trv.heading (2, text='Nombre', anchor=tk.CENTER)
    trv.heading (3, text='Modelo', anchor=tk.CENTER)
    trv.heading (4, text='Serial', anchor=tk.CENTER)
    trv.heading (5, text='Color', anchor=tk.CENTER)
    trv.heading (6, text='Colormb', anchor=tk.CENTER)
    trv.heading (7, text='CPU', anchor=tk.CENTER)
    trv.heading (8, text='RAM', anchor=tk.CENTER)
    trv.heading (9, text='HDD o SDD', anchor=tk.CENTER)
    trv.heading (10, text='Estado', anchor=tk.CENTER)
    trv.heading (11, text='Fecha de ingreso a la entidad', anchor=tk.CENTER)
    trv.heading (12, text='Fecha de salida de la entidad', anchor=tk.CENTER)

    #### Format that creates the divisions within the table
    trv.tag_configure ('oddrow', background= '#4a5052')
    trv.tag_configure ('evenrow', background= '#2a2d2e')

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=tk.HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=5, y=408, width=778, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=782, y=5, width=20, height=420)

    trv.place (x=5, y=5, width=774, height=400)

    ### Function of deleting data
    def button_del ():
        selected = trv.selection ()
        if selected:
            rowid = selected [0]
            Resources.Connection.del_pc (rowid)
            trv.delete (rowid)
        else:
            messagebox.showerror('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

    ### Function to edit data
    def button_dem ():

        #### Format of the window interface
        data_editing_menu = customtkinter.CTkToplevel ()
        data_editing_menu.title ('Menu de edición de datos del computador')
        data_editing_menu.geometry ('700x500')
        data_editing_menu.resizable (False, False)

        #### Fonts for the letters
        font1 = ('Roboto', 30, 'bold')
        font2 = ('Roboto', 18, 'bold')

        #### User interface objects
        title_label = CTkLabel (data_editing_menu, font=font1, text='Datos del computador', text_color='#fff')
        title_label.place (x=25, y=0)

        ##### Objects within the frame
        ###### Front row
        idpc_label = CTkLabel (data_editing_menu, font=font2, text='ID:', text_color='#fff')
        idpc_label.place (x=50, y=60)

        idpc_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        idpc_entry.place (x=50, y=90)

        name_label = CTkLabel (data_editing_menu, font=font2, text='Nombre:', text_color='#fff')
        name_label.place (x=250, y=60)

        name_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        name_entry.place (x=250, y=90)

        model_label = CTkLabel (data_editing_menu, font=font2, text='Modelo:', text_color='#fff')
        model_label.place (x=445, y=60)

        model_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        model_entry.place (x=445, y=90)

        ###### Second row
        serial_label = CTkLabel (data_editing_menu, font=font2, text='Serial:', text_color='#fff')
        serial_label.place (x=50, y=140)

        serial_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        serial_entry.place (x=50, y=170)

        color_label = CTkLabel (data_editing_menu, font=font2, text='Color:', text_color='#fff')
        color_label.place (x=250, y=140)

        color_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        color_entry.place (x=250, y=170)

        colormb_label = CTkLabel (data_editing_menu, font=font2, text='Color de la placa madre:', text_color='#fff')
        colormb_label.place (x=445, y=140)

        colormb_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        colormb_entry.place (x=445, y=170)

        ###### Third row
        cpu_label = CTkLabel (data_editing_menu, font=font2, text='CPU:', text_color='#fff')
        cpu_label.place (x=50, y=220)

        cpu_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        cpu_entry.place (x=50, y=250)

        ram_label = CTkLabel (data_editing_menu, font=font2, text='RAM:', text_color='#fff')
        ram_label.place (x=250, y=220)

        ram_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        ram_entry.place (x=250, y=250)

        HDDorSDD_label = CTkLabel (data_editing_menu, font=font2, text='Unidad de almacenamiento:', text_color='#fff')
        HDDorSDD_label.place (x=445, y=220)

        HDDorSDD_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        HDDorSDD_entry.place (x=445, y=250)

        ###### Fourth row
        stat_label = CTkLabel (data_editing_menu, font=font2, text='Estado:', text_color='#fff')
        stat_label.place (x=445, y=300)

        status = StringVar ()
        options = ['Operativo', 'Inoperativo']

        stat_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
        stat_options.set ('Operativo')
        stat_options.place (x=445, y=330)

        dateofarrival_label = CTkLabel (data_editing_menu, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff')
        dateofarrival_label.place (x=50, y=300)

        dateofarrival_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        dateofarrival_entry.place (x=50, y=330)

        ###### Fifth row
        departuredate_label = CTkLabel (data_editing_menu, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff')
        departuredate_label.place (x=50, y=380)

        departuredate_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        departuredate_entry.place (x=50, y=410)
        ##### The end of the frame objects

        #### Data verification input
        def check_input ():
            selected = trv.focus ()
            rowid = selected [0]
            idpc = idpc_entry.get ()
            name = name_entry.get ()
            model = model_entry.get ()
            serial = serial_entry.get ()
            color = color_entry.get ()
            colormb = colormb_entry.get ()
            cpu = cpu_entry.get ()
            ram = ram_entry.get ()
            disk = HDDorSDD_entry.get ()
            stat = status.get ()
            dfa = dateofarrival_entry.get ()
            dtd = departuredate_entry.get ()
            if not (idpc and name and model and serial and color and colormb and cpu and ram and disk and stat and dfa):
                messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
            else:
                Resources.Connection.edit_pc (rowid, idpc, name, model, serial, color, colormb, cpu, ram, disk, stat, dfa, dtd)
                for item in trv.get_children ():
                    trv.delete (item)
                find ()
                data_editing_menu.destroy ()
                messagebox.showinfo ('Elemento editado correctamente', 'El computador fue editado correctamente')

        #### Button area
        button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
        button_dem.place (x=300, y=450)

        #### Returns selected item for editing
        try:
            selected = trv.focus ()
            values = trv.item (selected, 'values')
            idpc_entry.insert (0, values[0])
            name_entry.insert (0, values[1])
            model_entry.insert (0, values[2])
            serial_entry.insert (0, values[3])
            color_entry.insert (0, values[4])
            colormb_entry.insert (0, values[5])
            cpu_entry.insert (0, values[6])
            ram_entry.insert (0, values[7])
            HDDorSDD_entry.insert (0, values[8])
            dateofarrival_entry.insert (0, values[10])
            departuredate_entry.insert (0, values[11])
        except IndexError:
            data_editing_menu.destroy ()
            messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

    ### Function to display a statistical graph on the operability of computer goods
    def graph_pc ():
        Resources.Connection.graph_pc ()

    ### Button area
    button_del = CTkButton (main_frame, font=font1, text='Borrar computador', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
    button_del.place (x=220, y=450)

    button_edi = CTkButton (main_frame, font=font1, text='Editar computador', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
    button_edi.place (x=420, y=450)

    button_graph = CTkButton (main_frame, font=font1, text='Estadisticas', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=graph_pc)
    button_graph.place (x=650, y=450)

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
        global count
        count = 0
        stat = status.get ()
        val = entry_search.get ()
        Resources.Connection.search_pk (val, stat)
        PK = Resources.Connection.cur.fetchall ()
        for row in PK:
            ##### Format so that the divisions of the data can be created within the table
            if count % 2 == 0:
                trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
            else:
                trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
            count += 1

    ### Fonts for the letters
    font1 = ('Roboto', 18, 'bold')

    ### Variable to display the text in the window
    area = "Teclados"
    title_label_area["text"] = area

    ### Search button
    button_search = CTkButton (main, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    button_search.place (x=540, y=10)

    ### Table where the data that is being searched will be displayed
    trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8))

    trv.column (1, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (2, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (3, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (4, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (5, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (6, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (7, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (8, stretch=NO, width=100, anchor=tk.CENTER)

    trv.heading (1, text='ID', anchor=tk.CENTER)
    trv.heading (2, text='Nombre', anchor=tk.CENTER)
    trv.heading (3, text='Modelo', anchor=tk.CENTER)
    trv.heading (4, text='Serial', anchor=tk.CENTER)
    trv.heading (5, text='Color', anchor=tk.CENTER)
    trv.heading (6, text='Estado', anchor=tk.CENTER)
    trv.heading (7, text='Fecha de ingreso a la entidad', anchor=tk.CENTER)
    trv.heading (8, text='Fecha de salida de la entidad', anchor=tk.CENTER)

    #### Format that creates the divisions within the table
    trv.tag_configure ('oddrow', background= '#4a5052')
    trv.tag_configure ('evenrow', background= '#2a2d2e')

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=tk.HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=5, y=408, width=778, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=782, y=5, width=20, height=420)

    trv.place (x=5, y=5, width=774, height=400)

    ### Function of deleting data
    def button_del ():
        selected = trv.selection ()
        if selected:
            rowid = selected [0]
            Resources.Connection.del_pk (rowid)
            trv.delete (rowid)
        else:
            messagebox.showerror('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

    ### Function to edit data
    def button_dem ():

        #### Format of the window interface
        data_editing_menu = customtkinter.CTkToplevel ()
        data_editing_menu.title ('Menu de edición de datos del teclado')
        data_editing_menu.geometry ('700x500')
        data_editing_menu.resizable (False, False)

        #### Fonts for the letters
        font1 = ('Roboto', 30, 'bold')
        font2 = ('Roboto', 18, 'bold')

        #### User interface objects
        title_label = CTkLabel (data_editing_menu, font=font1, text='Datos del teclado', text_color='#fff')
        title_label.place (x=25, y=0)

        ##### Objects within the frame
        ###### Front row
        idpk_label = CTkLabel (data_editing_menu, font=font2, text='ID:', text_color='#fff')
        idpk_label.place (x=50, y=60)

        idpk_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        idpk_entry.place (x=50, y=90)

        name_label = CTkLabel (data_editing_menu, font=font2, text='Nombre:', text_color='#fff')
        name_label.place (x=250, y=60)

        name_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        name_entry.place (x=250, y=90)

        model_label = CTkLabel (data_editing_menu, font=font2, text='Modelo:', text_color='#fff')
        model_label.place (x=445, y=60)

        model_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        model_entry.place (x=445, y=90)

        ###### Second row
        serial_label = CTkLabel (data_editing_menu, font=font2, text='Serial:', text_color='#fff')
        serial_label.place (x=50, y=140)

        serial_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        serial_entry.place (x=50, y=170)

        color_label = CTkLabel (data_editing_menu, font=font2, text='Color:', text_color='#fff')
        color_label.place (x=250, y=140)

        color_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        color_entry.place (x=250, y=170)

        ###### Third row

        ###### Fourth row
        stat_label = CTkLabel (data_editing_menu, font=font2, text='Estado:', text_color='#fff')
        stat_label.place (x=445, y=300)

        status = StringVar ()
        options = ['Operativo', 'Inoperativo']

        stat_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
        stat_options.set ('Operativo')
        stat_options.place (x=445, y=330)

        dateofarrival_label = CTkLabel (data_editing_menu, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff')
        dateofarrival_label.place (x=50, y=300)

        dateofarrival_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        dateofarrival_entry.place (x=50, y=330)

        ###### Fifth row
        departuredate_label = CTkLabel (data_editing_menu, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff')
        departuredate_label.place (x=50, y=380)

        departuredate_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        departuredate_entry.place (x=50, y=410)
        ##### The end of the frame objects

        #### Data verification input
        def check_input ():
            selected = trv.focus ()
            rowid = selected [0]
            idpk = idpk_entry.get ()
            name = name_entry.get ()
            model = model_entry.get ()
            serial = serial_entry.get ()
            color = color_entry.get ()
            stat = status.get ()
            dfa = dateofarrival_entry.get ()
            dtd = departuredate_entry.get ()
            if not (idpk and name and model and serial and color and stat and dfa):
                messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
            else:
                Resources.Connection.edit_pk (rowid, idpk, name, model, serial, color, stat, dfa, dtd)
                for item in trv.get_children ():
                    trv.delete (item)
                find ()
                data_editing_menu.destroy ()
                messagebox.showinfo ('Elemento editado correctamente', 'El teclado fue editado correctamente')

        #### Button area
        button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
        button_dem.place (x=300, y=450)

        #### Returns selected item for editing
        try:
            selected = trv.focus ()
            values = trv.item (selected, 'values')
            idpk_entry.insert (0, values[0])
            name_entry.insert (0, values[1])
            model_entry.insert (0, values[2])
            serial_entry.insert (0, values[3])
            color_entry.insert (0, values[4])
            dateofarrival_entry.insert (0, values[6])
            departuredate_entry.insert (0, values[7])
        except IndexError:
            data_editing_menu.destroy ()
            messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

    ### Function to display a statistical graph on the operability of computer goods
    def graph_pk ():
        Resources.Connection.graph_pk ()

    ### Button area
    button_del = CTkButton (main_frame, font=font1, text='Borrar teclado', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
    button_del.place (x=240, y=450)
    
    button_edi = CTkButton (main_frame, font=font1, text='Editar teclado', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
    button_edi.place (x=420, y=450)

    button_graph = CTkButton (main_frame, font=font1, text='Estadisticas', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=graph_pk)
    button_graph.place (x=650, y=450)

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
        global count
        count = 0
        stat = status.get ()
        val = entry_search.get ()
        Resources.Connection.search_pm (val, stat)
        PM = Resources.Connection.cur.fetchall ()
        for row in PM:
            ##### Format so that the divisions of the data can be created within the table
            if count % 2 == 0:
                trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
            else:
                trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
            count += 1

    ### Fonts for the letters
    font1 = ('Roboto', 18, 'bold')

    ### Variable to display the text in the window
    area = "Monitores"
    title_label_area["text"] = area

    ### Search button
    button_search = CTkButton (main, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    button_search.place (x=540, y=10)

    ### Table where the data that is being searched will be displayed
    trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8))

    trv.column (1, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (2, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (3, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (4, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (5, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (6, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (7, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (8, stretch=NO, width=100, anchor=tk.CENTER)

    trv.heading (1, text='ID', anchor=tk.CENTER)
    trv.heading (2, text='Nombre', anchor=tk.CENTER)
    trv.heading (3, text='Modelo', anchor=tk.CENTER)
    trv.heading (4, text='Serial', anchor=tk.CENTER)
    trv.heading (5, text='Color', anchor=tk.CENTER)
    trv.heading (6, text='Estado', anchor=tk.CENTER)
    trv.heading (7, text='Fecha de ingreso a la entidad', anchor=tk.CENTER)
    trv.heading (8, text='Fecha de salida de la entidad', anchor=tk.CENTER)

    #### Format that creates the divisions within the table
    trv.tag_configure ('oddrow', background= '#4a5052')
    trv.tag_configure ('evenrow', background= '#2a2d2e')

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=tk.HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=5, y=408, width=778, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=782, y=5, width=20, height=420)

    trv.place (x=5, y=5, width=774, height=400)

    ### Function to delete users
    def button_del ():
        selected = trv.selection ()
        if selected:
            rowid = selected [0]
            Resources.Connection.del_pm (rowid)
            trv.delete (rowid)
        else:
            messagebox.showerror('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

    ### Function to edit users
    def button_dem ():

        #### Format of the window interface
        data_editing_menu = customtkinter.CTkToplevel ()
        data_editing_menu.title ('Menu de edición de datos del monitor')
        data_editing_menu.geometry ('800x500')
        data_editing_menu.resizable (False, False)

        #### Fonts for the letters
        font1 = ('Roboto', 30, 'bold')
        font2 = ('Roboto', 18, 'bold')

        #### User interface objects
        title_label = CTkLabel (data_editing_menu, font=font1, text='Datos del monitor', text_color='#fff')
        title_label.place (x=25, y=0)

        ##### Objects within the frame
        ###### Front row
        idpm_label = CTkLabel (data_editing_menu, font=font2, text='ID:', text_color='#fff')
        idpm_label.place (x=50, y=60)

        idpm_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        idpm_entry.place (x=50, y=90)

        name_label = CTkLabel (data_editing_menu, font=font2, text='Nombre:', text_color='#fff')
        name_label.place (x=250, y=60)

        name_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        name_entry.place (x=250, y=90)

        model_label = CTkLabel (data_editing_menu, font=font2, text='Modelo:', text_color='#fff')
        model_label.place (x=445, y=60)

        model_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        model_entry.place (x=445, y=90)

        ###### Second row
        serial_label = CTkLabel (data_editing_menu, font=font2, text='Serial:', text_color='#fff')
        serial_label.place (x=50, y=140)

        serial_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        serial_entry.place (x=50, y=170)

        color_label = CTkLabel (data_editing_menu, font=font2, text='Color:', text_color='#fff')
        color_label.place (x=250, y=140)

        color_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        color_entry.place (x=250, y=170)

        ###### Third row

        ###### Fourth row
        stat_label = CTkLabel (data_editing_menu, font=font2, text='Estado:', text_color='#fff')
        stat_label.place (x=445, y=300)

        status = StringVar ()
        options = ['Operativo', 'Inoperativo']

        stat_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
        stat_options.set ('Operativo')
        stat_options.place (x=445, y=330)

        dateofarrival_label = CTkLabel (data_editing_menu, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff')
        dateofarrival_label.place (x=50, y=300)

        dateofarrival_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        dateofarrival_entry.place (x=50, y=330)

        ###### Fifth row
        departuredate_label = CTkLabel (data_editing_menu, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff')
        departuredate_label.place (x=50, y=380)

        departuredate_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        departuredate_entry.place (x=50, y=410)
        ##### The end of the frame objects

        #### Data verification input
        def check_input ():
            selected = trv.focus ()
            rowid = selected [0]
            idpm = idpm_entry.get ()
            name = name_entry.get ()
            model = model_entry.get ()
            serial = serial_entry.get ()
            color = color_entry.get ()
            stat = status.get ()
            dfa = dateofarrival_entry.get ()
            dtd = departuredate_entry.get ()
            if not (idpm and name and model and serial and color and stat and dfa):
                messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
            else:
                Resources.Connection.edit_pm (rowid, idpm, name, model, serial, color, stat, dfa, dtd)
                for item in trv.get_children ():
                    trv.delete (item)
                find ()
                data_editing_menu.destroy ()
                messagebox.showinfo ('Elemento editado correctamente', 'El usuario fue editado correctamente')

        #### Button area
        button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
        button_dem.place (x=300, y=450)

        #### Returns selected item for editing
        try:
            selected = trv.focus ()
            values = trv.item (selected, 'values')
            idpm_entry.insert (0, values[0])
            name_entry.insert (0, values[1])
            model_entry.insert (0, values[2])
            serial_entry.insert (0, values[3])
            color_entry.insert (0, values[4])
            dateofarrival_entry.insert (0, values[6])
            departuredate_entry.insert (0, values[7])
        except IndexError:
            data_editing_menu.destroy ()
            messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

    ### Function to display a statistical graph on the operability of computer goods
    def graph_pm ():
        Resources.Connection.graph_pm ()

    ### Button area
    button_del = CTkButton (main_frame, font=font1, text='Borrar monitor', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
    button_del.place (x=240, y=450)
    
    button_edi = CTkButton (main_frame, font=font1, text='Editar monitor', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
    button_edi.place (x=420, y=450)

    button_graph = CTkButton (main_frame, font=font1, text='Estadisticas', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=graph_pm)
    button_graph.place (x=650, y=450)

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
        global count
        count = 0
        stat = status.get ()
        val = entry_search.get ()
        Resources.Connection.search_pmo (val, stat)
        PMO = Resources.Connection.cur.fetchall ()
        for row in PMO:
            ##### Format so that the divisions of the data can be created within the table
            if count % 2 == 0:
                trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
            else:
                trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
            count += 1

    ### Fonts for the letters
    font1 = ('Roboto', 18, 'bold')

    ### Variable to display the text in the window
    area = "Mouses"
    title_label_area["text"] = area

    ### Search button
    button_search = CTkButton (main, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    button_search.place (x=540, y=10)

    ### Table where the data that is being searched will be displayed
    trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8))

    trv.column (1, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (2, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (3, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (4, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (5, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (6, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (7, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (8, stretch=NO, width=100, anchor=tk.CENTER)

    trv.heading (1, text='ID', anchor=tk.CENTER)
    trv.heading (2, text='Nombre', anchor=tk.CENTER)
    trv.heading (3, text='Modelo', anchor=tk.CENTER)
    trv.heading (4, text='Serial', anchor=tk.CENTER)
    trv.heading (5, text='Color', anchor=tk.CENTER)
    trv.heading (6, text='Estado', anchor=tk.CENTER)
    trv.heading (7, text='Fecha de ingreso a la entidad', anchor=tk.CENTER)
    trv.heading (8, text='Fecha de salida de la entidad', anchor=tk.CENTER)

    #### Format that creates the divisions within the table
    trv.tag_configure ('oddrow', background= '#4a5052')
    trv.tag_configure ('evenrow', background= '#2a2d2e')

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=tk.HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=5, y=408, width=778, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=782, y=5, width=20, height=420)

    trv.place (x=5, y=5, width=774, height=400)

    ### Function to delete users
    def button_del ():
        selected = trv.selection ()
        if selected:
            rowid = selected [0]
            Resources.Connection.del_pmo (rowid)
            trv.delete (rowid)
        else:
            messagebox.showerror('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

    ### Function to edit users
    def button_dem ():

        #### Format of the window interface
        data_editing_menu = customtkinter.CTkToplevel ()
        data_editing_menu.title ('Menu de edición de datos del mouse')
        data_editing_menu.geometry ('800x500')
        data_editing_menu.resizable (False, False)

        #### Fonts for the letters
        font1 = ('Roboto', 30, 'bold')
        font2 = ('Roboto', 18, 'bold')

        #### User interface objects
        title_label = CTkLabel (data_editing_menu, font=font1, text='Datos del mouse', text_color='#fff')
        title_label.place (x=25, y=0)

        ##### Objects within the frame
        ###### Front row
        idpmo_label = CTkLabel (data_editing_menu, font=font2, text='ID:', text_color='#fff')
        idpmo_label.place (x=50, y=60)

        idpmo_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        idpmo_entry.place (x=50, y=90)

        name_label = CTkLabel (data_editing_menu, font=font2, text='Nombre:', text_color='#fff')
        name_label.place (x=250, y=60)

        name_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        name_entry.place (x=250, y=90)

        model_label = CTkLabel (data_editing_menu, font=font2, text='Modelo:', text_color='#fff')
        model_label.place (x=445, y=60)

        model_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        model_entry.place (x=445, y=90)

        ###### Second row
        serial_label = CTkLabel (data_editing_menu, font=font2, text='Serial:', text_color='#fff')
        serial_label.place (x=50, y=140)

        serial_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        serial_entry.place (x=50, y=170)

        color_label = CTkLabel (data_editing_menu, font=font2, text='Color:', text_color='#fff')
        color_label.place (x=250, y=140)

        color_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        color_entry.place (x=250, y=170)

        ###### Third row

        ###### Fourth row
        stat_label = CTkLabel (data_editing_menu, font=font2, text='Estado:', text_color='#fff')
        stat_label.place (x=445, y=300)

        status = StringVar ()
        options = ['Operativo', 'Inoperativo']

        stat_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
        stat_options.set ('Operativo')
        stat_options.place (x=445, y=330)

        dateofarrival_label = CTkLabel (data_editing_menu, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff')
        dateofarrival_label.place (x=50, y=300)

        dateofarrival_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        dateofarrival_entry.place (x=50, y=330)

        ###### Fifth row
        departuredate_label = CTkLabel (data_editing_menu, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff')
        departuredate_label.place (x=50, y=380)

        departuredate_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        departuredate_entry.place (x=50, y=410)
        ##### The end of the frame objects

        #### Data verification input
        def check_input ():
            selected = trv.focus ()
            rowid = selected [0]
            idpmo = idpmo_entry.get ()
            name = name_entry.get ()
            model = model_entry.get ()
            serial = serial_entry.get ()
            color = color_entry.get ()
            stat = status.get ()
            dfa = dateofarrival_entry.get ()
            dtd = departuredate_entry.get ()
            if not (idpmo and name and model and serial and color and stat and dfa):
                messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
            else:
                Resources.Connection.edit_pmo (rowid, idpmo, name, model, serial, color, stat, dfa, dtd)
                for item in trv.get_children ():
                    trv.delete (item)
                find ()
                data_editing_menu.destroy ()
                messagebox.showinfo ('Elemento editado correctamente', 'El usuario fue editado correctamente')

        #### Button area
        button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
        button_dem.place (x=300, y=450)

        #### Returns selected item for editing
        try:
            selected = trv.focus ()
            values = trv.item (selected, 'values')
            idpmo_entry.insert (0, values[0])
            name_entry.insert (0, values[1])
            model_entry.insert (0, values[2])
            serial_entry.insert (0, values[3])
            color_entry.insert (0, values[4])
            dateofarrival_entry.insert (0, values[6])
            departuredate_entry.insert (0, values[7])
        except IndexError:
            data_editing_menu.destroy ()
            messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

    ### Function to display a statistical graph on the operability of computer goods
    def graph_pmo ():
        Resources.Connection.graph_pmo ()

    ### Button area
    button_del = CTkButton (main_frame, font=font1, text='Borrar mouse', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
    button_del.place (x=240, y=450)

    button_edi = CTkButton (main_frame, font=font1, text='Editar mouse', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
    button_edi.place (x=420, y=450)

    button_graph = CTkButton (main_frame, font=font1, text='Estadisticas', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=graph_pmo)
    button_graph.place (x=650, y=450)

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
        global count
        count = 0
        stat = status.get ()
        val = entry_search.get ()
        Resources.Connection.search_pp (val, stat)
        PP = Resources.Connection.cur.fetchall ()
        for row in PP:
            ##### Format so that the divisions of the data can be created within the table
            if count % 2 == 0:
                trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
            else:
                trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
            count += 1

    ### Fonts for the letters
    font1 = ('Roboto', 18, 'bold')

    ### Variable to display the text in the window
    area = "Impresoras"
    title_label_area["text"] = area

    ### Search button
    button_search = CTkButton (main, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
    button_search.place (x=540, y=10)

    ### Table where the data that is being searched will be displayed
    trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

    trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8))

    trv.column (1, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (2, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (3, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (4, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (5, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (6, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (7, stretch=NO, width=100, anchor=tk.CENTER)
    trv.column (8, stretch=NO, width=100, anchor=tk.CENTER)

    trv.heading (1, text='ID', anchor=tk.CENTER)
    trv.heading (2, text='Nombre', anchor=tk.CENTER)
    trv.heading (3, text='Modelo', anchor=tk.CENTER)
    trv.heading (4, text='Serial', anchor=tk.CENTER)
    trv.heading (5, text='Color', anchor=tk.CENTER)
    trv.heading (6, text='Estado', anchor=tk.CENTER)
    trv.heading (7, text='Fecha de ingreso a la entidad', anchor=tk.CENTER)
    trv.heading (8, text='Fecha de salida de la entidad', anchor=tk.CENTER)

    #### Format that creates the divisions within the table
    trv.tag_configure ('oddrow', background= '#4a5052')
    trv.tag_configure ('evenrow', background= '#2a2d2e')

    #### Format to move the data table both horizontally and vertically
    scrollbarx = ttk.Scrollbar (main_frame, orient=tk.HORIZONTAL, command=trv.xview)
    trv.configure (xscroll=scrollbarx.set)
    trv.configure (selectmode='extended')
    scrollbarx.place (x=5, y=408, width=778, height=20)

    scrollbary = ttk.Scrollbar (main_frame, orient=tk.VERTICAL, command=trv.yview)
    trv.configure (yscroll=scrollbary.set)
    trv.configure (selectmode='extended')
    scrollbary.place (x=782, y=5, width=20, height=420)

    trv.place (x=5, y=5, width=774, height=400)

    ### Function to delete users
    def button_del ():
        selected = trv.selection ()
        if selected:
            rowid = selected [0]
            Resources.Connection.del_pp (rowid)
            trv.delete (rowid)
        else:
            messagebox.showerror('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

    ### Function to edit users
    def button_dem ():

        #### Format of the window interface
        data_editing_menu = customtkinter.CTkToplevel ()
        data_editing_menu.title ('Menu de edición de datos de la impresora')
        data_editing_menu.geometry ('800x500')
        data_editing_menu.resizable (False, False)

        #### Fonts for the letters
        font1 = ('Roboto', 30, 'bold')
        font2 = ('Roboto', 18, 'bold')

        #### User interface objects
        title_label = CTkLabel (data_editing_menu, font=font1, text='Datos de la impresora', text_color='#fff')
        title_label.place (x=25, y=0)

        ##### Objects within the frame
        ###### Front row
        idpp_label = CTkLabel (data_editing_menu, font=font2, text='ID:', text_color='#fff')
        idpp_label.place (x=50, y=60)

        idpp_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        idpp_entry.place (x=50, y=90)

        name_label = CTkLabel (data_editing_menu, font=font2, text='Nombre:', text_color='#fff')
        name_label.place (x=250, y=60)

        name_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        name_entry.place (x=250, y=90)

        model_label = CTkLabel (data_editing_menu, font=font2, text='Modelo:', text_color='#fff')
        model_label.place (x=445, y=60)

        model_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        model_entry.place (x=445, y=90)

        ###### Second row
        serial_label = CTkLabel (data_editing_menu, font=font2, text='Serial:', text_color='#fff')
        serial_label.place (x=50, y=140)

        serial_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        serial_entry.place (x=50, y=170)

        color_label = CTkLabel (data_editing_menu, font=font2, text='Color:', text_color='#fff')
        color_label.place (x=250, y=140)

        color_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        color_entry.place (x=250, y=170)

        ###### Third row

        ###### Fourth row
        stat_label = CTkLabel (data_editing_menu, font=font2, text='Estado:', text_color='#fff')
        stat_label.place (x=445, y=300)

        status = StringVar ()
        options = ['Operativo', 'Inoperativo']

        stat_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
        stat_options.set ('Operativo')
        stat_options.place (x=445, y=330)

        dateofarrival_label = CTkLabel (data_editing_menu, font=font2, text='Fecha de entrada a la entidad:', text_color='#fff')
        dateofarrival_label.place (x=50, y=300)

        dateofarrival_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        dateofarrival_entry.place (x=50, y=330)

        ###### Fifth row
        departuredate_label = CTkLabel (data_editing_menu, font=font2, text='Fecha de salidad de la entidad:', text_color='#fff')
        departuredate_label.place (x=50, y=380)

        departuredate_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        departuredate_entry.place (x=50, y=410)
        ##### The end of the frame objects

        #### Data verification input
        def check_input ():
            selected = trv.focus ()
            rowid = selected [0]
            idpp = idpp_entry.get ()
            name = name_entry.get ()
            model = model_entry.get ()
            serial = serial_entry.get ()
            color = color_entry.get ()
            stat = status.get ()
            dfa = dateofarrival_entry.get ()
            dtd = departuredate_entry.get ()
            if not (idpp and name and model and serial and color and stat and dfa):
                messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
            else:
                Resources.Connection.edit_pp (rowid, idpp, name, model, serial, color, stat, dfa, dtd)
                for item in trv.get_children ():
                    trv.delete (item)
                find ()
                data_editing_menu.destroy ()
                messagebox.showinfo ('Elemento editado correctamente', 'El usuario fue editado correctamente')

        #### Button area
        button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
        button_dem.place (x=300, y=450)

        #### Returns selected item for editing
        try:
            selected = trv.focus ()
            values = trv.item (selected, 'values')
            idpp_entry.insert (0, values[0])
            name_entry.insert (0, values[1])
            model_entry.insert (0, values[2])
            serial_entry.insert (0, values[3])
            color_entry.insert (0, values[4])
            dateofarrival_entry.insert (0, values[6])
            departuredate_entry.insert (0, values[7])
        except IndexError:
            data_editing_menu.destroy ()
            messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

    ### Function to display a statistical graph on the operability of computer goods
    def graph_pp ():
        Resources.Connection.graph_pp ()

    ### Button area
    button_del = CTkButton (main_frame, font=font1, text='Borrar impresora', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
    button_del.place (x=240, y=450)
    
    button_edi = CTkButton (main_frame, font=font1, text='Editar impresora', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
    button_edi.place (x=420, y=450)

    button_graph = CTkButton (main_frame, font=font1, text='Estadisticas', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=graph_pp)
    button_graph.place (x=650, y=450)

    ### Function to display the data automatically after opening the window
    button_search ['command'] = find

    find ()

# Function to delete the window or close
def delete_pages ():
    for frame in main_frame.winfo_children ():
        frame.destroy ()

# Function to show which button and window is being selected
def hide_indicator ():

    exit_btn_indicator.config (bg=menu_bar_colour)
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

# Generator of help message for objects in which the cursor is needed to be positioned to know more about the object
class CustomHovertip (Hovertip):
    def showcontents (main):
        label = tk.Label (main.tipwindow, text=f'"{main.text}"', justify=tk.LEFT, bg='#151515', fg='#ffffff', relief=tk.SOLID, borderwidth=1, font=('Roboto', 12))
        label.pack ()

# Format of the menu
menu_bar_frame = tk.Frame (main, bg=menu_bar_colour)

## Fonts for the letters
font1 = ('Roboto', 18, 'bold')

## Format for the title to be displayed each time one of the menu sections is opened
title_label_area = tk.Label (main, font=font1, fg='#fff', background="#242424")
title_label_area.place (x=60, y=10)

## Menu buttons
exit_btn = CTkButton (menu_bar_frame, text='', image=exit_icon, width=10, height=10, command=lambda: switch_indication (exit_btn_indicator, delete_pages))
exit_btn.place (x=9, y=20)
CustomHovertip (exit_btn, text='Ir al menu', hover_delay=500)

## For the separation of the buttons you should always add 60 from where "Y" starts for example 130 + 60 = 190 + 60 = 250 and so on
pc_btn = CTkButton (menu_bar_frame, text='', image=pc_icon, width=10, height=10, command=lambda: switch_indication (pc_btn_indicator, pc_page))
pc_btn.place (x=9, y=130)
CustomHovertip (pc_btn, text='Ver las computadoras registradas', hover_delay=500)

pk_btn = CTkButton (menu_bar_frame, text='', image=pk_icon, width=10, height=10, command=lambda: switch_indication (pk_btn_indicator, pk_page))
pk_btn.place (x=9, y=190)
CustomHovertip (pk_btn, text='Ver los teclados registrados', hover_delay=500)

pm_btn = CTkButton (menu_bar_frame, text='', image=pm_icon, width=10, height=10, command=lambda: switch_indication (pm_btn_indicator, pm_page))
pm_btn.place (x=9, y=250)
CustomHovertip (pm_btn, text='Ver los monitores registrados', hover_delay=500)

pmo_btn = CTkButton (menu_bar_frame, text='', image=pmo_icon, width=10, height=10,  command=lambda: switch_indication (pmo_btn_indicator, pmo_page))
pmo_btn.place (x=9, y=310)
CustomHovertip (pmo_btn, text='Ver los mouses registrados', hover_delay=500)

pp_btn = CTkButton (menu_bar_frame, text='', image=pp_icon, width=10, height=10,  command=lambda: switch_indication (pp_btn_indicator, pp_page))
pp_btn.place (x=9, y=370)
CustomHovertip (pp_btn, text='Ver las impresoras registradas', hover_delay=500)

## Usage indicator for the button
exit_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
exit_btn_indicator.place (x=3, y=20, width=2, height=28)

pc_btn_indicator = tk.Label (menu_bar_frame, bg='white')
pc_btn_indicator.place (x=3, y=130, width=2, height=28)

pk_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pk_btn_indicator.place (x=3, y=190, width=2, height=28)

pm_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pm_btn_indicator.place (x=3, y=250, width=2, height=28)

pmo_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pmo_btn_indicator.place (x=3, y=310, width=2, height=28)

pp_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour)
pp_btn_indicator.place (x=3, y=370, width=2, height=28)

## Form of the menu
menu_bar_frame.pack (side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
menu_bar_frame.pack_propagate (flag=False)
menu_bar_frame.configure (width=45)

## Area where the objects that are selected in the menu will be displayed
main_frame = CTkFrame (main)
main_frame.pack (side=tk.LEFT)
main_frame.pack_propagate (False)
main_frame.configure (width=800, height=500)

## Search box and button to be used with the options box for filtering
entry_search = CTkEntry (main, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=300)
entry_search.place (x=230, y=10)

## Box of options for the search
status = StringVar ()
options = ['Operativo', 'Inoperativo']

stat_options = CTkComboBox (main, text_color='#000', fg_color='#fff', dropdown_hover_color='#7d01b2', button_color='#7d01b2', button_hover_color='#7d01b2', border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
stat_options.set ('Operativo')
stat_options.place (x=650, y=10)

# To display one of the pages
pc_page ()

main.mainloop ()
