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

#putting widgets in position
cal.place(x=120,y=10)
year.place(x=165,y=70)
year_field.place(x=130,y=100)
button.place(x=145,y=140)


new.mainloop()
