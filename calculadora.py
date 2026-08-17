import tkinter as tk 

janela = tk . Tk()    

display = tk.Entry(janela)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=8)

janela.title ("Calculadora")
janela. geometry("300x400")

def pressionar_botao(texto):
    display.insert(tk.END, texto)

def limpar_display():
    display.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(display.get())
        limpar_display()
        display.insert(tk.END, str(resultado))
    except Exception:
        limpar_display()
        display.insert(tk.END, "Erro")

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (texto, linha, coluna) in botoes:
    if texto == 'C':
        comando = limpar_display
    elif texto == '=':
        comando = calcular
    else:
        comando = lambda x=texto: pressionar_botao(x)
        
    btn = tk.Button(janela, text=texto, command=comando)
    btn.grid(row=linha, column=coluna, ipadx=18, ipady=12, padx=5, pady=5)


def tecla_pressionada(event):
    tecla = event.char
    if tecla in '0123456789+-*/':
        display.insert(tk.END, tecla)
    elif tecla == '\r':
        calcular()
    elif event.keysym == 'BackSpace':
        texto_atual = display.get()
        display.delete(0, tk.END)
        display.insert(0, texto_atual[:-1])
    elif event.keysym == 'Escape':
        limpar_display()

janela.bind('<Key>', tecla_pressionada)




janela.mainloop()