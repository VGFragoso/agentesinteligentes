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
            if set(condicoes).issubset(set(caracteristicas.items())):
                return self.regras[condicoes]
        return None

# Exemplo de uso
base = BaseConhecimento()
base.adicionar_fato("esportivo", {"rodas": 4, "motor": "potente", "tamanho": "pequeno", "portas": 2})
base.adicionar_fato("sedan", {"rodas": 4, "motor": "médio", "tamanho": "médio", "portas": 4})
base.adicionar_fato("minivan", {"rodas": 4, "motor": "potente", "tamanho": "grande", "portas": 5})

base.adicionar_regra({"rodas": 4, "motor": "potente"}, "esportivo")
base.adicionar_regra({"rodas": 4, "motor": "médio", "portas": 4}, "sedan")
base.adicionar_regra({"rodas": 4, "motor": "potente", "portas": 5}, "minivan")

caracteristicas_veiculo = {"rodas": 4, "motor": "potente", "tamanho": "pequeno", "portas": 2}
tipo_veiculo = base.inferir(caracteristicas_veiculo)
if tipo_veiculo:
    print(f"O veículo é um {tipo_veiculo}")
else:
    print("Não foi possível determinar o tipo do veículo")
