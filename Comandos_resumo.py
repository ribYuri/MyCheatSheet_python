""" Resuminho comandos e sitaxes de Python """

# Não precisa declarar tipo e {} são substituidas por identação
# Selecione um bloco e click ctrl + barra

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ATRIBUICOES MULTIPLAS

# (idade, altura, nome) = (28, 1.8, "Jorge")
# print(idade, altura, nome)
# 'sem parenteses tbm funciona'

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# SUPORTE PRINT COM STRINGS E FUNCIONA EM LISTAS

# nome = "Marcelo"
# print(nome)
# print(nome[0])
# print(nome[2:4])
# print(nome[2:])
# print(nome[-1])
# print(nome * 2)
# print(nome + "Silva")
# # combinacoes sao aceitas

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# DEFINICAO DE MATRIZES (LISTAS)

# matriz = [[1, 2, 3], [4, 5, 6]]
#
# outra_matriz = [[0 for i in range(3)] for j in range(2)]
# print(outra_matriz)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# TUPLAS SAO PARECIDAS COM LISTAS POREM TEM TAMANHO FIXO E NAO PODEM SER ALTERADAS

# nome_tupla = ("Ana", 22, 1.67)
# # formas de print de strigs tambem funciona aqui

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# DICIONARIO E TIPO TABELA-HASH, PAR CHAVE-VALOR

# dic = {}
# dic["um"] = "Joao"
# dic[2] = "Aline"
# dic_2 = {"nome": "Theo", "sexo": "M", "idade": 30}
# print(dic)
# print(dic["um"])
# print(dic[2])
# print(dic_2.keys())
# print(dic_2.values())

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# CONVERSAO DE TIPOS

# int(x) Converte x para um numero inteiro.
# float(x) Converte x para um numero de ponto-flutuante.
# str(x) Converte x para uma string.
# repr(x) Converte o objeto x para uma string.
# tuple(s) Converte s em uma tupla.
# list(s) Converte s em uma lista.
# set(s) Converte s em um conjunto

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# IMPRESSAO NA TELA E ENTRADA DE DADOS

# nome, idade, peso = input("Digite seu nome: "), int(input("Insira sua idade: ")), float(input("Peso: "))
# print("Nome:", nome, "|| Idade:", idade)
#
# print("Nome: %s || Idade: %d || Peso: %.2f" % (nome, idade, peso))
# print("Nome: {} || Idade: {} || Peso: {:.2f}".format(nome, idade, peso))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# TIPOS DE OPERADORES (ARITIMETICOS, LOGICOS E PERTINENCIA)

# a % b      ->  resto da divisao
# a ** b     ->  exponenciacao
# a // b     ->  divisao inteira

# operadores AND, OR e NOT
# a = 2
# if not (a < 5):
#     print("if")
# else:
#     print("else")

# in     ->  elemento pertence ao conjunto
# not in ->  elemento nao pertence ao conjunto
# conjunto = [4, 5, 6]
# if 6 in conjunto:
#     print("if")
# else:
#     print("else")

# IF, ELIF e ELSE

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# LACOS DE REPETICAO
# break
# continue  ->  ignora o resto do codigo, proxima interacao do laco

# # for
# frutas = ["Maca", "Pera", "Laranja"]
# # for fruta in frutas:
# #     print(fruta)
#
# # for i in range(0, len(frutas), 1):  # range -> 1º(opcional) comeca, 2º total, 3º(opc) pular
# #     print(frutas[i])
#
# # i = 0
# # while i < len(frutas):
# #     print(frutas[i])
# #     i += 1

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# FUNCOES
# ->todos os parametros sao passados por referencia<-

# def funcao(a, b):                             # pode ser definido valor padrao ex: (a, b = 0)
#     """Aqui pode ser definido oque funcao faz - documentation"""
#     soma = a + b
#     if soma == total:                         # ex var global
#         print("variavel global")
#     return soma
#
#
# total = 7                                     # ex var global
# resultado = funcao(2, 5)
# print(resultado)

# # passagem argumentos -> funcao(2, 5) || funcao(b=4, a=2) || funcao(a = 2) -> padrao definido pra b
# # ->variaveis dentro da funcao sao locais. Fora sao globais<-

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# MODULOS E IMPORT
# um arquivo .py e um modulo

# import math                  # importando modulo Python math (nativo)
#
# print(math.sqrt(9))
# print(math.factorial(3))
#
# # pode nomear o modulo ex: import math as matematico
# # matematico.sqrt()
# # from math import sqrt, factorial  -> possivel mas nao recomendado

# -> Podemos importar pacotes proprios
#  -> No mesmo diretorio
#        import caculadora
#        calculadora.soma()
#  -> Diretorio diferente
#        import pasta/caculadora

# documentacao modulos nativos Python: https://docs.python.org/3/library/

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ORIENTACAO A OBJETOS


# class Pessoa:
#     """Classe comum a pessoas"""                                          # String de documentacao
#     cont_pessoas = 0                                                      # Variavel da classe
#
#     def __init__(self, prim_nome: str, ult_nome: str, idade: int):        # Construtor
#         self.primeiro_nome = prim_nome
#         self.ultimo_nome = ult_nome
#         self.idade = idade
#         Pessoa.cont_pessoas += 1
#
#     def maior_de_idade(self):
#         if self.idade >= 18:
#             return True
#         else:
#             return False
#
#     def nome(self):
#         return self.primeiro_nome
#
#
# pessoa1 = Pessoa("Cesar", "Marcos", 20)
# print(pessoa1.maior_de_idade())

# -> HERANCA <-
# class Aluno (Pessoa):
#     """Classe Aluno que herda de pessoa"""
#
#     def __init__(self, pnome, unome, idade, nota: float, freq: float):
#         super().__init__(pnome, unome, idade)
#         self.nota = nota
#         self.freq = freq
#
#     def aprovado(self):
#         if self.nota >= 6.0 and self.freq >= 75.0:
#             return True
#         else:
#             return False


# POLIMORFISMO
# class AlunoPos (Aluno):
#     """Classe Aluno de Pos graduacao que herda de Aluno"""
#
#     def __init__(self, pnome, unome, idade, nota: float, freq: float):
#         super().__init__(pnome, unome, idade, nota, freq)
#
#     def aprovado(self):
#         if self.nota >= 7.0 and self.freq >= 75.0:
#             return True
#         else:
#             return False

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#  TRATAMENTO DE EXCECOES

# Exception           Classe base para todas excecoes.
# AritimeticError     Classe base para todas os erros de calculos numericos.
# ImportError         Declaracao import falhou.
# IndexError          Indice nao foi encontrado em uma sequencia.
# IOError             Erro ao ler ou escreve em arquivo.
# SyntaxError         Erro de sintaxe Python.
# TypeError           Operador ou funcao e feita com tipos incompatıveis.

# a = 5
# try:
#     a = a/0
# except ArithmeticError:
#     print("Erro o calculo nao foi possivel")
# else:
#     print("Operacao realizada com sucesso")
