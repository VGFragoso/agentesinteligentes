import base64


def mermaid(graph):
    graph_bytes = graph.encode("ascii")
    base64_bytes = base64.b64encode(graph_bytes)
    base64_string = base64_bytes.decode("ascii")

    return "https://mermaid.ink/img/" + base64_string


# def create_mermaid_diagram(graph, path, relationships, arrow_texts):
def create_mermaid_diagram(distancia_real, estacao_conexao, path, relationships, arrow_texts):
    mermaid_syntax = "flowchart TD;\n"

    for child, parent in relationships.items():
        if parent is not None:
            # new_cost_formatted = format(graph[parent][child], ".2f")
            new_cost_formatted = format(distancia_real[parent][estacao_conexao[parent].index(child)], ".2f")
            cost_so_far_formatted = format(arrow_texts[child], ".2f")

            attributes = (
                f"|Custo: +{new_cost_formatted}; Acumulado: {cost_so_far_formatted}|"
            )

            last_child_style = ":::destaque" if (child in path) else ""
            first_parent_style = ":::destaque" if (parent in path) else ""

            mermaid_syntax += f"{parent}{first_parent_style} --> {attributes} {child}{last_child_style}\n"

    mermaid_syntax += "classDef destaque fill:#09c \n"

    return mermaid_syntax
