from simulacion import simulacion
import simpy

def escenario3():
    """Simulación con tiempos más lentos para el humano."""
    SIMULATION_TIME = 8 * 60 * 60  # 8 horas en segundos
    ARRIVAL_INTERVAL = (10, 30)  # Intervalo estándar de llegada del robot
    BOARD_SIZES = [5]  # Tamaños mixtos de tablero
    
    # Sobrescribir la función solve_n_queens para simular tiempos más lentos
    from simulacion import solve_n_queens as original_solve, solve_n_queens_util
    import time
    def slow_solve_n_queens(n):
        """Resuelve el problema de las n reinas con slow y devuelve la solución."""
        start = time.time()
        board = [[False] * n for _ in range(n)]  # Crear tablero vacío
        if not solve_n_queens_util(board, 0, n):
            print("No hay solución para el tamaño dado.")
            return None
        time.sleep(0.1)
        return board
    # Reemplazar la función original en runtime
    import simulacion
    simulacion.solve_n_queens = slow_solve_n_queens
    
    print("\n=== Escenario 3: Tiempos más lentos para el humano ===")
    env = simpy.Environment()
    env.process(simulacion.simulacion(env, SIMULATION_TIME, ARRIVAL_INTERVAL, BOARD_SIZES))
    env.run()

if __name__ == "__main__":
    escenario3()
