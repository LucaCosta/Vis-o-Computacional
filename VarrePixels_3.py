# Importação das bibliotecas
import cv2 # Biblioteca para manipulação de imagens (OpenCV)

imagem = cv2.imread('ponte.jpg') # Verifica a imagem já existente na pasta: 'ponte.jpg'

for y in range(0, imagem.shape[0], 1): #percorre as linhas avançando de 1 em 1
    for x in range(0, imagem.shape[1], 1): #percorre as colunas avançando de 1 em 1
        imagem[y, x] = (0,(x*y)%256,0) # Atribui a cor (0,(x*y)%256,0) para cada pixel da imagem onde verde é o resultado do valor de (x*y)%256

cv2.imshow("Imagem modificada", imagem) # Mostra a imagem modificada

cv2.waitKey(0) # Espera o usuário pressionar qualquer tecla