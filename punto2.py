import tkinter as tk
from tkinter import messagebox
import math

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0
        self.area_superficial = 0

    def calcular_volumen(self):
        pass

    def calcular_area_superficial(self):
        pass

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.area_superficial = self.calcular_area_superficial()

    def calcular_volumen(self):
        return math.pi * self.altura * self.radio**2

    def calcular_area_superficial(self):
        return 2 * math.pi * self.radio * self.altura + 2 * math.pi * self.radio**2

class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.volumen = self.calcular_volumen()
        self.area_superficial = self.calcular_area_superficial()

    def calcular_volumen(self):
        return self.lado**3

    def calcular_area_superficial(self):
        return 6 * self.lado**2

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.area_superficial = self.calcular_area_superficial()

    def calcular_volumen(self):
        return (4/3) * math.pi * self.radio**3

    def calcular_area_superficial(self):
        return 4 * math.pi * self.radio**2

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.area_superficial = self.calcular_area_superficial()

    def calcular_volumen(self):
        return (self.base**2 * self.altura) / 3

    def calcular_area_superficial(self):
        area_base = self.base**2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral

class Prisma(FiguraGeometrica):
    def __init__(self, base, altura, profundidad):
        super().__init__()
        self.base = base
        self.altura = altura
        self.profundidad = profundidad
        self.volumen = self.calcular_volumen()
        self.area_superficial = self.calcular_area_superficial()

    def calcular_volumen(self):
        return self.base * self.altura * self.profundidad

    def calcular_area_superficial(self):
        return 2 * (self.base * self.altura + self.base * self.profundidad + self.altura * self.profundidad)

class VentanaBase(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("300x200")

    def crear_widget(self, label_text, entry_width):
        label = tk.Label(self, text=label_text)
        label.pack(pady=5)
        entry = tk.Entry(self, width=entry_width)
        entry.pack(pady=5)
        return entry

    def crear_boton(self, texto, funcion):
        boton = tk.Button(self, text=texto, command=funcion)
        boton.pack(pady=10)

class VentanaCilindro(VentanaBase):
    def __init__(self):
        super().__init__()
        self.radio_entry = self.crear_widget("Radio (cms):", 10)
        self.altura_entry = self.crear_widget("Altura (cms):", 10)
        self.crear_boton("Calcular", self.calcular_cilindro)
        self.resultado_label = tk.Label(self, text="")
        self.resultado_label.pack()

    def calcular_cilindro(self):
        try:
            radio = float(self.radio_entry.get())
            altura = float(self.altura_entry.get())
            cilindro = Cilindro(radio, altura)
            resultado = f"Volumen: {cilindro.volumen:.2f} cm³\nÁrea: {cilindro.area_superficial:.2f} cm²"
            self.resultado_label.config(text=resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

class VentanaCubo(VentanaBase):
    def __init__(self):
        super().__init__()
        self.lado_entry = self.crear_widget("Lado (cms):", 10)
        self.crear_boton("Calcular", self.calcular_cubo)
        self.resultado_label = tk.Label(self, text="")
        self.resultado_label.pack()

    def calcular_cubo(self):
        try:
            lado = float(self.lado_entry.get())
            cubo = Cubo(lado)
            resultado = f"Volumen: {cubo.volumen:.2f} cm³\nÁrea: {cubo.area_superficial:.2f} cm²"
            self.resultado_label.config(text=resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

class VentanaEsfera(VentanaBase):
    def __init__(self):
        super().__init__()
        self.radio_entry = self.crear_widget("Radio (cms):", 10)
        self.crear_boton("Calcular", self.calcular_esfera)
        self.resultado_label = tk.Label(self, text="")
        self.resultado_label.pack()

    def calcular_esfera(self):
        try:
            radio = float(self.radio_entry.get())
            esfera = Esfera(radio)
            resultado = f"Volumen: {esfera.volumen:.2f} cm³\nÁrea: {esfera.area_superficial:.2f} cm²"
            self.resultado_label.config(text=resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

class VentanaPiramide(VentanaBase):
    def __init__(self):
        super().__init__()
        self.base_entry = self.crear_widget("Base (cms):", 10)
        self.altura_entry = self.crear_widget("Altura (cms):", 10)
        self.apotema_entry = self.crear_widget("Apotema (cms):", 10)
        self.crear_boton("Calcular", self.calcular_piramide)
        self.resultado_label = tk.Label(self, text="")
        self.resultado_label.pack()

    def calcular_piramide(self):
        try:
            base = float(self.base_entry.get())
            altura = float(self.altura_entry.get())
            apotema = float(self.apotema_entry.get())
            piramide = Piramide(base, altura, apotema)
            resultado = f"Volumen: {piramide.volumen:.2f} cm³\nÁrea: {piramide.area_superficial:.2f} cm²"
            self.resultado_label.config(text=resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

class VentanaPrisma(VentanaBase):
    def __init__(self):
        super().__init__()
        self.base_entry = self.crear_widget("Base (cms):", 10)
        self.altura_entry = self.crear_widget("Altura (cms):", 10)
        self.profundidad_entry = self.crear_widget("Profundidad (cms):", 10)
        self.crear_boton("Calcular", self.calcular_prisma)
        self.resultado_label = tk.Label(self, text="")
        self.resultado_label.pack()

    def calcular_prisma(self):
        try:
            base = float(self.base_entry.get())
            altura = float(self.altura_entry.get())
            profundidad = float(self.profundidad_entry.get())
            prisma = Prisma(base, altura, profundidad)
            resultado = f"Volumen: {prisma.volumen:.2f} cm³\nÁrea: {prisma.area_superficial:.2f} cm²"
            self.resultado_label.config(text=resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("350x200")
        self.crear_boton("Cilindro", self.abrir_cilindro)
        self.crear_boton("Cubo", self.abrir_cubo)
        self.crear_boton("Esfera", self.abrir_esfera)
        self.crear_boton("Pirámide", self.abrir_piramide)
        self.crear_boton("Prisma", self.abrir_prisma)

    def crear_boton(self, texto, funcion):
        boton = tk.Button(self, text=texto, command=funcion)
        boton.pack(pady=5)

    def abrir_cilindro(self):
        ventana = VentanaCilindro()
        ventana.mainloop()

    def abrir_cubo(self):
        ventana = VentanaCubo()
        ventana.mainloop()

    def abrir_esfera(self):
        ventana = VentanaEsfera()
        ventana.mainloop()

    def abrir_piramide(self):
        ventana = VentanaPiramide()
        ventana.mainloop()

    def abrir_prisma(self):
        ventana = VentanaPrisma()
        ventana.mainloop()

if __name__ == "__main__":
    ventana_principal = VentanaPrincipal()
    ventana_principal.mainloop()
