import tkinter as tk

class Interface:

    def __init__(self, root):

        self.controller = None
        self.root = root

        root.title("Cadastro de Conta")
        root.geometry("400x350")
        root.configure(bg="#1e293b")

        titulo = tk.Label(
            root,
            text="Cadastro de Conta",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#1e293b"
        )
        titulo.pack(pady=15)

        frame = tk.Frame(root, bg="#334155", padx=20, pady=20)
        frame.pack(pady=10)

        tk.Label(frame, text="Nome", bg="#334155", fg="white").grid(row=0, column=0)
        self.entry_nome = tk.Entry(frame)
        self.entry_nome.grid(row=0, column=1)

        tk.Label(frame, text="CPF", bg="#334155", fg="white").grid(row=1, column=0)
        self.entry_cpf = tk.Entry(frame)
        self.entry_cpf.grid(row=1, column=1)

        tk.Label(frame, text="Saldo Inicial", bg="#334155", fg="white").grid(row=2, column=0)
        self.entry_saldo = tk.Entry(frame)
        self.entry_saldo.grid(row=2, column=1)

        botao = tk.Button(
            root,
            text="Criar Conta",
            command=self.criar_conta,
            bg="#22c55e",
            fg="white"
        )
        botao.pack(pady=15)

        self.resultado = tk.Label(root, text="", bg="#1e293b", fg="white")
        self.resultado.pack()

    def set_controller(self, controller):
        self.controller = controller

    def criar_conta(self):
        self.controller.criar_conta()

    def obter_dados(self):
        return (
            self.entry_nome.get(),
            self.entry_cpf.get(),
            self.entry_saldo.get()
        )

    def mostrar_conta(self, texto):
        self.resultado.config(text=texto)

    def limpar_campos(self):
        self.entry_nome.delete(0, 'end')
        self.entry_cpf.delete(0, 'end')
        self.entry_saldo.delete(0, 'end')