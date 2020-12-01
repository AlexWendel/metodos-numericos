# CUIDADO QUE ESSA PORRA PODE TROCAR OS VALORES, DEPENDENDO DA ORDEM DOS ITENS DO DICIONÁRIO
def get_partial_eq(eq, values):
    for k,v in values.items():
        eq = eq.replace(str(k), str(v))
    return eq