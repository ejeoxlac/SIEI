from customtkinter import *
set_appearance_mode ("dark")
set_default_color_theme ("blue")

main = CTk ()
main.title ("CTK - Login")
main.geometry ("500x500")

user = CTkFrame (main)
user.pack (expand = True, fill = "both", padx = 20, pady = 60 )

CTkLabel (user, text = "Login system", font= ("Roboto", 26)).pack (pady = 20)

em = CTkEntry (user, placeholder_text = "Email", width=250)
em.pack ()

ps= CTkEntry (user, placeholder_text = "Password", width=250)
ps.pack (pady = 15)

CTkButton (user, text = "Login").pack ()

main.mainloop ()