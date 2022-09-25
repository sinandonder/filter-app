import tkinter as tk
from tkinter import ttk, filedialog as fd
from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from matplotlib import image
from matplotlib.pyplot import text
import filter
import customtkinter



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x700")
        self.title('Filter')
        self.image = Image.new('L', (0, 0))
        self.photo = ImageTk.PhotoImage(self.image)
        self.label_file_dialog = ttk.Label()
        self.text_file_dialog = ttk.Entry()
        self.button_file_dialog = ttk.Button()
        self.label_original = ttk.Label()
        self.label_imageX = ttk.Label()
        self.label_imageY = ttk.Label()
        self.label_imageXY = ttk.Label()
        self.combo_filter = ttk.Combobox()
        self.text_k = ttk.Entry()
        self.button_filter = ttk.Button()
        self.filename = ""
        self.label_tresh = ttk.Label()
        self.button_binary = ttk.Button()
        


        # configure the grid
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.create_widgets()
    
    def choose_file(self):
        self.filename = fd.askopenfilename()
        self.text_file_dialog.config(textvariable=self.filename)
        
        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label_original.configure(image=self.photo)
        self.label_original.image = self.image
    
    def apply_filter(self):
        image = self.image.convert('L')
        
        
        if self.combo_filter.get() == "Sobel":

            imageX = filter.sobel(image, 'x')
            photoX = ImageTk.PhotoImage(imageX)

            self.label_imageX.configure(image=photoX)
            self.label_imageX.image = photoX

            imageY = filter.sobel(image, 'y')
            photoY = ImageTk.PhotoImage(imageY)

            self.label_imageY.configure(image=photoY)
            self.label_imageY.image = photoY

            imageXY = filter.sobel(image)
            photoXY = ImageTk.PhotoImage(imageXY)

            self.label_imageXY.configure(image=photoXY)
            self.label_imageXY.image = photoXY

            imageB = filter.binary(imageXY, int(self.text_k.get()))
            imageB.show()

        elif self.combo_filter.get() == "Prewitt":

            imageX = filter.prewitt(image, 'x')
            photoX = ImageTk.PhotoImage(imageX)

            self.label_imageX.configure(image=photoX)
            self.label_imageX.image = photoX

            imageY = filter.prewitt(image, 'y')
            photoY = ImageTk.PhotoImage(imageY)

            self.label_imageY.configure(image=photoY)
            self.label_imageY.image = photoY

            imageXY = filter.prewitt(image)
            photoXY = ImageTk.PhotoImage(imageXY)

            self.label_imageXY.configure(image=photoXY)
            self.label_imageXY.image = photoXY

            if self.text_k.get() != "" or self.text_k.get() != None: 
                imageB = filter.binary(imageXY, int(self.text_k.get()))
                imageB.show()


        else:

            messagebox.showinfo("Filtre Seçiniz", "Lütfen Geçerli Bir Filtre Seçiniz")
        

        







        
        

        

    def create_widgets(self):
        # username
        self.label_file_diaglog = ttk.Label(self, text="Dosya Seçiniz:")
        self.label_file_diaglog.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.text_file_dialog = ttk.Entry(self)
        self.text_file_dialog.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        self.button_file_dialog = ttk.Button(self, text="Dosya Seç", command=self.choose_file)
        self.button_file_dialog.grid(column=1, row=0, sticky=tk.E, padx=5, pady=2)

        self.label_original = ttk.Label(self)
        self.label_original.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

        self.label_imageX = ttk.Label(self)
        self.label_imageX.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.label_imageY = ttk.Label(self)
        self.label_imageY.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.label_imageXY = ttk.Label(self)
        self.label_imageXY.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

        self.combo_filter = ttk.Combobox(self)
        self.combo_filter['values'] = ("Sobel", "Prewitt")
        self.combo_filter.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

        self.button_filter = ttk.Button(self, text="Filtre Uygula", command=self.apply_filter)
        self.button_filter.grid(column=1, row=3, sticky=tk.E, padx=5, pady=2)

        self.label_tresh = ttk.Label(self, text="Treshold[0 - 100]: ")
        self.label_tresh.grid(column=0, row=3, sticky=tk.E, padx=350, pady= 5)

        self.text_k = ttk.Entry(self)
        self.text_k.grid(column=0, row=3, sticky=tk.E, padx=200, pady=5)
        
        

        



if __name__ == "__main__":
    app = App()
    app.mainloop()

