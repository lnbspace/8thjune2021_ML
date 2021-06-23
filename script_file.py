import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as tfd
from PIL import ImageTk, Image

app = tk.Tk()
app.title('Testing App')
app.geometry('300x800')

label = tk.Variable(app)
label.set('Simple Text')
tk.Label(app,textvariable = label).pack()

msg = tk.Variable(app)
msg.set('''first line
second line
third line''')
tk.Message(app,textvariable = msg).pack()

entry = tk.Variable(app)
entry.set('0')
tk.Entry(app,textvariable = entry).pack()

def cmd():
    print('clicked')
    print(sp.get())
    print('Python',cb1.get())
    print('DS',cb2.get())
    print('Batch:',rb.get())
    print('Combo:',cmb.get())
    if cmb.get() == 'Project 4':
        cmb_box['values'] = ('Topic 1','Topic 2')
        cmb.set("")
    print(opt.get())
    print(list_box.curselection())
    print(list_box.get(list_box.curselection()))
    
    
tk.Button(app,text='Click', command = cmd).pack()

sp = tk.Variable(app)
#sp = tk.IntVar(app)
tk.Spinbox(app, from_= 0, to=100, textvariable=sp).pack()


cb1 = tk.Variable(app, "0")
cb2 = tk.Variable(app, "0")
tk.Checkbutton(app, text='Python',
               variable=cb1, onvalue=1,offvalue=0,).pack()
tk.Checkbutton(app, text='Data Science',
               variable=cb2, onvalue=1,offvalue=0,).pack()



rb = tk.Variable(app, "1")
values = {'8th June - ML': '1', '15th June - ML':'2',
          '8th June - AI': '3', '15th June - AI':'4',}
for k,v in values.items():
    tk.Radiobutton(app, text=k, variable=rb, value=v).pack()


cmb = tk.Variable(app)
cmb_values = ('Project 1','Project 2','Project 3','Project 4')
cmb_box = ttk.Combobox(app, textvariable=cmb, values=cmb_values)
cmb_box.pack()

opt = tk.Variable(app)
opt_values = ('ML','DL')
opt_menu = tk.OptionMenu(app, opt, *opt_values)
opt_menu.pack()


lb = tk.Variable(app)
list_box = tk.Listbox(app, height = 5,
                      activestyle='dotbox',
                      fg = 'red')
list_box.insert(1, 'Face Recognition')
list_box.insert(2, 'Gesture Recognition')
list_box.insert(3, 'Speech Recognition')
list_box.pack()

def opn():
    global can
    global img
    file = tfd.askopenfiles(mode='r',
                        filetypes = [('Images','*.png')])
    if file:
        file_name = file[0].name        
        img = ImageTk.PhotoImage(Image.open(file_name))
        can.create_image(0,0,anchor=tk.NW, image = img)        
    print(file)

tk.Button(app, text = 'Select Image', command = opn).pack()


can = tk.Canvas(app,width=300,height=300)
can.pack()




app.mainloop()




















