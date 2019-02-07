from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from itertools import product
import math, random
import time
from subprocess import call

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

def binarizar(img):
    pix = img.load()

    width, height = img.size

    for y, x in product(range(height), range(width)):
        if pix[x,y] >= 127:
            pix[x,y] = 255
        else:
            pix[x,y] = 0

    return img

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
    img = abrir_imagem("image.tif")
    img = escala_de_cinza(img)
    # img.save("cinza.tif")
    
    # mostrar_imagem("cinza.tif")
    
    
    img = binarizar(img)
    img.save("binzarized_image.tif")
    # print(matriz_da_imagem(img))
    mostrar_imagem("binzarized_image.tif")

if __name__ == '__main__':
    main()