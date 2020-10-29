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
        print('Eu sou um {} e sei {}'.format(self.esp, self.ling))
    def __init__(self, espécie='animal', linguagem='emite sons '):
        'construtor '
        self.esp = espécie
        self.ling = linguagem
#8.5
from random import shuffle
class Baralho:
  'representa um baralho de 52 cartas'
  # valores e naipes são variáveis da classe Baralho
  valores = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
  #naipes são 4 símbolos Unicode representando os 4 naipes
  naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
  def __init__(self,lista = None):
    if lista != None:   # entra baralho fornecido
      self.baralho = lista
    else:# nenhum baralho incluído
      'inicializa baralho de 52 cartas'
      self.baralho = []       # baralho está inicialmente vazio 
      for naipe in Baralho.naipes: # naipes e valores são Baralho
        for valor in Baralho.valores: # variáveis da classe
        # inclui Carta com certo valor e naipe no baralho
          self.baralho.append(Carta(valor, naipe))
  def distribuiCarta(self):
    'distribui (remove e retorna) carta do topo do baralho'
    return self.baralho.pop()
  def shuffle(self):
    'mistura o baralho'
    shuffle(self.baralho)   
    # outros métodos de Baralho
  def __len__(self):
    'retorna tamanho do baralho'
    return len(self.baralho)
  def __repr__(self):
    'retorna representação de string canônica'
    return 'Baralho ({})'.format(self.baralho)
  def __eq__(self, outro):
    '''retorna True se baralho tiver as
         mesmas cartas na mesma ordem '''
    return self.baralho == outro.baralho




class Carta:
  'representa uma carta do jogo'
  def __init__(self, valor, suit):
    'inicializa valor e naipe da carta do jogo'
    self.valor = valor
    self.suit = suit
  
  def getRank(self):
    'retorna valor'
    return self.valor

  def getSuit(self):
    'retorna naipe'
    return self.suit
    # outros métodos de Carta
  def __repr__(self):
    'retorna representação formal'
    return "Carta('{}', '{}')".format(self.valor, self.suit)
  def __eq__(self, outro):
      'self = outro se valor e naipe forem os mesmos'
      return self.valor == outro.valor and self.suit == outro.suit


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

#####################################################################################################################################################################################################
# Exercício do cap 10 do livro
#####################################################################################################################################################################################################
from turtle import Screen,Turtle

#10.1

