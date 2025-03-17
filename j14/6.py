from tkinter import *


def showFullname():
    firstname = fname_ent.get()
    lastname = lname_ent.get()
    fullName = firstname + " " + lastname
    fullName_lbl.config(text=f"نام کامل شما : {fullName} است")


root = Tk()
root.geometry("400x400")
root.title("fullname app")
# root.config(bg="lightgreen")
root.resizable(False, 0)

fname_lbl = Label(root, text="نام", font=(("vazir", 16, "bold")))
fname_lbl.pack(pady=10)
fname_ent = Entry(root, font=(("vazir", 14)), justify="center")
fname_ent.pack()
lname_lbl = Label(root, text="نام خانوادگی", font=(("vazir", 16, "bold")))
lname_lbl.pack(pady=10)
lname_ent = Entry(root, font=(("vazir", 14)), justify="center")
lname_ent.pack()
fullName_btn = Button(
    root,
    text="کلیک کنید",
    bg="lightgreen",
    font=(("vazir", 16, "bold")),
    command=showFullname)
fullName_btn.pack(pady=20)
fullName_lbl = Label(root, text="", font=(("vazir", 16, "bold")))
fullName_lbl.pack()
root.mainloop()
