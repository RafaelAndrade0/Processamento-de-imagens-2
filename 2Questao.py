import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from copy import copy


def show_image(im):
    #image = mpimg.imread(im)
    plt.imshow(im, interpolation='nearest')
    plt.show()


def n_channels(altura, largura, nchannels):
    return nchannels


def size(altura, largura, nchannels):
    return altura, largura


def imreadgray(im):
    image = mpimg.imread(im)
    # Array slicing. A aplicação de uma pseudo cor só é relevante em um único canal,
    # por isso lum_img só recebe um canal. (Tanto faz o qual. R, G ou B)!
    lum_img = image[:, :, 0] 
    plt.imshow(lum_img, cmap="gray")
    plt.show()


def rgb2gray(im, altura, largura):
    for row in range(altura):
        for col in range(largura):
            red = im[row][col][0]
            green = im[row][col][1]
            blue = im[row][col][2]

            weight_average = (0.299*red + 0.587*green + 0.144*blue)/(0.299 + 0.587 + 0.144)
            im[row][col] = [weight_average]
            lum_img = im[:, :, 0]
            #lum_img = im[..., :3]
    return lum_img


def negative(im, altura, largura):
    for row in range(altura):
        for col in range(largura):
            red = 255 - im[row][col][0]
            green = 255 - im[row][col][1]
            blue = 255 - im[row][col][2]
            im[row][col] = [red, green, blue]
    return im


# Organizar Direito a função.
def thresh(im, altura, largura, value):
    #rgb2gray(im, altura, largura)
    numpy_iterator = np.nditer(im, flags=['multi_index'], op_flags=['writeonly'])
    while not numpy_iterator.finished:
        if numpy_iterator[0] > value:
            numpy_iterator[0] = value
        else:
            numpy_iterator[0] = 0
        numpy_iterator.iternext()


# Garante que os valores fiquem "presos" entre 0 e 255
def truncate(value):
    if value < 0:
        value = 0
    elif value > 255:
        value = 255
    return value


def contrast(im, r, m):
    shape = im.shape
    altura_largura = size(*shape)
    for row in range(altura_largura[0]):
        for col in range(altura_largura[1]):
            red = im[row][col][0]
            green = im[row][col][1]
            blue = im[row][col][2]

            # Fator de correção do contraste
            f = (259*(r + 255)) / (255*(259 - r))

            # r modifica o contraste e m modifica o brilho
            new_red = truncate(f*(red - 128) + 128 + m)
            new_green = truncate(f*(green - 128) + 128 + m)
            new_blue = truncate(f*(blue - 128) + 128 + m)

            im[row][col] = [new_red, new_green, new_blue]
    return im


def main():
    path = 'Images/emiliaclarke.jpg'
    #path = 'Images/emilia.png'

    # Exibe a imagem em nd.array
    img = mpimg.imread(path)
    print(img)
    tipo_da_imagem = img.dtype
    print(img.dtype)

    if tipo_da_imagem != 'uint8':
        img = (img * 255).round().astype(np.uint8) 
    #img = (img * 255).round().astype(np.uint8) # Conversão para uint8 (caso de png)
    print(img)
    print(img.dtype)


    # Converte a imagem en nd.array para uma imagem de fato
    imgplot = plt.imshow(img)
    plt.show(imgplot)

    # Mostra a imagem original no console
    # Recebe uma imagem como parametro e a exibe. Só isso.
    # show_image(path)

    # Recebe uma imagem como parametro e a retorna em escala de cinza.
    imreadgray(path)
    #show_image(img)

    shape = img.shape

    # Numero de canais da imagem
    print('O número de canais da imagem é de: {0}'
          .format(n_channels(*shape)))

    # Altura e Largura da imagem
    altura_largura = size(*shape)
    print('A altura da imagem é de: {0} e a largura é de: {1}'
          .format(altura_largura[0], altura_largura[1]))

    # negative() função ==NEGATIVA DA IMAGEM==
    copy_negative = copy(img)
    #negative_image = negative(copy_negative, altura_largura[0], altura_largura[1])
    #plt.imshow(copy_negative)
    #plt.show()


    # Rg2toGray() função ==ESCALA DE CINZA DA IMAGEM==
    #copy_grey = copy(img)
    #grey_image = rgb2gray(copy_grey, altura_largura[0], altura_largura[1])
    #print(grey_image)
    #plt.imshow(grey_image, cmap=plt.cm.gray)
    #plt.show()
    #print(grey_image.dtype)
    

    # thresh() função ==THRESHOLD DA IMAGEM==
    #copy_thresh = copy(img)
    #thresh_image = thresh(copy_thresh, altura_largura[0], altura_largura[1], 50)
    #plt.imshow(copy_thresh, cmap=plt.cm.gray)
    #plt.show()

    # contrast() função == MODIFICANDO O CONSTRASTE ==
    copy_contrast = copy(img)
    contrast_image = contrast(copy_contrast, -50 , 1)
    plt.imshow(contrast_image, vmin=0, vmax=255)
    plt.show()

if __name__ == '__main__':
    main()
