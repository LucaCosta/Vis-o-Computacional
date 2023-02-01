# Importação das bibliotecas
import cv2 # Biblioteca para manipulação de imagens (OpenCV)

imagem = cv2.imread('ponte.jpg') # Verifica a imagem já existente na pasta: 'ponte.jpg'

(b, g, r) = imagem[0, 0] # Verifica a cor da imagem 'ponte.jpg' na posição (0, 0)

print('O pixel (0, 0) tem as seguintes cores:') # Printa a mensagem em parênteses na tela

print('Vermelho:', r, 'Verde:', g, 'Azul:', b) # Printa a cor da imagem 'ponte.jpg' na tela na ordem R, G, B

cv2.imshow("Mostra Cores", imagem) # Mostra a imagem com a função imshow com o nome 'Mostra Cores'
cv2.waitKey() #espera pressionar qualquer tecla