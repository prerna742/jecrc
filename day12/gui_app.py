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

msg = ttk.Variable(app)
print(msg.get())
msg.set('Empty')
print(msg.get())


ttk.Label(app,text = 'A simple text Label').place(x=50,y=50)
ttk.Label(app,textvariable=msg).place(x=100,y=70)

def abc():
    print('Wow')
msg.set('jo tera man kare')

ttk.Button(app,text='Isko click krdo',command=abc).place(x=100,y=100) 
ttk.Button(app,text='Ye wala bhi hai',command = lambda:msg.set('pta nhi')).place(x=100,y=170)

f1 = ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result=ttk.Variable(app)

ttk.Entry(app,textvariable=f1,width=4,font=('Arial',22)).place(x=50,y=200)
ttk.Entry(app,textvariable=f2,font=('Arial',22)).place(x=150,y=200)
ttk.Label(app,text='Result').place(x=100,y=300)
ttk.Label(app,textvariable=result,font=('Arial',22)).place(x=100,y=330)

def calci(op):
    print('i will calculate')
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app,text='+',command=lambda:calci('+'),font=('Arial',22)).place(x=50,y=240)  
ttk.Button(app,text='-',command=lambda:calci('-'),font=('Arial',22)).place(x=100,y=240) 
ttk.Button(app,text='*',command=lambda:calci('*'),font=('Arial',22)).place(x=150,y=240) 
ttk.Button(app,text='/',command=lambda:calci('/'),font=('Arial',22)).place(x=200,y=240)  


box=ttk.Listbox(app,height=5,fg='red',activestyle='dotbox')
box.insert(1,'Sample1')
box.insert(2,'Sample2')
box.insert(3,'Sample3')
box.place(x=350,y=40)

def show():
    print(box.get(box.curselection()))
ttk.Button(app,text='show',command=show).place(x=350,y=250)







app.mainloop()