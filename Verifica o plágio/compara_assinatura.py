'''
def compara_assinatura(as_a, as_b):
#Compara duas assinaturas e retorna o grau de similaridade.
    return sum(abs(a - b) for a, b in zip(as_a, as_b)) / len(as_a)
'''