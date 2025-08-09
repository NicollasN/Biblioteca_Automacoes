# Automação de Arquivos

import os # Importando biblioteca

def organizar_arquivos(): # Criando a função 
    pasta = './arquivos'
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    arquivo_pasta_atual = os.listdir(".") # buscando arquivo

    for arquivo in arquivo_pasta_atual:
        if ".pdf" in arquivo:
            os.rename(arquivo, f'{pasta}/{arquivo}') 

    print("Arquivos organizados")

organizar_arquivos()