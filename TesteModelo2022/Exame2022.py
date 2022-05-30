def f (l1, l2):
    resultado = 0
    for x in l1:
        if x % 2 == 0:
            resultado = resultado + (1 if sum(l2)==0 else 2)
    return resultado

""" Grupo 1 [Complexidade algorítmica, 2 valores] """
#VER ISTO SE NÃO SABES NADA SOBRE O(n) 
#https://www.youtube.com/watch?v=D6xkbGLQesk
#https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/

#Considere que as duas listas l1 e l2 têm comprimentos na mesma ordem de grandeza. 
#Pretendemos analisar a complexidade de f em função de uma variável n

#a) Qual o significado do valor n que faz sentido para este caso?

print("O valor n que faz sentido para este caso é o comprimento da lista l1")
#... a l1 é a mais importante pk é a que está 

#b) Qual o número de operações básicas que a função f efetua, em função de n? Justifique.
#N sei se é isto que o stor tá a pedir.
print("MxN sendo N o comprimento da lista l1 e M o comprimento da lista l2")
print("A resposta é igual ao comprimento da lista l1 (pk a l1 está a ser iterado no for) vezes o cumprimento da l2 (pois esta também está a ser iterada dentro do sum())")

#c) Qual a complexidade algorítmica da função quando expressa na notação O? Justifique.

print("É igual a O(n^2), pois a complexidade é O(n) do for que percorre a l1 vezes o O(n) do sum() que percorre a l2")
print("O(n)*O(n)=O(n^2)")

""" Grupo 2 [Algoritmos de pesquisa & ordenação, 3 valores] (Vai sair o merge probs)"""

produtos = [('Grão', 78, 2.94), ('Seitan', 7, 3.14),
('Couve-roxa', 78, 1.79)]

#a) Utilize a função sorted para obter, a partir da lista original, uma outra lista em que os elementos se encontram por ordem crescente das quantidades disponíveis.

#Sorted: https://www.programiz.com/python-programming/methods/built-in/sorted
# https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python

print(sorted(produtos,key=lambda item:item[1]))

#b) Mesma questão, mas desta vez, em caso de empate, as entradas devem aparecer por ordem alfabética dos nomes. Para a lista acima, o triplo contendo a Couve-roxa deverá aparecer antes daquele que contém Grão.

                            #Sort pelo item[1] e desempata pelo item[2] (Isto é tudo automático)
print(sorted(produtos,key=lambda item:[item[1],item[0]] ))

#c) Considere o algoritmo de ordenação por seleção descrito do seguinte modo:
"""
-O algoritmo corre em tantas iterações quantos os elementos na
lista. 
-Na iteração i calcula-se o índice do menor valor da sublista
que começa em i. 
-O valor no índice assim obtido é trocado com o valor no índice i.

Considere dada uma função indice_minimo(lista) que dada uma lista não vazia devolve o índice do menor valor na lista. (Ele tá a mandar usar esta função)
Escreva uma função ordenacao_selecao que recebe uma lista e ordena-a pelo método de seleção. 
Note que a própria lista deve ser alterada, pelo que a função ordenacao_selecao não devolve nada.

"""
def  indice_minimo(lista): #Podes só assumir que já tens isto no teste n é preciso escreve-la
    return lista.index(min(lista))

def ordenacao_selecao(lista):
    '''
    Ordena a lista dada como parametro com o algoritmo descrito no enunciado

            Parameters:
                    lista (list): A lista para ser ordenada

            Returns:
                    None
    '''
    #O algoritmo corre em tantas iterações quantos os elementos nalista.

    for i in range(len(lista)):
        #Na iteração i calcula-se o índice do menor valor da sublista que começa em i.
        indice_menor = indice_minimo(lista[i:])
        #O valor no índice assim obtido é trocado com o valor no índice i.
        lista[i], lista[indice_menor + i] = lista[indice_menor + i], lista[i]






lista=[4,9,2,1,5,62,1]
ordenacao_selecao(lista)
print(lista)  
print(lista)  
print(lista)  
print(lista)  


""" Grupo 3 [Testes, 3 valores] """
#Considere uma função ordena que ordena uma lista. A lista é alterada pela função, a função não devolve nada. A função de ordenação poderia ser a função do grupo anterior.

#a) Proponha pelo menos 3 características para analisar o comportamento da função.
#(...)

""" Grupo 4 . [Ordem superior (Funções que recebem funções), 2 valores] """
#Considere uma função de inteiros para inteiros e um intervalo de números inteiros {n, n + 1, . . . , m} dado por um par (n, m).

# a) Escreva a função max_em_intervalo(funcao, intervalo) utilizando uma linha de código Python (para além da linha do def).
def max_em_intervalo(funcao, intervalo):
    return max(funcao(x) for x in range(intervalo[0], intervalo[1]+1))

