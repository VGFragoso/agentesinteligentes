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
    "Linha Azul": ["E6", "E7", "E3", "E8", "E10", "E12"],
    "Linha Vermelha": ["E1", "E2", "E3", "E4", "E14"], 
    "Linha Verde": ["E2", "E7", "E9", "E10", "E13"],
    "Linha Amarela": ["E11", "E9", "E8", "E4", "E5"]
}

distancia_direta = { 
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
baldeacao_temp = 0.05  # Em Horas

def distancia_euclidiana(estacao01, estacao02):
    """
    Calcula a distância euclidiana entre duas estações.
    """
    x1, y1 = estacao01[0], estacao01[1]
    x2, y2 = estacao02[0], estacao02[1]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def heuristica(estacao1, estacao2):
    ##Função heurística para o A* (distância euclidiana).
    return distancia_euclidiana(estacao1, estacao2) / velocidade

def astar(inicio, destino, log_file):
    ## (f(n), estação, G)
    fronteira = []
    heapq.heappush(fronteira, (0, inicio, 0))  
    move_de = {}
    custo_momento = {}
    move_de[inicio] = None
    custo_momento[inicio] = 0
    estacao_visita = []  
    mud_linha = 0  
    h_atual = heuristica(distancia_direta[inicio], distancia_direta[destino])

    log_file.write(f"Nó Raiz: {inicio} (G: {custo_momento[inicio]})\n")
    log_file.write("\n")

    while fronteira:
        _, m_atual, g_atual = heapq.heappop(fronteira)

        if m_atual == destino:
            log_file.write(f"Nó Final (Destino): {m_atual} (G: {g_atual})\n")
            log_file.write("\n")
            break

        for prox_estacao in estacao_conexao[m_atual]:
            novo_custo = custo_momento[m_atual] + distancia_real[m_atual][estacao_conexao[m_atual].index(prox_estacao)]
            if prox_estacao not in custo_momento or novo_custo < custo_momento[prox_estacao]:
                custo_momento[prox_estacao] = novo_custo
                prioridade = novo_custo + heuristica(distancia_direta[prox_estacao], distancia_direta[destino])
                heapq.heappush(fronteira, (prioridade, prox_estacao, novo_custo))
                move_de[prox_estacao] = m_atual
                estacao_visita.append(prox_estacao)  

                linha_prox_estacao = get_station_line(prox_estacao)
                log_file.write(f"Nó visitado: {prox_estacao} (Linha: {linha_prox_estacao}, G: {novo_custo})\n")
                log_file.write(f"Partindo de: {m_atual}\n")
                log_file.write("\n")

    rota = []
    m_atual = destino
    while m_atual != inicio:
        rota.append(m_atual)
        m_atual = move_de[m_atual]
    rota.append(inicio)
    rota.reverse()

    tempo = 0
    at_linha = None

    for i in range(len(rota) - 1):
        estacao_atual = rota[i]
        prox_estacao = rota[i + 1]

        l_estacao_atual = None
        l_prox_estacao = None
        prev_station = rota[i - 1] if i > 0 else None

        for line, estacao in linhas.items():
            if estacao_atual in estacao:
                l_estacao_atual = line
            if prox_estacao in estacao:
                l_prox_estacao = line

        if l_estacao_atual and l_prox_estacao and l_estacao_atual != l_prox_estacao:
            tempo += baldeacao_temp
            mud_linha += 1

        tempo += distancia_real[estacao_atual][estacao_conexao[estacao_atual].index(prox_estacao)] / velocidade

    return rota, custo_momento[destino], tempo, estacao_visita, mud_linha

def main():
    while True:
        linhas_disponiveis = ', '.join(linhas.keys())

        linha_inicio = input(f"Digite a linha da estação inicial ({linhas_disponiveis}): ")
        if linha_inicio not in linhas:
            print("Linha inicial inválida. As linhas disponíveis são:", linhas_disponiveis)
            continue
        estacao_inicio = input(f"Digite o número da estação inicial ({', '.join(linhas[linha_inicio])}): ")
        if estacao_inicio not in linhas[linha_inicio]:
            print("Estação inicial inválida para a linha selecionada.")
            continue

        linha_destino = input(f"Digite a linha da estação de destino ({linhas_disponiveis}): ")
        if linha_destino not in linhas:
            print("Linha de destino inválida. As linhas disponíveis são:", linhas_disponiveis)
            continue
        estacao_destino = input(f"Digite o número da estação de destino ({', '.join(linhas[linha_destino])}): ")
        if estacao_destino not in linhas[linha_destino]:
            print("Estação de destino inválida para a linha selecionada.")
            continue

        inicio = estacao_inicio
        destino = estacao_destino

        if inicio not in estacao_conexao or destino not in estacao_conexao:
            print("Estação inicial ou de destino não encontrada.")
            continue
        
        with open('log.txt', 'w') as log_file:
            rota, distance, tempo, no_visitado, _ = astar(inicio, destino, log_file)  
            print("Melhor rota:")
            for i, estacao in enumerate(rota):
                if i == len(rota) - 1:
                    print(estacao, f"({get_station_line(estacao)})")
                else:
                    print(estacao, f"({get_station_line(estacao)})", "->", end=" ")
            print("Distância percorrida:", round(distance, 1), "km")
            
            m_linha = 0
            at_linha = None
            tempo_min = 0

            if get_station_line(inicio) != get_station_line(destino):  # Verifica se a linha inicial é diferente da linha final
                for i in range(len(rota) - 1):
                    estacao_at = rota[i]
                    prox_estacao = rota[i + 1]

                    if at_linha is None:  
                        at_linha = get_station_line(estacao_at)
                    prox_linha = get_station_line(prox_estacao)

                    if at_linha != prox_linha:  
                        m_linha += 1
                        tempo_min += baldeacao_temp * 60  # Convertendo para minutos
                        at_linha = prox_linha  

                    tempo_min += distancia_real[estacao_at][estacao_conexao[estacao_at].index(prox_estacao)] / velocidade * 60  # Convertendo para minutos

            print("Tempo do percurso:", round(tempo_min, 2), "minutos")
            print("Nós Percorridos:", no_visitado)
            print("Mudanças de linha:", m_linha)

        continuar = input("Deseja fazer outra consulta? (Digite 'sim' para continuar ou qualquer outra coisa para sair): ")
        if continuar.lower() != 'sim':
            break

def get_station_line(station):
    """
    Retorna a linha à qual a estação pertence.
    """
    for linha, estacoes in linhas.items():
        if station in estacoes:
            return linha
    return None

if __name__ == "__main__":
    main()
