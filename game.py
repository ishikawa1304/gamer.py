import tkinter as tk
import random

# Estado del juego
puntos_usuario = 0
puntos_computadora = 0
META = 5
final_mostrado = False

def actualizar_marcador():
    etiqueta_marcador.config(
        text=f"Usuario: {puntos_usuario}   |   Computadora: {puntos_computadora}"
    )

def reiniciar(final):
    global puntos_usuario, puntos_computadora, final_mostrado
    puntos_usuario = puntos_computadora = 0
    final_mostrado = False
    actualizar_marcador()
    etiqueta_resultado.config(text="")
    for b in botones:
        b.config(state="normal")
    final.destroy()

def mostrar_final(ganador):
    global final_mostrado
    if final_mostrado:
        return
    final_mostrado = True

    final = tk.Toplevel(ventana)
    final.title("Juego terminado")
    final.geometry("550x380")
    final.config(bg="#0d47a1")

    tk.Label(
        final, text=f"¡{ganador} ha ganado el juego!",
        font=("Arial", 24, "bold"), bg="#0d47a1", fg="white",
        wraplength=500, justify="center"
    ).pack(pady=50)

    tk.Button(final, text="Reiniciar juego", font=("Arial", 16, "bold"),
              bg="white", width=18, command=lambda: reiniciar(final)).pack(pady=10)

    tk.Button(final, text="Cerrar juego", font=("Arial", 16, "bold"),
              bg="#bbdefb", width=18, command=ventana.destroy).pack(pady=10)

def jugar(eleccion):
    global puntos_usuario, puntos_computadora

    if final_mostrado:
        return

    comp = random.choice(["piedra", "papel", "tijera"])

    if eleccion == comp:
        resultado = "Empate"
    elif (eleccion == "piedra" and comp == "tijera") or \
         (eleccion == "papel" and comp == "piedra") or \
         (eleccion == "tijera" and comp == "papel"):
        resultado = "Ganaste"
        puntos_usuario += 1
    else:
        resultado = "Perdiste"
        puntos_computadora += 1

    etiqueta_resultado.config(
        text=f"Tú elegiste: {eleccion}\n"
             f"La computadora eligió: {comp}\n\n"
             f"Resultado: {resultado}"
    )

    actualizar_marcador()

    if puntos_usuario >= META or puntos_computadora >= META:
        for b in botones:
            b.config(state="disabled")
        ganador = "El usuario" if puntos_usuario >= META else "La computadora"
        mostrar_final(ganador)


# ---------------- INTERFAZ ----------------

ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("520x520")
ventana.config(bg="#e3f2fd")

tk.Label(
    ventana, text="Piedra, Papel o Tijera",
    font=("Arial", 28, "bold"), bg="#e3f2fd"
).pack(pady=20)

etiqueta_marcador = tk.Label(
    ventana, text="Usuario: 0   |   Computadora: 0",
    font=("Arial", 18), bg="#e3f2fd"
)
etiqueta_marcador.pack(pady=10)

frame = tk.Frame(ventana, bg="#e3f2fd")
frame.pack()

btn_piedra = tk.Button(frame, text="Piedra", width=12, height=2,
                       bg="#ffca28", fg="white", font=("Arial", 14, "bold"),
                       command=lambda: jugar("piedra"))
btn_piedra.grid(row=0, column=0, padx=10)

btn_papel = tk.Button(frame, text="Papel", width=12, height=2,
                      bg="#66bb6a", fg="white", font=("Arial", 14, "bold"),
                      command=lambda: jugar("papel"))
btn_papel.grid(row=0, column=1, padx=10)

btn_tijera = tk.Button(frame, text="Tijera", width=12, height=2,
                       bg="#ef5350", fg="white", font=("Arial", 14, "bold"),
                       command=lambda: jugar("tijera"))
btn_tijera.grid(row=0, column=2, padx=10)

botones = [btn_piedra, btn_papel, btn_tijera]

etiqueta_resultado = tk.Label(
    ventana, text="", font=("Arial", 18), bg="#e3f2fd"
)
etiqueta_resultado.pack(pady=40)

ventana.mainloop()
