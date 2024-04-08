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
            if all(item in caracteristicas.items() for item in condicoes):
                return self.regras[condicoes]
        return None

# Exemplo de uso
base = BaseConhecimento()
base.adicionar_fato("romance", {"autor": "", "formato": "", "ano_lancamento": ""})
base.adicionar_fato("ficcao_cientifica", {"autor": "", "formato": "", "ano_lancamento": ""})
base.adicionar_fato("biografia", {"autor": "", "formato": "", "ano_lancamento": ""})
base.adicionar_fato("fantasia", {"autor": "", "formato": "", "ano_lancamento": ""})
base.adicionar_fato("poesia", {"autor": "", "formato": "", "ano_lancamento": ""})

base.adicionar_regra({"autor": "Jane Austen", "formato": "fisico", "ano_lancamento": "1800s"}, "romance")
base.adicionar_regra({"autor": "Isaac Asimov", "formato": "digital", "ano_lancamento": "1950s"}, "ficcao_cientifica")
base.adicionar_regra({"autor": "Walter Isaacson", "formato": "fisico", "ano_lancamento": "2000s"}, "biografia")
base.adicionar_regra({"autor": "Neil Gaiman", "formato": "digital", "ano_lancamento": "1990s"}, "fantasia")
base.adicionar_regra({"autor": "Emily Dickinson", "formato": "fisico", "ano_lancamento": "1800s"}, "poesia")
base.adicionar_regra({"autor": "Charles Dickens", "formato": "fisico", "ano_lancamento": "1800s"}, "romance")
base.adicionar_regra({"autor": "Agatha Christie", "formato": "fisico", "ano_lancamento": "1900s"}, "romance")
base.adicionar_regra({"autor": "George Orwell", "formato": "digital", "ano_lancamento": "1940s"}, "ficcao_cientifica")
base.adicionar_regra({"autor": "Pablo Neruda", "formato": "fisico", "ano_lancamento": "1900s"}, "poesia")
base.adicionar_regra({"autor": "J.R.R. Tolkien", "formato": "digital", "ano_lancamento": "1950s"}, "fantasia")

print("Preencha as informações do livro:")
print("Autores disponíveis: Jane Austen, Isaac Asimov, Walter Isaacson, Neil Gaiman, Emily Dickinson, Charles Dickens, Agatha Christie, George Orwell, Pablo Neruda, J.R.R. Tolkien")
autor = input("Autor (Digite o nome exatamente como listado acima): ")
print("Formato disponível: fisico, digital")
formato = input("Formato (fisico ou digital): ")
ano_lancamento = input("Ano de lançamento: ")

caracteristicas_livro = {"autor": autor, "formato": formato, "ano_lancamento": ano_lancamento}
categoria_livro = base.inferir(caracteristicas_livro)
if categoria_livro:
    print(f"O livro se enquadra na categoria: {categoria_livro}")
else:
    print("Não foi possível determinar a categoria do livro")
