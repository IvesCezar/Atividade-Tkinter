from tkinter import *
from tkinter import *
from tkinter import ttk, messagebox

def cadastrar_cliente():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    convenio = entry_convenio.get()
    contato_emergencia = entry_contato_emergencia.get()

    if nome == "" or telefone == "" or email == "" or convenio == "":
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
    else:
        tabela.insert("", "end", values=(nome, telefone, email, convenio, contato_emergencia))
        entry_nome.delete(0, END)
        entry_telefone.delete(0, END)
        entry_email.delete(0, END)
        entry_convenio.delete(0, END)
        entry_contato_emergencia.delete(0, END)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

janela = Tk()
janela.title("Cadastro de Paciente")
janela.geometry("800x600")

abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)

aba1 = Frame(abas)
abas.add(aba1, text="Cadastro do Paciente")
aba2 = Frame(abas)
abas.add(aba2, text="Pacientes Cadastrados")

Label(aba1, text="Nome Completo:").pack(pady=5)
entry_nome = Entry(aba1, width=40)
entry_nome.pack()

Label(aba1, text="CPF:").pack(pady=5)
entry_cpf = Entry(aba1, width=40)
entry_cpf.pack()

Label (aba1, text="Data de Nascimento:").pack(pady=5)
entry_data_nascimento = Entry(aba1, width=40)   
entry_data_nascimento.pack()

Label(aba1, text="Telefone:").pack(pady=5)
entry_telefone = Entry(aba1, width=40)
entry_telefone.pack()

Label(aba1, text="Email:").pack(pady=5)
entry_email = Entry(aba1, width=40)
entry_email.pack()

Label(aba1, text="Convenio/SUS:").pack(pady=5)
entry_convenio = Entry(aba1, width=40)
entry_convenio.pack()

Label(aba1, text="Contato de Emergência:").pack(pady=5)
entry_contato_emergencia = Entry(aba1, width=40)
entry_contato_emergencia.pack()


Button(
    aba1,
    text="Salvar Paciente",
    bg="green",
    fg="white",
    width=20,
    command=cadastrar_cliente
).pack(pady=20)

colunas = ("nome", "telefone", "email", "cidade")
tabela = ttk.Treeview(aba2, columns=colunas, show="headings")
for coluna in colunas:
    tabela.heading(coluna, text=coluna.capitalize())
tabela.pack(fill="both", expand=True, pady=20)

janela.mainloop()