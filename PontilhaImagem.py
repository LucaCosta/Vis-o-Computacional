import cv2 # Importa Biblioteca

imagem = cv2.imread('ponte.jpg') # Abre a imagem

for y in range(0, imagem.shape[0], 10): #percorre linhas de 10 em 10
    for x in range(0, imagem.shape[1], 10): #percorre colunas de 10 em 10
        imagem[y:y+5, x: x+5] = (0,255,255) # Define a cor da imagem para (0, 255, 255) com 5 pixels de largura e altura

cv2.imshow("Imagem modificada", imagem) # Mostra a imagem modificada

cv2.waitKey(0) # Espera o usuário pressionar qualquer tecla