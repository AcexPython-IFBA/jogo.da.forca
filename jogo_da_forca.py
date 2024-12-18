import tkinter as tk
import random
from tkinter import messagebox

palavras = ['python', 'computador', 'curso', 'aula', 'sistema']

# Desenho da forca
desenho_forca = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n=========",
    "   +---+\n   |   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n========="
]

def escolher_palavra():
    return random.choice(palavras)

def desenhar_forca(erros):
    forca_label.config(text=desenho_forca[erros])

def advinhar_letra(letra):
    global palavra_oculta, letras_usadas, erros
    letra = letra.lower()
    if len(letra) != 1 or not letra.isalpha():
        messagebox.showerror("Erro", "Digite apenas uma letra válida!")
        return
    
    if letra in letras_usadas:
        messagebox.showwarning("Aviso", f"A letra '{letra}' já foi escolhida!")
        return

    letras_usadas.add(letra)
    letras_usadas_label.config(text="Letras usadas: " + ", ".join(sorted(letras_usadas)))

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_oculta = palavra_oculta[:i] + letra + palavra_oculta[i + 1:]
        palavra_label.config(text=palavra_oculta)
        if '_' not in palavra_oculta:
            end_game("venceu")
    else:
        erros += 1
        desenhar_forca(erros)
        if erros == 6:
            end_game("perdeu")

def advinhar_palavra(palpite):
    palpite = palpite.lower()
    if palpite == palavra:
        end_game("venceu")
    else:
        end_game("perdeu")

def end_game(resultado):
    if resultado == "venceu":
        texto_resultado = "Você venceu!"
    else:
        texto_resultado = f"Você perdeu! A palavra era: {palavra}"

    resultado_label.config(text=texto_resultado)
    entrada_letra.config(state="disabled")
    botao_advinhar.config(state="disabled")
    entrada_palavra.config(state="disabled")
    botao_palavra.config(state="disabled")
    botao_reiniciar.config(state="normal")  # Ativar o botão de reiniciar

def reiniciar_jogo():
    global palavra, palavra_oculta, letras_usadas, erros
    palavra = escolher_palavra()
    palavra_oculta = '_' * len(palavra)
    letras_usadas = set()
    erros = 0
    desenhar_forca(erros)
    palavra_label.config(text=palavra_oculta)
    letras_usadas_label.config(text="Letras usadas: ")
    resultado_label.config(text="")
    entrada_letra.config(state="normal")
    botao_advinhar.config(state="normal")
    entrada_palavra.config(state="normal")
    botao_palavra.config(state="normal")
    botao_reiniciar.config(state="disabled")  # Desativar o botão de reiniciar

def criar_widgets():
    global forca_label, palavra_label, letras_usadas_label, entrada_letra, botao_advinhar, entrada_palavra, botao_palavra, resultado_label, botao_reiniciar

    forca_label = tk.Label(root, font=("Courier", 16))
    forca_label.grid(row=0, column=0, columnspan=2, pady=10)

    palavra_label = tk.Label(root, text=palavra_oculta, font=("Arial", 24))
    palavra_label.grid(row=1, column=0, columnspan=2, pady=10)

    letras_usadas_label = tk.Label(root, text="Letras usadas: ", font=("Arial", 12))
    letras_usadas_label.grid(row=2, column=0, columnspan=2, pady=10)

    entrada_letra = tk.Entry(root, width=3, font=("Arial", 24))
    entrada_letra.grid(row=3, column=0, pady=10)

    botao_advinhar = tk.Button(root, text="Advinhar Letra", command=lambda: advinhar_letra(entrada_letra.get()))
    botao_advinhar.grid(row=3, column=1, pady=10)

    entrada_palavra = tk.Entry(root, width=15, font=("Arial", 18))
    entrada_palavra.grid(row=4, column=0, pady=10)

    botao_palavra = tk.Button(root, text="Advinhar Palavra", command=lambda: advinhar_palavra(entrada_palavra.get()))
    botao_palavra.grid(row=4, column=1, pady=10)

    resultado_label = tk.Label(root, font=("Arial", 14))
    resultado_label.grid(row=5, column=0, columnspan=2, pady=10)

    botao_reiniciar = tk.Button(root, text="Reiniciar Jogo", command=reiniciar_jogo)
    botao_reiniciar.grid(row=6, column=0, columnspan=2, pady=10)
    botao_reiniciar.config(state="disabled")  # Desativar o botão inicialmente

# Iniciar a aplicação
root = tk.Tk()
root.title("Jogo da Forca")
root.geometry("500x500")

palavra = escolher_palavra()
palavra_oculta = '_' * len(palavra)

criar_widgets()

letras_usadas = set()
erros = 0
desenhar_forca(erros)

root.mainloop()
