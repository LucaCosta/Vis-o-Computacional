# Importação das bibliotecas
import cv2 # Biblioteca para manipulação de imagens (OpenCV)

imagem = cv2.imread('ponte.jpg') # Verifica a imagem já existente na pasta: 'ponte.jpg'

for y in range(0, imagem.shape[0]): # Percorre a imagem em y
    for x in range(0, imagem.shape[1]): # Percorre a imagem em x
        imagem[y, x] = (255,0,0) # Define a cor da imagem em toda extensão x e y para azul (255, 0, 0)

cv2.imshow("Imagem modificada", imagem) # Mostra a imagem modificada

cv2.waitKey() #espera pressionar qualquer tecla