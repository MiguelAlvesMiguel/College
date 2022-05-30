
"""
Escreva uma função maior_zero que transforme um iterável de
iteráveis de inteiros num iterável de iteráveis de valores lógicos. Cada
entrada no iterável resultante indica se o valor na respetiva posição do
iterável original é ou não maior do que zero. Lembre-se que um iterável
é qualquer objeto que possa ser convertido num iterador. Por exemplo:

>>> [list(it) for it in maior_zero([[-1, -2, 3], [2,
-1, 3, 7]])]
[[False, False, True], [True, False, True, True]]

"""
#Receive iterable of iterables of integers and return iterable of iterables of booleans
def maior_zero(iterableOfIterables):
    return ([i > 0 for i in it] for it in iterableOfIterables)

#def maior_zero(iterableOfIterables):
 #   return [map(lambda x: x>0,)]

#print(list(maior_zero([[-1, -2, 3], [2, -1, 3, 7]])))

#def zip_with(f, lista1, lista2):
    #return (f(x,y) for x,y in zip(lista1,lista2))

#print(list(zip_with(max, [5, 2, 0, 9], [2, 3, 4])))


def zip_with(f, lista1, lista2):
      return (map(f,zip(lista1,lista2)))

#print(list(zip_with(lambda x, y: (x, y),['a', 'b','c'], [2, 3, 4])))    

def converter(iteravel, iteravel_de_funcoes):
    """
    iterável cujos elementos são obtidos por
    aplicação de cada função a cada elemento
    Args:
    iteravel (iter): iterável de valores
    iteravel_de_funcoes (iter): iterável de fun
    ções
    Returns:
    (iter) novo iterável de valores
    """
    return (map(lambda x: x(iteravel), iteravel_de_funcoes))

print(list(converter([1, 2, 3], [lambda x: x + 1, lambda x: x * 2])))