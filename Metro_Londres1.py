import heapq
from math import sqrt

estacao_conexao = { 
    "E1": ["E2"],
    "E2": ["E1", "E3", "E7", "E9"],
    "E3": ["E2", "E4", "E7", "E8"],
    "E4": ["E3", "E5", "E8", "E14"],
    "E5": ["E4"],
    "E6": ["E7"],
    "E7": ["E2", "E3", "E6"],
    "E8": ["E3", "E4", "E9", "E10"],
    "E9": ["E2", "E8", "E10", "E11"],
    "E10": ["E8", "E9", "E12", "E13"],
    "E11": ["E9"],
    "E12": ["E10"],
    "E13": ["E10"],
    "E14": ["E4"]
}

linhas = {
    "Linha Vermelha": ["E1", "E2", "E3", "E4", "E14"], 
    "Linha Verde": ["E7", "E2", "E9", "E10", "E13"],
    "Linha Azul": ["E6", "E7", "E3", "E8", "E10", "E12"],
    "Linha Amarela": ["E11", "E9", "E8", "E4", "E5"]
}


distancia_reta = { 
    "E1": [4.3, 9, 14.7, 17.2, 13.1, 11.8, 11.3, 8.2, 10.7, 8.4, 14.1, 18.5, 17.3],
    "E2": [4.3, 5.3, 10.3, 13.1, 12.7, 10.3, 6.9, 4.3, 7.4, 5.9, 11.3, 14.8, 12.9],
    "E3": [9, 5.3, 5.9, 8.5, 10.9, 7.7, 4.1, 6.5, 8.9, 9.4, 14.5, 13.9, 10.3],
    "E4": [14.7, 10.3, 5.9, 2.9, 15, 12.7, 4, 9.1, 9.7, 12.2, 14.7, 10.6, 6],
    "E5": [17.2, 13.1, 8.5, 2.9, 16, 12.3, 7, 12, 15.3, 14.8, 17.3, 12.7, 6.9],
    "E6": [13.1, 12.7, 10.9, 15, 16, 3.2, 15.1, 16.5, 18.5, 19, 24.3, 25.2, 21.1],
    "E7": [11.8, 10.3, 7.7, 12.7, 12.3, 3.2, 12, 13.3, 16.4, 16, 22.2, 22.6, 17.1],
    "E8": [11.3, 6.9, 4.1, 4, 7, 15.1, 12, 5, 5.6, 7.9, 12.4, 9.8, 6.4],
    "E9": [8.2, 4.3, 6.5, 9.1, 12, 16.5, 13.3, 5, 3, 3.4, 8.1, 10.9, 9.6],
    "E10": [10.7, 7.4, 8.9, 9.7, 15.3, 18.5, 16.4, 5.6, 3, 3.4, 5.6, 7.7, 8.4],
    "E11": [8.4, 5.9, 9.4, 12.2, 14.8, 19, 16, 7.9, 3.4, 3.4, 5.9, 11.2, 12.7],
    "E12": [14.1, 11.3, 14.5, 14.7, 17.3, 24.3, 22.2, 12.4, 8.1, 5.6, 5.9, 11.2, 12.7],
    "E13": [18.5, 14.8, 13.9, 10.6, 12.7, 25.2, 22.6, 9.8, 10.9, 7.7, 11.2, 8.6, 12.3],
    "E14": [17.3, 12.9, 10.3, 6, 6.9, 21.1, 17.1, 6.4, 9.6, 8.4, 12.7, 12.3, 6.1]
}

distancia_real = {
    "E1": [4.3],
    "E2": [4.3, 5.3, 14.3, 4.3],
    "E3": [5.3, 5.9, 8.5, 4.1],
    "E4": [5.9, 2.9, 4, 6.2],
    "E5": [2.9],
    "E6": [3.2],
    "E7": [14.3, 8.5, 3.2],
    "E8": [4.1, 4, 5, 6],
    "E9": [4.3, 5, 3, 3.4],
    "E10": [6, 3, 5.6, 9.1],
    "E11": [3.4],
    "E12": [5.6],
    "E13": [9.1],
    "E14": [6.2]
}


