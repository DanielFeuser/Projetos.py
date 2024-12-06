import re

def le_assinatura():
    '''Lê os valores da assinatura típica de um texto infectado e retorna uma lista com os traços.'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho médio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''Lê e retorna uma lista com os textos a serem analisados.'''
    textos = []
    i = 1
    while True:
        texto = input(f"Digite o texto {i} (aperte enter para sair): ")
        if not texto:
            break
        textos.append(texto)
        i += 1
    return textos

def separa_sentencas(texto):
    '''Recebe um texto e retorna uma lista com as sentenças dentro dele.'''
    sentencas = re.split(r'[.!?]+', texto)
    return [s.strip() for s in sentencas if s.strip()]

def separa_frases(sentenca):
    '''Recebe uma sentença e retorna uma lista com as frases dentro dela.'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''Recebe uma frase e retorna uma lista com as palavras dentro dela.'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Retorna o número de palavras que aparecem uma única vez.'''
    freq = {}
    for palavra in lista_palavras:
        p = palavra.lower()
        freq[p] = freq.get(p, 0) + 1
    return sum(1 for count in freq.values() if count == 1)

def n_palavras_diferentes(lista_palavras):
    '''Retorna o número de palavras diferentes usadas.'''
    freq = {}
    for palavra in lista_palavras:
        p = palavra.lower()
        freq[p] = freq.get(p, 0) + 1
    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Compara duas assinaturas e retorna o grau de similaridade.'''
    return sum(abs(a - b) for a, b in zip(as_a, as_b)) / len(as_a)

def calcula_assinatura(texto):
    '''Calcula a assinatura de um texto e retorna uma lista com seus traços linguísticos.'''
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []

    # Comprimento total de sentenças
    tam_sentencas = sum(len(sentenca) for sentenca in sentencas)
    
    for sentenca in sentencas:
        sub_frases = separa_frases(sentenca)
        frases.extend(sub_frases)
    
    # Comprimento total de frases
    tam_frases = sum(len(frase) for frase in frases)
    
    for frase in frases:
        palavras.extend(separa_palavras(frase))
    
    # Comprimento total de palavras
    tam_palavras = sum(len(palavra) for palavra in palavras)

    # Calcula métricas linguísticas
    wal = tam_palavras / len(palavras) if palavras else 0
    ttr = n_palavras_diferentes(palavras) / len(palavras) if palavras else 0
    hlr = n_palavras_unicas(palavras) / len(palavras) if palavras else 0
    sal = tam_sentencas / len(sentencas) if sentencas else 0
    sac = len(frases) / len(sentencas) if sentencas else 0
    pal = tam_frases / len(frases) if frases else 0

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Identifica o texto mais provável de ter sido infectado com base na assinatura típica.'''
    diferencas = []
    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        diferenca = compara_assinatura(ass_cp, assinatura_texto)
        diferencas.append(diferenca)

    return diferencas.index(min(diferencas)) + 1
