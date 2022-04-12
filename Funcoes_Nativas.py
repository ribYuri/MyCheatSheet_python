"""Algumas funcoes nativas do Python"""

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# FUNCOES MATEMATICAS

# abs(x)             Valor absoluto de x
# ceil(x)            Arredondamento para cima de x
# exp(x)             Exponencial de x: e^x
# floor(x)           Arredondamento para baixo de x
# log(x)             Logaritmo natural de x
# max(x1, x2, ...)   Maior valor dentre os argumentos x
# min(x1, x2, ...)   Menor valor dentre os argumentos x
# pow(x, y)          Potenciacao x^y
# sqrt(x)            Raiz quadrada de x

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# FUNCOES DE ALEATORIEDADE

# choice(V)                            Escolhe aleatoriamente um elemento de V
# randrange([inicio,] fim [,passo])    Elemento aleatorio dentre range(inicio, fim, passo)
# random()                             Ponto-flutuante aleatorio r ∈ [0, 1]
# seed([x])                            Define a semente aleatoria do programa como x
# shuffle(V)                           Randomiza a ordem dos itens em V
# uniform(x, y)                        Ponto-flutuante aleat´orio entre x e y

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# FUNCOES DE STRINGS

# str.count(substr [, beg=0] [, end=len(str)])         Conta quantas vezes substr ocorre em str
# str.find(substr [, beg=0] [, end=len(str)]           Determina se  substr esta presente em str e retorna o indice
#                                                      da ocorrencia ou -1 caso nao seja encontrado.

# len(str)                                             Retorna o comprimento de uma string
# str.replace(old, new [,max])                         Substitui todas as ocorrencias de old por new em str
#                                                      (ou no maximo max) ocorrencias se especificado

# str.split(sep=‘‘ ’’)                                 Divide str em sub-strings de acordo com o separador sep,
#                                                      por padr˜ao “ ”

# str.strip()                                          Remove, se houver, espacos do inıcio e do final da string (rstrip -> right, lstrip -> left)
# (-).join(str)                                        Junta todos os elementos de uma lista com o carctere '-'

# str.upper()                                          Transforma todas as letras da string em maiúsculo
# str.lower()                                          Faz as letras da string serem minusculas
# str.capitalize()                                     Faz a primeira letra da string ser maiúscula
# str.title()                                          Faz a primeira letra de cada palavra ser maiúscula

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# FUNCOES DE LISTAS

# avg(L)               Retorna a media dos elementos de L
# len(L)               Retorna o comprimento de L
# max(L)               Retorna o elemento de maior valor de L
# min(L)               Retorna o elemento de menor valor de L
# L.append(x)          Adiciona x ao final de L
# L.count(x)           Retorna o numero de vezes que x ocorre em L
# L.index(x)           Retorna o indice mais baixo onde x ocorre em L
# L.insert(idx, x)     Insere x no indice idx de L
# L.pop(idx=-1)        Remove o elemento do indice idx de L, por padrao o ultimo elemento
# L.remove(x)          Remove o objeto x de L
# L.reverse()          Inverte a ordem dos elementos de L
# L.sort([func])       Ordena os elementos de L de acordo com a funcao func passada como parametro
