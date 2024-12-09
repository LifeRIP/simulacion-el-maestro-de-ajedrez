from simulacion import simulacion
import simpy

def escenario2():
    """Simulación con tableros más grandes."""
    SIMULATION_TIME = 8 * 60 * 60  # 8 horas en segundos
    ARRIVAL_INTERVAL = (10, 30)  # Intervalo estándar de llegada del robot
    BOARD_SIZES = [8, 10, 12, 15]  # Tamaños más grandes de tablero
    
    print("\n=== Escenario 2: Tableros más grandes ===")
    env = simpy.Environment()
    env.process(simulacion(env, SIMULATION_TIME, ARRIVAL_INTERVAL, BOARD_SIZES))
    env.run()

if __name__ == "__main__":
    escenario2()