import base64
import io
import urllib

import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('Agg')


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

    plt.barh(pessoas, pontuacoes)
    plt.autoscale()
    plt.title("Pontuação dos participantes!")
    plt.xlabel("Nome dos participantes")
    plt.ylabel("Pontuação")

    fig = plt.gcf()
    plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri


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
