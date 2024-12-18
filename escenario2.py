from simulacion import simulacion
import simpy

def escenario2():
    """
    Simulación con tableros de mayores ganancias en un intervalo reducido de 
    llegada del robot.
    """
    SIMULATION_TIME = 8 * 60 * 60  # 8 horas en segundos
    ARRIVAL_INTERVAL = (1, 10)  # Intervalo más corto para la llegada del robot
    BOARD_SIZES = [5, 6, 10]  # Tamaños de tablero donde se evidencia ganancias
    
    print("\n=== Escenario 2: Mayores ganancias en intervalo reducido ===")
    env = simpy.Environment()
    env.process(simulacion(env, SIMULATION_TIME, ARRIVAL_INTERVAL, BOARD_SIZES))
    env.run()

if __name__ == "__main__":
    escenario2()