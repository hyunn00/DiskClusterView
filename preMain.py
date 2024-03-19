from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import choice


# 라인 그리기 함수
def lineDraw() :
    window.update()
    global lineWidth, gapSpace
    sizeValue = input_value.sizeValue

    if window.winfo_width() >= window.winfo_height() :
        gapSpace = int(canvas.winfo_width() / sizeValue)
    elif window.winfo_width() < window.winfo_height() :
        gapSpace = int(canvas.winfo_height() / sizeValue)

    wstartX, wstartY, wstopX, wstopY = 0, 0, 0, 0
    hstartX, hstartY, hstopX, hstopY = 0, 0, 0, 0
    wstopX = gapSpace * sizeValue
    hstopY = gapSpace * sizeValue
    
    for i in range(0, gapSpace) :
        line = canvas.create_line(wstartX, wstartY, wstopX, wstopY,
                                  fill = "light gray", width = lineWidth)
        wstartY += sizeValue
        wstopY += sizeValue
        
        for j in range (0, gapSpace) :
            canvas.create_line(hstartX, hstartY, hstopX, hstopY,
                                  fill = "light gray", width = lineWidth)
            hstartX += sizeValue
            hstopX += sizeValue
    ColorFill()


# 셀 단위 색 채우기
def ColorFill() :
    window.update()
    global countColumn, countRow, cWidth, cHeight, startX, startY, stopX, stopY
    sizeValue = input_value.sizeValue

    if window.winfo_width() >= window.winfo_height() :
        gapSpace = int(canvas.winfo_width() / sizeValue)
    elif window.winfo_width() < window.winfo_height() :
        gapSpace = int(canvas.winfo_height() / sizeValue)

    for countRow in range (0, gapSpace) :
        for countColumn in range(0, gapSpace) :
            startX = countRow*sizeValue
            startY = countColumn*sizeValue
            stopX = sizeValue+countRow*sizeValue
            stopY = sizeValue+countColumn*sizeValue
            
            canvas.create_rectangle(startX, startY, stopX, stopY,
                               fill="white", width=lineWidth,
                               outline = "light gray", tags="rect")


# canvas 확대 함수
def ZoomIn() :
    global sizeValue
    ZoomIn.sizeValue = int(input_value.sizeValue+1)
    input_value(ZoomIn.sizeValue)
    canvas.delete(ALL)
    lineDraw()
ZoomIn.sizeValue = 10


# canvas 축소 함수
def ZoomOut() :
    global sizeValue
    ZoomOut.sizeValue = int(input_value.sizeValue-1)
    input_value(ZoomOut.sizeValue)
    canvas.delete(ALL)
    lineDraw()
ZoomIn.sizeValue = 10


# 라인 간격 조정에 따른 변수 값 저장 함수
def input_value(sizeValue) :
    if input_value.sizeValue > sizeValue :
        input_value.sizeValue = ZoomOut.sizeValue
        if input_value.sizeValue < 5 :
            input_value.sizeValue = 5
        
    elif input_value.sizeValue < sizeValue :
        input_value.sizeValue = ZoomIn.sizeValue
        if input_value.sizeValue > 20 :
            input_value.sizeValue = 20
input_value.sizeValue = 10


# 랜덤 셀 색 지정            
def getRandomColor():
    return choice(['blue','red','green1','yellow','white', 'light green', 'dark blue'])


# 랜덤 셀 수 지정
def getRandomNum() :
    return choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


# 창 크기 조정에 따른 lineDraw 함수 호출
def configure(event) :
    canvas.delete(ALL)

    lineDraw()
    ColorFill()
    
    canvas.configure(scrollregion = canvas.bbox("all"))


# mouseWheel에 scrollbar 연동
def mousewheel(event) :
    global scrollCount
    sizeValue = input_value.sizeValue
    
    if window.winfo_width() >= window.winfo_height() :
        gapSpace = int(canvas.winfo_width() / sizeValue)
    elif window.winfo_width() < window.winfo_height() :
        gapSpace = int(canvas.winfo_height() / sizeValue)
        
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    if event.delta > 0 :
        scrollCount -= 1
        if scrollCount < 0 :
            scrollCount = 0
    elif event.delta < 0 :
        if scrollCount > gapSpace / sizeValue + int(-1*(event.delta/120)) :
            scrollCount -= 1
        scrollCount += 1


# canvas 클릭시 섹션 번호 출력함수
def click(event) :
    window.update()
    global countColumn, countRow, cWidth, cHeight
    sizeValue = input_value.sizeValue
    
    cellNum = getRandomNum()
    
    # 섹션 번호 출력
    if window.winfo_width() >= window.winfo_height() :
        gapSpace = int(canvas.winfo_width() / sizeValue)
    elif window.winfo_width() < window.winfo_height() :
        gapSpace = int(canvas.winfo_height() / sizeValue)

    for i in range(0, gapSpace) :
        if event.y >= i * sizeValue and event.y <= (i+1) * sizeValue :
            countRow = i
        for j in range(0, gapSpace) :
            if event.x >= j * sizeValue and event.x <= (j+1) * sizeValue :
                countColumn = j

    # 클릭시 랜덤 수만큼 파란색 박스 출력
    Count = 0

    for i in range (0, gapSpace) :
        if i < countRow  :
            continue;
        for j in range(0, gapSpace) :
            if j < countColumn and Count == 0 :
                continue;
            else   :
                startX = j*sizeValue
                startY = (i+scrollCount*2)*sizeValue
                stopX = sizeValue+j*sizeValue
                stopY = sizeValue+(i+scrollCount*2)*sizeValue
            
                canvas.create_rectangle(startX, startY, stopX, stopY,
                               fill='blue', width=lineWidth,
                               outline = "light gray", tags="rect")

                Count += 1

                if Count >= cellNum :
                    break;
        if Count >= cellNum :
            break;   
        
    spaceOrder = countRow * gapSpace + (countColumn+1) + scrollCount * gapSpace * 2
            
    messagebox.showinfo("클릭위치", spaceOrder)
                        
# 전역변수
cWidth, cHeight = 300, 200
lineWidth = 1
gapSpace = 0
sizeValue = 10
spaceOrder=0
countColumn, countRow = 0, 0
scrollCount=0


# main
window = Tk()
window.resizable(1, 1)

frame = Frame(window, relief = "flat", bd = 1)
frame.pack(padx = 5, pady = 5, fill = BOTH, expand = 1)

canvas = Canvas(frame, width = cWidth, height = cHeight, bg = "white")
canvas.bind("<Button-1>", click)
canvas.bind("<Configure>", configure)
canvas.bind_all("<MouseWheel>", mousewheel)

scrollbar = Scrollbar(frame, command = canvas.yview)
canvas.configure(yscrollcommand = scrollbar.set)

scrollbar.pack(side = "right", fill = "y")
canvas.pack(fill = BOTH, expand = 1, anchor = NW)

btnZoomIn = Button(window, text = "+", command = ZoomIn)
btnZoomOut = Button(window, text = "-", command = ZoomOut)
btnZoomIn.pack()
btnZoomOut.pack()

window.update()

window.mainloop()
