from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

## 함수 선언 ##
def func_open_Statistics() :
    messagebox.showinfo("Volume Properties", "Files:, Fragements:, %Free Space:")
    
def func_exit() :
    window.quit()
    window.destroy()

def func_open_file() :
    filename = askopenfilename(parent = window, filetypes = ("모든 파일","*.*"))
    
## 전역 변수 선언 ##
window = None

## 메인 코드 ##
if __name__ == "__main__":
    window = Tk()
    window.title("ex1")
    window.geometry("800x600")
    window.resizable(width = False, height = False)

    frame_canvas = Frame(window, relief = "solid", bd = 1)
    frame_canvas.place(x = 8, y = 40)
    canvas = Canvas(frame_canvas, height = 350, width = 780)
    canvas.pack()

    frame_canvas2 = Frame(window, relief = "solid", bd = 1)
    frame_canvas2.place(x = 8, y = 420)
    canvas2 = Canvas(frame_canvas2, height = 100, width = 780)
    canvas2.pack()
    
    highlight = Label(window, text = "Highlight : ")
    highlight.place(x = 0, y = 5)
    
    volume = Label(window, text = "Volume : ")
    volume.place(x = 0, y = 560)

    volList = Listbox(window, selectmode = "extended", height = 0, width = 7)
    volList.insert(0, "C:\\")
    volList.place(x= 60, y = 562)
    # List x, combobax로 바꾸기
    
    zoom = Label(window, text = "Zoom : ")
    zoom.place(x = 180, y = 560)

    txtpath = Text(window, width = 45, height = 1)
    txtpath.place(x = 70, y = 8)

    # 버튼 구현
    btnNone = Button(window, text = "...", command = func_open_file)
    btnNone.place(x = 400, y = 5)

    btnShow = Button(window, text = "Show next")
    btnShow.place(x = 715, y = 5)
    
    btnQuit = Button(window, text = "Quit", command = func_exit)
    btnQuit.place(x = 750, y = 560)
    
    btnExport = Button(window, text = "Export...")
    btnExport.place(x = 680, y = 560)

    btnRefresh = Button(window, text = "Refresh")
    btnRefresh.place(x = 120, y = 560)

    btnUp = Button(window, text = "△")
    btnUp.place(x = 230, y = 547)

    btnUp = Button(window, text = "▽")
    btnUp.place(x = 230, y = 573)
    
    # 메뉴 추가
    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    fileMenu = Menu(mainMenu, tearoff = 0)
    mainMenu.add_cascade(label = "File", menu = fileMenu)
    fileMenu.add_command(label = "Statistics...", command = func_open_Statistics)
    fileMenu.add_separator()
    fileMenu.add_command(label = "Exit", command = func_exit)

    optionsMenu = Menu(mainMenu, tearoff = 0)
    mainMenu.add_cascade(label = "Options", menu = optionsMenu)
    optionsMenu.add_checkbutton(label = "Show Fragment Boundaries")

    helpMenu = Menu(mainMenu, tearoff = 0)
    mainMenu.add_cascade(label = "Help", menu = helpMenu)
    helpMenu.add_command(label = "Legend...")
    helpMenu.add_separator()
    helpMenu.add_command(label = "About...")

    window.mainloop()
