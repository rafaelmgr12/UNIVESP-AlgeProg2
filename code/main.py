
#############################################################################################################
# Esse código foi feito Por Rafael Ribeiro, Facilitador da disciplina Algoritmos e Programação de 
# Computadores II
#
#
# Aqui terá esritas funções que, serão usadas durante os exercícios durante a semana.
#
# Os exercícios são tirados do livro : Introduçao a Computacão com Python  PERKOVIC, Ljubomir
#############################################################################################################

#########################################################################################################################
# Exercício do cap 8 do livro
####################################################################################################################################################

#####################################################################################################################################
# Aqui, vamos implementar as classe criadas no arquivo functions
#####################################################################################################################################
from functions import Point

a = Point()

a.setx(10)
a.sety(15)

print('As Coordenadas no plano é\n:',a.get())
print("\nCoordenada em x é",a.getx())
'''
from functions import Retangulo
print("\nAgora vamos fazer uma definição do Retângulo\n")
a = eval(input('Digite a altura\n'))
l = eval(input("\nDigite a largura"))

r = Retangulo(a,l)


print("\nÁrea do Retangulo é ",r.area(),"\n O perimetro é ",r.perimetro())
from functions import funcionario,gerente

f = funcionario('Rafael',900,'25/05/2019')
g = gerente('João',1000,'01/05/2019')

print("\nFuncionario:\n")
print('Nome:',g.getNome(),'\nSalário:',g.getSal(),'\nData de admissão:',g.getData(),'\nBonus:',g.getBonus())
'''
print("\nIniciando a classe baralho:")
from functions import Baralho

baralho = Baralho(['1', '2', '3', '4'])
baralho.shuffle()
print(baralho.distribuiCarta())
print(len(Baralho()),'\n')
