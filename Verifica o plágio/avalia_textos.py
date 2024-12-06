'''
def avalia_textos(textos, ass_cp):
    #Identifica o texto mais provável de ter sido infectado com base na assinatura típica.
    diferencas = []
    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        diferenca = compara_assinatura(ass_cp, assinatura_texto)
        diferencas.append(diferenca)

    return diferencas.index(min(diferencas)) + 1
'''