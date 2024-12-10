import random
from time import time
from tkinter import messagebox

#################################################################################
# Algoritmo determinista para resolver el problema de las n reinas
#################################################################################
def is_safe(board, row, col, n):
    """Verifica si una reina puede ser colocada en la posición (row, col)."""
    # Verificar esta columna hacia arriba
    for i in range(row):
        if board[i][col]:
            return False

    # Verificar diagonal superior izquierda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Verificar diagonal superior derecha
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, row, n):
    """Función recursiva para resolver el problema."""
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True  # Colocar reina
            if solve_n_queens_util(board, row + 1, n):  # Intentar con la siguiente fila
                return True
            board[row][col] = False  # Backtracking: remover reina si no hay solución

    return False

def solve_n_queens(n):
    """Resuelve el problema de las n reinas y devuelve la solución."""
    board = [[False] * n for _ in range(n)]  # Crear tablero vacío
    if not solve_n_queens_util(board, 0, n):
        print("No hay solución para el tamaño dado.")
        return None
    return board


#################################################################################
# Algoritmo Las Vegas para resolver el problema de las n reinas
#################################################################################
def is_safe_las_vegas(board, row, col, n):
    """Verifica si una reina puede ser colocada en la posición (row, col)."""
    for i in range(row):
        if board[i][col]:
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)]:
            return False
        if col + (row - i) < n and board[i][col + (row - i)]:
            return False
    return True

def las_vegas_n_queens(n):
    """Resuelve el problema de las n reinas usando el método Las Vegas."""
    while True:
        board = [[False] * n for _ in range(n)]
        for row in range(n):
            safe_columns = [col for col in range(n) if is_safe_las_vegas(board, row, col, n)]
            if not safe_columns:
                break  # Reiniciar si no hay columnas seguras
            col = random.choice(safe_columns)  # Elegir una columna aleatoria segura
            board[row][col] = True
        else:
            return board  # Solución encontrada
    
# Imprimir el tablero en consola con las reinas ubicadas
def print_solution(board):
    """Imprime el tablero con las reinas ubicadas."""
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

# Ejemplo de uso
""" if __name__ == "__main__":
    n = 15  # Cambia este valor para probar otros tamaños de tablero
    solution = las_vegas_n_queens(n)
    if solution:
        print_solution(solution) """

#################################################################################
# Simulación de la competencia entre el robot y el humano
#################################################################################

# Configuración de la simulación
SIMULATION_TIME = 8 * 60 * 60 # 8 horas en segundos
ARRIVAL_INTERVAL = (10, 30)  # Intervalo de llegada del robot en segundos
BOARD_SIZES = [5]  # Tamaños posibles del tablero
#BOARD_SIZES = [4, 5, 6, 8, 10, 12, 15]  # Tamaños posibles del tablero

def simulacion(env, sim_time=SIMULATION_TIME, arrival_interval=ARRIVAL_INTERVAL, board_sizes=BOARD_SIZES, root=None):
    """Configura el ambiente de simulación."""
    #resultados = []  # Lista de resultados de las partidas
    ganancias = [0]  # Ganancias acumuladas
    fin_simulacion = sim_time  # Definir el tiempo máximo de simulación
    
    while env.now < fin_simulacion:
        # Seleccionar tamaño del tablero aleatorio (para ambos jugadores)
        n = random.choice(board_sizes)
        print(f"{env.now:.2f}s - Comienza juego con tablero de tamaño {n}x{n}")

        # Resolver con el algoritmo Las Vegas para el robot
        start_time = time()
        robot_solution = las_vegas_n_queens(n)
        robot_time = time() - start_time
        
        # Resolver con el algoritmo determinista para el humano
        start_time = time()
        humano_solution = solve_n_queens(n)
        humano_time = time() - start_time
        
        # Registrar resultados
        if robot_solution:
            print(f"{env.now:.2f}s - Robot resolvió el tablero en {robot_time:.8f} segundos")
            #resultados.append(('Robot', robot_time, n))
        else:
            print(f"{env.now:.2f}s - El Robot no resolvió el tablero")
        
        if humano_solution:
            print(f"{env.now:.2f}s - Humano resolvió el tablero en {humano_time:.8f} segundos")
            #resultados.append(('Humano', humano_time, n))
        else:
            print(f"{env.now:.2f}s - El Humano no resolvió el tablero")
        
        # Comparar resultados
        if robot_time < humano_time:
            print(f"{env.now:.2f}s - El robot gana con un tiempo de {robot_time:.8f} segundos")
            ganancias[0] -= 10  # El robot gana
        elif humano_time < robot_time:
            print(f"{env.now:.2f}s - El humano gana con un tiempo de {humano_time:.8f} segundos")
            ganancias[0] += 15  # El humano gana
        else:
            print(f"{env.now:.2f}s - Empate")
        
        # Esperar para la próxima simulación
        yield env.timeout(random.uniform(*arrival_interval))
    
    # Al finalizar la simulación, mostrar el resumen
    print("\n=== Resumen de la simulación ===")
    print(f"Ganancia total: {ganancias[0]} unidades")
    """ print("Resultados de las partidas:")
    for tipo, tiempo, n in resultados:
        print(f"  {tipo} resolvió el tablero de tamaño {n}x{n} en {tiempo:.4f} segundos") """
    
    # Mostrar ventana emergente con el resultado de ganancias[0]
    if root:
        root.after(0, lambda: messagebox.showinfo("Resultado", f"Ganancia total: {ganancias[0]} unidades", parent=root))

# Ejemplo de uso
""" if __name__ == "__main__":
    env = simpy.Environment()
    env.process(simulacion(env))
    env.run() """