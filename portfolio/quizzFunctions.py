import matplotlib.pyplot as plt


def informacao_utilizadores(objetos):
    dados = {}
    for quizz in objetos:
        dados[quizz.nome] = QuizzPontuacao(quizz)

    return dados


def desenha_grafico_resultados(objetos):
    # creating the dataset
    dados = informacao_utilizadores(objetos)
    dados = dict(sorted(dados.items(), key=lambda item: item[1], reverse=False))

    pessoas = list(dados.keys())
    pontuacoes = list(dados.values())

    plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.plot(pessoas, pontuacoes)

    plt.title("Pontuação dos participantes!")
    plt.xlabel("Nome dos participantes")
    plt.ylabel("Pontuação")
    plt.savefig(upload_to='media')
    plt.close()


def QuizzPontuacao(input):
    pontuacao = 0

    if input.pergunta1 == 'linguagem de marcação':
        pontuacao += 5

    if input.pergunta2 == 'framework':
        pontuacao += 5

    if input.pergunta3 == 2005:
        pontuacao += 3

    if input.pergunta4 == 1991:
        pontuacao += 3

    if input.pergunta5 == 'cascading style sheet':
        pontuacao += 4

    return pontuacao
