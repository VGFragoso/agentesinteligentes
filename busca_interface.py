import heapq
import tkinter as tk
from tkinter import messagebox

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

def calculate_time(distance_km, speed_kmph, change_line=False):
    time_hours = distance_km / speed_kmph
    if change_line:
        time_hours += 3 / 60  # 3 minutos referentes a mudança de linha
    return time_hours, 3 / 60 if change_line else 0  # Retorna também o tempo de baldeação se houver

def a_star(start_state, goal_state, connections, distances, lines):
    open_list = []
    closed_set = set()
    log = []
    num_transfers = 0

    start_node = Node(start_state)
    start_node.heuristic = calculate_heuristic(start_node, goal_state)
    heapq.heappush(open_list, start_node)
    log.append((start_node.state, start_node.cost))

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            path = []
            total_distance = current_node.cost
            total_time = current_node.cost / 40  # 40 é referente a velocidade do trem
            while current_node.parent:
                path.append(current_node.state)
                current_node = current_node.parent
            path.append(start_state)
            path.reverse()  # Inverte a lista para mostrar o caminho do início ao fim
            return path, total_distance, total_time, num_transfers, log

        closed_set.add(current_node.state)

        for neighbor, distance in zip(connections[current_node.state], distances[current_node.state]):
            if neighbor not in closed_set:
                neighbor_node = Node(neighbor, current_node, cost=current_node.cost + distance)
                neighbor_node.heuristic = calculate_heuristic(neighbor_node, goal_state)

                # Conferindo a mudança entre as linhas
                current_line = None
                neighbor_line = None
                for line, stations in lines.items():
                    if current_node.state in stations:
                        current_line = line
                    if neighbor in stations:
                        neighbor_line = line

                change_line = current_line != neighbor_line
                neighbor_node.cost += calculate_time(distance, 40, change_line)[0]  # Adiciona apenas o tempo de viagem
                num_transfers += 1 if change_line else 0  # Incrementa o número de baldeações se houver

                heapq.heappush(open_list, neighbor_node)
                log.append((neighbor_node.state, neighbor_node.cost))

    return None, -1, -1, -1, log

def find_path():
    global connections, distances, lines
    start_station = entry_start.get()
    goal_station = entry_goal.get()

    if start_station not in connections or goal_station not in connections:
        messagebox.showerror("Erro", "Estações inválidas. Certifique-se de digitar valores válidos.")
    else:
        path, total_distance, total_time, num_transfers, log = a_star(start_station, goal_station, connections, distances, lines)

        if path and total_distance != -1 and total_time != -1:
            result_str = f"Melhor caminho encontrado:\n"
            result_str += f"Caminho percorrido: {' -> '.join(path)}\n"
            result_str += f"Tempo total de viagem: {round(total_time, 2)} horas\n"
            result_str += f"Número de baldeações: {num_transfers}\n"
            result_str += f"Valor total percorrido: {round(total_distance, 2)} km\n"
            messagebox.showinfo("Resultado", result_str)
        else:
            messagebox.showerror("Erro", "Não foi possível encontrar um caminho.")

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

lines = {
    "Linha Vermelha": ["E1", "E2", "E3", "E4", "E14"],
    "Linha Verde": ["E7", "E2", "E9", "E10", "E13"],
    "Linha Azul": ["E6", "E7", "E3", "E8", "E10", "E12"],
    "Linha Amarela": ["E11", "E9", "E8", "E4", "E5"]
}

window = tk.Tk()
window.title("Planejador de Viagens de Trem")
window.geometry("400x200")

label_start = tk.Label(window, text="Estação de partida:")
label_start.pack()
entry_start = tk.Entry(window)
entry_start.pack()

label_goal = tk.Label(window, text="Estação de destino:")
label_goal.pack()
entry_goal = tk.Entry(window)
entry_goal.pack()

button_find = tk.Button(window, text="Buscar Caminho", command=find_path)
button_find.pack()

window.mainloop()

