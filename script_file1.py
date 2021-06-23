# GUI Development using Tkinter
import tkinter as t

app = t.Tk()
app.title('Arithmetic Tool')
app.geometry('280x150')

result = t.Variable(app)
result.set('Result')
t.Label(app,textvariable=result).place(x=120,y=120)

first_val = t.Variable(app)
second_val = t.Variable(app)

t.Entry(app, textvariable=first_val, width=10).place(x=50,y=20)
t.Entry(app, textvariable=second_val, width=10).place(x=160,y=20)

def operate(e):
    first = first_val.get()
    second = second_val.get()
    exp = first + e + second
    #print(exp)
    result.set(eval(exp))

def plus():
    first = first_val.get()
    second = second_val.get()
    exp = first + '+' + second
    #print(exp)
    result.set(eval(exp))

def minus():
    first = first_val.get()
    second = second_val.get()
    exp = first + '-' + second
    #print(exp)
    result.set(eval(exp))
    
t.Button(app, text='+', width = 2, command=plus).place(x=50,y=70)
t.Button(app, text='-', width = 2, command=minus).place(x=100,y=70)
t.Button(app, text='x', width = 2, command=lambda:operate('*')).place(x=160,y=70)
t.Button(app, text='/', width = 2, command=lambda:operate('/')).place(x=210,y=70)



app.mainloop()


##t.Label(app, text = 'Hello').pack()
##t.Label(app, text = 'Bye').pack()
##t.Label(app, text = 'Hi').pack()

##t.Label(app, text = 'Hello').grid(row=0,column=0)
##t.Label(app, text = 'Bye').grid(row=1,column=1)
##t.Label(app, text = 'Hi').grid(row=2,column=1)

##t.Label(app, text = 'Hello').place(x=100, y=20)
##t.Label(app, text = 'Bye').place(x=130, y=80)
##t.Label(app, text = 'Hi').place(x=200, y=120)

##
##class Abc():
##    a=10
##    def fun(self,v):
##        print(self.a)
##        print('hello')
##
