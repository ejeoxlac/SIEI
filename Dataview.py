# Libraries
import customtkinter
from customtkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
from PIL import Image
from tkcalendar import *
from datetime import datetime

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection
import Resources.Previewpk
import Resources.Previewpc
import Resources.Previewpm
import Resources.Previewpmo
import Resources.Previewpp

# I define the view so I can call it
def dataviewview (mainmenu):

    ## Defined appearance
    set_appearance_mode ('dark')
    set_default_color_theme ('blue')

    ### Model of the menu
    menu_bar_colour = '#383838'

    ## Format of the window interface
    maindataview = customtkinter.CTkToplevel ()
    maindataview.after(250, lambda:  maindataview.iconbitmap('Resources\\Img\\Ico.ico'))
    maindataview.title ('Datos de los equipos')
    maindataview.geometry ('1000x580')
    maindataview.resizable (False, False)

    ## Code to center the application window
    ### Refresh the window to make sure the size of it
    maindataview.update_idletasks ()
    ### Get the screen size
    screen_width = maindataview.winfo_screenwidth ()
    screen_height = maindataview.winfo_screenheight ()
    ### Get the size of the window
    win_width = maindataview.winfo_width ()
    win_height = maindataview.winfo_height ()
    ### Calculate the centered position
    x = (screen_width // 2) - (win_width // 2)
    y = (screen_height // 2) - (win_height // 2)
    ### Set the new position
    maindataview.geometry(f"+{x}+{y}")

    ## Setting the table and scrollbar style
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

    ## Icons
    exit_icon = CTkImage (Image.open('Resources\\Img\\ExitWhite.png'), size=(20, 20))
    pc_icon = CTkImage (Image.open('Resources\\Img\\Computer.png'), size=(20, 20))
    pk_icon = CTkImage (Image.open('Resources\\Img\\Keyboard.png'), size=(20, 20))
    pm_icon = CTkImage (Image.open('Resources\\Img\\Monitor.png'), size=(20, 20))
    pmo_icon = CTkImage (Image.open('Resources\\Img\\Mouse.png'), size=(20, 20))
    pp_icon = CTkImage (Image.open('Resources\\Img\\Printer.png'), size=(20, 20))

    ## Generator of help message for objects in which the cursor is needed to be positioned to know more about the object
    class CustomHovertip (Hovertip):
        def showcontents (main):
            label = tk.Label (main.tipwindow, text=f'''{main.text}''', justify=tk.LEFT, bg='#151515', fg='#ffffff', relief=tk.SOLID, borderwidth=1, font=('Roboto', 12))
            label.pack ()

    ## Fonts for the letters
    font1 = ('Roboto', 18, 'bold')

    ### Format for the title to be displayed each time one of the menu sections is opened
    title_label_area = tk.Label (maindataview, font=font1, fg='#fff', background="#242424")
    title_label_area.place (x=60, y=10)

    ## Format of the menu
    menu_bar_frame = tk.Frame (maindataview, bg=menu_bar_colour)

    ### Menu buttons
    exit_btn = CTkButton (menu_bar_frame, text='', image=exit_icon, width=10, height=10, command=lambda: switch_indication (exit_btn_indicator, menu_page))
    exit_btn.grid (row=0, column=0, padx=(5, 0), pady=(13.2, 0))
    CustomHovertip (exit_btn, text='Ir al menu', hover_delay=500)

    ### For the separation of the buttons you should always add 60 from where "Y" starts for example 130 + 60 = 190 + 60 = 250 and so on
    pc_btn = CTkButton (menu_bar_frame, text='', image=pc_icon, width=10, height=10, command=lambda: switch_indication (pc_btn_indicator, pc_page))
    pc_btn.grid (row=1, column=0, padx=(5, 0), pady=(60, 0))
    CustomHovertip (pc_btn, text='Ver las computadoras registradas', hover_delay=500)

    pk_btn = CTkButton (menu_bar_frame, text='', image=pk_icon, width=10, height=10, command=lambda: switch_indication (pk_btn_indicator, pk_page))
    pk_btn.grid (row=2, column=0, padx=(5, 0), pady=(20, 0))
    CustomHovertip (pk_btn, text='Ver los teclados registrados', hover_delay=500)

    pm_btn = CTkButton (menu_bar_frame, text='', image=pm_icon, width=10, height=10, command=lambda: switch_indication (pm_btn_indicator, pm_page))
    pm_btn.grid (row=3, column=0, padx=(6, 0), pady=(20, 0))
    CustomHovertip (pm_btn, text='Ver los monitores registrados', hover_delay=500)

    pmo_btn = CTkButton (menu_bar_frame, text='', image=pmo_icon, width=10, height=10,  command=lambda: switch_indication (pmo_btn_indicator, pmo_page))
    pmo_btn.grid (row=4, column=0, padx=(6, 0), pady=(20, 0))
    CustomHovertip (pmo_btn, text='Ver los mouses registrados', hover_delay=500)

    pp_btn = CTkButton (menu_bar_frame, text='', image=pp_icon, width=10, height=10,  command=lambda: switch_indication (pp_btn_indicator, pp_page))
    pp_btn.grid (row=5, column=0, padx=(6, 0), pady=(20, 0))
    CustomHovertip (pp_btn, text='Ver las impresoras registradas', hover_delay=500)

    ### Usage indicator for the button
    exit_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
    exit_btn_indicator.grid(row=0, column=1, padx=(2, 0), pady=(15, 0), sticky='n')

    pc_btn_indicator = tk.Label (menu_bar_frame, bg='white', width=0, height=3)
    pc_btn_indicator.grid(row=1, column=1, padx=(2, 0), pady=(72, 0), sticky='n')

    pk_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
    pk_btn_indicator.grid(row=2, column=1, padx=(2, 0), pady=(23, 0), sticky='n')

    pm_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
    pm_btn_indicator.grid(row=3, column=1, padx=(2, 0), pady=(23, 0), sticky='n')

    pmo_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
    pmo_btn_indicator.grid(row=4, column=1, padx=(2, 0), pady=(23, 0), sticky='n')

    pp_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
    pp_btn_indicator.grid(row=5, column=1, padx=(2, 0), pady=(23, 0), sticky='n')

    ### Form of the menu
    menu_bar_frame.pack (side=tk.LEFT, fill=tk.Y, pady=4, padx=3)
    menu_bar_frame.pack_propagate (flag=False)
    menu_bar_frame.configure (width=45)

    ### Area where the objects that are selected in the menu will be displayed
    main_frame = CTkFrame (maindataview)
    main_frame.pack (fill='both', side=tk.LEFT, padx=(0,20), pady=(40, 10))
    main_frame.pack_propagate (False)
    main_frame.configure (width=910, height=500)

    ## Functions to display the data
    ### Computers data window
    def pc_page ():

        #### The window that is open is saved in the variable
        global current_page
        current_page = 'pc_page'

        #### Search function within the database for obtaining data from computers
        def find ():

            ##### Clear treeview
            for item in trv.get_children ():
                trv.delete (item)
            global count
            count = 0
            val = entry_search.get ()
            stat = status.get ()
            dp = departments.get ()
            Resources.Connection.search_pc (val, stat, dp)
            PC = Resources.Connection.cur.fetchall ()
            for row in PC:
                ###### Format so that the divisions of the data can be created within the table
                if count % 2 == 0:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
                else:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
                count += 1

        #### Fonts for the letters
        font1 = ('Roboto', 18, 'bold')

        #### Variable to display the text in the window
        area = "Computadoras"
        title_label_area["text"] = area

        #### Search button
        button_search = CTkButton (maindataview, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
        button_search.place (x=540, y=10)

        #### Table where the data that is being searched will be displayed
        trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

        trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

        ##### Defines the columns of the table, all equally and automatically
        for col in range (1, 21):
            trv.column (col, stretch=NO, anchor=tk.CENTER)

        trv.heading (1, text='ID', anchor=tk.CENTER)
        trv.heading (2, text='Nombre', anchor=tk.CENTER)
        trv.heading (3, text='Modelo', anchor=tk.CENTER)
        trv.heading (4, text='Serial', anchor=tk.CENTER)
        trv.heading (5, text='Color', anchor=tk.CENTER)
        trv.heading (6, text='Modelomb', anchor=tk.CENTER)
        trv.heading (7, text='Colormb', anchor=tk.CENTER)
        trv.heading (8, text='Marca de la gráfica', anchor=tk.CENTER)
        trv.heading (9, text='Modelo de la gráfica', anchor=tk.CENTER)
        trv.heading (10, text='CPU', anchor=tk.CENTER)
        trv.heading (11, text='RAM', anchor=tk.CENTER)
        trv.heading (12, text='HDD o SDD', anchor=tk.CENTER)
        trv.heading (13, text='Sistema operativo', anchor=tk.CENTER)
        trv.heading (14, text='Departamentos', anchor=tk.CENTER)
        trv.heading (15, text='Usuarios', anchor=tk.CENTER)
        trv.heading (16, text='Estado', anchor=tk.CENTER)
        trv.heading (17, text='Fecha de ingreso a la entidad', anchor=tk.CENTER)
        trv.heading (18, text='Fecha de modificación', anchor=tk.CENTER)
        trv.heading (19, text='Fecha de salida de la entidad', anchor=tk.CENTER)
        trv.heading (20, text='Observaciones', anchor=tk.CENTER)

        ##### Format that creates the divisions within the table
        trv.tag_configure ('oddrow', background='#4a5052')
        trv.tag_configure ('evenrow', background='#2a2d2e')

        #### Format to move the data table both horizontally and vertically
        scrollbarx = ttk.Scrollbar (main_frame, orient=HORIZONTAL, command=trv.xview)
        trv.configure (xscroll=scrollbarx.set)
        trv.configure (selectmode='extended')
        scrollbarx.grid (row=1, column=0,  columnspan=2, sticky='ew')

        scrollbary = ttk.Scrollbar (main_frame, orient=VERTICAL, command=trv.yview)
        trv.configure (yscroll=scrollbary.set)
        trv.configure (selectmode='extended')
        scrollbary.grid (row=0, column=1,  columnspan=2, sticky='ns')

        trv.grid (row=0, column=0,  columnspan=2, padx=(0, 16), pady=(0, 1), sticky='nsew')

        #### Setting so that the objects are centered
        main_frame.grid_rowconfigure (0, weight=1)
        main_frame.grid_columnconfigure (0, weight=1)

        #### Function of deleting data
        def button_del ():
            selected = trv.selection ()
            if selected:
                rowid = selected [0]
                Resources.Connection.del_pc (rowid)
                trv.delete (rowid)
            else:
                messagebox.showerror('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

        #### Function to edit data
        def button_dem ():

            ##### Format of the window interface
            data_editing_menu = customtkinter.CTkToplevel ()
            data_editing_menu.after(250, lambda:  data_editing_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            data_editing_menu.title ('Menu de edición de datos del computador')
            data_editing_menu.geometry ('960x600')
            data_editing_menu.resizable (False, False)

            ##### Validates if they are only numbers and dashes
            def validate_numbers_entry (char):
                if char == '' or all (c.isdigit() or c == '-' for c in char):
                    return True
                else:
                    return False

            ##### Fonts for the letters
            font1 = ('Roboto', 30, 'bold')
            font2 = ('Roboto', 18, 'bold')
            font3 = ('Roboto', 16, 'bold')

            ##### User interface objects
            title_label = CTkLabel (data_editing_menu, font=font1, text='Datos del computador', text_color='#fff')
            title_label.place (x=25, y=5)

            ###### Objects within the frame
            ####### Front row
            idpc_label = CTkLabel (data_editing_menu, font=font2, text='ID:', text_color='#fff')
            idpc_label.place (x=50, y=60)

            idpc_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            idpc_entry.place (x=50, y=90)

            name_label = CTkLabel (data_editing_menu, font=font2, text='Nombre de la marca:', text_color='#fff')
            name_label.place (x=280, y=60)

            namepc = StringVar ()
            options = ['Vit', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Microsoft', 'Google', 'Apple']

            name_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepc, values=options, state='readonly')
            name_options.place (x=280, y=90)

            model_label = CTkLabel (data_editing_menu, font=font2, text='Modelo:', text_color='#fff')
            model_label.place (x=485, y=60)

            model_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            model_entry.place (x=485, y=90)

            serial_label = CTkLabel (data_editing_menu, font=font2, text='Serial:', text_color='#fff')
            serial_label.place (x=680, y=60)

            serial_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            serial_entry.place (x=680, y=90)

            ####### Second row
            color_label = CTkLabel (data_editing_menu, font=font2, text='Color:', text_color='#fff')
            color_label.place (x=50, y=140)

            colorpc = StringVar ()
            options = ['Negro', 'Plata', 'Gris', 'Azul', 'Blanco']

            color_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpc, values=options, state='readonly')
            color_options.place (x=50, y=170)

            modelmb_label = CTkLabel (data_editing_menu, font=font3, text='Modelo de la placa madre:', text_color='#fff')
            modelmb_label.place (x=280, y=140)

            modelmb_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            modelmb_entry.place (x=280, y=170)

            colormb_label = CTkLabel (data_editing_menu, font=font3, text='Color de la placa madre:', text_color='#fff')
            colormb_label.place (x=485, y=140)

            colormbpc = StringVar ()
            options = ['Verde', 'Negro', 'Azul', 'Rojo', 'Blanco']

            colormb_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colormbpc, values=options, state='readonly')
            colormb_options.place (x=485, y=170)

            graphicscardname_label = CTkLabel (data_editing_menu, font=font3, text='Marca de la grafica:', text_color='#fff')
            graphicscardname_label.place (x=680, y=140)

            graphicscardpc = StringVar ()
            options = ['NVIDIA', 'AMD', 'Intel', 'ASUS', 'EVGA', 'MSI', 'Zotac']

            graphicscardname_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=graphicscardpc, values=options, state='readonly')
            graphicscardname_options.place (x=680, y=170)

            ####### Third row
            graphicscardmodel_label = CTkLabel (data_editing_menu, font=font3, text='Modelo de la grafica:', text_color='#fff')
            graphicscardmodel_label.place (x=50, y=220)

            graphicscardmodel_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            graphicscardmodel_entry.place (x=50, y=250)

            cpu_label = CTkLabel (data_editing_menu, font=font2, text='CPU:', text_color='#fff')
            cpu_label.place (x=280, y=220)

            cpu_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            cpu_entry.place (x=280, y=250)

            ram_label = CTkLabel (data_editing_menu, font=font2, text='RAM:', text_color='#fff')
            ram_label.place (x=485, y=220)

            memory = StringVar ()
            options = ['1 GB DDR2', '2 GB DDR2', '4 GB DDR2', '8 GB DDR2', '16 GB DDR2', '32 GB DDR2', '1 GB DDR3', '2 GB DDR3', '4 GB DDR3', '8 GB DDR3', '16 GB DDR3', '32 GB DDR3']

            ram_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=memory, values=options, state='readonly')
            ram_options.place (x=485, y=250)

            HDDorSDD_label = CTkLabel (data_editing_menu, font=font3, text='Unidad de almacenamiento:', text_color='#fff')
            HDDorSDD_label.place (x=680, y=220)

            HDDorSDD_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            HDDorSDD_entry.place (x=680, y=250)

            ####### Fourth row
            win_label = CTkLabel (data_editing_menu, font=font2, text='Sistema operativo:', text_color='#fff')
            win_label.place (x=50, y=300)

            so = StringVar ()
            options = ['Windows 11', 'Windows 10', 'Windows 8', 'Windows 7', 'Windows XP', 'GNU/Linux']

            win_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=so, values=options, state='readonly')
            win_options.place (x=50, y=330)

            department_label = CTkLabel (data_editing_menu, font=font2, text='Departamento:', text_color='#fff')
            department_label.place (x=280, y=300)

            departments = StringVar ()
            options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Presupuesto', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo', 'Despacho', 'Dirección general']

            department_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
            department_options.place (x=280, y=330)

            user_label = CTkLabel (data_editing_menu, font=font2, text='Usuario:', text_color='#fff')
            user_label.place (x=485, y=300)

            user_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            user_entry.place (x=485, y=330)

            stat_label = CTkLabel (data_editing_menu, font=font2, text='Estado:', text_color='#fff')
            stat_label.place (x=680, y=300)

            status = StringVar ()
            options = ['Operativo', 'Inoperativo']

            stat_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
            stat_options.place (x=680, y=330)

            ####### Fifth row
            departuredate_label = CTkLabel (data_editing_menu, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
            departuredate_label.place (x=50, y=380)

            departuredate_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(data_editing_menu.register(validate_numbers_entry), '%S'))
            departuredate_entry.place (x=50, y=410)

            ######## Displays a calendar to facilitate the selection of the date
            ######### Global variable so that the window does not open more than one
            global calendar_window
            calendar_window = False

            def calendar ():
                ######### Specifying the global variable
                global calendar_window

                ######### Conditional that tells me if there is already an open window
                if calendar_window:
                    messagebox.showerror ('Nueva ventana', 'Ya existe una ventana abierta')
                    return

                ######### Create a new window for the calendar
                window_callendary = tk.Toplevel (data_editing_menu)
                window_callendary.title ('Calendario seleccionable')
                calendar_window = True

                ######### Create a calendar widget
                calendar = Calendar (window_callendary, date_pattern='dd-mm-y', selectmode='day')
                calendar.pack (pady=20)

                ######### Function to show the selected date in the Entry of the main window
                def show_calendar_date ():
                    date_selected = calendar.get_date ()
                    departuredate_entry.configure (state='normal')
                    departuredate_entry.delete (0, tk.END)
                    departuredate_entry.insert (0, date_selected)
                    departuredate_entry.configure (state='readonly')

                ######### button to show the selected date
                date_button = tk.Button (window_callendary, text='Mostrar fecha', command=show_calendar_date)
                date_button.pack (pady=10)

                ######### Function to reset the variable, so that you can reopen the window
                def calendar_close ():
                    global calendar_window
                    window_callendary.destroy ()
                    calendar_window = None

                window_callendary.protocol('WM_DELETE_WINDOW', calendar_close)

            calendar_button = CTkButton (data_editing_menu, text='Abrir Calendario', command=calendar)
            calendar_button.place (x=54, y=460)

            ####### Sixth row

            ####### Fifth and sixth row
            observation_label = CTkLabel (data_editing_menu, font=font2, text='Observación:', text_color='#fff')
            observation_label.place (x=485, y=380)

            observation_entry = CTkTextbox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
            observation_entry.place (x=485, y=410)

            ###### The end of the frame objects

            ##### Data verification input
            def check_input ():
                selected = trv.focus ()
                rowid = selected [0]
                idpc = idpc_entry.get ()
                name = namepc.get ()
                model = model_entry.get ()
                serial = serial_entry.get ()
                color = colorpc.get ()
                modelmb = modelmb_entry.get ()
                colormb = colormbpc.get ()
                gcn = graphicscardpc.get ()
                gcm = graphicscardmodel_entry.get ()
                cpu = cpu_entry.get ()
                ram = memory.get ()
                disk = HDDorSDD_entry.get ()
                pcso = so.get ()
                dp = departments.get ()
                user = user_entry.get ()
                stat = status.get ()
                dom = datetime.now().strftime ('%d-%m-%Y')
                dtd = departuredate_entry.get ()
                obs = observation_entry.get ('1.0', 'end-1c')
                if not (idpc and name and model and serial and color and modelmb and colormb and cpu and ram and disk and pcso and dp and stat and dom):
                    messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
                else:
                    Resources.Connection.edit_pc (rowid, idpc, name, model, serial, color, modelmb, colormb, gcn, gcm, cpu, ram, disk, pcso, dp, user, stat, dom, dtd, obs)
                    for item in trv.get_children ():
                        trv.delete (item)
                    find ()
                    data_editing_menu.destroy ()
                    messagebox.showinfo ('Elemento editado correctamente', 'El computador fue editado correctamente')

            ##### Button area
            button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
            button_dem.place (x=300, y=520)

            ##### Returns selected item for editing
            try:
                selected = trv.focus ()
                values = trv.item (selected, 'values')
                idpc_entry.insert (0, values[0])
                name_options.set (values[1])
                model_entry.insert (0, values[2])
                serial_entry.insert (0, values[3])
                color_options.set (values[4])
                modelmb_entry.insert (0, values[5])
                colormb_options.set (values[6])
                graphicscardname_options.set (values[7])
                graphicscardmodel_entry.insert (0, values[8])
                cpu_entry.insert (0, values[9])
                ram_options.set (values[10])
                HDDorSDD_entry.insert (0, values[11])
                win_options.set (values[12])
                departments.set (values[13])
                user_entry.insert (0, values[14])
                stat_options.set (values[15])
                departuredate_entry.insert (0, values[18])
                observation_entry.insert (1.0, values[19])
            except IndexError:
                data_editing_menu.destroy ()
                messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

            ##### Settings to avoid modifying the ID of the registered computing device
            idpc_entry.configure (state='readonly')
            departuredate_entry.configure (state='readonly')

        #### Function to generate a word document about the device status report
        def button_docx ():

            ##### Format of the window interface
            print_data_menu = customtkinter.CTkToplevel ()
            print_data_menu.after(250, lambda:  print_data_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            print_data_menu.title ('Menu para generar el oficio')
            print_data_menu.geometry ('500x550')
            print_data_menu.resizable (False, False)

            ###### Configuring the grid to center
            for i in range (10):
                print_data_menu.grid_rowconfigure (i, weight=1)
            print_data_menu.grid_columnconfigure (0, weight=1)
            print_data_menu.grid_columnconfigure (1, weight=1)

            ##### Fonts for the letters
            font2 = ('Roboto', 18, 'bold')

            ##### Specifying the global variables
            global addressed_to_entry
            global by_entry
            global subject_entry
            global namepc, model, serial, mb, cpu, ram, disk
            global observation_docx_entry
            global item_values

            ##### Boxes to write to whom the letter is addressed and who sends it
            addressed_to_label = CTkLabel (print_data_menu, font=font2, text='Dirigido a:', text_color='#fff')
            addressed_to_label.grid (row=0, column=0)

            addressed_to_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            addressed_to_entry.grid (row=1, column=0, pady=2, ipady=4)

            by_label = CTkLabel (print_data_menu, font=font2, text='Por:', text_color='#fff')
            by_label.grid (row=2, column=0)

            by_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            by_entry.grid (row=3, column=0, pady=2, ipady=4)

            ##### Box to write the reason for the letter
            subject_label = CTkLabel (print_data_menu, font=font2, text='Asunto:', text_color='#fff')
            subject_label.grid (row=4, column=0, columnspan=2)

            subject_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            subject_entry.grid (row=5, column=0, columnspan=2, pady=2, ipady=4)

            ##### Frame of the checkboxes
            checkbox_frame = CTkFrame (print_data_menu)
            checkbox_frame.grid (row=0, column=1, rowspan=4)

            ##### Status of the checkboxes
            namepc = IntVar (value=1)
            model = IntVar (value=1)
            serial = IntVar (value=1)
            mb = IntVar (value=0)
            cpu = IntVar (value=0)
            ram = IntVar (value=0)
            disk = IntVar (value=0)

            ##### Checkboxes to say include more data
            Include_data_label = CTkLabel (checkbox_frame, font=font2, text='Incluir datos:', text_color='#fff')
            Include_data_label.grid (row=0, column=0, pady=(0,10), columnspan=2)

            CTkCheckBox (checkbox_frame, text='Incluir Nombre', variable=namepc).grid (row=1, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Modelo', variable=model).grid (row=2, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Serial', variable=serial).grid (row=3, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Placa madre', variable=mb).grid (row=4, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir CPU', variable=cpu).grid (row=1, column=1, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir RAM', variable=ram).grid (row=2, column=1, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Disco', variable=disk).grid (row=3, column=1, pady=6, padx=5, sticky='w')

            ##### Box to write the observations to be reported
            observation_docx_label = CTkLabel (print_data_menu, font=font2, text='Reporte:', text_color='#fff')
            observation_docx_label.grid (row=6, column=0, columnspan=2)

            observation_docx_entry = CTkTextbox (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=250, height=150, corner_radius=10, wrap=WORD)
            observation_docx_entry.grid (row=7, column=0, columnspan=2, pady=5)

            ##### Conditional so that when an element is chosen it allows to open the window or not, in addition to saving the element's data to use
            selected_item = trv.selection ()
            if not selected_item:
                print_data_menu.destroy ()
                messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para generar un oficio')
                return

            ##### Gets the values of the selected register
            item_values = trv.item (selected_item[0], 'values')

            ##### Button to confirm and generate the document
            button_confirm = CTkButton (print_data_menu, font=font2, text='Generar oficio', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=lambda: Resources.Connection.docx_pc (print_data_menu, addressed_to_entry, by_entry, subject_entry, namepc, model, serial, mb, cpu, ram, disk, observation_docx_entry, item_values))
            button_confirm.grid (row=8, column=0, columnspan=2, padx=(0, 60),  pady=5)

            button_confirm_pv = CTkButton (print_data_menu, font=font2, text='Vista Previa', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=lambda: Resources.Previewpc.convertir_a_pdf (addressed_to_entry, by_entry, subject_entry, namepc, model, serial, mb, cpu, ram, disk, observation_docx_entry, item_values))
            button_confirm_pv.grid (row=8, column=1, columnspan=2, padx=(60, 0),  pady=5)

        #### Function to display a statistical graph on the operability of computer goods
        def graph_pc ():
            Resources.Connection.graph_pc ()

        #### Button area
        button_docx = CTkButton (main_frame, font=font1, text='Generar oficio', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_docx)
        button_docx.grid (row=3, column=0, columnspan=2, pady=10, padx=(136, 0), sticky='w')

        #### Button area
        button_del = CTkButton (main_frame, font=font1, text='Borrar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
        button_del.grid (row=3, column=0, columnspan=2, pady=10, padx=(300, 0), sticky='w')

        button_edi = CTkButton (main_frame, font=font1, text='Editar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
        button_edi.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 300), sticky='e')

        button_graph = CTkButton (main_frame, font=font1, text='Estadisticas', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=graph_pc)
        button_graph.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 150), sticky='e')

        #### Function to display the data automatically after opening the window
        button_search ['command'] = find

        find ()

    ### Keyboards data window
    def pk_page ():

        #### The window that is open is saved in the variable
        global current_page
        current_page = 'pk_page'

        #### Search function within the database to get data from keyboards
        def find ():

            ##### Clear treeview
            for item in trv.get_children ():
                trv.delete (item)
            global count
            count = 0
            val = entry_search.get ()
            stat = status.get ()
            dp = departments.get ()
            Resources.Connection.search_pk (val, stat, dp)
            PK = Resources.Connection.cur.fetchall ()
            for row in PK:
                ###### Format so that the divisions of the data can be created within the table
                if count % 2 == 0:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
                else:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
                count += 1

        #### Fonts for the letters
        font1 = ('Roboto', 18, 'bold')

        #### Variable to display the text in the window
        area = "Teclados"
        title_label_area["text"] = area

        #### Search button
        button_search = CTkButton (maindataview, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
        button_search.place (x=540, y=10)

        #### Table where the data that is being searched will be displayed
        trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

        trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

        ##### Defines the columns of the table, all equally and automatically
        for col in range (1, 13):
            trv.column (col, stretch=NO, anchor=tk.CENTER)

        trv.heading (1, text='ID', anchor=tk.CENTER)
        trv.heading (2, text='Nombre', anchor=tk.CENTER)
        trv.heading (3, text='Modelo', anchor=tk.CENTER)
        trv.heading (4, text='Serial', anchor=tk.CENTER)
        trv.heading (5, text='Color', anchor=tk.CENTER)
        trv.heading (6, text='Departamentos', anchor=tk.CENTER)
        trv.heading (7, text='Usuarios', anchor=tk.CENTER)
        trv.heading (8, text='Estado', anchor=tk.CENTER)
        trv.heading (9, text='Fecha de ingreso a la entidad', anchor=tk.CENTER)
        trv.heading (10, text='Fecha de modificación', anchor=tk.CENTER)
        trv.heading (11, text='Fecha de salida de la entidad', anchor=tk.CENTER)
        trv.heading (12, text='Observaciones', anchor=tk.CENTER)

        ##### Format that creates the divisions within the table
        trv.tag_configure ('oddrow', background='#4a5052')
        trv.tag_configure ('evenrow', background='#2a2d2e')

        #### Format to move the data table both horizontally and vertically
        scrollbarx = ttk.Scrollbar (main_frame, orient=HORIZONTAL, command=trv.xview)
        trv.configure (xscroll=scrollbarx.set)
        trv.configure (selectmode='extended')
        scrollbarx.grid (row=1, column=0,  columnspan=2, sticky='ew')

        scrollbary = ttk.Scrollbar (main_frame, orient=VERTICAL, command=trv.yview)
        trv.configure (yscroll=scrollbary.set)
        trv.configure (selectmode='extended')
        scrollbary.grid (row=0, column=1,  columnspan=2, sticky='ns')

        trv.grid (row=0, column=0,  columnspan=2, padx=(0, 16), pady=(0, 1), sticky='nsew')

        #### Setting so that the objects are centered
        main_frame.grid_rowconfigure (0, weight=1)
        main_frame.grid_columnconfigure (0, weight=1)

        #### Function of deleting data
        def button_del ():
            selected = trv.selection ()
            if selected:
                rowid = selected [0]
                Resources.Connection.del_pk (rowid)
                trv.delete (rowid)
            else:
                messagebox.showerror('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

        #### Function to edit data
        def button_dem ():

            ##### Format of the window interface
            data_editing_menu = customtkinter.CTkToplevel ()
            data_editing_menu.after(250, lambda:  data_editing_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            data_editing_menu.title ('Menu de edición de datos del teclado')
            data_editing_menu.geometry ('960x600')
            data_editing_menu.resizable (False, False)

            ##### Validates if they are only numbers and dashes
            def validate_numbers_entry (char):
                if char == '' or all (c.isdigit() or c == '-' for c in char):
                    return True
                else:
                    return False

            ##### Fonts for the letters
            font1 = ('Roboto', 30, 'bold')
            font2 = ('Roboto', 18, 'bold')
            font3 = ('Roboto', 16, 'bold')

            ##### User interface objects
            title_label = CTkLabel (data_editing_menu, font=font1, text='Datos del teclado', text_color='#fff')
            title_label.place (x=25, y=5)

            ###### Objects within the frame
            ####### Front row
            idpk_label = CTkLabel (data_editing_menu, font=font2, text='ID:', text_color='#fff')
            idpk_label.place (x=50, y=60)

            idpk_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            idpk_entry.place (x=50, y=90)

            name_label = CTkLabel (data_editing_menu, font=font2, text='Nombre de la marca:', text_color='#fff')
            name_label.place (x=280, y=60)

            namepk = StringVar ()
            options = ['Vit', 'Dell', 'Logitech', 'Corsair']

            name_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepk, values=options, state='readonly')
            name_options.place (x=280, y=90)

            model_label = CTkLabel (data_editing_menu, font=font2, text='Modelo:', text_color='#fff')
            model_label.place (x=485, y=60)

            model_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            model_entry.place (x=485, y=90)

            serial_label = CTkLabel (data_editing_menu, font=font2, text='Serial:', text_color='#fff')
            serial_label.place (x=680, y=60)

            serial_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            serial_entry.place (x=680, y=90)

            ####### Second row
            color_label = CTkLabel (data_editing_menu, font=font2, text='Color:', text_color='#fff')
            color_label.place (x=50, y=140)

            colorpk = StringVar ()
            options = ['Negro', 'Plata', 'Gris', 'Blanco', 'Verde', 'Amarillo', 'Rojo']

            color_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpk, values=options, state='readonly')
            color_options.place (x=50, y=170)

            department_label = CTkLabel (data_editing_menu, font=font2, text='Departamento:', text_color='#fff')
            department_label.place (x=280, y=140)

            departments = StringVar ()
            options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Presupuesto', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo', 'Despacho', 'Dirección general']

            department_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
            department_options.place (x=280, y=170)

            user_label = CTkLabel (data_editing_menu, font=font2, text='Usuario:', text_color='#fff')
            user_label.place (x=485, y=140)

            user_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            user_entry.place (x=485, y=170)

            stat_label = CTkLabel (data_editing_menu, font=font2, text='Estado:', text_color='#fff')
            stat_label.place (x=680, y=140)

            status = StringVar ()
            options = ['Operativo', 'Inoperativo']

            stat_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
            stat_options.place (x=680, y=170)

            ####### Third row
            departuredate_label = CTkLabel (data_editing_menu, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
            departuredate_label.place (x=50, y=220)

            departuredate_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(data_editing_menu.register(validate_numbers_entry), '%S'))
            departuredate_entry.place (x=50, y=250)

            ######## Displays a calendar to facilitate the selection of the date
            ######### Global variable so that the window does not open more than one
            global calendar_window
            calendar_window = False

            def calendar ():
                ######### Specifying the global variable
                global calendar_window

                ######### Conditional that tells me if there is already an open window
                if calendar_window:
                    messagebox.showerror ('Nueva ventana', 'Ya existe una ventana abierta')
                    return

                ######### Create a new window for the calendar
                window_callendary = tk.Toplevel (data_editing_menu)
                window_callendary.title ('Calendario seleccionable')
                calendar_window = True

                ######### Create a calendar widget
                calendar = Calendar (window_callendary, date_pattern='dd-mm-y', selectmode='day')
                calendar.pack (pady=20)

                ######### Function to show the selected date in the Entry of the main window
                def show_calendar_date ():
                    date_selected = calendar.get_date ()
                    departuredate_entry.configure (state='normal')
                    departuredate_entry.delete (0, tk.END)
                    departuredate_entry.insert (0, date_selected)
                    departuredate_entry.configure (state='readonly')

                ######### button to show the selected date
                date_button = tk.Button (window_callendary, text='Mostrar fecha', command=show_calendar_date)
                date_button.pack (pady=10)

                ######### Function to reset the variable, so that you can reopen the window
                def calendar_close ():
                    global calendar_window
                    window_callendary.destroy ()
                    calendar_window = None

                window_callendary.protocol('WM_DELETE_WINDOW', calendar_close)

            calendar_button = CTkButton (data_editing_menu, text='Abrir Calendario', command=calendar)
            calendar_button.place (x=54, y=300)

            ####### Fourth row

            ####### Fifth row

            ####### Sixth row

            ####### Fifth and sixth row
            observation_label = CTkLabel (data_editing_menu, font=font2, text='Observación:', text_color='#fff')
            observation_label.place (x=485, y=380)

            observation_entry = CTkTextbox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
            observation_entry.place (x=485, y=410)

            ###### The end of the frame objects

            ##### Data verification input
            def check_input ():
                selected = trv.focus ()
                rowid = selected [0]
                idpk = idpk_entry.get ()
                name = namepk.get ()
                model = model_entry.get ()
                serial = serial_entry.get ()
                color = colorpk.get ()
                dp = departments.get ()
                user = user_entry.get ()
                stat = status.get ()
                dom = datetime.now().strftime ('%d-%m-%Y')
                dtd = departuredate_entry.get ()
                obs = observation_entry.get ('1.0', 'end-1c')
                if not (idpk and name and model and serial and color and dp and stat and dom):
                    messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
                else:
                    Resources.Connection.edit_pk (rowid, idpk, name, model, serial, color, dp, user, stat, dom, dtd, obs)
                    for item in trv.get_children ():
                        trv.delete (item)
                    find ()
                    data_editing_menu.destroy ()
                    messagebox.showinfo ('Elemento editado correctamente', 'El teclado fue editado correctamente')

            ##### Button area
            button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
            button_dem.place (x=300, y=520)

            ##### Returns selected item for editing
            try:
                selected = trv.focus ()
                values = trv.item (selected, 'values')
                idpk_entry.insert (0, values[0])
                name_options.set (values[1])
                model_entry.insert (0, values[2])
                serial_entry.insert (0, values[3])
                color_options.set (values[4])
                department_options.set (values[5])
                user_entry.insert (0, values[6])
                stat_options.set (values[7])
                departuredate_entry.insert (0, values[10])
                observation_entry.insert (1.0, values[11])
            except IndexError:
                data_editing_menu.destroy ()
                messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

            ##### Settings to avoid modifying the ID of the registered computing device
            idpk_entry.configure (state='readonly')
            departuredate_entry.configure (state='readonly')

        #### Function to generate a word document about the device status report
        def button_docx ():

            ##### Format of the window interface
            print_data_menu = customtkinter.CTkToplevel ()
            print_data_menu.after(250, lambda:  print_data_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            print_data_menu.title ('Menu para generar el oficio')
            print_data_menu.geometry ('500x550')
            print_data_menu.resizable (False, False)

            ###### Configuring the grid to center
            for i in range (10):
                print_data_menu.grid_rowconfigure (i, weight=1)
            print_data_menu.grid_columnconfigure (0, weight=1)
            print_data_menu.grid_columnconfigure (1, weight=1)

            ##### Fonts for the letters
            font2 = ('Roboto', 18, 'bold')

            ##### Specifying the global variables
            global addressed_to_entry
            global by_entry
            global subject_entry
            global namepk, model, serial
            global observation_docx_entry
            global item_values

            ##### Boxes to write to whom the letter is addressed and who sends it
            addressed_to_label = CTkLabel (print_data_menu, font=font2, text='Dirigido a:', text_color='#fff')
            addressed_to_label.grid (row=0, column=0)

            addressed_to_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            addressed_to_entry.grid (row=1, column=0, pady=2, ipady=4)

            by_label = CTkLabel (print_data_menu, font=font2, text='Por:', text_color='#fff')
            by_label.grid (row=2, column=0)

            by_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            by_entry.grid (row=3, column=0, pady=2, ipady=4)

            ##### Box to write the reason for the letter
            subject_label = CTkLabel (print_data_menu, font=font2, text='Asunto:', text_color='#fff')
            subject_label.grid (row=4, column=0, columnspan=2)

            subject_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            subject_entry.grid (row=5, column=0, columnspan=2, pady=2, ipady=4)

            ##### Frame of the checkboxes
            checkbox_frame = CTkFrame (print_data_menu)
            checkbox_frame.grid (row=0, column=1, rowspan=4)

            ##### Status of the checkboxes
            namepk = IntVar (value=1)
            model = IntVar (value=1)
            serial = IntVar (value=1)

            ##### Checkboxes to say include more data
            Include_data_label = CTkLabel (checkbox_frame, font=font2, text='Incluir datos:', text_color='#fff')
            Include_data_label.grid (row=0, column=0, pady=(0,10), columnspan=2)

            CTkCheckBox (checkbox_frame, text='Incluir Nombre', variable=namepk).grid (row=1, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Modelo', variable=model).grid (row=2, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Serial', variable=serial).grid (row=1, column=1, pady=6, padx=5, sticky='w')

            ##### Box to write the observations to be reported
            observation_docx_label = CTkLabel (print_data_menu, font=font2, text='Reporte:', text_color='#fff')
            observation_docx_label.grid (row=6, column=0, columnspan=2)

            observation_docx_entry = CTkTextbox (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=250, height=150, corner_radius=10, wrap=WORD)
            observation_docx_entry.grid (row=7, column=0, columnspan=2, pady=5)

            ##### Conditional so that when an element is chosen it allows to open the window or not, in addition to saving the element's data to use
            selected_item = trv.selection ()
            if not selected_item:
                print_data_menu.destroy ()
                messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para generar un oficio')
                return

            ##### Gets the values of the selected register
            item_values = trv.item (selected_item[0], 'values')

            ##### Button to confirm and generate the document
            button_confirm = CTkButton (print_data_menu, font=font2, text='Generar oficio', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=lambda: Resources.Connection.docx_pk (print_data_menu, addressed_to_entry, by_entry, subject_entry, namepk, model, serial, observation_docx_entry, item_values))
            button_confirm.grid (row=8, column=0, columnspan=2,  padx=(0, 60),  pady=5)

            button_confirm_pv = CTkButton (print_data_menu, font=font2, text='Vista Previa', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=lambda: Resources.Previewpk.convertir_a_pdf (addressed_to_entry, by_entry, subject_entry, namepk, model, serial, observation_docx_entry, item_values))
            button_confirm_pv.grid (row=8, column=1, columnspan=2, padx=(60, 0),  pady=5)

        #### Function to display a statistical graph on the operability of computer goods
        def graph_pk ():
            Resources.Connection.graph_pk ()

        #### Button area
        button_docx = CTkButton (main_frame, font=font1, text='Generar oficio', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_docx)
        button_docx.grid (row=3, column=0, columnspan=2, pady=10, padx=(136, 0), sticky='w')

        #### Button area
        button_del = CTkButton (main_frame, font=font1, text='Borrar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
        button_del.grid (row=3, column=0, columnspan=2, pady=10, padx=(300, 0), sticky='w')

        button_edi = CTkButton (main_frame, font=font1, text='Editar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
        button_edi.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 300), sticky='e')

        button_graph = CTkButton (main_frame, font=font1, text='Estadisticas', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=graph_pk)
        button_graph.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 150), sticky='e')

        #### Function to display the data automatically after opening the window
        button_search ['command'] = find

        find ()

    ### Monitors data window
    def pm_page ():

        #### The window that is open is saved in the variable
        global current_page
        current_page = 'pm_page'

        #### Search function within the database to get data from the monitors
        def find ():

            ##### Clear treeview
            for item in trv.get_children ():
                trv.delete (item)
            global count
            count = 0
            val = entry_search.get ()
            stat = status.get ()
            dp = departments.get ()
            Resources.Connection.search_pm (val, stat, dp)
            PM = Resources.Connection.cur.fetchall ()
            for row in PM:
                ###### Format so that the divisions of the data can be created within the table
                if count % 2 == 0:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
                else:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
                count += 1

        #### Fonts for the letters
        font1 = ('Roboto', 18, 'bold')

        #### Variable to display the text in the window
        area = "Monitores"
        title_label_area["text"] = area

        #### Search button
        button_search = CTkButton (maindataview, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
        button_search.place (x=540, y=10)

        #### Table where the data that is being searched will be displayed
        trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

        trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))

        ##### Defines the columns of the table, all equally and automatically
        for col in range (1, 15):
            trv.column (col, stretch=NO, anchor=tk.CENTER)

        trv.heading (1, text='ID', anchor=tk.CENTER)
        trv.heading (2, text='Nombre', anchor=tk.CENTER)
        trv.heading (3, text='Modelo', anchor=tk.CENTER)
        trv.heading (4, text='Serial', anchor=tk.CENTER)
        trv.heading (5, text='Color', anchor=tk.CENTER)
        trv.heading (6, text='Tamaño de la pantalla', anchor=tk.CENTER)
        trv.heading (7, text='Tipo de contector de la pantalla', anchor=tk.CENTER)
        trv.heading (8, text='Departamentos', anchor=tk.CENTER)
        trv.heading (9, text='Usuarios', anchor=tk.CENTER)
        trv.heading (10, text='Estado', anchor=tk.CENTER)
        trv.heading (11, text='Fecha de ingreso a la entidad', anchor=tk.CENTER)
        trv.heading (12, text='Fecha de modificación', anchor=tk.CENTER)
        trv.heading (13, text='Fecha de salida de la entidad', anchor=tk.CENTER)
        trv.heading (14, text='Observaciones', anchor=tk.CENTER)

        ##### Format that creates the divisions within the table
        trv.tag_configure ('oddrow', background= '#4a5052')
        trv.tag_configure ('evenrow', background= '#2a2d2e')

        #### Format to move the data table both horizontally and vertically
        scrollbarx = ttk.Scrollbar (main_frame, orient=HORIZONTAL, command=trv.xview)
        trv.configure (xscroll=scrollbarx.set)
        trv.configure (selectmode='extended')
        scrollbarx.grid (row=1, column=0,  columnspan=2, sticky='ew')

        scrollbary = ttk.Scrollbar (main_frame, orient=VERTICAL, command=trv.yview)
        trv.configure (yscroll=scrollbary.set)
        trv.configure (selectmode='extended')
        scrollbary.grid (row=0, column=1,  columnspan=2, sticky='ns')

        trv.grid (row=0, column=0,  columnspan=2, padx=(0, 16), pady=(0, 1), sticky='nsew')

        #### Setting so that the objects are centered
        main_frame.grid_rowconfigure (0, weight=1)
        main_frame.grid_columnconfigure (0, weight=1)

        #### Function to delete users
        def button_del ():
            selected = trv.selection ()
            if selected:
                rowid = selected [0]
                Resources.Connection.del_pm (rowid)
                trv.delete (rowid)
            else:
                messagebox.showerror('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

        #### Function to edit users
        def button_dem ():

            ##### Format of the window interface
            data_editing_menu = customtkinter.CTkToplevel ()
            data_editing_menu.after(250, lambda:  data_editing_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            data_editing_menu.title ('Menu de edición de datos del monitor')
            data_editing_menu.geometry ('960x600')
            data_editing_menu.resizable (False, False)

            ##### Validates if they are only numbers and dashes
            def validate_numbers_entry (char):
                if char == '' or all (c.isdigit() or c == '-' for c in char):
                    return True
                else:
                    return False

            ##### Fonts for the letters
            font1 = ('Roboto', 30, 'bold')
            font2 = ('Roboto', 18, 'bold')
            font3 = ('Roboto', 16, 'bold')

            ##### User interface objects
            title_label = CTkLabel (data_editing_menu, font=font1, text='Datos del monitor', text_color='#fff')
            title_label.place (x=25, y=5)

            ###### Objects within the frame
            ####### Front row
            idpm_label = CTkLabel (data_editing_menu, font=font2, text='ID:', text_color='#fff')
            idpm_label.place (x=50, y=60)

            idpm_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            idpm_entry.place (x=50, y=90)

            name_label = CTkLabel (data_editing_menu, font=font2, text='Nombre de la marca:', text_color='#fff')
            name_label.place (x=280, y=60)

            namepm = StringVar ()
            options = ['Vit', 'Dell', 'Samsung', 'Asus', 'LG', 'Acer', 'Dahua', 'BenQ', 'HP']

            name_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepm, values=options, state='readonly')
            name_options.place (x=280, y=90)

            model_label = CTkLabel (data_editing_menu, font=font2, text='Modelo:', text_color='#fff')
            model_label.place (x=485, y=60)

            model_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            model_entry.place (x=485, y=90)

            serial_label = CTkLabel (data_editing_menu, font=font2, text='Serial:', text_color='#fff')
            serial_label.place (x=680, y=60)

            serial_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            serial_entry.place (x=680, y=90)

            ####### Second row
            color_label = CTkLabel (data_editing_menu, font=font2, text='Color:', text_color='#fff')
            color_label.place (x=50, y=140)

            colorpm = StringVar ()
            options = ['Negro', 'Plata', 'Gris', 'Blanco']

            color_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpm, values=options, state='readonly')
            color_options.place (x=50, y=170)

            typescreen_label = CTkLabel (data_editing_menu, font=font2, text='Tipo de pantalla:', text_color='#fff')
            typescreen_label.place (x=280, y=140)

            typescreeninch = StringVar ()
            options = ['18 pulgadas', '19 pulgadas', '22 pulgadas', '24 pulgadas', '28 pulgadas', '32 pulgadas', '40 pulgadas', '42 pulgadas', '43 pulgadas', '48 pulgadas', '49 pulgadas', '50 pulgadas', '55 pulgadas', '60 pulgadas', '65 pulgadas', '70 pulgadas', '75 pulgadas', '77 pulgadas', '85 pulgadas']

            typescreen_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=typescreeninch, values=options, state='readonly')
            typescreen_options.place (x=280, y=170)

            typeconnector_label = CTkLabel (data_editing_menu, font=font2, text='Tipo de conector:', text_color='#fff')
            typeconnector_label.place (x=485, y=140)

            typeconnectorport = StringVar ()
            options = ['VGA', 'HDMI', 'DisplayPort', 'DVI']

            typeconnector_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=typeconnectorport, values=options, state='readonly')
            typeconnector_options.place (x=485, y=170)

            department_label = CTkLabel (data_editing_menu, font=font2, text='Departamento:', text_color='#fff')
            department_label.place (x=680, y=140)

            departments = StringVar ()
            options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Presupuesto', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo', 'Despacho', 'Dirección general']

            department_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
            department_options.place (x=680, y=170)

            ####### Third row
            user_label = CTkLabel (data_editing_menu, font=font2, text='Usuario:', text_color='#fff')
            user_label.place (x=50, y=220)

            user_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            user_entry.place (x=50, y=250)

            stat_label = CTkLabel (data_editing_menu, font=font2, text='Estado:', text_color='#fff')
            stat_label.place (x=280, y=220)

            status = StringVar ()
            options = ['Operativo', 'Inoperativo']

            stat_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
            stat_options.place (x=280, y=250)

            ####### Fourth row
            departuredate_label = CTkLabel (data_editing_menu, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
            departuredate_label.place (x=50, y=300)

            departuredate_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(data_editing_menu.register(validate_numbers_entry), '%S'))
            departuredate_entry.place (x=50, y=330)

            ######## Displays a calendar to facilitate the selection of the date
            ######### Global variable so that the window does not open more than one
            global calendar_window
            calendar_window = False

            def calendar ():
                ######### Specifying the global variable
                global calendar_window

                ######### Conditional that tells me if there is already an open window
                if calendar_window:
                    messagebox.showerror ('Nueva ventana', 'Ya existe una ventana abierta')
                    return

                ######### Create a new window for the calendar
                window_callendary = tk.Toplevel (data_editing_menu)
                window_callendary.title ('Calendario seleccionable')
                calendar_window = True

                ######### Create a calendar widget
                calendar = Calendar (window_callendary, date_pattern='dd-mm-y', selectmode='day')
                calendar.pack (pady=20)

                ######### Function to show the selected date in the Entry of the main window
                def show_calendar_date ():
                    date_selected = calendar.get_date ()
                    departuredate_entry.configure (state='normal')
                    departuredate_entry.delete (0, tk.END)
                    departuredate_entry.insert (0, date_selected)
                    departuredate_entry.configure (state='readonly')

                ######### button to show the selected date
                date_button = tk.Button (window_callendary, text='Mostrar fecha', command=show_calendar_date)
                date_button.pack (pady=10)

                ######### Function to reset the variable, so that you can reopen the window
                def calendar_close ():
                    global calendar_window
                    window_callendary.destroy ()
                    calendar_window = None

                window_callendary.protocol('WM_DELETE_WINDOW', calendar_close)

            calendar_button = CTkButton (data_editing_menu, text='Abrir Calendario', command=calendar)
            calendar_button.place (x=54, y=380)

            ####### Fifth row

            ####### Sixth row

            ####### Fifth and sixth row
            observation_label = CTkLabel (data_editing_menu, font=font2, text='Observación:', text_color='#fff')
            observation_label.place (x=485, y=380)

            observation_entry = CTkTextbox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
            observation_entry.place (x=485, y=410)

            ###### The end of the frame objects

            ##### Data verification input
            def check_input ():
                selected = trv.focus ()
                rowid = selected [0]
                idpm = idpm_entry.get ()
                name = namepm.get ()
                model = model_entry.get ()
                serial = serial_entry.get ()
                color = colorpm.get ()
                tsi = typescreeninch.get ()
                tcp = typeconnectorport.get ()
                dp = departments.get ()
                user = user_entry.get ()
                stat = status.get ()
                dom = datetime.now().strftime ('%d-%m-%Y')
                dtd = departuredate_entry.get ()
                obs = observation_entry.get ('1.0', 'end-1c')
                if not (idpm and name and model and serial and color and tsi and tcp and dp and stat and dom):
                    messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
                else:
                    Resources.Connection.edit_pm (rowid, idpm, name, model, serial, color, tsi, tcp, dp, user, stat, dom, dtd, obs)
                    for item in trv.get_children ():
                        trv.delete (item)
                    find ()
                    data_editing_menu.destroy ()
                    messagebox.showinfo ('Elemento editado correctamente', 'El usuario fue editado correctamente')

            ##### Button area
            button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
            button_dem.place (x=300, y=520)

            ##### Returns selected item for editing
            try:
                selected = trv.focus ()
                values = trv.item (selected, 'values')
                idpm_entry.insert (0, values[0])
                name_options.set (values[1])
                model_entry.insert (0, values[2])
                serial_entry.insert (0, values[3])
                color_options.set (values[4])
                typescreen_options.set (values[5])
                typeconnector_options.set (values[6])
                department_options.set (values[7])
                user_entry.insert (0, values[8])
                stat_options.set (values[9])
                departuredate_entry.insert (0, values[12])
                observation_entry.insert (1.0, values[13])
            except IndexError:
                data_editing_menu.destroy ()
                messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

            ##### Settings to avoid modifying the ID of the registered computing device
            idpm_entry.configure (state='readonly')
            departuredate_entry.configure (state='readonly')

        #### Function to generate a word document about the device status report
        def button_docx ():

            ##### Format of the window interface
            print_data_menu = customtkinter.CTkToplevel ()
            print_data_menu.after(250, lambda:  print_data_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            print_data_menu.title ('Menu para generar el oficio')
            print_data_menu.geometry ('500x550')
            print_data_menu.resizable (False, False)

            ###### Configuring the grid to center
            for i in range (10):
                print_data_menu.grid_rowconfigure (i, weight=1)
            print_data_menu.grid_columnconfigure (0, weight=1)
            print_data_menu.grid_columnconfigure (1, weight=1)

            ##### Fonts for the letters
            font2 = ('Roboto', 18, 'bold')

            ##### Specifying the global variables
            global addressed_to_entry
            global by_entry
            global subject_entry
            global namepm, model, serial
            global observation_docx_entry
            global item_values

            ##### Boxes to write to whom the letter is addressed and who sends it
            addressed_to_label = CTkLabel (print_data_menu, font=font2, text='Dirigido a:', text_color='#fff')
            addressed_to_label.grid (row=0, column=0)

            addressed_to_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            addressed_to_entry.grid (row=1, column=0, pady=2, ipady=4)

            by_label = CTkLabel (print_data_menu, font=font2, text='Por:', text_color='#fff')
            by_label.grid (row=2, column=0)

            by_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            by_entry.grid (row=3, column=0, pady=2, ipady=4)

            ##### Box to write the reason for the letter
            subject_label = CTkLabel (print_data_menu, font=font2, text='Asunto:', text_color='#fff')
            subject_label.grid (row=4, column=0, columnspan=2)

            subject_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            subject_entry.grid (row=5, column=0, columnspan=2, pady=2, ipady=4)

            ##### Frame of the checkboxes
            checkbox_frame = CTkFrame (print_data_menu)
            checkbox_frame.grid (row=0, column=1, rowspan=4)

            ##### Status of the checkboxes
            namepm = IntVar (value=1)
            model = IntVar (value=1)
            serial = IntVar (value=1)

            ##### Checkboxes to say include more data
            Include_data_label = CTkLabel (checkbox_frame, font=font2, text='Incluir datos:', text_color='#fff')
            Include_data_label.grid (row=0, column=0, pady=(0,10), columnspan=2)

            CTkCheckBox (checkbox_frame, text='Incluir Nombre', variable=namepm).grid (row=1, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Modelo', variable=model).grid (row=2, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Serial', variable=serial).grid (row=1, column=1, pady=6, padx=5, sticky='w')

            ##### Box to write the observations to be reported
            observation_docx_label = CTkLabel (print_data_menu, font=font2, text='Reporte:', text_color='#fff')
            observation_docx_label.grid (row=6, column=0, columnspan=2)

            observation_docx_entry = CTkTextbox (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=250, height=150, corner_radius=10, wrap=WORD)
            observation_docx_entry.grid (row=7, column=0, columnspan=2, pady=5)

            ##### Conditional so that when an element is chosen it allows to open the window or not, in addition to saving the element's data to use
            selected_item = trv.selection ()
            if not selected_item:
                print_data_menu.destroy ()
                messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para generar un oficio')
                return

            ##### Gets the values of the selected register
            item_values = trv.item (selected_item[0], 'values')

            ##### Button to confirm and generate the document
            button_confirm = CTkButton (print_data_menu, font=font2, text='Generar oficio', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=lambda: Resources.Connection.docx_pm (print_data_menu, addressed_to_entry, by_entry, subject_entry, namepm, model, serial, observation_docx_entry, item_values))
            button_confirm.grid (row=8, column=0, columnspan=2, padx=(0, 60),  pady=5)
            
            button_confirm_pv = CTkButton (print_data_menu, font=font2, text='Vista Previa', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=lambda: Resources.Previewpm.convertir_a_pdf (addressed_to_entry, by_entry, subject_entry, namepm, model, serial, observation_docx_entry, item_values))
            button_confirm_pv.grid (row=8, column=1, columnspan=2, padx=(60, 0),  pady=5)

        #### Function to display a statistical graph on the operability of computer goods
        def graph_pm ():
            Resources.Connection.graph_pm ()

        #### Button area
        button_docx = CTkButton (main_frame, font=font1, text='Generar oficio', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_docx)
        button_docx.grid (row=3, column=0, columnspan=2, pady=10, padx=(136, 0), sticky='w')

        #### Button area
        button_del = CTkButton (main_frame, font=font1, text='Borrar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
        button_del.grid (row=3, column=0, columnspan=2, pady=10, padx=(300, 0), sticky='w')

        button_edi = CTkButton (main_frame, font=font1, text='Editar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
        button_edi.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 300), sticky='e')

        button_graph = CTkButton (main_frame, font=font1, text='Estadisticas', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=graph_pm)
        button_graph.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 150), sticky='e')

        #### Function to display the data automatically after opening the window
        button_search ['command'] = find

        find ()

    ### Mouses data window
    def pmo_page ():

        #### The window that is open is saved in the variable
        global current_page
        current_page = 'pmo_page'

        #### Search function within the database for obtaining data from mouses
        def find ():

            ##### Clear treeview
            for item in trv.get_children ():
                trv.delete (item)
            global count
            count = 0
            val = entry_search.get ()
            stat = status.get ()
            dp = departments.get ()
            Resources.Connection.search_pmo (val, stat, dp)
            PMO = Resources.Connection.cur.fetchall ()
            for row in PMO:
                ###### Format so that the divisions of the data can be created within the table
                if count % 2 == 0:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
                else:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
                count += 1

        #### Fonts for the letters
        font1 = ('Roboto', 18, 'bold')

        #### Variable to display the text in the window
        area = 'Mouses'
        title_label_area['text'] = area

        #### Search button
        button_search = CTkButton (maindataview, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
        button_search.place (x=540, y=10)

        #### Table where the data that is being searched will be displayed
        trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

        trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

        ##### Defines the columns of the table, all equally and automatically
        for col in range (1, 13):
            trv.column (col, stretch=NO, anchor=tk.CENTER)

        trv.heading (1, text='ID', anchor=tk.CENTER)
        trv.heading (2, text='Nombre', anchor=tk.CENTER)
        trv.heading (3, text='Modelo', anchor=tk.CENTER)
        trv.heading (4, text='Serial', anchor=tk.CENTER)
        trv.heading (5, text='Color', anchor=tk.CENTER)
        trv.heading (6, text='Departamentos', anchor=tk.CENTER)
        trv.heading (7, text='Usuarios', anchor=tk.CENTER)
        trv.heading (8, text='Estado', anchor=tk.CENTER)
        trv.heading (9, text='Fecha de ingreso a la entidad', anchor=tk.CENTER)
        trv.heading (10, text='Fecha de modificación', anchor=tk.CENTER)
        trv.heading (11, text='Fecha de salida de la entidad', anchor=tk.CENTER)
        trv.heading (12, text='Observaciones', anchor=tk.CENTER)

        ##### Format that creates the divisions within the table
        trv.tag_configure ('oddrow', background='#4a5052')
        trv.tag_configure ('evenrow', background='#2a2d2e')

        #### Format to move the data table both horizontally and vertically
        scrollbarx = ttk.Scrollbar (main_frame, orient=HORIZONTAL, command=trv.xview)
        trv.configure (xscroll=scrollbarx.set)
        trv.configure (selectmode='extended')
        scrollbarx.grid (row=1, column=0,  columnspan=2, sticky='ew')

        scrollbary = ttk.Scrollbar (main_frame, orient=VERTICAL, command=trv.yview)
        trv.configure (yscroll=scrollbary.set)
        trv.configure (selectmode='extended')
        scrollbary.grid (row=0, column=1,  columnspan=2, sticky='ns')

        trv.grid (row=0, column=0,  columnspan=2, padx=(0, 16), pady=(0, 1), sticky='nsew')

        #### Setting so that the objects are centered
        main_frame.grid_rowconfigure (0, weight=1)
        main_frame.grid_columnconfigure (0, weight=1)

        #### Function to delete users
        def button_del ():
            selected = trv.selection ()
            if selected:
                rowid = selected [0]
                Resources.Connection.del_pmo (rowid)
                trv.delete (rowid)
            else:
                messagebox.showerror('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

        #### Function to edit users
        def button_dem ():

            ##### Format of the window interface
            data_editing_menu = customtkinter.CTkToplevel ()
            data_editing_menu.after(250, lambda:  data_editing_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            data_editing_menu.title ('Menu de edición de datos del mouse')
            data_editing_menu.geometry ('960x600')
            data_editing_menu.resizable (False, False)

            ##### Validates if they are only numbers and dashes
            def validate_numbers_entry (char):
                if char == '' or all (c.isdigit() or c == '-' for c in char):
                    return True
                else:
                    return False

            ##### Fonts for the letters
            font1 = ('Roboto', 30, 'bold')
            font2 = ('Roboto', 18, 'bold')
            font3 = ('Roboto', 16, 'bold')

            ##### User interface objects
            title_label = CTkLabel (data_editing_menu, font=font1, text='Datos del mouse', text_color='#fff')
            title_label.place (x=25, y=5)

            ###### Objects within the frame
            ####### Front row
            idpmo_label = CTkLabel (data_editing_menu, font=font2, text='ID:', text_color='#fff')
            idpmo_label.place (x=50, y=60)

            idpmo_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            idpmo_entry.place (x=50, y=90)

            name_label = CTkLabel (data_editing_menu, font=font2, text='Nombre de la marca:', text_color='#fff')
            name_label.place (x=280, y=60)

            namepmo = StringVar ()
            options = ['Vit', 'Logitech', 'Corsair', 'Genius', 'Argom', 'Lenovo', 'HP']

            name_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepmo, values=options, state='readonly')
            name_options.place (x=280, y=90)

            model_label = CTkLabel (data_editing_menu, font=font2, text='Modelo:', text_color='#fff')
            model_label.place (x=485, y=60)

            model_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            model_entry.place (x=485, y=90)

            serial_label = CTkLabel (data_editing_menu, font=font2, text='Serial:', text_color='#fff')
            serial_label.place (x=680, y=60)

            serial_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            serial_entry.place (x=680, y=90)

            ####### Second row
            color_label = CTkLabel (data_editing_menu, font=font2, text='Color:', text_color='#fff')
            color_label.place (x=50, y=140)

            colorpmo = StringVar ()
            options = ['Negro', 'Plata', 'Gris', 'Blanco']

            color_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpmo, values=options, state='readonly')
            color_options.place (x=50, y=170)

            department_label = CTkLabel (data_editing_menu, font=font2, text='Departamento:', text_color='#fff')
            department_label.place (x=280, y=140)

            departments = StringVar ()
            options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Presupuesto', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo', 'Despacho', 'Dirección general']

            department_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
            department_options.place (x=280, y=170)

            user_label = CTkLabel (data_editing_menu, font=font2, text='Usuario:', text_color='#fff')
            user_label.place (x=485, y=140)

            user_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            user_entry.place (x=485, y=170)

            stat_label = CTkLabel (data_editing_menu, font=font2, text='Estado:', text_color='#fff')
            stat_label.place (x=680, y=140)

            status = StringVar ()
            options = ['Operativo', 'Inoperativo']

            stat_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
            stat_options.place (x=680, y=170)

            ####### Third row
            departuredate_label = CTkLabel (data_editing_menu, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
            departuredate_label.place (x=50, y=220)

            departuredate_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(data_editing_menu.register(validate_numbers_entry), '%S'))
            departuredate_entry.place (x=50, y=250)

            ######## Displays a calendar to facilitate the selection of the date
            ######### Global variable so that the window does not open more than one
            global calendar_window
            calendar_window = False

            def calendar ():
                ######### Specifying the global variable
                global calendar_window

                ######### Conditional that tells me if there is already an open window
                if calendar_window:
                    messagebox.showerror ('Nueva ventana', 'Ya existe una ventana abierta')
                    return

                ######### Create a new window for the calendar
                window_callendary = tk.Toplevel (data_editing_menu)
                window_callendary.title ('Calendario seleccionable')
                calendar_window = True

                ######### Create a calendar widget
                calendar = Calendar (window_callendary, date_pattern='dd-mm-y', selectmode='day')
                calendar.pack (pady=20)

                ######### Function to show the selected date in the Entry of the main window
                def show_calendar_date ():
                    date_selected = calendar.get_date ()
                    departuredate_entry.configure (state='normal')
                    departuredate_entry.delete (0, tk.END)
                    departuredate_entry.insert (0, date_selected)
                    departuredate_entry.configure (state='readonly')

                ######### button to show the selected date
                date_button = tk.Button (window_callendary, text='Mostrar fecha', command=show_calendar_date)
                date_button.pack (pady=10)

                ######### Function to reset the variable, so that you can reopen the window
                def calendar_close ():
                    global calendar_window
                    window_callendary.destroy ()
                    calendar_window = None

                window_callendary.protocol('WM_DELETE_WINDOW', calendar_close)

            calendar_button = CTkButton (data_editing_menu, text='Abrir Calendario', command=calendar)
            calendar_button.place (x=54, y=300)

            ####### Fourth row

            ####### Fifth row

            ####### Sixth row

            ####### Fifth and sixth row
            observation_label = CTkLabel (data_editing_menu, font=font2, text='Observación:', text_color='#fff')
            observation_label.place (x=485, y=380)

            observation_entry = CTkTextbox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
            observation_entry.place (x=485, y=410)

            ###### The end of the frame objects

            ##### Data verification input
            def check_input ():
                selected = trv.focus ()
                rowid = selected [0]
                idpmo = idpmo_entry.get ()
                name = namepmo.get ()
                model = model_entry.get ()
                serial = serial_entry.get ()
                color = colorpmo.get ()
                dp = departments.get ()
                user = user_entry.get ()
                stat = status.get ()
                dom = datetime.now().strftime ('%d-%m-%Y')
                dtd = departuredate_entry.get ()
                obs = observation_entry.get ('1.0', 'end-1c')
                if not (idpmo and name and model and serial and color and dp and stat and dom):
                    messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
                else:
                    Resources.Connection.edit_pmo (rowid, idpmo, name, model, serial, color, dp, user, stat, dom, dtd, obs)
                    for item in trv.get_children ():
                        trv.delete (item)
                    find ()
                    data_editing_menu.destroy ()
                    messagebox.showinfo ('Elemento editado correctamente', 'El usuario fue editado correctamente')

            ##### Button area
            button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
            button_dem.place (x=300, y=520)

            ##### Returns selected item for editing
            try:
                selected = trv.focus ()
                values = trv.item (selected, 'values')
                idpmo_entry.insert (0, values[0])
                name_options.set (values[1])
                model_entry.insert (0, values[2])
                serial_entry.insert (0, values[3])
                color_options.set (values[4])
                department_options.set (values[5])
                user_entry.insert (0, values[6])
                stat_options.set (values[7])
                departuredate_entry.insert (0, values[10])
                observation_entry.insert (1.0, values[11])
            except IndexError:
                data_editing_menu.destroy ()
                messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

            ##### Settings to avoid modifying the ID of the registered computing device
            idpmo_entry.configure (state='readonly')
            departuredate_entry.configure (state='readonly')

        #### Function to generate a word document about the device status report
        def button_docx ():

            ##### Format of the window interface
            print_data_menu = customtkinter.CTkToplevel ()
            print_data_menu.after(250, lambda:  print_data_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            print_data_menu.title ('Menu para generar el oficio')
            print_data_menu.geometry ('500x550')
            print_data_menu.resizable (False, False)

            ###### Configuring the grid to center
            for i in range (10):
                print_data_menu.grid_rowconfigure (i, weight=1)
            print_data_menu.grid_columnconfigure (0, weight=1)
            print_data_menu.grid_columnconfigure (1, weight=1)

            ##### Fonts for the letters
            font2 = ('Roboto', 18, 'bold')

            ##### Specifying the global variables
            global addressed_to_entry
            global by_entry
            global subject_entry
            global namepmo, model, serial
            global observation_docx_entry
            global item_values

            ##### Boxes to write to whom the letter is addressed and who sends it
            addressed_to_label = CTkLabel (print_data_menu, font=font2, text='Dirigido a:', text_color='#fff')
            addressed_to_label.grid (row=0, column=0)

            addressed_to_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            addressed_to_entry.grid (row=1, column=0, pady=2, ipady=4)

            by_label = CTkLabel (print_data_menu, font=font2, text='Por:', text_color='#fff')
            by_label.grid (row=2, column=0)

            by_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            by_entry.grid (row=3, column=0, pady=2, ipady=4)

            ##### Box to write the reason for the letter
            subject_label = CTkLabel (print_data_menu, font=font2, text='Asunto:', text_color='#fff')
            subject_label.grid (row=4, column=0, columnspan=2)

            subject_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            subject_entry.grid (row=5, column=0, columnspan=2, pady=2, ipady=4)

            ##### Frame of the checkboxes
            checkbox_frame = CTkFrame (print_data_menu)
            checkbox_frame.grid (row=0, column=1, rowspan=4)

            ##### Status of the checkboxes
            namepmo = IntVar (value=1)
            model = IntVar (value=1)
            serial = IntVar (value=1)

            ##### Checkboxes to say include more data
            Include_data_label = CTkLabel (checkbox_frame, font=font2, text='Incluir datos:', text_color='#fff')
            Include_data_label.grid (row=0, column=0, pady=(0,10), columnspan=2)

            CTkCheckBox (checkbox_frame, text='Incluir Nombre', variable=namepmo).grid (row=1, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Modelo', variable=model).grid (row=2, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Serial', variable=serial).grid (row=1, column=1, pady=6, padx=5, sticky='w')

            ##### Box to write the observations to be reported
            observation_docx_label = CTkLabel (print_data_menu, font=font2, text='Reporte:', text_color='#fff')
            observation_docx_label.grid (row=6, column=0, columnspan=2)

            observation_docx_entry = CTkTextbox (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=250, height=150, corner_radius=10, wrap=WORD)
            observation_docx_entry.grid (row=7, column=0, columnspan=2, pady=5)

            ##### Conditional so that when an element is chosen it allows to open the window or not, in addition to saving the element's data to use
            selected_item = trv.selection ()
            if not selected_item:
                print_data_menu.destroy ()
                messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para generar un oficio')
                return

            ##### Gets the values of the selected register
            item_values = trv.item (selected_item[0], 'values')

            ##### Button to confirm and generate the document
            button_confirm = CTkButton (print_data_menu, font=font2, text='Generar oficio', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=lambda: Resources.Connection.docx_pmo (print_data_menu, addressed_to_entry, by_entry, subject_entry, namepmo, model, serial, observation_docx_entry, item_values))
            button_confirm.grid (row=8, column=0, columnspan=2, padx=(0, 60),  pady=5)
            
            button_confirm_pv = CTkButton (print_data_menu, font=font2, text='Vista Previa', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=lambda: Resources.Previewpmo.convertir_a_pdf (addressed_to_entry, by_entry, subject_entry, namepmo, model, serial, observation_docx_entry, item_values))
            button_confirm_pv.grid (row=8, column=1, columnspan=2, padx=(60, 0),  pady=5)

        #### Function to display a statistical graph on the operability of computer goods
        def graph_pmo ():
            Resources.Connection.graph_pmo ()

        #### Button area
        button_docx = CTkButton (main_frame, font=font1, text='Generar oficio', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_docx)
        button_docx.grid (row=3, column=0, columnspan=2, pady=10, padx=(136, 0), sticky='w')

        #### Button area
        button_del = CTkButton (main_frame, font=font1, text='Borrar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
        button_del.grid (row=3, column=0, columnspan=2, pady=10, padx=(300, 0), sticky='w')

        button_edi = CTkButton (main_frame, font=font1, text='Editar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
        button_edi.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 300), sticky='e')

        button_graph = CTkButton (main_frame, font=font1, text='Estadisticas', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=graph_pmo)
        button_graph.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 150), sticky='e')

        #### Function to display the data automatically after opening the window
        button_search ['command'] = find

        find ()

    ### Printers data window
    def pp_page ():

        #### The window that is open is saved in the variable
        global current_page
        current_page = 'pp_page'

        #### Search function within the database to get data from printers
        def find ():

            ##### Clear treeview
            for item in trv.get_children ():
                trv.delete (item)
            global count
            count = 0
            val = entry_search.get ()
            stat = status.get ()
            dp = departments.get ()
            Resources.Connection.search_pp (val, stat, dp)
            PP = Resources.Connection.cur.fetchall ()
            for row in PP:
                ###### Format so that the divisions of the data can be created within the table
                if count % 2 == 0:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
                else:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
                count += 1

        #### Fonts for the letters
        font1 = ('Roboto', 18, 'bold')

        #### Variable to display the text in the window
        area = 'Impresoras'
        title_label_area['text'] = area

        #### Search button
        button_search = CTkButton (maindataview, command=find, text_color='#fff', text='Buscar', fg_color='#02ab10', hover_color='#02920D', bg_color='#292933', cursor='hand2', corner_radius=5, width=100)
        button_search.place (x=540, y=10)

        #### Table where the data that is being searched will be displayed
        trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

        trv.configure (columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))

        ##### Defines the columns of the table, all equally and automatically
        for col in range (1, 14):
            trv.column (col, stretch=NO, anchor=tk.CENTER)

        trv.heading (1, text='ID', anchor=tk.CENTER)
        trv.heading (2, text='Nombre', anchor=tk.CENTER)
        trv.heading (3, text='Modelo', anchor=tk.CENTER)
        trv.heading (4, text='Serial', anchor=tk.CENTER)
        trv.heading (5, text='Color', anchor=tk.CENTER)
        trv.heading (6, text='Tipo de impresión', anchor=tk.CENTER)
        trv.heading (7, text='Departamentos', anchor=tk.CENTER)
        trv.heading (8, text='Usuarios', anchor=tk.CENTER)
        trv.heading (9, text='Estado', anchor=tk.CENTER)
        trv.heading (10, text='Fecha de ingreso a la entidad', anchor=tk.CENTER)
        trv.heading (11, text='Fecha de modificación', anchor=tk.CENTER)
        trv.heading (12, text='Fecha de salida de la entidad', anchor=tk.CENTER)
        trv.heading (13, text='Observaciones', anchor=tk.CENTER)

        ##### Format that creates the divisions within the table
        trv.tag_configure ('oddrow', background='#4a5052')
        trv.tag_configure ('evenrow', background='#2a2d2e')

        #### Format to move the data table both horizontally and vertically
        scrollbarx = ttk.Scrollbar (main_frame, orient=HORIZONTAL, command=trv.xview)
        trv.configure (xscroll=scrollbarx.set)
        trv.configure (selectmode='extended')
        scrollbarx.grid (row=1, column=0,  columnspan=2, sticky='ew')

        scrollbary = ttk.Scrollbar (main_frame, orient=VERTICAL, command=trv.yview)
        trv.configure (yscroll=scrollbary.set)
        trv.configure (selectmode='extended')
        scrollbary.grid (row=0, column=1,  columnspan=2, sticky='ns')

        trv.grid (row=0, column=0,  columnspan=2, padx=(0, 16), pady=(0, 1), sticky='nsew')

        #### Setting so that the objects are centered
        main_frame.grid_rowconfigure (0, weight=1)
        main_frame.grid_columnconfigure (0, weight=1)

        #### Function to delete users
        def button_del ():
            selected = trv.selection ()
            if selected:
                rowid = selected [0]
                Resources.Connection.del_pp (rowid)
                trv.delete (rowid)
            else:
                messagebox.showerror('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

        #### Function to edit users
        def button_dem ():

            ##### Format of the window interface
            data_editing_menu = customtkinter.CTkToplevel ()
            data_editing_menu.after(250, lambda:  data_editing_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            data_editing_menu.title ('Menu de edición de datos de la impresora')
            data_editing_menu.geometry ('960x600')
            data_editing_menu.resizable (False, False)

            ##### Validates if they are only numbers and dashes
            def validate_numbers_entry (char):
                if char == '' or all (c.isdigit() or c == '-' for c in char):
                    return True
                else:
                    return False

            ##### Fonts for the letters
            font1 = ('Roboto', 30, 'bold')
            font2 = ('Roboto', 18, 'bold')
            font3 = ('Roboto', 16, 'bold')

            ##### User interface objects
            title_label = CTkLabel (data_editing_menu, font=font1, text='Datos de la impresora', text_color='#fff')
            title_label.place (x=25, y=5)

            ###### Objects within the frame
            ####### Front row
            idpp_label = CTkLabel (data_editing_menu, font=font2, text='ID:', text_color='#fff')
            idpp_label.place (x=50, y=60)

            idpp_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            idpp_entry.place (x=50, y=90)

            name_label = CTkLabel (data_editing_menu, font=font2, text='Nombre de la marca:', text_color='#fff')
            name_label.place (x=280, y=60)

            namepp = StringVar ()
            options = ['HP', 'Canon', 'Epson', 'Samsung', 'Brother', 'Lexmark', 'Xerox']

            name_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=namepp, values=options, state='readonly')
            name_options.place (x=280, y=90)

            model_label = CTkLabel (data_editing_menu, font=font2, text='Modelo:', text_color='#fff')
            model_label.place (x=485, y=60)

            model_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            model_entry.place (x=485, y=90)

            serial_label = CTkLabel (data_editing_menu, font=font2, text='Serial:', text_color='#fff')
            serial_label.place (x=680, y=60)

            serial_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            serial_entry.place (x=680, y=90)

            ####### Second row
            color_label = CTkLabel (data_editing_menu, font=font2, text='Color:', text_color='#fff')
            color_label.place (x=50, y=140)

            colorpp = StringVar ()
            options = ['Negro', 'Plata', 'Gris', 'Blanco']

            color_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=colorpp, values=options, state='readonly')
            color_options.place (x=50, y=170)

            type_label = CTkLabel (data_editing_menu, font=font2, text='Tipo de impresión:', text_color='#fff')
            type_label.place (x=280, y=140)

            typeprinting = StringVar ()
            options = ['Tóner', 'Cartucho']

            type_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=typeprinting, values=options, state='readonly')
            type_options.place (x=280, y=170)

            department_label = CTkLabel (data_editing_menu, font=font2, text='Departamento:', text_color='#fff')
            department_label.place (x=485, y=140)

            departments = StringVar ()
            options = ['Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Presupuesto', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo', 'Despacho', 'Dirección general']

            department_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=departments, values=options, state='readonly')
            department_options.place (x=485, y=170)

            user_label = CTkLabel (data_editing_menu, font=font2, text='Usuario:', text_color='#fff')
            user_label.place (x=680, y=140)

            user_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
            user_entry.place (x=680, y=170)

            ####### Third row
            stat_label = CTkLabel (data_editing_menu, font=font2, text='Estado:', text_color='#fff')
            stat_label.place (x=50, y=220)

            status = StringVar ()
            options = ['Operativo', 'Inoperativo']

            stat_options = CTkComboBox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', dropdown_hover_color='#3484F0', button_color='#3484F0', button_hover_color='#1a4278', border_color="#3484F0", width=150, variable=status, values=options, state='readonly')
            stat_options.place (x=50, y=250)

            ####### Fourth row
            departuredate_label = CTkLabel (data_editing_menu, font=font3, text='Fecha de salidad de la entidad:', text_color='#fff')
            departuredate_label.place (x=50, y=300)

            departuredate_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(data_editing_menu.register(validate_numbers_entry), '%S'))
            departuredate_entry.place (x=50, y=330)

            ######## Displays a calendar to facilitate the selection of the date
            ######### Global variable so that the window does not open more than one
            global calendar_window
            calendar_window = False

            def calendar ():
                ######### Specifying the global variable
                global calendar_window

                ######### Conditional that tells me if there is already an open window
                if calendar_window:
                    messagebox.showerror ('Nueva ventana', 'Ya existe una ventana abierta')
                    return

                ######### Create a new window for the calendar
                window_callendary = tk.Toplevel (data_editing_menu)
                window_callendary.title ('Calendario seleccionable')
                calendar_window = True

                ######### Create a calendar widget
                calendar = Calendar (window_callendary, date_pattern='dd-mm-y', selectmode='day')
                calendar.pack (pady=20)

                ######### Function to show the selected date in the Entry of the main window
                def show_calendar_date ():
                    date_selected = calendar.get_date ()
                    departuredate_entry.configure (state='normal')
                    departuredate_entry.delete (0, tk.END)
                    departuredate_entry.insert (0, date_selected)
                    departuredate_entry.configure (state='readonly')

                ######### button to show the selected date
                date_button = tk.Button (window_callendary, text='Mostrar fecha', command=show_calendar_date)
                date_button.pack (pady=10)

                ######### Function to reset the variable, so that you can reopen the window
                def calendar_close ():
                    global calendar_window
                    window_callendary.destroy ()
                    calendar_window = None

                window_callendary.protocol('WM_DELETE_WINDOW', calendar_close)

            calendar_button = CTkButton (data_editing_menu, text='Abrir Calendario', command=calendar)
            calendar_button.place (x=54, y=380)

            ####### Fifth row

            ####### Sixth row

            ####### Fifth and sixth row
            observation_label = CTkLabel (data_editing_menu, font=font2, text='Observación:', text_color='#fff')
            observation_label.place (x=485, y=380)

            observation_entry = CTkTextbox (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=347, height=110, corner_radius=10, wrap=WORD)
            observation_entry.place (x=485, y=410)

            ###### The end of the frame objects

            ##### Data verification input
            def check_input ():
                selected = trv.focus ()
                rowid = selected [0]
                idpp = idpp_entry.get ()
                name = namepp.get ()
                model = model_entry.get ()
                serial = serial_entry.get ()
                color = colorpp.get ()
                tp = typeprinting.get ()
                dp = departments.get ()
                user = user_entry.get ()
                stat = status.get ()
                dom = datetime.now().strftime ('%d-%m-%Y')
                dtd = departuredate_entry.get ()
                obs = observation_entry.get ('1.0', 'end-1c')
                if not (idpp and name and model and serial and color and tp and dp and stat and dom):
                    messagebox.showerror ('Error', 'Por favor asegurese que todos los campos este completos antes de editar el elemento')
                else:
                    Resources.Connection.edit_pp (rowid, idpp, name, model, serial, color, tp, dp, user, stat, dom, dtd, obs)
                    for item in trv.get_children ():
                        trv.delete (item)
                    find ()
                    data_editing_menu.destroy ()
                    messagebox.showinfo ('Elemento editado correctamente', 'El usuario fue editado correctamente')

            ##### Button area
            button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
            button_dem.place (x=300, y=520)

            ##### Returns selected item for editing
            try:
                selected = trv.focus ()
                values = trv.item (selected, 'values')
                idpp_entry.insert (0, values[0])
                name_options.set (values[1])
                model_entry.insert (0, values[2])
                serial_entry.insert (0, values[3])
                color_options.set (values[4])
                typeprinting.set (values[5])
                department_options.set (values[6])
                user_entry.insert (0, values[7])
                stat_options.set (values[8])
                departuredate_entry.insert (0, values[11])
                observation_entry.insert (1.0, values[12])

            except IndexError:
                data_editing_menu.destroy ()
                messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para editarlo de la base de datos')

            ##### Settings to avoid modifying the ID of the registered computing device
            idpp_entry.configure (state='readonly')
            departuredate_entry.configure (state='readonly')

        #### Function to generate a word document about the device status report
        def button_docx ():

            ##### Format of the window interface
            print_data_menu = customtkinter.CTkToplevel ()
            print_data_menu.after(250, lambda:  print_data_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            print_data_menu.title ('Menu para generar el oficio')
            print_data_menu.geometry ('500x550')
            print_data_menu.resizable (False, False)

            ###### Configuring the grid to center
            for i in range (10):
                print_data_menu.grid_rowconfigure (i, weight=1)
            print_data_menu.grid_columnconfigure (0, weight=1)
            print_data_menu.grid_columnconfigure (1, weight=1)

            ##### Fonts for the letters
            font2 = ('Roboto', 18, 'bold')

            ##### Specifying the global variables
            global addressed_to_entry
            global by_entry
            global subject_entry
            global namepp, model, serial, typeprinting
            global observation_docx_entry
            global item_values

            ##### Boxes to write to whom the letter is addressed and who sends it
            addressed_to_label = CTkLabel (print_data_menu, font=font2, text='Dirigido a:', text_color='#fff')
            addressed_to_label.grid (row=0, column=0)

            addressed_to_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            addressed_to_entry.grid (row=1, column=0, pady=2, ipady=4)

            by_label = CTkLabel (print_data_menu, font=font2, text='Por:', text_color='#fff')
            by_label.grid (row=2, column=0)

            by_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            by_entry.grid (row=3, column=0, pady=2, ipady=4)

            ##### Box to write the reason for the letter
            subject_label = CTkLabel (print_data_menu, font=font2, text='Asunto:', text_color='#fff')
            subject_label.grid (row=4, column=0, columnspan=2)

            subject_entry = CTkEntry (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=30, corner_radius=10)
            subject_entry.grid (row=5, column=0, columnspan=2, pady=2, ipady=4)

            ##### Frame of the checkboxes
            checkbox_frame = CTkFrame (print_data_menu)
            checkbox_frame.grid (row=0, column=1, rowspan=4)

            ##### Status of the checkboxes
            namepp = IntVar (value=1)
            model = IntVar (value=1)
            serial = IntVar (value=1)
            typeprinting = IntVar (value=0)

            ##### Checkboxes to say include more data
            Include_data_label = CTkLabel (checkbox_frame, font=font2, text='Incluir datos:', text_color='#fff')
            Include_data_label.grid (row=0, column=0, pady=(0,10), columnspan=2)

            CTkCheckBox (checkbox_frame, text='Incluir Nombre', variable=namepp).grid (row=1, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Modelo', variable=model).grid (row=2, column=0, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Serial', variable=serial).grid (row=1, column=1, pady=6, padx=5, sticky='w')

            CTkCheckBox (checkbox_frame, text='Incluir Tipo de impresión', variable=typeprinting).grid (row=2, column=1, pady=6, padx=5, sticky='w')

            ##### Box to write the observations to be reported
            observation_docx_label = CTkLabel (print_data_menu, font=font2, text='Reporte:', text_color='#fff')
            observation_docx_label.grid (row=6, column=0, columnspan=2)

            observation_docx_entry = CTkTextbox (print_data_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=250, height=150, corner_radius=10, wrap=WORD)
            observation_docx_entry.grid (row=7, column=0, columnspan=2, pady=5)

            ##### Conditional so that when an element is chosen it allows to open the window or not, in addition to saving the element's data to use
            selected_item = trv.selection ()
            if not selected_item:
                print_data_menu.destroy ()
                messagebox.showerror ('Error - sin elemento no seleccionado', 'Se debe seleccionar un elemento para generar un oficio')
                return

            ##### Gets the values of the selected register
            item_values = trv.item (selected_item[0], 'values')

            ##### Button to confirm and generate the document
            button_confirm = CTkButton (print_data_menu, font=font2, text='Generar oficio', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=lambda: Resources.Connection.docx_pp (print_data_menu, addressed_to_entry, by_entry, subject_entry, namepp, model, serial, typeprinting, observation_docx_entry, item_values))
            button_confirm.grid (row=8, column=0, columnspan=2, padx=(0, 60),  pady=5)
            
            button_confirm_pv = CTkButton (print_data_menu, font=font2, text='Vista Previa', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=lambda: Resources.Previewpp.convertir_a_pdf (addressed_to_entry, by_entry, subject_entry, namepp, model, serial, typeprinting, observation_docx_entry, item_values))
            button_confirm_pv.grid (row=8, column=1, columnspan=2, padx=(60, 0),  pady=5)

        #### Function to display a statistical graph on the operability of computer goods
        def graph_pp ():
            Resources.Connection.graph_pp ()

        #### Button area
        button_docx = CTkButton (main_frame, font=font1, text='Generar oficio', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_docx)
        button_docx.grid (row=3, column=0, columnspan=2, pady=10, padx=(136, 0), sticky='w')

        #### Button area
        button_del = CTkButton (main_frame, font=font1, text='Borrar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
        button_del.grid (row=3, column=0, columnspan=2, pady=10, padx=(300, 0), sticky='w')

        button_edi = CTkButton (main_frame, font=font1, text='Editar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
        button_edi.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 300), sticky='e')

        button_graph = CTkButton (main_frame, font=font1, text='Estadisticas', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=graph_pp)
        button_graph.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 150), sticky='e')

        #### Function to display the data automatically after opening the window
        button_search ['command'] = find

        find ()

    ### Function to delete the window or close
    def delete_pages ():

        for frame in main_frame.winfo_children ():
            frame.destroy ()

    ### Function to return to the menu window
    def menu_page ():

        #### Calls the variable to find out what its previous state was
        global current_page

        #### Fonts for the letters
        font1 = ('Roboto', 22, 'bold')

        #### Format for the background of the output page
        CTkLabel (main_frame, text='Sistema de inventario', font=font1).pack (pady=(80, 0))
        CTkLabel (main_frame, text='para', font=font1).pack (pady=2)
        CTkLabel (main_frame, text='equipos informáticos', font=font1).pack (pady=2)
        logo_image_central = CTkImage (Image.open('Resources\\Img\\Logo_SIEI_icon.png'), size=(150, 150))
        logo_image_central_label = CTkLabel (main_frame, text='', image=logo_image_central, fg_color=None, bg_color='transparent')
        logo_image_central_label.pack (pady=20)

        #### Exit confirmation message, also if the exit is rejected it will return to the window that was open
        if messagebox.askyesno ('Confirmación', '¿Está seguro que desea salir?'):
            maindataview.destroy ()
            mainmenu.deiconify ()
        else:
            if current_page == 'pc_page':
                delete_pages ()
                pc_page ()
                pc_btn_indicator.config (bg='white')
                exit_btn_indicator.config (bg=menu_bar_colour)
            elif current_page == 'pk_page':
                delete_pages ()
                pk_page ()
                pk_btn_indicator.config (bg='white')
                exit_btn_indicator.config (bg=menu_bar_colour)
            elif current_page == 'pm_page':
                delete_pages ()
                pm_page ()
                pm_btn_indicator.config (bg='white')
                exit_btn_indicator.config (bg=menu_bar_colour)
            elif current_page == 'pmo_page':
                delete_pages ()
                pmo_page ()
                pmo_btn_indicator.config (bg='white')
                exit_btn_indicator.config (bg=menu_bar_colour)
            elif current_page == 'pp_page':
                delete_pages ()
                pp_page ()
                pp_btn_indicator.config (bg='white')
                exit_btn_indicator.config (bg=menu_bar_colour)

    ## Function to detect when I want to leave the window
    def closing ():
        switch_indication (exit_btn_indicator, menu_page)

    ## Detector of whether I want to close the window
    maindataview.protocol ("WM_DELETE_WINDOW", closing)

    ## Function to show which button and window is being selected
    def hide_indicator ():

        exit_btn_indicator.config (bg=menu_bar_colour)
        pc_btn_indicator.config (bg=menu_bar_colour)
        pk_btn_indicator.config (bg=menu_bar_colour)
        pm_btn_indicator.config (bg=menu_bar_colour)
        pmo_btn_indicator.config (bg=menu_bar_colour)
        pp_btn_indicator.config (bg=menu_bar_colour)

    ## Function that shows the page and marks which button is being used and allows to work with the variable
    def switch_indication (lb, page):
        global current_page
        hide_indicator ()
        lb.config (bg='white')
        delete_pages ()
        page ()



    ## Search box and button to be used with the options box for filtering
    entry_search = CTkEntry (maindataview, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=300)
    entry_search.place (x=230, y=10)

    ## Box of options for the search
    status = StringVar ()
    options = ['Operativo', 'Inoperativo']

    stat_options = CTkComboBox (maindataview, text_color='#000', fg_color='#fff', dropdown_hover_color='#7d01b2', button_color='#7d01b2', button_hover_color='#7d01b2', border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
    stat_options.set ('Operativo')
    stat_options.place (x=650, y=10)

    departments = StringVar ()
    options = ['Todo', 'Informática', 'Tesorería', 'Contabilidad', 'Administración', 'Recursos humanos', 'Presupuesto', 'Sala situacional', 'Catastro', 'Proyectos especiales', 'Turismo', 'Despacho', 'Dirección general']

    department_options = CTkComboBox (maindataview, text_color='#000', fg_color='#fff', dropdown_hover_color='#7d01b2', button_color='#7d01b2', button_hover_color='#7d01b2', border_color="#7d01b2", width=150, variable=departments, values=options, state='readonly')
    department_options.set ('Todo')
    department_options.place (x=810, y=10)



    ## To display one of the pages
    pc_page ()

    maindataview.mainloop ()
