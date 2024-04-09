class BaseConhecimento:
    def __init__(self):
        self.fatos = {}
        self.regras = {}

    def adicionar_fato(self, item, caracteristicas):
        self.fatos[item] = caracteristicas

    def adicionar_regra(self, condicoes, resultado):
        self.regras[tuple(sorted(condicoes.items()))] = resultado

    def inferir(self, caracteristicas):
        for condicoes in self.regras:
            print("passou n_1")
            if all(item in caracteristicas.items() for item in condicoes):
                print("passou n_2")
                return self.regras[condicoes]
        return None

# Exemplo dos carros - Flavia

base = BaseConhecimento()

#adicionei somente um fato para ve ro que acontece
#base.adicionar_fato("CarroSport", {"veiculoTipo": "automovel", "tamanho": "pequeno", "portas": 2})


#regras iniciais – eu não sei se posso usar sinal de maior ou menor que. #Então fiz duas regras para o caso do ciclo.
base.adicionar_regra({"rodas": 2}, "ciclo")
base.adicionar_regra({"rodas": 3}, "ciclo")
base.adicionar_regra({"rodas": 4, "motor": "sim"}, "automovel")

#regras finais
base.adicionar_regra({"veiculoTipo": "ciclo", "rodas": 2, "motor": "nao"}, "bicicleta")
base.adicionar_regra({"veiculoTipo": "ciclo", "rodas": 3, "motor": "nao"}, "triciclo")
base.adicionar_regra({"veiculoTipo": "ciclo", "rodas": 2, "motor": "sim"}, "motocicleta")

base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "pequeno", "portas": 2}, "CarroSport")
base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "medio", "portas": 4}, "Sedan")
base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "medio", "portas": 3}, "Minivan")
base.adicionar_regra({"veiculoTipo": "automovel", "tamanho": "grande", "portas": 4}, "UtilitarioSport")

#input dentro do código – botei o input diferente do fato incluído na base.
caracteristicas_veiculo = {"rodas": 4, "motor": "sim"}
##caracteristicas_veiculo = {"tamanho": "medio", "portas": 3}

# código da inferencia

entrada: None
input(entrada)
if entrada == "Fim":
    print("Terminou")

tipo_veiculo = base.inferir(caracteristicas_veiculo)
if tipo_veiculo:
    print(f"O veículo é um {tipo_veiculo}")
else:
    print("Não foi possível determinar o tipo do veículo")
    tipo_veiculo = base.inferir(caracteristicas_veiculo)

#caracteristicas_veiculo = {"veiculoTipo": "automovel", "tamanho": "medio", "portas": 3}
#tipo_veiculo = base.inferir(caracteristicas_veiculo)
#if tipo_veiculo:
#    print(f"O veículo é um {tipo_veiculo}")
#else:
#    print("Não foi possível determinar o tipo do veículo")
#    tipo_veiculo = base.inferir(caracteristicas_veiculo)







