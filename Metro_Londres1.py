import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def calculate_heuristic(node, goal_state):
    return abs(int(node.state[1:]) - int(goal_state[1:]))

def a_star(start_state, goal_state, connections, distances):
    open_list = []
    closed_set = set()
    log = []

    start_node = Node(start_state)
    start_node.heuristic = calculate_heuristic(start_node, goal_state)
    heapq.heappush(open_list, start_node)
    log.append((start_node.state, start_node.cost))

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            path = []
            total_distance = current_node.cost
            while current_node.parent:
                path.append(current_node.state)
                current_node = current_node.parent
            path.append(start_state)
            return path[::-1], total_distance, log

        closed_set.add(current_node.state)

        for neighbor, distance in zip(connections[current_node.state], distances[current_node.state]):
            if neighbor not in closed_set:
                neighbor_node = Node(neighbor, current_node, cost=current_node.cost + distance)
                neighbor_node.heuristic = calculate_heuristic(neighbor_node, goal_state)
                heapq.heappush(open_list, neighbor_node)
                log.append((neighbor_node.state, neighbor_node.cost))

    return None, -1, log

connections = {
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

distances = {
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

start_station = input("Digite a estação de partida (E1, E2, ..., E14): ")
goal_station = input("Digite a estação de destino (E1, E2, ..., E14): ")

if start_station not in connections or goal_station not in connections:
    print("Estações inválidas. Certifique-se de digitar valores válidos.")
else:
    path, total_distance, log = a_star(start_station, goal_station, connections, distances)

    if path and total_distance != -1:
        print("Caminho percorrido entre os nós:", path)
        print("Tempo em horas para percorrer essa rota:", "{:.2f}".format(total_distance / 60))
        print("Custo de cada nó do caminho percorrido:")
        for node, cost in log:
            print(f"{node} ({cost})")
        print("Valor total percorrido em km:", total_distance)
    else:
        print("Não foi possível encontrar um caminho.")
