import tkinter as tk

from View.interface import Interface
from Controller.conta_controller import ContaController

root = tk.Tk()

view = Interface(root)

controller = ContaController(view)

view.set_controller(controller)

root.mainloop()