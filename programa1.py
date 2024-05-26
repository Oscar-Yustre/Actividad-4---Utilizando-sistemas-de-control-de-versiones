import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.resultado_var = tk.StringVar()

        self.entrada = tk.Entry(master, textvariable=self.resultado_var, font=('Arial', 14), bd=10, insertwidth=4, width=15, justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4)

        self.botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('^', 5, 3),
        ]

        for (text, row, column) in self.botones:
            boton = tk.Button(master, text=text, font=('Arial', 14), bd=5, width=5, command=lambda t=text: self.presionar(t))
            boton.grid(row=row, column=column)

    def presionar(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.resultado_var.get())
                self.resultado_var.set(resultado)
            except Exception as e:
                messagebox.showerror("Error", "Operación no válida")
        elif valor == 'C':
            self.resultado_var.set('')
        else:
            self.resultado_var.set(self.resultado_var.get() + valor)

def main():
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main()