print(max_em_intervalo(lambda x: x**2, (1, 20)))
# b) Este exercício é semelhante ao anterior, mas desta vez pretendemos não o valor da função mas o ponto do domínio onde a função toma o valor máximo.
# Para resolver este exercício deve utilizar uma função de ordem superior e não deve utilizar nem iteração (ciclos) nem recursão.

def indice_max_em_intervalo(funcao, intervalo):
    return list(map(funcao, range(intervalo[0], intervalo[1]+1))).index(max(map(funcao, range(intervalo[0], intervalo[1]+1))))+1

print(indice_max_em_intervalo(lambda x: x**2, (1,20)))

"""Isto de forma não retardada ficava tipo assim:"""
def indice_max_em_intervalo(funcao, intervalo):
    listaMapeada=list(map(funcao, range(intervalo[0], intervalo[1]+1)))
    return listaMapeada.index(max(listaMapeada))+1

print(indice_max_em_intervalo(lambda x: x**2, (1,20)))

""" Grupo 5 [Visualização com matplotlib, 2 valores] """ 
#Usando módulo matplotlib escreva uma função grafico que gere o seguinte gráfico.
from matplotlib import pyplot as plotter

cordsX=[1,2,3,4,5,6]
cordsY=[2,3,10,4,3,6]
plotter.plot(cordsX,cordsY)

plotter.title("O meu gráfico preferido")
plotter.xlabel("Abcissas")
plotter.ylabel("Ordenadas")

#plotter.show()

""" Grupo 6. [Valores separados por vírgulas, 2 valores] 
Ver isto:
https://www.programiz.com/python-programming/reading-csv-files"""

#Considere um ficheiro lista com as existências num supermercado em formato de valores separados por vírgulas. O ficheiro tem uma linha cabeçalho.
"""
Produto, Stock, Preço
Grão, 78, 2.94
Seitan, 7, 3.1
Couve-roxa, 78, 1.79
"""

#Escreva uma função que dado um ficheiro de valores separados por vírgulas, devolva a linha (em forma de triplo) com o produto com menor stock
#Aqui não sei se a função recebe o caminho para o ficheiro ou o objeto mm
import csv 

def menor_stock(ficheiro):
    with open(ficheiro,"r") as ficheiro:
        reader = csv.reader(ficheiro,delimiter=',')
        lista = [x for cnt,x in enumerate(reader) if cnt!=0]
        lista.sort(key=lambda tupla:tupla[1])

menor_stock("TesteModelo2022\\lista.csv")

""" Grupo 7. [Programação de sistema, 2 valores] """
#Para testar isto é pela consola
import sys, os #sys é para receber argumentos pela consola


print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
#sys.argv[0] é sempre o caminho até este programa, pelo menos para o meu caso no WINDOWS 10

#root = "C:\\Users\\myUsername\\Downloads" #Caminho do ficheiro para testar no windows pk o windows n tem src
#root = sys.argv[1] #Como o enunciado está a pder
root="Stop crashing pls" 
# o subdirectories tem que estar aqui porque o os.walk(root) vai buscar as 3 coisas e é preciso desempacota-las todas.
for path, subdirectories, files in os.walk(root):
    for name in files:
        if(name.endswith("*"+sys.argv[2])):
            #print(os.path.join(path, name))
            print("Stop crashing pls")


""" Grupo 8. [Expressões regulares, 2 valores]"""
#Não acredito que tive que aprender esta merda
"""
https://regexone.com/ Basta abrir este site para aprender tudo em <30 minutos (vai ser uma cena simples não vai ser tipo um email)
Basta chegar á Lesson 6 para resolver o a) e á 10 para saber o b
https://regex101.com/ e este para brincar e testar com feedback

"""

#"para efeitos deste exercício vamos imaginar que cada um dos números contém entre um e três algarismos."
# a) Defina uma expressão regular que reconheça endereços IPv4 válidos. (xxx.xxx.xxx.xxx ou x.x.x.x ou xx.xx.xx.xx ou x.xx.xxx.xxx etc)
# Portanto 4 números de 1 a 3 digitos separados por 1 ponto.

    # r" " é de raw , para não interpretar o \ como um caracter especial
regex = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"

# b) Os encaminhadores domésticos utilizam automaticamente endereços começados por 192. 
# Escreva uma função domestico que, dada uma frase (uma string) devolva True se...
# ..a) a frase contém pelo menos uma ocorrência de um endereço IPv4 e 
# .b) o endereço começa por 192.
import re as regex

def domestico(frase):
    pattern= r"^192\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    if(regex.match(pattern,frase)): #Devolve a primeira match ou assim
        return True
    else: return False

print("Grupo 8:"+str(domestico("192.1.1.1")))


