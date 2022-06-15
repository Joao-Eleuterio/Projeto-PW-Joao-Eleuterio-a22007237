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
    plt.savefig(upload_to='media')
    fig = plt.gcf()
    plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri


def cria_grafico(objetos):
    dados = informacao_utilizadores(objetos)

    dados = dict(sorted(dados.items(), key=lambda item: item[1], reverse=False))

    pessoa = list(dados.keys())
    pontuacao = list(dados.values())
    plt.figure(figsize=(13, 5))
    plt.barh(pessoa, pontuacao)
    plt.title("Pontuação dos participantes!")
    plt.ylabel("Nome dos participantes")
    plt.xlabel("Pontuação")
    plt.autoscale()

    fig = plt.gcf()
    plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')

    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    print(pessoa, flush=True)
    print(pontuacao, flush=True)
    print(string, flush=True)
    print(uri, flush=True)
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
