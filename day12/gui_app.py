# GUI - graphical user interface

#Libraries
##########
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk   
app = ttk.Tk()
app.title('my app')
app.geometry('600x400')

ttk.Label(app,text = 'A simple text Label').place(x=50,y=50)
ttk.Label(app,text = 'prerna chauhan').place(x=80,y=80)  
  
app.mainloop()