def reverse(n):
  'Exibe os dígitos de n verticalmente, começando com dígito de baixa ordem'
  if n < 10:          # caso básico: número de um dígito
    print(n)
  else:               # n tem pelo menos 2 dígitos
    print(n%10)     # exibe último dígito de n
    reverse(n//10)  # exibe recursivamente, em reverso,
                      # tudo menos o último dígito
#10.2
def cheers(n):
  if n == 0 :
    print("Hurrah!!!")
  else: # n > 0
    print("Hip",end = " ")
    cheers(n-1)

#10.3
# def fat(n):
  if n in [0, 1]: # caso básico
    return 1
  return fat(n-1)*n
fat(4) 



# 10.4
#  O codigo pattern
def pattern(n):
  'exibe o enésimo padrão'
  if n == 0:           # caso básico
    print(0, end=' ')
  else:                # etapa recursiva: n > 0
    pattern(n-1)         # exibe padrão n-1
    print(n, end=' ')    # exibe n
    pattern(n-1)         # exibe padrão n-1

# pattern2()
def pattern2(n):

    'exibe o enésimo padrão'

    if n > 0:

        pattern2(n-1)  # exibe pattern2(n-1

        print(n * '*')   # exibe n estrelas

        pattern2(n-1)  # exibe pattern2(n-1

# 10.5
# 
def koch(n):
  'retorna direções turtle para desenhar a curva Koch(n)'
  if n == 0:       # caso básico
    return 'F'
  tmp = koch(n-1)  # etapa recursiva: obtém direções para Koch(n – 1)
                    # usa isso para construir direções para Koch(n)
  return tmp + 'L' + tmp + 'R' + tmp + 'L' + tmp
def drawKoch(n):
  'desenha enésima curva de Koch usando instruções da função koch()'
  s = Screen()            # cria tela
  t = Turtle()            # cria turtle
  directions = koch(n)    # obtém direções para desenhar Koch(n)
  for move in directions: # segue os movimentos especificados
    if move == 'F':
      t.forward(300/3**n) # move para frente, tamanho normalizado
    if move == 'L':
      t.lt(60)            # gira 60 graus para a esquerda
    if move == 'R':
      t.rt(120)           # gira 120 graus para a direita
  s.bye()
def drawSnowflake(n):
  'desenha enésima curva de floco de neve com função koch() 3 vezes'
  s = Screen()
  t = Turtle()
  directions = koch(n)
  for i in range(3):
    for move in directions: # desenha koch(n)
      if move == 'F':
        t.fd(300/3**n)
      if move == 'L':
        t.lt(60)
      if move == 'R':
        t.rt(120)
    t.rt(120)               # gira 120 graus para a direita

  s.bye()

#10.6
# função powr definada no livro
def power(a, n):
  'retorna a à potência n '
  res = 1
  for i in range(n):
    res *= a
  return res


def rpower(a,n):
  'retorna a à potência n '
  counter = 0   # conta número de multiplicações
  if n==0:
    return 1
   # if n > 0:
  tmp = rpower(a, n//2)
  if n % 2 == 0:
    counter += 1
    return tmp*tmp      # 1 multiplicação
  else: # n % 2 == 1
    counter += 2
    return a*tmp*tmp    # 2 multiplicações

def buildInput(n):
  return n


def timing(func,n):
  'roda func sobre entrada retorna por buildInput'
  funcInput = buildInput(n) #obtém entrada para func 

  start = time.time() # Hora inicial
  func(funcInput)     # roda func sobre funcInput
  end = time.time()   # hora fina

  return end-start


def timingAnalysis(func,start,stop,inc,runs):
  '''exitbe tempos de execução médios da função func sobre entradas de tamanho
      star,start+inc ....até o stop '''
  for n in range(start,stop,inc): # para cada tamanho de entrada n
    acc = 0.0 #inicializa o acumalador

    for i in range(runs):
      acc += timing(func,n) #implementa func sobre a entrad de tamanho n
                            #acumula tempos de execucão
      #exibe tempos de execuçao médios para tamnap de entrada n
      formatStr = 'Tempo de execução de {}({}) é {:.7f} segundos.'
      print(formatStr.format(func.__name__, n, acc/runs))



def power2(n):
 
    return power(2,n)
 
def rpower2(n):
 
    return rpower(2,n)
 
def pow2(n):
 
    return 2**n


#10.7

import random
 
 def buildInput1(n):
 
    'retorna uma lista de n inteiros aleatórios no intervalo [0, n**2]'
 
    res = []
 
    for i in range(n):
 
        res.append(random.choice(range(n**2)))
 
    return res

def dup1(lst):
  'retorna True se lista lst tiver duplicatas; caso contrário, False'
  for item in lst:
    if lst.count(item) > 1:
      return True
  
  return False
def dup2(lst):
  'retorna True se lista lst tiver duplicatas; caso contrário, False'
  lst.sort()
  for index in range(1, len(lst)):
    if lst[index] == lst[index-1]:
      return True
  return False

def dup3(lst):
  'retorna True se lista lst tiver duplicatas, caso contrário, False'
  s = set()
  for item in lst:
    if item in s:
      return False
    else:
      s.add(item)
  return True

def dup4(lst):
  'retorna True se lista lst tiver duplicatas, caso contrário, False'
  return len(lst) != len(set(lst))
#############################################################################
# Modificações feitas na funções de analíse tempos para o probelma 10.7
#############################################################################
  def timing(func,n):
  'roda func sobre entrada retorna por buildInput'
  funcInput = buildInput1(n) #obtém entrada para func 

  start = time.time() # Hora inicial
  func(funcInput)     # roda func sobre funcInput
  end = time.time()   # hora fina

  return end-start


def timingAnalysis1(func,start,stop,inc,runs):
  '''exitbe tempos de execução médios da função func sobre entradas de tamanho
      star,start+inc ....até o stop '''
  for n in range(start,stop,inc): # para cada tamanho de entrada n
    acc = 0.0 #inicializa o acumalador

    for i in range(runs):
      acc += timing(func,n) #implementa func sobre a entrad de tamanho n
                            #acumula tempos de execucão
      #exibe tempos de execuçao médios para tamnap de entrada n
      formatStr = 'Tempo de execução de {}({}) é {:.7f} segundos.'
      print(formatStr.format(func.__name__, n, acc/runs))



#10.8
#############################################################################
# É possivél usar as funções definidas no problema 10.7, para analisar o 
# tempo
#############################################################################
def frequent(lst):
  '''retorna item que ocorre com mais frequência
     na lista lst não vazia'''
  lst.sort()                   # primeiro classifica lista
  currentLen = 1               # tamanho da sequência atual
  longestLen = 1               # tamanho da sequência mais longa
  mostFreq   = lst[0]          # item com sequência mais longa
  for i in range(1, len(lst)):
   # compara item atual com anterior
    if lst[i] == lst[i-1]:  # se igual
                            # sequência atual continua
      currentLen+=1
    else: # se não igual
          # atualiza sequência mais longa, se necessário
      if currentLen > longestLen:    # se sequência que terminou
        longestLen = currentLen    # armazena seu tamanho
        mostFreq = lst[i-1]        # e o item
                                   # inicia nova sequência
      currentLen = 1

  return mostFreq
def frequent2(lst):
  'retorna frequência dos itens em listaItens'
  contadores = {}          # inicializa dicionário de contadores
  for item in lst:
    if item in contadores:   # contador para o item já existe
     contadores[item] += 1    # portanto, incrementa
    else:                    # contador para item é criado
     contadores[item] = 1     # e inicializado em 1
  return contadores

#############################################################################
# Semana 4 - Pilhas,Filas,listas e Árvores
#############################################################################
#############################################################################
# Definindo classes e resolvendo exercios do livros
#############################################################################

# Pilha
class Pilha():
  def __init__(self):
    self.data = []
  
  def push(self,x):
    self.data.append(x)
  
  def pop(self):
    if len(self.data) > 0:
      return self.data.pop(-1)
  
  def top(self):
    if len(self.data)>0:
      return self.data[-1]

  def empty(self):
    return not len(self.data) > 0

class Fila():
  def __init__(self):
    self.data = []
  
  def inserir(self,x):
    self.data.append(x)
  
  def remover(self):
    if len(self.data) > 0:
      return self.data.pop(0)
    else:
      return None
  def top(self):
    if len(self.data) > 0:
      return self.data[0]
  
  def empty(self):
    return not len(self.data) > 0

