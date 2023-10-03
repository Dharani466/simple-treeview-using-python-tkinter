import tkinter
from tkinter import ttk
win=tkinter.Tk()
h=win.winfo_screenheight()
w=win.winfo_screenwidth()
win.configure(height=h,width=w)
win.title('treeview practice')


tree=ttk.Treeview(win)
tree['columns']=('name','position','salary')
#column sizes
tree.column('#0',width=0,stretch='NO')
tree.column('name',width=100)
tree.column('position',width=150)
tree.column('salary',width=80)
#column headings
tree.heading('#0',text='')
tree.heading('name',text='NAME')
tree.heading('position',text='POSITION')
tree.heading('salary',text='PAYSCALE')
data=[['Dharani','cloud architect',69000],['Priya','software developer',100000],['Deepika','testing',50000],['Hema','Architecture',90000]]
global count
count=0
for i in data:
       tree.insert(parent='',index='end',iid=count,values=(i[0],i[1],i[2]))
       count+=1
tree.pack(pady=20)

#creating frames
frm=tkinter.Frame(win)
frm.pack(pady=20)

lb1=tkinter.Label(frm,text='NAME',font=('arialbalck',15,'bold'))
lb2=tkinter.Label(frm,text='POSITION',font=('arialbalck',15,'bold'))
lb3=tkinter.Label(frm,text='PAYSCALE',font=('arialbalck',15,'bold'))
lb1.grid(row=0,column=0)
lb2.grid(row=0,column=1)
lb3.grid(row=0,column=2)


tb1=tkinter.Entry(frm,font=('arialblack',15,'bold'))
tb2=tkinter.Entry(frm,font=('arialblack',15,'bold'))
tb3=tkinter.Entry(frm,font=('arialblack',15,'bold'))
tb1.grid(row=1,column=0)
tb2.grid(row=1,column=1)
tb3.grid(row=1,column=2)

def add_record():
      global count
      tree.insert(parent='',index='end',iid=count,values=(tb1.get(),tb2.get(),tb3.get()))
      count+=1
      tb1.delete(0,'end')
      tb2.delete(0,'end')
      tb3.delete(0,'end')
      tb1.focus()

def rem_record():
    x=tree.selection()
    tree.delete(x)

def rem_sel_record():
    x=tree.selection()
    for i in x:
        tree.delete(i)
def rem_all_record():
    x=tree.get_children()
    for i in x:
        tree.delete(i)
        

#buttons
add=tkinter.Button(win,text='Add Record',font=('arialblack',15,'bold'),fg='green',bg='yellow',command=add_record)
add.pack(pady=10)

#remove data
rem=tkinter.Button(win,text='Remove Record',font=('arialblack',15,'bold'),fg='green',bg='red',command=add_record)
rem.pack(pady=10)

#remove selection record
rem_sel=tkinter.Button(win,text='Remove Selection Record',font=('arialblack',15,'bold'),fg='green',bg='pink',command=rem_sel_record)
rem_sel.pack(pady=10)

#rem all record
rem_all=tkinter.Button(win,text='Remove All Record',font=('arialblack',15,'bold'),fg='green',bg='yellow',command=rem_all_record)
rem_all.pack(pady=10)



win.mainloop()
            
