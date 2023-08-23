from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkFont
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox
import os

# colores
cBlack='#1c1c1c'

def download(self):
    title = self.titlem.get()

    if title == "":
        CTkMessagebox(title="Info", message="Debes agregar un titulo")

    url = self.url.get()
    pathm = self.pathm.get()
    if os.path.isdir(pathm+'/'+title) == False:
        os.mkdir(title)
    pathm=pathm+'/'+title
    

class App(CTk):
    def __init__(self, fg_color: cBlack, **kwargs):
        super().__init__(fg_color, **kwargs)
        # config window
        self.geometry('500x600+350+20')
        self.minsize(480, 500)
        self.config(bg=cBlack)
        self.title('Descargar manga')
        self.columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # frame
        self.frame = CTkFrame(self, fg_color=cBlack)
        self.frame.grid(column = 0, row = 0, sticky = 'nsew', pady = 10, padx=10)

        # titulo del manga
        CTkLabel(self.frame, text="Titulo del manga", font=CTkFont(size=20)).grid(column=0, row=0, pady=16, sticky='ew')
        self.titlem = CTkEntry(self.frame, placeholder_text="Ingresa titulo del manga")
        self.titlem.grid(column=0, row=1, columnspan=4, sticky='ew')
        
        # url a descargar
        CTkLabel(self.frame, text="URL a descargar", font=CTkFont(size=20)).grid(column=0, row=2, pady=16, sticky='ew')
        self.url = CTkEntry(self.frame, placeholder_text="Ingresa la url para descargar un capitulo")
        self.url.grid(column=0, row=3, columnspan=4, sticky='ew')
        
        # selecciona donde guardar descargas
        CTkLabel(self.frame, text="Guardar en:", font=CTkFont(size=20)).grid(column=0, row=4, pady=16, sticky='w')
        CTkButton(self.frame, text="Seleccionar", command=self.openDir).grid(column=0, row=5, sticky='w')
        self.pathm = CTkEntry(self.frame, placeholder_text="Selecciona donde guardar el manga")
        self.pathm.grid(column=1, row=5, sticky='ew')
        
        
        
        
        
        
        CTkButton(self, text="Descargar", command=lambda: download(self)).grid(column=0, row=0, columnspan=2, sticky='ews', padx=20, pady=20)
        
        
        # self.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12], weight=1)
    def button_event(self):
        print(self.titlem.get())

    def openDir(self):
        dir=filedialog.askdirectory()
        if dir != "":
            os.chdir(dir)
        self.pathm.insert(0, os.getcwd())








# titlem = CTkEntry(frame, placeholder_text="Ingresa titulo del manga").grid(column=0, row=12)

# # value = titlem.get("value")

# # boton descargar
# def button_event():
#     print("titulo del manga es: "+"sad")
# CTkButton(frame, text="Descargar", command=button_event).grid(column=4, row=12)

# frame.columnconfigure([0, 1], weight=1)
# frame.rowconfigure([0,1,2,3,4,5,], weight=1)



if __name__ == "__main__":

    app = App(fg_color=cBlack)
    app.grid_columnconfigure((0,1), weight=1)
    app.mainloop();


