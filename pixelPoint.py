import pyautogui as pag
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from time import sleep
import webbrowser

win = Tk()
win.geometry('320x280+200+200')
win.resizable(False, False)
win.attributes('-topmost', True)
win.title("Pixel Point")
win.columnconfigure(0, minsize=200)

mouseCurrentPosition = StringVar()
mouseCurrentRGB = StringVar()
Running = IntVar()
Running.set(1)
inputText = StringVar(win, value='295,418')


def update_label():
    i = 0
    while Running.get():
        i = i+1
        x, y = pag.position()
        r, g, b = pag.pixel(x, y)
        hexadecimal = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        mouseCurrentPosition.set(str(f'Pixel atual: {x},{y}'))
        mouseCurrentRGB.set(str(f'Cor RGB: {r},{g},{b}, HTML: {hexadecimal}'))
        lblColor.config(bg=hexadecimal)
        win.update()


def moveTo(self=''):
    posicao = inputText.get().split(',')
    # print(posicao)
    if len(posicao) != 2:
        messagebox.showwarning(title='Erro', message='Posição Inválida!')
        return
    try:
        pag.moveTo(int(posicao[0]), int(posicao[1]), duration=0.5)
    except ValueError:
        messagebox.showwarning(title='Erro', message='Posição Inválida!')


def about():
    about = Toplevel(win)
    about.geometry('305x240+520+200')
    about.resizable(False, False)
    about.attributes('-topmost', True)
    about.title("Sobre")
    lblTitleAbout = Label(about, text="Sobre o PixelPoint",
                          font="Verdana 10 bold")
    lblTitleAbout.grid(row=0, columnspan=2, padx=20, pady=(15, 5))

    lblVersao = Label(about, text="Versão:")
    lblVersao.grid(row=1, column=0, pady=(5, 0), sticky=E)
    lblTxtVersao = Label(about, text="v1.0.0",
                         fg="blue", cursor="hand2")
    lblTxtVersao.grid(row=1, column=1, pady=(5, 0), sticky=W)
    lblTxtVersao.bind("<Button-1>",
                      lambda e: webbrowser.open_new('https://github.com/guisaldanha/pixelpoint/blob/main/CHANGELOG.MD'))

    lblAutor = Label(about, text="Autor:")
    lblAutor.grid(row=2, column=0, pady=(5, 0), sticky=E)
    lblTxtAutor = Label(about, text="Guilherme Saldanha",
                        fg="blue", cursor="hand2")
    lblTxtAutor.grid(row=2, column=1, pady=(5, 0), sticky=W)
    lblTxtAutor.bind("<Button-1>",
                     lambda e: webbrowser.open_new('https://guisaldanha.com'))

    lblLicenca = Label(about, text="Licença:")
    lblLicenca.grid(row=3, column=0, pady=(5, 0), sticky=E)
    lblTxtLicenca = Label(about, text="MIT", fg="blue", cursor="hand2")
    lblTxtLicenca.grid(row=3, column=1, pady=(5, 0), sticky=W)
    lblTxtLicenca.bind("<Button-1>",
                       lambda e: webbrowser.open_new('https://github.com/guisaldanha/pixelpoint/blob/main/LICENSE'))

    lblSite = Label(about, text="Mais informações na página do projeto",
                    fg="blue", cursor="hand2")
    lblSite.grid(row=4, columnspan=2, padx=20, pady=(10, 0))
    lblSite.bind("<Button-1>",
                 lambda e: webbrowser.open_new('https://github.com/guisaldanha/pixelpoint'))

    btnClose = Button(about, text="Fechar",
                      command=lambda: [about.destroy()])
    btnClose.grid(row=5, columnspan=2, pady=(10, 0))


win.bind('<Return>', moveTo)

lblGoToPixel = Label(win, text="Pixel Point",
                     font="Verdana 18 bold", fg='#417690')
lblGoToPixel.grid(row=0, columnspan=2, padx=20, pady=(20, 0))

lblCurrentPosition = Label(win, textvariable=mouseCurrentPosition)
lblCurrentPosition.grid(row=1, columnspan=2, pady=(10, 2))

lblCurrentColor = Label(win, textvariable=mouseCurrentRGB)
lblCurrentColor.grid(row=2, columnspan=2, pady=(2, 10), padx=(7, 0), sticky=W)

lblColor = Label(win, text="     ")
lblColor.grid(row=2, columnspan=2, pady=(2, 10), padx=(270, 0), sticky=W)

lblGoTo = Label(win, text="Mover o mouse para a posição (left, top):")
lblGoTo.grid(row=3, columnspan=2, pady=(0, 0), padx=(15, 0))

inputText = Entry(win, textvariable=inputText)
inputText.grid(row=4, column=0, pady=(0, 25), sticky=E)

btnGo = Button(win, text="Mover", command=lambda: [moveTo()])
btnGo.grid(row=4, column=1, pady=(0, 25), sticky=W, padx=10)

btnSair = Button(win, text="Fechar", command=lambda: [
                 Running.set(0), win.update(), win.destroy(), exit()])
btnSair.grid(row=5, column=0, pady=(0, 20), padx=(50, 0), ipadx=50, ipady=1)

lblFooter = Label(win, text="ℹ", fg="blue", cursor="hand2")
lblFooter.grid(row=5, column=1, pady=(0, 20), sticky=E)
lblFooter.bind('<Button-1>', lambda e: about())

update_label()

win.mainloop()
