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
    dados = informacao_utilizadores(objetos)

    dados = dict(sorted(dados.items(), key=lambda item: item[1], reverse=False))

    pessoa = list(dados.keys())
    pontuacao = list(dados.values())

    plt.figure(figsize=(13, 5))

    plt.barh(pessoa, pontuacao)

    plt.title("Pontuação dos participantes!")
    plt.ylabel("Nome dos participantes")
    plt.xlabel("Pontuação")

    plt.savefig('static/portfolio/images/grafico_quizz.png')
    plt.savefig(upload_to='media')


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
