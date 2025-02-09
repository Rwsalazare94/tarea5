#Ejercicio 8.2

import tkinter as tk
import math

def calcular():
    try:
        notas = [float(entry.get()) for entry in entries]
        
        promedio = sum(notas) / len(notas)
        varianza = sum((nota - promedio) ** 2 for nota in notas) / len(notas)
        desviacion_estandar = math.sqrt(varianza)
        mayor_nota = max(notas)
        menor_nota = min(notas)
        
        resultados.set(f"Promedio: {promedio:.2f}\n"
                       f"Desviación Estándar: {desviacion_estandar:.2f}\n"
                       f"Valor mayor: {mayor_nota:.2f}\n"
                       f"Valor menor: {menor_nota:.2f}")
    except ValueError:
        resultados.set("Ingrese valores numéricos válidos.")

ventana = tk.Tk()
ventana.title("Cálculo de Notas")

entries = [tk.Entry(ventana) for _ in range(5)]
for i, entry in enumerate(entries):
    tk.Label(ventana, text=f"Nota {i + 1}:").grid(row=i, column=0)
    entry.grid(row=i, column=1)

tk.Button(ventana, text="Calcular", command=calcular).grid(row=5, column=0, columnspan=2)
resultados = tk.StringVar()
tk.Label(ventana, textvariable=resultados, justify="left").grid(row=6, column=0, columnspan=2)

ventana.mainloop()