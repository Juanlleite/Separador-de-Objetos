import cv2  # Importa a biblioteca OpenCV para processamento de imagens

# Lê a imagem 'objetos.jpg' e redimensiona para 600x500 pixels
img = cv2.imread('objetos.jpg')
img = cv2.resize(img, (600, 500))

# Converte a imagem para tons de cinza
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Detecta as bordas da imagem usando o algoritmo Canny
# Os valores 30 e 200 são os limiares inferior e superior para a detecção
imgCanny = cv2.Canny(imgCinza, 30, 200)

# Aplica o fechamento morfológico para fechar pequenos buracos nos contornos
imgClose = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE, (7, 7))

# Encontra os contornos externos dos objetos na imagem
contours, hierarchy = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Itera sobre cada contorno encontrado
for cnt in contours:
    # Encontra a caixa delimitadora do contorno
    x, y, w, h = cv2.boundingRect(cnt)

    # Extrai a região de interesse (ROI) da imagem original
    objeto = img[y:y+h, x:x+w]

    # Salva a ROI como uma nova imagem
    cv2.imwrite(f'objetos/objeto{num0b}.jpg', objeto)

    # Desenha um retângulo ao redor do objeto na imagem original
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Incrementa o contador para nomear o próximo objeto
    num0b += 1

# Exibe as imagens
cv2.imshow('Imagem', img)
cv2.imshow('Imagem Cinza', imgCinza)
cv2.imshow('Imagem Canny', imgCanny)

# Aguarda uma tecla ser pressionada antes de fechar as janelas
cv2.waitKey(0)