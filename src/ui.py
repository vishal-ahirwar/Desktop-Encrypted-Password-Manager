#Copyright© 2022 Vishal Ahirwar.
from tkinter import*

def InitManager():
    window=Tk()
    window.title("Your Personal Password Manager")
    window.config(padx=45,pady=45)
    canvas =Canvas(height=200,width=200)
    logo_img=PhotoImage(file="../res/logo.png")
    canvas.create_image(100,100,image=logo_img)
    canvas.grid(column=1,row=0)
    Label(text="Website Url/Name:").grid(column=0,row=1)
    website=Entry(width=25)
    website.grid(column=1,row=1)
    email=Entry(width=25)
    email.grid(column=1,row=2)
    password=Entry(width=26)
    password.grid(column=1,row=3)
    btn_gen=Button(text="Generate Password")
    btn_gen.grid(column=2,row=3)
    btn_save=Button(text="Save and Encrypt Password")
    btn_save.grid(column=1,row=4)
    btn_search=Button(text="Search and Decrypt Password")
    btn_search.grid(column=2,row=1)
    Label(text="Copyright© 2022 Vishal Ahirwar.").grid(column=0,row=6)
    Label(text="Email/Username:").grid(column=0,row=2)
    Label(text="Password:").grid(column=0,row=3)
    window.mainloop()
