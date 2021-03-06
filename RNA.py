# importação das bibliotecas necessárias

# pybrain
from pybrain.datasets.supervised import SupervisedDataSet 
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer


# gráficos 
import matplotlib.pyplot as plt
import numpy as np

# função para carregar os dados de treinamento
def getData( path ):
    #Open file
    file = open( path, "r" )
    
    data = []    
    
    for linha in file:        # obtem cada linha do arquivo
      linha = linha.rstrip()  # remove caracteres de controle, \n
      digitos = linha.split(" ")  # pega os dígitos
      for numero in digitos:   # para cada número da linha
        data.append( numero )  # add ao vetor de dados  
    
    file.close()
    return data


# configurando a rede neural artificial e o dataSet de treinamento
network = buildNetwork( 45, 500, 500, 1 )    # define network 
dataSet = SupervisedDataSet( 45, 1 )  # define dataSet

'''
arquivos = ['1.txt', '1a.txt', '1b.txt', '1c.txt',
            '1d.txt', '1e.txt', '1f.txt']
'''  
arquivos = ['0.txt', '0a.txt' , '1.txt', '1a.txt', '2.txt', '2a.txt', '3.txt', '3a.txt',
            '4.txt', '4a.txt',  '5.txt', '5a.txt', '6.txt', '6a.txt', '7.txt', '7a.txt',
            '8.txt', '8a.txt',  '9.txt', '9a.txt' ]          
# a resposta do número
resposta = [ [0], [0], [1], [1], [2], [2], [3], [3], [4], [4], [5], [5] ,[6], [6], [7], [7], [8],[8], [9],[9] ] 
#resposta = [[1], [1], [1], [1], [1], [1], [1]] 


i = 0
for arquivo in arquivos:           # para cada arquivo de treinamento
    data =  getData( arquivo )            # pegue os dados do arquivo
    dataSet.addSample( data, resposta[i] )  # add dados no dataSet
    i = i + 1


# trainer
trainer = BackpropTrainer( network, dataSet )
error = 1
iteration = 0
outputs = []
file = open("outputs.txt", "w") # arquivo para guardar os resultados

while error > 0.001: # 10 ^ -3
    error = trainer.train()
    outputs.append( error )
    iteration += 1    
    print ( iteration, error )
    file.write( str(error)+"\n" )

file.close()

# Fase de teste
arquivos = ['1- test.txt', '2-test.txt', '5-test.txt']
for arquivo in arquivos:
    data =  getData( arquivo )
    print ( "Arquivo " , arquivo , " resultado " , network.activate( data ) )


# plot graph
plt.ioff()
plt.plot( outputs )
plt.xlabel('Iterações')
plt.ylabel('Erro Quadrático')
plt.show()

