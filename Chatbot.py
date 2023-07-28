from chatterbot import ChatBot as cb
from chatterbot.trainers import ListTrainer
import tkinter as tk
from tkinter import messagebox
import sys

def trainer_chat_bot():

    global chatbot
    #chatbot = cb("Chessy")
    chatbot = cb(
        "Chessy",
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "default_response": "Desculpe, não entendi. Poderia reformular a pergunta?",
                "maximum_similarity_threshold": 0.8, # Adaptador lógico de similaridade quanto maior, mais restrito, boa heurística
            }
        ]
    )
    """
    #chatbot.storage.drop() #Limpar banco
    #sys.exit()
    """
    questions_answers = []
    with open("db_questions_Chessy.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            question = lines[i].strip()
            answer = lines[i+1].strip()
            questions_answers.append(question)
            questions_answers.append(answer)

    trainer = ListTrainer(chatbot)
    trainer.train(questions_answers)

trainer_chat_bot()

def chat_bot():
    question = entry.get()
    cb_answer = str(chatbot.get_response(question.lower().strip()))
    if question.lower() == "sair":
        window.quit()
    elif question.lower() == "":
        return
    else:
        text_cb.configure(state="normal")  # Habilitando a edição da entrada
        entry_question = "Você: " + question + "\n"
        entry_answer = "Chessy: " + cb_answer + "\n"
        text_cb.insert(tk.END, entry_question)
        text_cb.insert(tk.END, entry_answer)
        text_cb.configure(state="disabled")  # Desabilitando a edição da entrada
        entry.delete(0, tk.END)

# Variáveis
text = "Olá, meu nome é Chassy\nSou uma Inteligência Artificial especializada em Xadrez.\nFale comigo!"

window = tk.Tk()
window.title("Chessy")
window.configure(bg="slate gray")
window.geometry("920x500")

# Função para fechar a window
def fechar_window():
    if messagebox.askokcancel("Fechar", "Deseja abandonar o Chessy? :("):
        window.quit()

window.protocol("WM_DELETE_WINDOW", fechar_window)

# Mensagem de boas-vindas
label_welcome = tk.Label(window, text=text, font=("Arial",10, "bold"))
label_welcome.pack()
label_welcome.configure(bg="slate gray", fg="beige")

# Área de exibição das mensagens
text_cb = tk.Text(window,  width=110, state="disabled")
text_cb.pack()

# Caixa onde o usuário vai digitar a question
entry = tk.Entry(window, width=100)
entry.pack()

# Botão de envio
button_send = tk.Button(window, text="Enviar", command=chat_bot)
button_send.pack()
button_send.configure(bg="slate gray", fg="beige")

window.mainloop()
