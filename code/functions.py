import numpy as np
import math 

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
# Exercício do cap 4 do livro
####################################################################################################################################################

#4.8

def palavras(nomearq):

    'retorna a lista de palavras reais, sem pontuação'

    arqEntrada = open(nomearq, 'r')

    conteúdo = arqEntrada.read()

    arqEntrada.close()

    tabela = str.maketrans('!,.:;?', 6*' ')

    conteúdo=conteúdo.translate(tabela)

    conteúdo=conteúdo.lower()

    return conteúdo.split()



#4.9
def meuGrep(filename,alvo):
  file = open(filename)
  for linha in file:
    if alvo in linha:
      print(linha, end='')
###################################################################################################################################
# Exercios dada em Sala semana 2
#Exercício
#Considere uma entidade Funcionário, que possui nome, data de admissão e salário. Implemente sua classe, 
# definindo também alguns métodos para manipulação dos atributos.
# Em seguida, considere a entidade Gerente, que também é um funcionário. Além dos atributos de funcionário, um gerente também contém
# um bônus, que é uma porcentagem adicional aplicada no seu salário.
#Implemente a classe Gerente como uma extensão de Funcionário.
##################################################################################################################################
class funcionario:
    def __init__(self,nome,sal,data):
        'classe inicialzar o objeto'
        self.nome = nome
        self.sal = sal
        self.data = data
    def getSal(self):
        'salario'
        return self.sal
    def getNome(self):
        'get nome'
        return self.nome
    def getData(self):
        'Data'
        return self.data
    
class gerente(funcionario):
    def getBonus(self):
        'Add bonus'
        return 0.1*(self.sal)


#########################################################################################################################
# Exercício do cap 8 do livro
####################################################################################################################################################


class Point:
    'classe que representa pontos no plano'
    def setx(self, coordx):
        'define coordenada x do ponto como coordx'
        self.x = coordx
  
    def sety(self, coordy):
        'define coordenada y do ponto como coordy'
        self.y = coordy
    def get(self):
        'retorna tupla com coordenadas x e y do ponto'
        return (self.x, self.y)
  
    def move(self, dx, dy):
        'muda as coordenadas x e y por dx e dy'
        self.x += dx
        self.y += dy
    def getx(self): # 8.1
        'retorna coordenada x'
        return self.x

    

#8.3

class Retangulo:
    'classe que representa retângulos'
    def __init__(self,coordx,coordy):
        'construtor'
        self.x = coordx
        self.y = coordy
    def perimetro(self):
        'retorna o perimêtro do retângulo'
        return 2*(self.x+self.y)
    def area(self):
        'retorna area do retangulo'
        return self.x*self.y

#8.4
	
class Animal:
    'representa um animal'
    def setEspécie(self, espécie):
        'define a espécie do animal'
        self.esp = espécie
    def setLinguagem(self, linguagem):
        'define a linguagem do animal'
        self.ling = linguagem
    def fala(self):
        ' exibe uma sentença pelo animal'
        print('IEu sou um {} e sei {}'.format(self.esp, self.ling))
    def __init__(self, espécie='animal', linguagem='emite sons '):
        'construtor '
        self.esp = espécie
        self.ling = linguagem
#8.5 (dúvida)

#8.6

class Carta:

    # outros métodos de Carta
    def __repr__(self):
        'retorna representação formal'
        return "Carta('{}', '{}')".format(self.valor, self.naipe)
    def __eq__(self, outro):
        'self = outro se valor e naipe forem os mesmos'
        return self.valor == outro.valor and self.naipe == outro.naipe


# 8.8
class Vetor(Point):
    'uma classe de vetor 2D'
  
    def __mul__(self, v):
        'produto de vetores'
        return self.x * v.x + self.y * v.y
    
    def __add__(self, v):
        'adição de vetores'
        return Vector(self.x+v.x, self.y+v.y)
    
    def __repr__(self):
        'retorna representação de string canônica'
        return 'Vetor{}'.format(self.get())


# 8.9
class Queue:
    'uma classe de fila clássica'
     # métodos __init__(), enqueue(), isEmpty(), __repr__(),
     # __len__(), __eq__() implementados aqui
    def dequeue(self):

        '''remove e retorna item na frente da fila

           levanta exceção KeyboardInterrupt se fila vazia '''

        if len(self) == 0:

            raise KeyboardInterrupt('remove da fila vazia ')

        return self.q.pop(0)
