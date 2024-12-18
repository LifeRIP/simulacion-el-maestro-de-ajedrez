from simulacion import simulacion, las_vegas_n_queens, solve_n_queens
import simpy
import random

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
    simulacion_process = env.process(simulacion(env, SIMULATION_TIME, ARRIVAL_INTERVAL, BOARD_SIZES))
    env.run()
    ganancias, end_time, partidas = simulacion_process.value

    # Obtener soluciones del robot y del humano
    n = random.choice(BOARD_SIZES)
    _, robot_solution = las_vegas_n_queens(n)
    _, humano_solution = solve_n_queens(n)

    return robot_solution, humano_solution, ganancias, BOARD_SIZES, SIMULATION_TIME, ARRIVAL_INTERVAL, end_time, partidas

if __name__ == "__main__":
    escenario3()