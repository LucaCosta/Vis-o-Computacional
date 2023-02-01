# Importação das bibliotecas
import cv2 # Biblioteca para manipulação de imagens (OpenCV)

# Leitura da imagem com a função imread()
imagem = cv2.imread('entrada.jpg') # Abre a imagem já existente na pasta: 'entrada.jpg'
print('Largura em pixels: ', end='') # Printa a largura em pixels da imagem
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='') # Printa a altura em pixels da imagem
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='') # Printa a quantidade de canais da imagem
print(imagem.shape[2]) # Neste caso possui 3 canais (pois é colorida)

# Mostra a imagem com a função imshow
cv2.imshow("Hello World", imagem)
cv2.waitKey() #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem) # Salva uma nova imagem alterando com o nome "saida.jpg"
