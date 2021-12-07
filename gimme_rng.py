# jdv 09172021
from tkinter import *
import random

window_title = "gimme_rng"
# window_loc = ("120x48+1783+5") # upper right but hard coded
window_loc = ('120x36-0-27') # bottom right, general
update_time = 1500
font_color = "Red"
font_and_size = ("Helvetica", 26)
alpha = 1
background_color = 'black'

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg=font_color, font=font_and_size)
        self.label.place(relx=0.5, rely=0.5, anchor = 'center')
        self.label.configure(bg=background_color)
        self.label.bind("<Button-1>", self.quit)
        self.update_rng()

    def update_rng(self):
        n = round(random.random()*100)
        self.label.configure(text=n)
        self.after(update_time, self.update_rng)
        # print(self.master.geometry()) # for positional debugging

    def quit(self, event):
        self.master.destroy()

root = Tk()
app=App(root)
root.wm_title(window_title)
root.geometry(window_loc)
root.after(update_time, app.update_rng)
root.attributes('-alpha', alpha)
root.configure(bg=background_color)
root.overrideredirect(True) # no background
root.mainloop()
