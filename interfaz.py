import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import simpy
from simulacion import simulacion

class SimulacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación - El maestro de ajedrez")

        # Crear marco principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar grid
        main_frame.columnconfigure(1, weight=1)

        # Widgets usando grid consistentemente
        ttk.Label(main_frame, text="Tamaño del tablero:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.n_size = tk.StringVar(value="8")
        tk.OptionMenu(main_frame, self.n_size, "4", "5", "6", "8", "10", "12", "15").grid(row=0, column=1, sticky=tk.W, pady=5)

        ttk.Label(main_frame, text="Tiempo de simulación (en horas):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.sim_time = tk.StringVar(value="8")
        ttk.Entry(main_frame, textvariable=self.sim_time).grid(row=1, column=1, sticky=tk.W, pady=5)

        ttk.Label(main_frame, text="Intervalo de llegada del robot (segundos):").grid(row=2, column=0, sticky=tk.W, pady=5)
        interval_frame = ttk.Frame(main_frame)
        interval_frame.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        self.interval_min = tk.StringVar(value="10")
        self.interval_max = tk.StringVar(value="30")
        ttk.Entry(interval_frame, textvariable=self.interval_min, width=5).pack(side=tk.LEFT)
        ttk.Label(interval_frame, text="-").pack(side=tk.LEFT, padx=2)
        ttk.Entry(interval_frame, textvariable=self.interval_max, width=5).pack(side=tk.LEFT)

        # Botón para iniciar simulación
        ttk.Button(main_frame, text="Iniciar simulación", command=self.start_simulation).grid(row=3, column=0, columnspan=2, pady=10)
        
    def start_simulation(self):
        try:
            # Actualizar variables globales de simulación
            SIMULATION_TIME = float(self.sim_time.get()) * 3600  # Convertir horas a segundos
            ARRIVAL_INTERVAL = (float(self.interval_min.get()), float(self.interval_max.get()))
            BOARD_SIZES = [int(self.n_size.get())]
            
            # Validar intervalo de llegada
            if ARRIVAL_INTERVAL[0] >= ARRIVAL_INTERVAL[1]:
                messagebox.showerror("Error", "El intervalo de llegada mínimo debe ser menor que el máximo.")
                return

            # Iniciar simulación
            env = simpy.Environment()
            env.process(simulacion(env, SIMULATION_TIME, ARRIVAL_INTERVAL, BOARD_SIZES))
            env.run()
            
        except ValueError as e:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
        except Exception as e:
            messagebox.showerror(f"Error: {str(e)}\n")

def main():
    root = tk.Tk()
    app = SimulacionGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()