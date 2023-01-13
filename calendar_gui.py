#Importing tkinter module
from tkinter import *
#importing calendar module
import calendar

#function to show calendar of the given year
def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()


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
