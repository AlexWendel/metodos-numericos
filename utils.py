import math

pi = math.pi

# CUIDADO QUE ESSA PORRA PODE TROCAR OS VALORES, DEPENDENDO DA ORDEM DOS ITENS DO DICIONÁRIO
def get_partial_eq(eq, values):
    for k,v in values.items():
        eq = eq.replace(str(k), str(v))
    return eq

def ln(x):
    return math.log(x, 10)

def sen(x):
    return math.sin(x)

def tg(x):
    return math.tan(x)

def cos(x):
    return math.cos(x)

def arcos(x):
    return math.acos()

def arcsen(x):
    return math.asin()