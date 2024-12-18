import random
from time import time

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
    start_time = time();
    """Resuelve el problema de las n reinas y devuelve la solución."""
    board = [[False] * n for _ in range(n)]  # Crear tablero vacío
    if not solve_n_queens_util(board, 0, n):
        print("No hay solución para el tamaño dado.")
        return None
    end_time = time() - start_time;
    return end_time, board


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
    start_time = time();
    while True:
        board = [[False] * n for _ in range(n)]
        for row in range(n):
            safe_columns = [col for col in range(n) if is_safe_las_vegas(board, row, col, n)]
            if not safe_columns:
                break  # Reiniciar si no hay columnas seguras
            col = random.choice(safe_columns)  # Elegir una columna aleatoria segura
            board[row][col] = True
        else:
            end_time = time() - start_time;
            return end_time, board  # Solución encontrada

#################################################################################
# Simulación de la competencia entre el robot y el humano
#################################################################################

# Configuración de la simulación
SIMULATION_TIME = 8 * 60 * 60 # 8 horas en segundos
ARRIVAL_INTERVAL = (10, 30)  # Intervalo de llegada del robot en segundos
BOARD_SIZES = [4, 5, 6, 8, 10, 12, 15]  # Tamaños posibles del tablero

def simulacion(env, sim_time=SIMULATION_TIME, arrival_interval=ARRIVAL_INTERVAL, board_sizes=BOARD_SIZES, root=None):
    print("Iniciando simulación...")

    """Configura el ambiente de simulación."""
    #resultados = []  # Lista de resultados de las partidas
    ganancias = [0]  # Ganancias acumuladas
    fin_simulacion = sim_time  # Definir el tiempo máximo de simulación
    start_time = time()
    partidas = 0
    
    while env.now < fin_simulacion:
        partidas += 1
        # Seleccionar tamaño del tablero (para ambos jugadores)
        if len(board_sizes) == 1:
            n = board_sizes[0]
        else:
            n = random.choice(board_sizes)

        # Resolver con el algoritmo Las Vegas para el robot
        robot_time, _ = las_vegas_n_queens(n)
        print(f"{env.now:.2f}s - Robot resolvió el tablero en {robot_time:.8f} segundos")
        
        # Resolver con el algoritmo determinista para el humano
        humano_time, _ = solve_n_queens(n)
        print(f"{env.now:.2f}s - Humano resolvió el tablero en {humano_time:.8f} segundos")

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
    
    end_time = time() - start_time

    # Al finalizar la simulación, mostrar el resumen
    print("\nSimulación finalizada en {:.2f} segundos".format(end_time))
    print("\n=== Resumen de la simulación ===")
    print(f"Partidas jugadas: {partidas}")
    print(f"Ganancia total: {ganancias[0]} unidades")
    print(f"Tiempo de simulación: {sim_time / 3600} horas")
    print(f"Intervalo de llegada: {arrival_interval[0]} - {arrival_interval[1]} segundos")
    print(f"Tamaños de tablero: {board_sizes}\n")
    
    return ganancias[0], end_time, partidas