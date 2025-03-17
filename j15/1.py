# pip install tk

from tkinter import *
# import tkinter as tk


def showFullName():
    full_name = f"نام کامل شما {fname_ent.get()} {lname_ent.get()} است"
    fullName_lbl.config(text=full_name)


main_bg = "#2D889E"
main_font = ("vazir", 16, "bold")

root = Tk()
root.title("fullname app")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg=main_bg)


# fname_lbl = Label(root, text="نام", font=main_font, bg=main_bg).pack()
# lname_lbl = Label(root, text="نام خانوادگی", font=main_font, bg=main_bg).pack()
# fname_lbl = Label(root, text="نام", font=main_font, bg=main_bg).place(x=350, y=10)
# lname_lbl = Label(root, text="نام خانوادگی", font=main_font, bg=main_bg).place(x=270, y=50)
fname_lbl = Label(root, text="نام", font=main_font, bg=main_bg).pack(pady=10)
fname_ent = Entry(root, font=(("vazir", 12, "bold")), justify="center")
fname_ent.pack()
lname_lbl = Label(root, text="نام خانوادگی", font=main_font, bg=main_bg).pack(pady=10)
lname_ent = Entry(root, font=(("vazir", 12, "bold")), justify="center")
lname_ent.pack()
fullName_btn = Button(root, text="کلیک کنید", bg="lightgreen", font=main_font, command=showFullName).pack(pady=30)
fullName_lbl = Label(root, text="", font=main_font, bg=main_bg)
fullName_lbl.pack()
# fname_lbl = Label(root, text="نام", font=main_font, bg=main_bg).grid(row=0, column=0)
# fname_ent = Entry(root, font=(("vazir", 12, "bold")), justify="center")
# fname_ent.grid(row=0, column=1)
# lname_lbl = Label(root, text="نام خانوادگی", font=main_font, bg=main_bg)
# lname_lbl.grid(row=1, column=0)
# lname_ent = Entry(root, font=(("vazir", 12, "bold")), justify="center")
# lname_ent.grid(row=1, column=1)
# fullName_btn = Button(root, text="کلیک کنید", bg="lightgreen", font=main_font, command=showFullName)
# fullName_btn.grid(row=2, column=1)
# fullName_lbl = Label(root, text="", font=main_font, bg=main_bg)
# fullName_lbl.grid(row=3, column=1)

t1 = Text(root, width=40, height=5).pack()


root.mainloop()
