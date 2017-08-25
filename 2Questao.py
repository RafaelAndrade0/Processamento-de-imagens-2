import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def show_image(im):
    image = mpimg.imread(im)
    plt.imshow(image, interpolation='nearest')
    plt.show()

def n_channels(altura, largura, nchannels):
    return nchannels

def size(altura, largura, nchannels):
    return altura, largura

def imreadgray(im):
    image = mpimg.imread(im)
    # Array slicing. A aplicação de uma pseudo cor só é relevante em um único canal,
    # por isso lum_img só recebe um canal. (Tanto faz o qual. R, G ou B)!
    lum_img = image[:,:,0] 
    plt.imshow(lum_img, cmap="gray")
    plt.show()
    

def negative(im, altura, largura):
	for row in range(altura):
		for col in range(largura):
			red = 255 - im[row][col][0]
			green = 255 - im[row][col][1]
			blue = 255 - im[row][col][2]
			im[row][col] = [red, green, blue]
	return im


def main():
    path = '/home/rafael/Documentos/ProceImgs/emiliaclarke.jpg'

    #Exibe a imagem em nd.array
    img = mpimg.imread(path)
    print(img)

    #Converte a imagem en nd.array para uma imagem de fato
    imgplot = plt.imshow(img)
    #plt.show(imgplot)

    #Mostra a imagem original no console
    #Recebe uma imagem como parametro e a exibe. Só isso.
    #show_image(path)

    #Recebe uma imagem como parametro e a retorna em escala de cinza.
    imreadgray(path)

    shape = img.shape

    #Numero de canais da imagem
    print('O número de canais da imagem é de: {0}'
          .format(n_channels(*shape)))

    #Altura e Largura da imagem
    altura_largura = size(*shape)
    print('A altura da imagem é de: {0} e a largura é de: {1}'
          .format(altura_largura[0], altura_largura[1]))

    #Negativa da Imagem
    negative_image = negative(img, altura_largura[0], altura_largura[1])
    imgplot_negative = plt.imshow(negative_image)
    plt.show(imgplot_negative)

if __name__ == '__main__':
    main()