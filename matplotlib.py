from tkinter import *
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk

f = open('age.csv', 'r')
data = csv.reader(f)
header = next(data)

fig = Figure(figsize = (6, 4))
fig2 = Figure(figsize=(6, 4))
x = range(0, 101, 10)
ax1 = fig.add_subplot(1,1,1)
ax2 = fig2.add_subplot(1,1,1)

def listInsert() :
    order = 0
    for row in data :
        listBox.insert(order, row[0])
        order += 1

def clear():
    for item in cvs_map.get_tk_widget().find_all() :
        cvs_map.get_tk_widget().delete(item)

def insert_data() :
    text.delete('1.0', 'end')
    
    global Tdata
    Tdata = []
        
    num = list(listBox.curselection())[0]+1
        
    f = open('age.csv', 'r')
    
    data = f.readlines()
    Tdata = data[num].split(',')
    
    for i in range(0, len(header)) :
        text.insert(END, header[i] + " : " + Tdata[i] + "\n")
    text.configure(font=("Malgun Gothic", 9))
        
def map_draw() :
    global ax1, ax2, x
    
    ax1.clear()
    ax2.clear()
    
    num = list(listBox.curselection())[0]+1
    
    total, man, woman = [0]*11, [0]*11, [0]*11

    for i in range(0, len(Tdata)):
        if i >= 3 and i< 14 :
            total[i-3] = int(Tdata[i])
        
        elif i >= 16 and i < 27 :
            man[i-16] = int(Tdata[i])
    
        elif i >= 29 :
            woman[i-29] = int(Tdata[i])
            
    ax1.plot(x, total, label = "Total")
    ax1.plot(x, man, label = "Man")
    ax1.plot(x, woman, label = "Woman")
    ax1.set_xlabel("age")
    ax1.set_ylabel("value")
    ax1.set_title("plot graph")
    
    fig.legend()
    cvs_map.draw()
    
    for i in range(0, len(woman)) :
        woman[i] = -woman[i]

    ax2.barh(x, woman, height = 3, label = "Woman")
    ax2.barh(x, man, height = 3, label = "Man")
    ax2.set_ylabel("age")
    ax2.set_xlabel("value")
    ax2.set_title("barh graph")
    
    fig2.legend()
    cvs_map2.draw()

def view_data() :
    insert_data()
    map_draw()


if __name__=="__main__" :
    # root
    root = Tk()
    root.title("행정구역별 인구 데이터 조회")
    root.geometry("1900x1000+0+0")

    # frame_top
    frame_left = Frame(root)
    frame_left.pack(side = "left", fill = "both", expand = True)

    #frame_bottom
    frame_right = Frame(root)
    frame_right.pack(side = "right", fill = "both", expand = True)

    # frame_list
    frame_list = Frame(frame_left)
    frame_list.pack(side = "top", fill = "both", expand = True)

    label_list = Label(frame_list, text = "행정구역 선택")
    label_list.pack(side = "top", fill = "x")

    btn_choice = Button(frame_list, text = "선택", command = view_data)
    btn_choice.pack(side = "bottom", fill = "x")

    scroll_list = Scrollbar(frame_list)
    scroll_list.pack(side = 'right', fill = 'y')

    listBox = Listbox(frame_list, selectmode = "single", height = 0, yscrollcommand = scroll_list.set)
    listInsert()
    listBox.pack(side = 'left', fill = 'both', expand = True)

    scroll_list.config(command = listBox.yview)

    # frame_data
    frame_data = Frame(frame_right)
    frame_data.pack(side = "top", fill = "both", expand = True)

    label_data = Label(frame_data, text = "해당 행정구역 인구 수")
    label_data.pack(side = "top", fill = "x")

    scroll_data = Scrollbar(frame_data)
    scroll_data.pack(side = 'right', fill = 'y')

    text = Text(frame_data, yscrollcommand = scroll_data.set)
    text.pack(side = "left", fill = "both", expand = True)

    scroll_data.config(command = text.yview)

    # frame_map
    frame_map = Frame(frame_right)
    frame_map.pack(side = "top", fill = "both", expand = True)

    cvs_map = FigureCanvasTkAgg(fig, master=frame_map)
    cvs_map.draw()
    cvs_map.get_tk_widget().pack(side = "left", fill = "both", expand = True)

    # frame_map2
    frame_map2 = Frame(frame_right)
    frame_map2.pack(side = "top", fill = "both", expand = True)

    cvs_map2 = FigureCanvasTkAgg(fig2, master=frame_map2)
    cvs_map2.draw()
    cvs_map2.get_tk_widget().pack(side = "left", fill = "both", expand = True)

    root.mainloop()