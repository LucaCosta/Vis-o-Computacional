# Importação das bibliotecas
import cv2 # Biblioteca para manipulação de imagens (OpenCV)

imagem = cv2.imread('ponte.jpg') # Abre a imagem já existente na pasta: 'ponte.jpg'

for y in range(0, imagem.shape[0]): # Percorre a imagem em y
    for x in range(0, imagem.shape[1]): # Percorre a imagem em x
        imagem[y, x] = (x%256,y%256,x%256) # Define a cor de cada pixel da imagem em x%256 (para ficar entre 0 e 255)

cv2.imshow("Imagem modificada", imagem) # Mostra a imagem modificada

cv2.waitKey(0) # Espera o usuário pressionar qualquer tecla
