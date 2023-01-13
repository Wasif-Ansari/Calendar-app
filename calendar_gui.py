#Importing tkinter module
from tkinter import *
#importing calendar module
import calendar



new = Tk()
new.config(background='grey')
new.title("Calendar")
new.geometry("400x200")
cal = Label(new, text="Calendar",bg='grey',font=("times", 28, "bold"))
year = Label(new, text="Enter year", bg='dark grey')
year_field=Entry(new)
button = Button(new, text='Show Calender',
fg='Black',bg='Blue')


new.mainloop()
