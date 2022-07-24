import os

#Author: João
#deleter
#selecione o caminho onde você quer apagar os arquivos
# Lembrando que os arquivos serão deletados do dísco rígido do pc, eles não são movidos para lixeira

caminho = "C:/Users/joao/Documents"
arquivos = os.listdir(caminho)

for arquivo in lista_arquivos:
	nome_completo = f'{caminho}/{arquivo}' 
	tamanho = OS.path.getsize(arquivo) / 100000 #mb
	if tamanho > 10000:
	os.remove(nome_completo)