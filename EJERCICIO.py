import tkinter as tk

def convertir():
    try:
        kilometros = float(entrada_kilometros.get())

        millas = kilometros * 0.621371

        etiqueta_resultados.config(text=f"{kilometros} kilómetros son {millas} millas")
        
    except ValueError:

        etiqueta_resultados.config(text="Ingrese un valor numérico válido")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Kileimetros a Millas")
ventana.geometry("300x150") # Establece el tamdio de la ventana

# Crear etiqueta de instrucciOn y colocarla en la cuadricula
etiqueta_instruccion = tk.Label(ventana, text="Ingrese la distancia en kileimetros:")
etiqueta_instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10) 

# Crear campo de entrada y colocarlo en la cuadricula
entrada_kilometros = tk.Entry(ventana)
entrada_kilometros.grid(row=1, column=0, padx=10, pady=10) 

# Crear boton de conversion y colocarlo en la cuadricula
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(row=1, column=1, padx=10, pady=10) 

# Crear etiqueta de resultado y colocarla en la cuadricula
etiqueta_resultados = tk.Label(ventana, text="")
etiqueta_resultados.grid(row=2, column=0, columnspan=2, padx=10, pady=10) 

# Iniciar la aplicaciOn
ventana.mainloop()