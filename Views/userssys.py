# Libraries
import customtkinter
from customtkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
from PIL import Image

# Communication with SQLite3 to get the data from the database
import Services.DB.Connection

# I define the view so I can call it
def userssysview (mainmenu):

    ## Defined appearance
    set_appearance_mode ('dark')
    set_default_color_theme ('blue')

    ### Model of the menu
    menu_bar_colour = '#383838'

    ## Format of the window interface
    mainuserssys = customtkinter.CTkToplevel ()
    mainuserssys.after(250, lambda:  mainuserssys.iconbitmap('Resources\\Img\\Ico.ico'))
    mainuserssys.title ('Datos de los usuarios')
    mainuserssys.geometry ('860x580')
    mainuserssys.resizable (False, False)

    ## Code to center the application window
    ### Refresh the window to make sure the size of it
    mainuserssys.update_idletasks ()
    ### Get the screen size
    screen_width = mainuserssys.winfo_screenwidth ()
    screen_height = mainuserssys.winfo_screenheight ()
    ### Get the size of the window
    win_width = mainuserssys.winfo_width ()
    win_height = mainuserssys.winfo_height ()
    ### Calculate the centered position
    x = (screen_width // 2) - (win_width // 2)
    y = (screen_height // 2) - (win_height // 2)
    ### Set the new position
    mainuserssys.geometry(f"+{x}+{y}")

    ## Variable that saves which window is open
    current_page = None

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
    reg_icon = CTkImage (Image.open('Resources\\Img\\User.png'), size=(20, 20))
    view_icon = CTkImage (Image.open('Resources\\Img\\Userdetail.png'), size=(20, 20))

    ## Generator of help message for objects in which the cursor is needed to be positioned to know more about the object
    class CustomHovertip (Hovertip):
        def showcontents (main):
            label = tk.Label (main.tipwindow, text=f'''{main.text}''', justify=tk.LEFT, bg='#151515', fg='#ffffff', relief=tk.SOLID, borderwidth=1, font=('Roboto', 12))
            label.pack ()

    ## Format of the menu
    menu_bar_frame = tk.Frame (mainuserssys, bg=menu_bar_colour)

    ### Menu buttons
    exit_btn = CTkButton (menu_bar_frame, text='', image=exit_icon, width=10, height=10, command=lambda: switch_indication (exit_btn_indicator, menu_page))
    exit_btn.grid (row=0, column=0, padx=(5, 0), pady=(13.2, 0))
    CustomHovertip (exit_btn, text='Ir al menu', hover_delay=500)

    reg_btn = CTkButton (menu_bar_frame, text='', image=reg_icon, width=10, height=10, command=lambda: switch_indication (reg_btn_indicator, reg_page))
    reg_btn.grid (row=1, column=0, padx=(5, 0), pady=(60, 0))
    CustomHovertip (reg_btn, text='Ventana para añadir datos de usuarios', hover_delay=500)

    view_btn = CTkButton (menu_bar_frame, text='', image=view_icon, width=10, height=10, command=lambda: switch_indication (view_btn_indicator, view_page))
    view_btn.grid (row=2, column=0, padx=(5, 0), pady=(20, 0))
    CustomHovertip (view_btn, text='Ventana para ver los datos de usuarios', hover_delay=500)

    ### Usage indicator for the button
    exit_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
    exit_btn_indicator.grid (row=0, column=1, padx=(2, 0), pady=(15, 0), sticky='n')

    reg_btn_indicator = tk.Label (menu_bar_frame, bg='white', width=0, height=3)
    reg_btn_indicator.grid (row=1, column=1, padx=(2, 0), pady=(72, 0), sticky='n')

    view_btn_indicator = tk.Label (menu_bar_frame, bg=menu_bar_colour, width=0, height=3)
    view_btn_indicator.grid (row=2, column=1, padx=(2, 0), pady=(23, 0), sticky='n')

    #### Form of the menu
    menu_bar_frame.pack (side=tk.LEFT, fill=Y, pady=4, padx=3)
    menu_bar_frame.pack_propagate (flag=False)
    menu_bar_frame.configure (width=45)

    ### Area where the objects that are selected in the menu will be displayed
    main_frame = CTkFrame (mainuserssys)
    main_frame.pack (fill='both', expand=True, side=LEFT, padx=(0,20), pady=20)
    main_frame.pack_propagate (False)
    main_frame.configure (width=800, height=500)

    ## Functions to display the windows
    ### Window where the user's data can be registered
    def reg_page ():

        #### The window that is open is saved in the variable
        global current_page
        current_page = 'reg_page'

        #### Database manipulators
        ##### Input re-initiator for data logging
        def new_dt ():
            idus_entry.delete (0, END)
            user_entry.delete (0, END)
            psw_entry.delete (0, END)
            firstnameperson_entry.delete (0, END)
            lastnameperson_entry.delete (0, END)
            idcardperson_entry.delete (0, END)

        ##### Entry that records the data in the database
        def submit_dt ():
            idus = idus_entry.get ()
            user = user_entry.get ()
            psw = psw_entry.get ()
            firstnameperson = firstnameperson_entry.get ()
            lastnameperson = lastnameperson_entry.get ()
            idcardperson = idcardperson_entry.get ()
            try:
                if not (idus and user and psw and firstnameperson and lastnameperson and idcardperson):
                    messagebox.showerror ('Error', 'Se deben llenar todas las celdas')
                elif Services.DB.Connection.id_exist_users (idus):
                    messagebox.showerror ('Error', 'El ID ya existe')
                else:
                    Services.DB.Connection.insert_users (idus, user, psw, firstnameperson, lastnameperson, idcardperson)
                    messagebox.showinfo ('Éxito', 'La información fue registrada')
            except:
                messagebox.showerror ('Error', 'A ocurrido un error')

        ##### This function is to validate input of only numbers and omit letters
        def validate_numbers_entry(char):
            if char.isdigit() or char == '.':
                return True
            else:
                return False

        #### Fonts for the letters
        font1 = ('Roboto', 30, 'bold')
        font2 = ('Roboto', 18, 'bold')

        #### User interface objects
        title_label = CTkLabel (main_frame, font=font1, text='Datos de registro del usuario', text_color='#fff')
        title_label.grid (row=0, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

        ##### Objects to register the users that is inside the frame
        ###### Front row
        idus_label = CTkLabel (main_frame, font=font2, text='ID del usuario:', text_color='#fff')
        idus_label.grid (row=1, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

        idus_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        idus_entry.grid (row=2, column=0, padx=(40, 20), pady=(0, 10), sticky='w')

        user_label = CTkLabel (main_frame, font=font2, text='Nombre de usuario:', text_color='#fff')
        user_label.grid (row=1, column=1, padx=20, pady=(10, 5), sticky='w')

        user_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        user_entry.grid (row=2, column=1, padx=20, pady=(0, 10), sticky='w')

        psw_label = CTkLabel (main_frame, font=font2, text='Contraseña del usuario:', text_color='#fff')
        psw_label.grid (row=1, column=2, padx=20, pady=(10, 5), sticky='w')

        psw_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        psw_entry.grid (row=2, column=2, padx=20, pady=(0, 10), sticky='w')

        ###### Second row
        firstnameperson_label = CTkLabel (main_frame, font=font2, text='Nombre real del usuario:', text_color='#fff')
        firstnameperson_label.grid  (row=3, column=0, padx=(40, 20), pady=(10, 5), sticky='w')

        firstnameperson_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        firstnameperson_entry.grid (row=4, column=0, padx=(40, 20), pady=(5, 5), sticky='w')

        lastnameperson_label = CTkLabel (main_frame, font=font2, text='Apellido real del usuario:', text_color='#fff')
        lastnameperson_label.grid (row=3, column=1, padx=20, pady=(10, 5), sticky='w')

        lastnameperson_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10)
        lastnameperson_entry.grid (row=4, column=1, padx=20, pady=(5, 5), sticky='w')

        idcardperson_label = CTkLabel (main_frame, font=font2, text='C.I. real del usuario:', text_color='#fff')
        idcardperson_label.grid (row=3, column=2, padx=20, pady=(10, 5), sticky='w')

        idcardperson_entry = CTkEntry (main_frame, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(main_frame.register(validate_numbers_entry), '%S'))
        idcardperson_entry.grid (row=4, column=2, padx=20, pady=(5, 5), sticky='w')

        ###### Button area
        submit_button = CTkButton (main_frame, font=font2, text='Guardar', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=submit_dt)
        submit_button.grid (row=5, column=0, columnspan=3, padx=(0, 200), pady=(265, 10))

        clear_button = CTkButton (main_frame, font=font2, text='Nuevo registro', border_width=1.5, corner_radius=15, border_color="#3484F0", fg_color='#343638', command=new_dt)
        clear_button.grid (row=5, column=0, columnspan=3, padx=(200, 0), pady=(265, 10))
        ##### The end of the frame objects

    ### Window where users' data can be viewed
    def view_page ():

        #### The window that is open is saved in the variable
        global current_page
        current_page = 'view_page'

        #### Search function within the database to get user data
        def find ():

            ##### Clear treeview
            for item in trv.get_children ():
                trv.delete (item)
            global count
            count = 0
            Services.DB.Connection.search_users ()
            users = Services.DB.Connection.cur.fetchall ()
            for row in users:
                ###### Format so that the divisions of the data can be created within the table
                if count % 2 == 0:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='evenrow')
                else:
                    trv.insert (parent='', index='end', iid=row[0], text='', values=row, tags='oddrow')
                count += 1

        #### Fonts for the letters
        font1 = ('Roboto', 18, 'bold')

        #### Table where the data will be displayed
        trv = ttk.Treeview (main_frame, height=17, selectmode='browse', show='headings')

        trv.configure (columns=(1, 2, 3, 4, 5, 6))

        ##### Defines the columns of the table, all equally and automatically
        for col in range (1, 7):
            trv.column (col, stretch=NO, anchor=tk.CENTER)

        trv.heading (1, text='ID', anchor=CENTER)
        trv.heading (2, text='Usuario', anchor=CENTER)
        trv.heading (3, text='Contraseña', anchor=CENTER)
        trv.heading (4, text='Nombre real del usuario', anchor=CENTER)
        trv.heading (5, text='Apellido del usuario', anchor=CENTER)
        trv.heading (6, text='Cedula de identidad del usuario', anchor=CENTER)

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
                Services.DB.Connection.del_users (rowid)
                trv.delete (rowid)
            else:
                messagebox.showerror ('Error - sin elemento seleccionado', 'Se debe seleccionar un elemento para eliminarlo de la base de datos')

        #### Function to edit users
        def button_dem ():

            ##### Format of the window interface
            data_editing_menu = customtkinter.CTkToplevel ()
            data_editing_menu.after(250, lambda:  data_editing_menu.iconbitmap('Resources\\Img\\Ico.ico'))
            data_editing_menu.title ('Menu de edición de datos')
            data_editing_menu.geometry ('800x500')
            data_editing_menu.resizable (False, False)

            ##### This function is to validate input of only numbers and omit letters
            def validate_numbers_entry (char):
                if char == '' or all(c.isdigit() or c == '.' for c in char):
                    return True
                else:
                    return False

            ##### Fonts for the letters
            font1 = ('Roboto', 30, 'bold')
            font2 = ('Roboto', 18, 'bold')

            ##### User interface objects
            title_label = CTkLabel (data_editing_menu, font=font1, text='Datos del usuario', text_color='#fff')
            title_label.place (x=25, y=0)

            ###### Objects to register the users that is inside the frame
            ####### Front row
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

            ####### Second row
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

            idcardperson_entry = CTkEntry (data_editing_menu, font=font2, text_color='#000', fg_color='#fff', border_color='#3484F0', border_width=3, width=150, height=35, corner_radius=10, validate='key', validatecommand=(data_editing_menu.register(validate_numbers_entry), '%S'))
            idcardperson_entry.place (x=520, y=170)
            ###### The end of the frame objects

            ##### Data verification input
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
                    Services.DB.Connection.edit_users (rowid, idus, user, psw, firstnameperson, lastnameperson, idcardperson)
                    for item in trv.get_children ():
                        trv.delete (item)
                    Services.DB.Connection.search_users ()
                    users = Services.DB.Connection.cur.fetchall ()
                    for row in users:
                        trv.insert (parent='', index='end', iid=row[0], text='', values=row)
                    data_editing_menu.destroy ()
                    messagebox.showinfo ('Elemento editado correctamente', 'El usuario fue editado correctamente')

            ##### Button area
            button_dem = CTkButton (data_editing_menu, font=font2, text='Editar', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=check_input)
            button_dem.place (x=300, y=450)

            ##### Returns selected item for editing
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

            ##### Settings to avoid modifying the ID of the registered computing device
            idus_entry.configure (state='readonly')

        #### Button area
        button_del = CTkButton (main_frame, font=font1, text='Borrar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_del)
        button_del.grid (row=3, column=0, columnspan=2, pady=10, padx=(200, 0), sticky='w')

        button_edi = CTkButton (main_frame, font=font1, text='Editar usuario', border_width=1.5, corner_radius=15, border_color='#3484F0', fg_color='#343638', command=button_dem)
        button_edi.grid (row=3, column=0, columnspan=2, pady=10, padx=(0, 200), sticky='e')

        #### Function to display the data automatically after opening the window
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
            mainuserssys.destroy ()
            mainmenu.deiconify ()
        else:
            if current_page == 'view_page':
                delete_pages ()
                view_page ()
                view_btn_indicator.config (bg='white')
                exit_btn_indicator.config (bg=menu_bar_colour)
            elif current_page == 'reg_page':
                delete_pages ()
                reg_page ()
                reg_btn_indicator.config (bg='white')
                exit_btn_indicator.config (bg=menu_bar_colour)

    ## Function to detect when I want to leave the window
    def closing ():
        switch_indication (exit_btn_indicator, menu_page)

    ## Detector of whether I want to close the window
    mainuserssys.protocol ("WM_DELETE_WINDOW", closing)

    ## Function to show which button and window is being selected
    def hide_indicator ():

        exit_btn_indicator.config (bg=menu_bar_colour)
        reg_btn_indicator.config (bg=menu_bar_colour)
        view_btn_indicator.config (bg=menu_bar_colour)

    ## Function that shows the page and marks which button is being used and allows to work with the variable
    def switch_indication (lb, page):
        global current_page
        hide_indicator ()
        lb.config (bg='white')
        delete_pages ()
        page ()

    ## To display one of the pages
    reg_page ()

    mainuserssys.mainloop ()