velocidade = 40


baldeacao_time = 0.05

def distancia_euclidiana(estacao01, station02):
    """
    Calcula a distância euclidiana entre duas estações.
    """
    x1, y1 = estacao01[0], estacao01[1]
    x2, y2 = station02[0], station02[1]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def heuristica(estacao1, estacao2):
    """
    Função heurística para o A* (distância euclidiana).
    """
    return distancia_euclidiana(estacao1, estacao2) / velocidade

def astar(inicio, destino):
    """
    Algoritmo A* para encontrar o melhor caminho entre a estação inicial e o destino.
    """
    fronteira = []
    heapq.heappush(fronteira, (0, inicio))  # (f(n), estação)
    came_from = {}
    cost_so_far = {}
    came_from[inicio] = None
    cost_so_far[inicio] = 0
    stations_visited = []  # Manter registro das estações visitadas
    line_changes = 0  # Contador de mudanças de linha

    while fronteira:
        _, current = heapq.heappop(fronteira)

        if current == destino:
            break

        for next_station in estacao_conexao[current]:
            new_cost = cost_so_far[current] + distancia_real[current][estacao_conexao[current].index(next_station)]
            if next_station not in cost_so_far or new_cost < cost_so_far[next_station]:
                cost_so_far[next_station] = new_cost
                priority = new_cost + heuristica(distancia_reta[next_station], distancia_reta[destino])
                heapq.heappush(fronteira, (priority, next_station))
                came_from[next_station] = current
                stations_visited.append(next_station)  # Registrar estação visitada

    # Reconstruir o caminho
    path = []
    current = destino
    while current != inicio:
        path.append(current)
        current = came_from[current]
    path.append(inicio)
    path.reverse()

    # Calcular tempo de percurso e contagem de mudanças de linha
    tempo = 0
    current_line = None

    for i in range(len(path) - 1):
        current_station = path[i]
        next_station = path[i + 1]

        # Verificar mudança de linha e adicionar tempo de baldeação
        current_station_line = None
        next_station_line = None

        for line, stations in linhas.items():
            if current_station in stations:
                current_station_line = line
            if next_station in stations:
                next_station_line = line

        if current_station_line and next_station_line and current_station_line != next_station_line:
            tempo += baldeacao_time
            line_changes += 1

        tempo += distancia_real[current_station][estacao_conexao[current_station].index(next_station)] / velocidade

    return path, cost_so_far[destino], tempo, stations_visited, line_changes

def main():
    inicio = input("Digite a estação inicial: ")
    destino = input("Digite a estação de destino: ")

    if inicio not in estacao_conexao or destino not in estacao_conexao:
        print("Estação inicial ou de destino não encontrada.")
        return

    rota, distance, time, stations_visited, _ = astar(inicio, destino)  # Ignorar o número de mudanças de linha aqui
    print("Melhor rota:")
    for i, estacao in enumerate(rota):
        if i == len(rota) - 1:
            print(estacao)
        else:
            print(estacao, "->", end=" ")
    print("Distância percorrida:", round(distance, 1), "km")
    
    # Verificar mudanças de linha após encontrar a melhor rota
    line_changes = 0
    current_line = None
    tempo = 0

    for i in range(len(rota) - 1):
        current_station = rota[i]
        next_station = rota[i + 1]

        # Verificar se houve mudança de linha
        if current_line is None:  # Primeira estação do caminho
            current_line = get_station_line(current_station)
        next_line = get_station_line(next_station)

        if current_line != next_line:  # Se houver mudança de linha
            line_changes += 1
            tempo += baldeacao_time  # Adicionar tempo de baldeação
            current_line = next_line  

        tempo += distancia_real[current_station][estacao_conexao[current_station].index(next_station)] / velocidade

    print("Tempo do percurso:", round(tempo, 2), "horas")
    print("Estações visitadas:", stations_visited)
    print("Mudanças de linha:", line_changes)

def get_station_line(station):
    """
    Retorna a linha à qual a estação pertence.
    """
    for line, stations in linhas.items():
        if station in stations:
            return line
    return None  

if __name__ == "__main__":
    main()
