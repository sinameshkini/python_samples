#!/usr/bin/python

#import the required libraries
import datetime
import time
from tkinter import *

#Functions for splitting the different components of date and time
def nowYear():
    now = datetime.datetime.now()
    year = now.year
    return str(year)

def nowMonth():
    now = datetime.datetime.now()
    month = now.month
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"

def nowDay():
    now = datetime.datetime.now()
    day = now.day
    return str(day)

def nowHour():
    now = datetime.datetime.now()
    hour = now.hour
    return str(hour)

def nowMinute():
    now = datetime.datetime.now()
    minute = now.minute
    return str(minute)

def nowSecond():
    now = datetime.datetime.now()
    second = now.second
    return str(second)

########################################################
######################FRAMEWORK#########################
########################################################

def year_label(label):
  def count1():
    label.config(text=nowYear())
    label.after(1000, count1)
  count1()

def month_label(label):
  def count2():
    label.config(text=nowMonth())
    label.after(1000, count2)
  count2()

def day_label(label):
  def count3():
    label.config(text=nowDay())
    label.after(1000, count3)
  count3()

def hour_label(label):
  def count4():
    label.config(text=nowHour())
    label.after(1000, count4)
  count4()

def minute_label(label):
  def count5():
    label.config(text=nowMinute())
    label.after(1000, count5)
  count5()

def second_label(label):
  def count6():
    label.config(text=nowSecond())
    label.after(1000, count6)
  count6()

root = Tk()
root.title("Clock")

#############################Menu################################
def about():
   filewin = Toplevel(root)
   tx ="""
    Clock program 2014 -
    by Pooria Taghdiri
    saakhtani.ir
    """
   message = Message(filewin, text=tx, relief = RIDGE , width = 170)
   message.pack(fill="both", expand="yes")


menubar = Menu(root)

filemenu = Menu(menubar)
filemenu.add_command(label="Exit", command = root.quit)
menubar.add_cascade(label="File", menu = filemenu)

helpmenu = Menu(menubar)
helpmenu.add_command(label = "About...", command = about)
menubar.add_cascade(label = "Help", menu = helpmenu)

root.config(menu = menubar)

#############################TIME################################
labelframe = LabelFrame(root, text="Time:" , font=("Ravie", 18))
labelframe.pack(fill="both", expand="yes")

hourLabel = Label(labelframe, relief = GROOVE, bd = 5,
                  width = 7,font=("Ravie", 15))
hourLabel.pack(side = LEFT, expand="yes")
hour_label(hourLabel)

colon = Label(labelframe, text = ":")
colon.pack(side = LEFT, expand="yes")

minuteLabel = Label(labelframe, text = nowMinute(),
                    relief = GROOVE, bd = 5, width = 7,font=("Ravie", 15))
minuteLabel.pack(side = LEFT, expand="yes")
minute_label(minuteLabel)

colon = Label(labelframe, text = ":")
colon.pack(side = LEFT, expand="yes")

secondLabel = Label(labelframe, text = nowSecond(),
                    relief = GROOVE, bd = 5, width = 7,font=("Ravie", 15))
secondLabel.pack(side = LEFT, expand="yes")
second_label(secondLabel)

#############################DATE################################
labelframe1 = LabelFrame(root, text="Date:", font=("Ravie", 18))
labelframe1.pack(fill="both", expand="yes")

dayLabel = Label(labelframe1, text = nowSecond(),
                 relief = GROOVE, bd = 5, width = 7, font=("Ravie", 15))
dayLabel.pack(side = LEFT, expand="yes")
day_label(dayLabel)

monthLabel = Label(labelframe1, text = nowSecond(),
                   relief = GROOVE, bd = 5, width = 9, font=("Ravie", 15))
monthLabel.pack(side = LEFT, expand="yes")
month_label(monthLabel)

yearLabel = Label(labelframe1, text = nowSecond(),
                  relief = GROOVE, bd = 5, width = 7, font=("Ravie", 15))
yearLabel.pack(side = LEFT, expand="yes")
year_label(yearLabel)

#################################################################
time.sleep(1)
root.mainloop()
