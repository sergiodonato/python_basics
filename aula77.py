#       Tkinter - ProgressBar
# barra de progresso, mostrando feedback da progressão de algo

from tkinter import *
from tkinter import ttk

def valBarra(m):
    cont=0
    etapas=m/100
    while cont<etapas:
        cont=cont+1
        i=0
        while i<1000000:
            i=i+1
        varBarra.set(cont)
        app.update()

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

varBarra=DoubleVar()
varBarra.set(0)

pb=ttk.Progressbar(app, variable=varBarra, maximum=100)
pb.place(x=0, y=0, width=500, height=40)

btn=Button(app, text="Definir barra", command=lambda:valBarra(10000))
btn.place(x=0, y=50, width=100, height=40 )

app.mainloop()