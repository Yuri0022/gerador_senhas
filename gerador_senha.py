import tkinter as tk
from tkinter import messagebox
import string
import random

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        usar_maiusculas = var_maiusculas.get()
        usar_minusculas = var_minusculas.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()

        caracteres = ''
        if usar_maiusculas:
            caracteres += string.ascii_uppercase
        if usar_minusculas:
            caracteres += string.ascii_lowercase
        if usar_numeros:
            caracteres += string.digits
        if usar_simbolos:
            caracteres += string.punctuation

        if not caracteres:
            raise ValueError("Selecione pelo menos um tipo de caractere.")

        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, senha)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Cores do tema dark
bg_color = "#1e1e1e"
fg_color = "#ffffff"
highlight_color = "#3a3a3a"
button_color = "#3c8dbc"

# Janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas Fortes")
janela.geometry("400x320")
janela.resizable(False, False)
janela.configure(bg=bg_color)

# Título
tk.Label(janela, text="Gerador de Senhas", font=("Arial", 16, "bold"), bg=bg_color, fg=fg_color).pack(pady=10)

# Tamanho da senha
frame_tamanho = tk.Frame(janela, bg=bg_color)
frame_tamanho.pack()
tk.Label(frame_tamanho, text="Tamanho da senha:", bg=bg_color, fg=fg_color).pack(side=tk.LEFT)
entry_tamanho = tk.Entry(frame_tamanho, width=5, bg=highlight_color, fg=fg_color, insertbackground=fg_color)
entry_tamanho.insert(0, "12")
entry_tamanho.pack(side=tk.LEFT)

# Checkbuttons
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)

def criar_check(texto, var):
    return tk.Checkbutton(janela, text=texto, variable=var, bg=bg_color, fg=fg_color, selectcolor=highlight_color, activebackground=bg_color, activeforeground=fg_color)

criar_check("Letras maiúsculas", var_maiusculas).pack(anchor='w', padx=20)
criar_check("Letras minúsculas", var_minusculas).pack(anchor='w', padx=20)
criar_check("Números", var_numeros).pack(anchor='w', padx=20)
criar_check("Símbolos", var_simbolos).pack(anchor='w', padx=20)

# Botão de gerar senha
tk.Button(janela, text="Gerar Senha", command=gerar_senha,
          bg=button_color, fg=fg_color, activebackground=highlight_color).pack(pady=10)

# Campo de resultado
entry_resultado = tk.Entry(janela, font=("Arial", 12), justify='center',
                           bg=highlight_color, fg=fg_color, insertbackground=fg_color)
entry_resultado.pack(pady=5, fill='x', padx=20)

# Rodar o app
janela.mainloop()
