from tkinter import *
import math
import binascii
import os

# tCanvas Drawing
def mainDraw() :
    global lineWidth, numGridX, numGridY, hy, sh, moveNum
    sizeGrid=input_value.sizeValue
    tCanvas.delete(ALL)

        
    cWidth=tCanvas.winfo_width()-(sizeGrid-1) #화면 오른쪽 끝에서 격자가 반쯤 그려지는 걸 막기 위해서 설정함.
    cHeight= window.winfo_height()
    
    numGridX=int(cWidth/sizeGrid)
    #y방향으로 몇 라인 그릴지는 클러스터의 수에 따라 결정된다.
    #격자크기x한줄격자수x는 x방향크기와 같다. print('numGridY=',numGridY)
    numGridY=int(totalClusters/numGridX)

    # 캔버스 전체 범위 확보
    i = totalClusters -1
    numLine=int(i/numGridX)
    posY=numLine *sizeGrid
    posX=(i%numGridX)*sizeGrid
    tCanvas.create_rectangle(0, 0, sizeGrid, sizeGrid,outline="light gray",
                                    fill = "white", width = lineWidth)
    tCanvas.create_rectangle(posX, posY, posX+sizeGrid, posY+sizeGrid,outline="light gray",
                                    fill = "white", width = lineWidth)
    
    sy = int(sh * numGridY * sizeGrid) # 스크롤 했을 때 화면에 보이는 y좌표
    start = int((sy // sizeGrid) * numGridX) # 그리기 시작할 셀 번호
    viewLine = int(cHeight / sizeGrid) # 화면에 보이는 부분에 그려지는 줄 수
    end = viewLine * numGridX + start # 마지막으로 그리는 셀 번호
    if start + end >= totalClusters : # 계산 결과가 totalClusters보다 커지는 경우를 방지하기 위한 if문
        end = totalClusters

    for i in range(start, end):
        numLine = int(i/numGridX)
        posY = numLine * sizeGrid
        posX = (i % numGridX) * sizeGrid
            
        if((i%100)==0):
            tCanvas.create_rectangle(posX, posY, posX+sizeGrid, posY+sizeGrid,outline="light gray",
                                    fill = "red", width = lineWidth)
            lineDraw(i)
        else:
            tCanvas.create_rectangle(posX, posY, posX+sizeGrid, posY+sizeGrid,outline="light gray",
                                    fill = "white", width = lineWidth)
        

    
def lineDraw(num) :
    sWidth = sCanvas.winfo_width()-10
    sHeight = sCanvas.winfo_height()-10
    sArea = sWidth * sHeight
    cellArea = sArea/totalClusters
    cW = lineWidth
    cH = math.ceil(cellArea)
    line = int(sHeight / cH)
    numY = num % (line)
    numX = int(num / (line))
    sy = numY * cH +2
    sx = numX+2
    sCanvas.create_line(sx, sy, sx, sy+cH, fill = "red", width =cW)


# tCanvas ZoomIn
def ZoomIn() :
    global sizeValue
    ZoomIn.sizeValue = int(input_value.sizeValue+1)
    input_value(ZoomIn.sizeValue)
    tCanvas.delete(ALL)
    mainDraw()
    tCanvas.configure(width = window.winfo_width()-250, height = window.winfo_height()-250,
                      scrollregion = tCanvas.bbox("all"))

ZoomIn.sizeValue = 10


# tCanvas ZoomOut
def ZoomOut() :
    global sizeValue
    ZoomOut.sizeValue = int(input_value.sizeValue-1)
    input_value(ZoomOut.sizeValue)
    tCanvas.delete(ALL)
    mainDraw()
    tCanvas.configure(width = window.winfo_width()-250, height = window.winfo_height()-250,
                      scrollregion = tCanvas.bbox("all"))

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



# tCanvas configure
def tConfigure(event) :
    tCanvas.delete("all")

    mainDraw()

    tCanvas.configure(width = window.winfo_width()-250, height = window.winfo_height()-250,
                      scrollregion = tCanvas.bbox("all"))


# sCanvas configure
def sConfigure(event) :
    sCanvas.delete("all")
    
    mainDraw()
    #sCanvas.configure(scrollregion = sCanvas.bbox("all"))


# tCanvas Click
def tClick(event) :
    global sizeGrid, thisNum
    sizeGrid = input_value.sizeValue

    mouseCanvasX, mouseCanvasY = tCanvas.canvasx(event.x), tCanvas.canvasy(event.y)
    clickPosX, clickPosY = int(mouseCanvasX / sizeGrid), int(mouseCanvasY/sizeGrid)
    
    thisNum = clickPosX + (numGridX * clickPosY) + 1

    clusterN.delete(0, "end")
    clusterN.insert(0, thisNum)
    
    #sx, sy = sCanvas.canvasx(event.x), sCanvas.canvasy(event.y)


# sCanvas Click
def sClick(event) :
    sx, sy = sCanvas.canvasx(event.x), sCanvas.canvasy(event.y)
    
    cWidth = window.winfo_width()

    # sCanvas에서 마우스 클릭한 위치로 tCanvas 창의 내용을 스크롤업/다운
    tCanvas.update_idletasks()
    tCanvas.yview_moveto(sx/cWidth)


# Button-2 Func
def delete(dummy_event):
    global clusterNo

    class Pointer() :
        def __init__(self) :
            self.b_List = []


    def drawCluster(f, clusterNo) :
        global CLUSTER_SIZE

        position = CLUSTER_SIZE * clusterNo
        p = Pointer()
        hexdump(p, CLUSTER_SIZE, position)

    def hexdump(p, n, a) :
        global r
        i, j = 0, 0
        pos = ''
        hexS = ''
        hexSP = ''
        ascS = ''
    
        while(n > 0) :
            if n >= 16 :
                i = 16
            else :
                i = n

            f.seek(a)
            p = Pointer()
        
            pos = '{:08x} :'.format(a)
    
            for j in range(0, i) :
                p.b_List.append(f.read(1))
                hexS += ' ' + p.b_List[j].hex()
            
            for j in range(i, 16) :
                hexSP += '  '


            for j in range (0, 16) :
                s = p.b_List[j].decode()
                if s == '\n' :
                    s = '\\n'
                ascS += s
            
            text.insert(END, pos+hexS+hexSP+' | '+ascS+'\n')
            text.pack()

            del(p.b_List)
        
            n -= i
            a += i
            r += 1

    def data() :
        clusterNo = 0
        f = open("forecasts1.csv", "rb")

        text.insert(END, "clusterNo = %d\n\n" % clusterNo)
        text.pack()

        for clusterNo in range(clusterNo, clusterNo+400) :
            drawCluster(f, clusterNo)
            
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    delWin = Toplevel()
    delWin.geometry("600x400+0+0")
    delWin.title("Hexdump")
    delWin.resizable(True, True)
                        
    frame = Frame(delWin)
    frame.pack(fill = BOTH, expand = 1)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill = "y")

    text = Text(frame, yscrollcommand = scrollbar.set)
    text.pack(side = LEFT, fill = BOTH, expand = 1)

    data()

    scrollbar.config(command=text.yview)
    delWin.mainloop()
    

# Cluster Properties window
def newWindow(dummy_event) :
    newWin = Toplevel()
    newWin.geometry("300x500+0+0")
    newWin.title("Cluster Properties")
    newWin.resizable(True, True)

    # newWin exit
    def win_exit() :
        newWin.destroy()
        newWin.update()
        
    label1 = Label(newWin, text = "Cluster on Disk :", pady = 10)
    label1.grid(row= 0, column = 0, sticky = "W")

    txt1 = Entry(newWin)
    txt1.insert(0, "%d" % thisNum)
    txt1.configure(state="readonly")
    txt1.grid(row= 0, column = 1, sticky = "W", padx = 10, pady = 10)

    
    label2 = Label(newWin, text = "File Path :", pady = 10)
    label2.grid(row= 1, column = 0, sticky = "W")
    
    txt2 = Entry(newWin)
    # txt2.insert(0, "%s" % (선택한 클러스터의 경로))
    txt2.configure(state="readonly")
    txt2.grid(row= 1, column = 1, sticky = "W", padx = 10, pady = 10)

    
    label3 = Label(newWin, text = "File Cluster :", pady = 10)
    label3.grid(row= 2, column = 0, sticky = "W")
    
    txt3 = Entry(newWin)
    #txt3.insert(0, "%d of %d {%s}" % (선택한 클러스터의 전체 수 중 x 번째, 그리고 그 클러스터의 타입))
    txt3.configure(state="readonly")
    txt3.grid(row= 2, column = 1, sticky = "W", padx = 10, pady = 10)

    
    label4 = Label(newWin, text = "File Fragments :", pady = 10)
    label4.grid(row= 3, column = 0, sticky = "W")

    btnOk = Button(newWin, text = "OK", command = win_exit)
    btnOk.grid(row =4, column = 1, sticky = "n")


#Volume Properties
def Vproperties() :
    volWin = Toplevel()
    volWin.geometry("250x150+0+0")
    volWin.title("Volume Properties")
    volWin.resizable(True, True)

    import shutil

    diskLabel = 'c:\\'
    total, used, free = shutil.disk_usage(diskLabel)

    label1 = Label(volWin, text = "Files :", pady = 10)
    label1.grid(row= 0, column = 0, sticky = "W")

    txt1 = Entry(volWin)
    txt1.insert(0, "%d" % (total))
    txt1.configure(state="readonly")
    txt1.grid(row= 0, column = 1, sticky = "W", padx = 10, pady = 10)

    
    label2 = Label(volWin, text = "Fragments :", pady = 10)
    label2.grid(row= 1, column = 0, sticky = "W")
    
    txt2 = Entry(volWin)
    txt2.insert(0, "%d" % (used))
    txt2.configure(state="readonly")
    txt2.grid(row= 1, column = 1, sticky = "W", padx = 10, pady = 10)

    
    label3 = Label(volWin, text = "% Free Space :", pady = 10)
    label3.grid(row= 2, column = 0, sticky = "W")
    
    txt3 = Entry(volWin)
    txt3.insert(0, "%0.2f%%" % float(100*(free/total)))
    txt3.configure(state="readonly")
    txt3.grid(row= 2, column = 1, sticky = "W", padx = 10, pady = 10)

    btnOk = Button(volWin, text = "OK")
    btnOk.grid(row =4, column = 1, sticky = "n")


# DiskView Legend
def Legend() :
    legend = Toplevel()
    legend.geometry("350x350+0+0")
    legend.title("DiskvView Legend")
    legend.resizable(True, True)

    color1 = Entry(legend, readonlybackground = 'dark blue')
    color1.configure(state="readonly")
    color1.grid(row= 0, column = 0, sticky = "W", padx = 10, pady = 10)

    label1 = Label(legend, text = "First cluster of file fragment", pady = 10)
    label1.grid(row= 0, column = 1, sticky = "W")

    color2 = Entry(legend, readonlybackground = 'blue')
    color2.configure(state="readonly")
    color2.grid(row= 1, column = 0, sticky = "W", padx = 10, pady = 10)
    
    label2 = Label(legend, text = "contiguous file cluster", pady = 10)
    label2.grid(row= 1, column = 1, sticky = "W")

    color3 = Entry(legend, readonlybackground = 'red')
    color3.configure(state="readonly")
    color3.grid(row= 2, column = 0, sticky = "W", padx = 10, pady = 10)
    
    label3 = Label(legend, text = "Fragmented file cluster", pady = 10)
    label3.grid(row= 2, column = 1, sticky = "W")

    color4 = Entry(legend, readonlybackground = 'green1')
    color4.configure(state="readonly")
    color4.grid(row= 3, column = 0, sticky = "W", padx = 10, pady = 10)

    label4 = Label(legend, text = "System file cluster", pady = 10)
    label4.grid(row= 3, column = 1, sticky = "W")

    color5 = Entry(legend, readonlybackground = 'white')
    color5.configure(state="readonly")
    color5.grid(row= 4, column = 0, sticky = "W", padx = 10, pady = 10)
    
    label5 = Label(legend, text = "Unused cluster", pady = 10)
    label5.grid(row= 4, column = 1, sticky = "W")

    color6 = Entry(legend, readonlybackground = 'light green')
    color6.configure(state="readonly")
    color6.grid(row= 5, column = 0, sticky = "W", padx = 10, pady = 10)
    
    label6 = Label(legend, text = "Unused cluster in MFT zone", pady = 10)
    label6.grid(row= 5, column = 1, sticky = "W")

    color7 = Entry(legend, readonlybackground = 'yellow')
    color7.configure(state="readonly")
    color7.grid(row= 6, column = 0, sticky = "W", padx = 10, pady = 10)
    
    label7 = Label(legend, text = "User highlighted file cluster", pady = 10)
    label7.grid(row= 6, column = 1, sticky = "W")
    
    btnOk = Button(legend, text = "OK")
    btnOk.grid(row = 7, column = 1)


def pop_window(dummy_event) :
    top = Toplevel(window)
    Label(top, text=f'popup window \nfor data: {data}').pack()


# window exit
def win_exit() :
    window.quit()
    window.destroy()

def pageUp() :
    global firstLine, numGridY
    sizeGrid=input_value.sizeValue
    
    viewLine = int(cHeight / sizeGrid)
    
    tCanvas.yview_scroll(-1, "pages") # 위로 스크롤
    f, l = scrollbar.get()
    
    firstLine -= viewLine # 화면에 보이는 줄 수 만큼 줄 수 증가
    if f == 0.0 :
        firstLine += viewLine # 스크롤바가 맨위면 더이상 감소x
        
    sy = firstLine / numGridY # 이동하려는 스크롤 위치
    #tCanvas.yview_moveto(sy)
    mainDraw()
    return "break"

def pageDown() :
    global firstLine, numGridY
    sizeGrid=input_value.sizeValue
    
    viewLine = int(cHeight / sizeGrid) # 화면에 보이는 줄 수 계산

    tCanvas.yview_scroll(-1, "pages") # 아래로 스크롤
    f, l = scrollbar.get()

    firstLine += viewLine # 화면에 보이는 줄 수 만큼 줄 수 증가
    if l == 1.0 :
        firstLine -= viewLine # 스크롤바가 맨밑이면 더이상 증가x

    sy = firstLine / numGridY # 이동하려는 스크롤 위치
    #tCanvas.yview_moveto(sy)
    mainDraw()
    return "break"

def scroll_sh(scroll, first, last) :
    global f1, f2, sh
    f2, l2 = float(first), float(last)
    scroll.set(f2, l2)
    sh = f2 - f1
    mainDraw()


def getClusterNo(n) :
    global numGridX, numGridY

    i = int(clusterN.get()) # entry에 입력된 값 저장
    numLine=int(i/numGridX) # 값이 몇번째 줄에 해당되는지 계산

    sy = numLine / numGridY # 이동하려는 스크롤 위치

    #tCanvas.yview_moveto(sy)
    mainDraw()


# 전역 변수 선언
cWidth, cHeight = 750, 500
totalClusters = 1000000
lineWidth = 1
sizeValue = 10
sizeGrid=sizeValue
mouseX,mouseY=0,0
numGridX,numGridY=0,0
thisNum = 0
position = 0
CLUSTER_SIZE = 16
f = open('forecasts1.csv', 'rb')
r=1
f1, l1 = 0.0, 0.0
sh = 0.0
moveNum=0
firstLine = 1

# main
if __name__=="__main__" :
    window = Tk()
    window.geometry("%dx%d+00+00" % (cWidth, cHeight))
    window.resizable(True, True)
    window.title("DiskView")

    # Menu
    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    fileMenu = Menu(mainMenu, tearoff = 0)
    mainMenu.add_cascade(label = "File", menu = fileMenu)
    fileMenu.add_command(label = "Statistics...", command = Vproperties)
    fileMenu.add_separator()
    fileMenu.add_command(label = "Exit", command = win_exit)

    optionsMenu = Menu(mainMenu, tearoff = 0)
    mainMenu.add_cascade(label = "Options", menu = optionsMenu)
    optionsMenu.add_checkbutton(label = "Show Fragment Boundaries")

    helpMenu = Menu(mainMenu, tearoff = 0)
    mainMenu.add_cascade(label = "Help", menu = helpMenu)
    helpMenu.add_command(label = "Legend...", command = Legend)
    helpMenu.add_separator()
    helpMenu.add_command(label = "About...")

    # Up Frame
    uFrame = Frame(window)
    uFrame.pack(fill = BOTH, expand = 1)

    # main Frame
    tFrame = Frame(window, bd = 1, bg = 'gray', relief = 'flat')
    tFrame.pack(fill = BOTH, expand = 1, padx = 5, pady = 10)

    # second Frame
    sFrame = Frame(window, bd = 1, bg = 'gray', relief = 'flat')
    sFrame.pack(fill = BOTH, expand = 1, padx = 5, pady = 10)

    # button Frame
    bFrame = Frame(window)
    bFrame.pack(fill = BOTH, expand = 1)

    # upFrame widget
    highlight = Label(uFrame, text = "Highlight :")
    highlight.pack(side = LEFT, ipadx = 5)

    path = Entry(uFrame, width = 40)
    path.pack(side = LEFT, ipadx = 5)
    path.insert(0, "/Users/cho/sample.txt")

    btnNone = Button(uFrame, text = "...")
    btnNone.pack(side = LEFT, padx = 5)

    btnShow = Button(uFrame, text = "Show next")
    btnShow.pack(side = RIGHT, padx = 5)
        
    # main Canvas
    tCanvas = Canvas(tFrame, width = cWidth -2, height = cHeight-2, bg = "white")
    tCanvas.pack(side=LEFT, fill = BOTH, expand = 1)

    scrollbar = Scrollbar(tFrame, orient = VERTICAL, command = tCanvas.yview)
    scrollbar.pack(side = RIGHT, fill = Y)

    tCanvas['yscrollcommand'] = lambda f, l : scroll_sh(scrollbar, f, l)

    tCanvas.bind("<Configure>", tConfigure)
    tCanvas.bind("<Button-1>", tClick)
    tCanvas.bind("<Button-2>", delete)
    tCanvas.bind("<Double-Button-1>", newWindow)

    # second Canvas
    sCanvas = Canvas(sFrame, width = 200, height = 50, bg = "white")
    sCanvas.pack(side = TOP, fill = BOTH, expand = 1)

    sCanvas.bind("<Configure>", sConfigure)
    sCanvas.bind("<Button-1>", sClick)

    # bFrame Widget
    volume = Label(bFrame, text = "Volume :")
    volume.pack(side = LEFT, ipadx = 5)

    volList = Listbox(bFrame, selectmode = "extended", height = 0, width = 9)
    volList.insert(0,"/dev/disk2s1")
    volList.pack(side = LEFT, ipadx = 5)

    btnRefresh = Button(bFrame, text = "Refresh")
    btnRefresh.pack(side = LEFT, padx = 5)

    zoom = Label(bFrame, text = "Zoom :")
    zoom.pack(side = LEFT, ipadx = 5)
    
    btnZoomIn = Button(bFrame, text = "+", command = ZoomIn)
    btnZoomIn.pack(side = LEFT, padx = 1)

    btnZoomOut = Button(bFrame, text = "-", command = ZoomOut)
    btnZoomOut.pack(side=LEFT, padx = 5)
    
    page = Label(bFrame, text = "PageUp/Dn :")
    page.pack(side = LEFT, ipadx = 5)
    
    btnUp = Button(bFrame, text = "↑", command = pageUp)
    btnUp.pack(side = LEFT, padx = 1)

    btnDown = Button(bFrame, text = "↓", command = pageDown)
    btnDown.pack(side=LEFT, padx = 5)

    cN = Label(bFrame, text = "ClusterNo :")
    cN.pack(side = LEFT, ipadx = 5)

    clusterN = Entry(bFrame, width = 10)
    clusterN.bind("<Return>", getClusterNo) # enter 치면 함수 실행
    clusterN.pack(side = LEFT, ipadx = 5)
    
    btnQuit = Button(bFrame, text = "Quit", command = win_exit)
    btnQuit.pack(side = RIGHT, padx = 5)

    btnExport = Button(bFrame, text = "Export...")
    btnExport.pack(side = RIGHT, padx = 5)

    window.mainloop()
