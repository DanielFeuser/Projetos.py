"""
def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto) # ---> Separa o texto em sentenças.
    palavras = [] # ---> Lista que armazena todas as palavras .
    num_sentencas = len(sentencas) # ---> Número total de sentenças.
    num_frases = 0 # ---> Variável para contar o número de frases.

    for sentenca in sentencas:
        frases = separa_frases(sentenca) # ---> Separa a sentença em frases
        num_frases = num_frases + len(frases) # ---> Soma o número de frases em cada sentença.
        for frase in frases:#---> Para cada frase na sentença, separa as palavras
            palavras.extend(separa_palavras(frase))

    wal = sum(len(palavra) for palavra in palavras) / len(palavras)
    ttr = n_palavras_diferentes(palavras) / len(palavras)
    hlr = n_palavras_unicas(palavras) / len(palavras)
    sal = len(palavras) / num_sentencas
    sac = num_frases / num_sentencas
    """