from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from itertools import product
import math, random
import time
from subprocess import call
from matplotlib import pyplot


#Abre uma imagem
def abrir_imagem(nome_img):
    return Image.open(nome_img)

#Converte a imagem para escala de cinza
def escala_de_cinza(img):
    return img.convert('L')

def gerar_matriz (n_linhas, n_colunas):
    matriz = np.zeros((n_linhas, n_colunas), dtype=np.str)
    return matriz

def imprimir_matriz(matriz):
    print(np.asarray(matriz))

def matriz_da_imagem(img):
    return np.asarray(img.convert('L'))

def nova_imagem(img):
    new_img = Image.new('L', (img.width, img.height), color = 'black')
    new_img.save('nova_imagem.png')
    # new_img.show()
    return new_img


def plotar_grafico(lista_para_plotar = [], titulo = "titulo"):
    pyplot.plot(lista_para_plotar)
    pyplot.title(titulo)
    pyplot.show()


def vetor_de_zeros(qtd):
    lista = []
    for i in range(qtd):
        lista.append(0)
    return lista

def histograma(img = Image):
    pix = img.load()
    histograma = vetor_de_zeros(255)
    # histograma = np.zeros((255,), dtype=int)
    # print(histograma)
    # return 0

    width, height = img.size
    for y, x in product(range(height), range(width)):
        valor_atual = histograma.pop(pix[x,y])
        valor_atual += 1
        print(pix[x,y])
        histograma.insert(pix[x,y], valor_atual)
        # histograma[pix[x,y]] = histograma.
    
    return histograma
        


def imprimir_valores(img):
    pix = img.load()
    width, height = img.size
    for y, x in product(range(height), range(width)):
        if pix[x,y] != 0:
            time.sleep(0.1)
        print("x: {}| y: {} = {}".format(x, y, pix[x,y]))

def mostrar_imagem(nome_img):
    call(["ristretto", nome_img])


def main():
    nome_da_imagem = "lenna.png"
    img = abrir_imagem(nome_da_imagem)
    img = escala_de_cinza(img)
    print(matriz_da_imagem(img))
    # img.save("cinza.tif")
    
    mostrar_imagem("cinza.tif")
    
    hist = histograma(img)

    print(hist)
    # img = binarizar(img)
    # img.save("binzarized_image.tif")
    # print(matriz_da_imagem(img))
    # mostrar_imagem("binzarized_image.tif")

    plotar_grafico(hist, "Histograma da imagem {}".format(nome_da_imagem))


if __name__ == '__main__':
    main()