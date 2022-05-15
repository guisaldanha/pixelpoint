import pyautogui as pag
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import sleep
import tkinter.font as font

win=Tk()
win.geometry('320x280+200+200')
win.resizable(False, False)
win.attributes('-topmost', True)
win.title("Pixel Point")
fontTitle=font.Font(family='Verdana', size=18, weight='bold')
win.columnconfigure(0, minsize=200)

mouseCurrentPosition = StringVar()
mouseCurrentRGB = StringVar()
Running = IntVar()
Running.set(1)
inputText = StringVar(win,value='295,418')
# inputText = StringVar(win,value='229,293')

def update_label():
    i=0
    while Running.get():
        i=i+1
        x, y = pag.position()
        r, g, b = pag.pixel(x, y)
        hexadecimal = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        mouseCurrentPosition.set(str(f'Pixel atual: {x},{y}'))
        mouseCurrentRGB.set(str(f'Cor RGB: {r},{g},{b}, HTML: {hexadecimal}'))
        lblColor.config(bg=hexadecimal)
        win.update()

def moveTo(self = ''):
    posicao = inputText.get().split(',')
    # print(posicao)
    if len(posicao) != 2:
        messagebox.showwarning(title='Erro', message='Posição Inválida!')
        # print('Posição inválida!')
        return 
    try:
        pag.moveTo(int(posicao[0]), int(posicao[1]),duration=0.5)
        # print('Mouse na posição: {}'.format(pag.position()))
    except ValueError:
        messagebox.showwarning(title='Erro', message='Posição Inválida!')
        # print('Posição inválida!'+ValueError)


win.bind('<Return>', moveTo)

lblGoToPixel = Label(win, text="Pixel Point", font=fontTitle)
lblGoToPixel.grid(row=0, columnspan=2, padx=20, pady=(20, 0))
    
lblCurrentPosition=Label(win,textvariable=mouseCurrentPosition)
lblCurrentPosition.grid(row=1, columnspan=2, pady=(10,2))

lblCurrentColor=Label(win,textvariable=mouseCurrentRGB)
lblCurrentColor.grid(row=2, columnspan=2, pady=(2, 10), padx=(7, 0), sticky=W)

lblColor=Label(win, text="     ")
lblColor.grid(row=2, columnspan=2, pady=(2, 10), padx=(270,0), sticky=W)

lblGoTo=Label(win, text="Mover o mouse para a posição (left, top):")
lblGoTo.grid(row=3, columnspan=2, pady=(0,0), padx=(15, 0))

inputText = Entry(win, textvariable=inputText)
inputText.grid(row=4, column=0, pady=(0,25), sticky=E)
# inputText.pack(side=LEFT, padx=(40,0), pady=(0,70))

btnGo = Button(win, text="Mover", command=lambda: [moveTo()])
btnGo.grid(row=4, column=1, pady=(0,25), sticky=W, padx=10)
# btnGo.pack(side=RIGHT, padx=(0,40), pady=(0,70))

btnSair = Button(win, text="Sair", command=lambda: [Running.set(0), win.update(), win.destroy(), exit()])
btnSair.grid(row=5, columnspan=2, pady=(0,20), ipadx=30, ipady=1)
# btnSair.place(anchor=CENTER, relx=0.5, rely=0.9, width=100, height=30)
update_label()

win.mainloop()
