import tkinter as tk
from random import choice
def getRandomColor():
    return choice(['red','blue','green','yellow','orange'])

def click(event):
    item = event.widget.find_withtag('current')
    event.widget.itemconfig(item,fill='black')
    
root = tk.Tk()
#root.grid()
c = tk.Canvas(root,width=300,height=300)
c.grid()

step=30
for i in range (0, 300, step) :
    for j in range(0, 300, step) :
        c.create_rectangle(i, j, step+i, step+j, fill=getRandomColor(),
                           tag = "%d"%(int(i/step) * int(300 / step) + (int(j/step) + 1)),
                           width=0)
c.bind("<Button-1>", click)    
root.mainloop()
