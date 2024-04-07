from customtkinter import *
# from sqlite3 import Communication
set_appearance_mode ("dark")
set_default_color_theme ("blue")

main = CTk ()
main.title ("CTK - Main")
main.geometry ("500x500")
main.resizable(False,False)

font1 = ('Roboto',20, 'bold')

ID_label = CTkLabel (main, font=font1, text='ID:',text_color='#fff', bg_color='#161c25')
ID_label.place(x=20, y=20)

ID_entry = CTkEntry (main, font=font1, text_color='#000', fg_color='#fff', border_color='#0c9295', border_width=2, width=180)
ID_entry.place(x=100, y=20)

main.mainloop ()
