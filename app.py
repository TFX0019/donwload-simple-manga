import customtkinter as ctk

cBlack='#1c1c1c'

def imprimir_valores():
    texto1 = input_text1.get()
    texto2 = input_text2.get()
    numero1 = input_num1.get()
    numero2 = input_num2.get()
    
    print("Texto 1:", texto1)
    print("Texto 2:", texto2)
    print("Número 1:", numero1)
    print("Número 2:", numero2)

# Crear una ventana
root = ctk.CTk()
root.title("Interfaz con CustomTkinter")
root.geometry('500x600+350+20')
root.minsize(480, 500)
root.config(bg=cBlack)
root.title('Descargar manga')
root.columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Crear widgets
label_text1 = ctk.CTkLabel(root, text="Titulo del manga")
label_text1.grid(column=0,row=0)
input_text1 = ctk.CTkEntry(root)

label_text2 = ctk.CTkLabel(root, text="Texto 2:")
input_text2 = ctk.CTkEntry(root)

label_num1 = ctk.CTkLabel(root, text="Número 1:")
input_num1 = ctk.CTkEntry(root)

label_num2 = ctk.CTkLabel(root, text="Número 2:")
input_num2 = ctk.CTkEntry(root)

boton = ctk.CTkButton(root, text="Imprimir Valores", command=imprimir_valores)

# Ubicar widgets en la root
label_text1.pack()
input_text1.pack()
label_text2.pack()
input_text2.pack()
label_num1.pack()
input_num1.pack()
label_num2.pack()
input_num2.pack()
boton.pack()

# Iniciar el bucle de eventos
root.mainloop()