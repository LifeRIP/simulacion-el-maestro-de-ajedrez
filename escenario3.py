from simulacion import simulacion
import simpy

def escenario3():
    """
    Simulación con tablero de mayor ganancias en un intervalo aún más reducido
    de llegada del robot y en menor tiempo de simulación.
    """
    SIMULATION_TIME = 10 * 60  # 10 minutos en segundos
    ARRIVAL_INTERVAL = (0.1, 0.2)  # Intervalo aún más corto para la llegada del robot
    BOARD_SIZES = [6]  # Tamaño del tablero donde se evidencia la mayor ganancia
    
    print("\n=== Escenario 3: Mayor ganancia en intervalo aún más reducido y menor tiempo de simulación ===")
    env = simpy.Environment()
    env.process(simulacion(env, SIMULATION_TIME, ARRIVAL_INTERVAL, BOARD_SIZES))
    env.run()

if __name__ == "__main__":
    escenario3()