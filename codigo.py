# Author: João
# deleter
# selecione o caminho onde você quer apagar os arquivos
# Lembrando que os arquivos acima de 10mb serão deletados do dísco rígido do pc, eles não são movidos para lixeira

import os

caminho = "caminho_para_pasta"
lista_arquivos = os.listdir(caminho)

for arquivo in lista_arquivos:
	nome_completo = f"{caminho}/{arquivo}"
	tamanho = os.path.getsize(arquivo) / 1000000 #mb
	if tamanho > 10:
    	os.remove(nome_completo)
