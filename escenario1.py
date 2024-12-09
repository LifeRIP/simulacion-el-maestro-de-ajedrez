from simulacion import simulacion
import simpy

def escenario1():
    """Simulación con intervalo reducido de llegada del robot."""
    SIMULATION_TIME = 8 * 60 * 60  # 8 horas en segundos
    ARRIVAL_INTERVAL = (5, 15)  # Intervalo más corto para la llegada del robot
    BOARD_SIZES = [4, 5, 6, 8, 10]  # Tamaños de tablero considerados
    
    print("\n=== Escenario 1: Intervalo reducido de llegada del robot ===")
    env = simpy.Environment()
    env.process(simulacion(env, SIMULATION_TIME, ARRIVAL_INTERVAL, BOARD_SIZES))
    env.run()

if __name__ == "__main__":
    escenario1()