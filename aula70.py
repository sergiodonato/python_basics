#       Tkinter - Password
from tkinter import *

def impSenha():
    print("Senha digitada:" +vsenha.get())

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

vsenha=StringVar()

p_senha=Entry(app, textvariable=vsenha, show= "*")
p_senha.pack()

btn_mostraSenha=Button(app, text="Imprimir Senha", command=impSenha)
btn_mostraSenha.pack()

app.mainloop()