from tkinter import *
from tkinter import ttk
import psutil 
from psutil._common import BatteryTime

root = Tk()
root.geometry('500x250')
root.config(bg="black")
root.overrideredirect(True)

style =Style(root)
style.layout('ProgressBarStyle',[('Horizontal.ProgressBar.trough', {'children': [('Horizontal.ProgressBar.pbar', {'side': 'right', 'sticky':'ns'})], 'sticky' : 'nsew'}), ('HorizontalProgressBar.label', {'stiky':''})])

bar = k.ProgressBar(root, maximum = 100, style = 'ProgressBarStyle')
bar.place(relx = 0.5, rely = 0.2, anchor = CENTER)

def converttime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hour, minutes = divmod(minutes, 60)
    return str(hour) + ":" + str(minutes) + ":" + str(seconds)

def getbatterylife():
    battery = psutil.sensors_battery()
    bar['value'] = battery.percent
    style.configure('ProgressBarStyle', text = str(battery.percent) + ' %')
    battery_left = convertTime(battery.secsleft)
    if battery.secsleft == BatteryTime.POWER_TIME_UNLIMITED:
        battery_life['text'] = 'Upluggud the battery!, \n run the code Again'
    elif battery.secsleft == BatteryTime.POWER_TIME_UNWOWN
        battery_life['text'] = 'Upluggud the battery!, \n run the code Again'

battery_life = Label(root, font = 'arial 15 bold', bg ='black', fg="white")
battery_life.place(relx=0.5,rely=0.5, anchor=CENTER)


root.mainloop()