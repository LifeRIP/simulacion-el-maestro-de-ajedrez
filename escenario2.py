from simulacion import simulacion, las_vegas_n_queens, solve_n_queens
import simpy
import random

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
    simulacion_process = env.process(simulacion(env, SIMULATION_TIME, ARRIVAL_INTERVAL, BOARD_SIZES))
    env.run()
    ganancias, end_time, partidas = simulacion_process.value

    # Obtener soluciones del robot y del humano
    n = random.choice(BOARD_SIZES)
    _, robot_solution = las_vegas_n_queens(n)
    _, humano_solution = solve_n_queens(n)

    return robot_solution, humano_solution, ganancias, BOARD_SIZES, SIMULATION_TIME, ARRIVAL_INTERVAL, end_time, partidas

if __name__ == "__main__":
    escenario2()