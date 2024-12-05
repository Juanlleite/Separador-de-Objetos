# Segmentação de Objetos com OpenCV: Isolando o que importa!

## O que é isso?

Este repositório contém um script Python que utiliza a poderosa biblioteca OpenCV para segmentar objetos em imagens. Em outras palavras, ele "recorta" os objetos de uma imagem, isolando-os do fundo.

## Por que usar?

* **Pré-processamento de imagens:** Prepara imagens para tarefas mais complexas como reconhecimento de objetos ou análise de vídeo.
* **Segmentação semântica:** Identifica e separa diferentes objetos em uma imagem.
* **Detecção de bordas:** Encontra os contornos dos objetos.

## Como funciona?

1. **Carregamento da imagem:** A imagem é lida e preparada para o processamento.
2. **Detecção de bordas:** Utilizamos o detector de bordas Canny para identificar os contornos dos objetos.
3. **Fechamento morfológico:** "Consertamos" pequenos buracos nos contornos para obter resultados mais precisos.
4. **Encontrar contornos:** Identificamos os contornos externos dos objetos.
5. **Criar caixas delimitadoras:** Criamos caixas ao redor dos objetos para facilitar a localização.
6. **Extrair e salvar:** Isolamos cada objeto e salvamos como uma nova imagem.

## Requisitos

* **Python 3.12+:** A linguagem de programação que usamos.
* **OpenCV:** A biblioteca de visão computacional que faz a mágica acontecer.

## Contato

Para dúvidas ou sugestões, entre em contato em juanleitedev@gmail.com.


