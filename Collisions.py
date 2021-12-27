def collision_probability(elements_quantity, takes_quantity):
    buf = (1/elements_quantity) ** 2
    if takes_quantity == 0 or takes_quantity == 1:
        return 0
    for i in range(2, takes_quantity):
        buf = buf + (1-buf) * (i/elements_quantity)
    return round(buf*100)

def elements_by_probability(probability, takes_quantity):
    i = 1
    while i > 0:
        if collision_probability(i, takes_quantity) == probability:
            return i
        i = i+1
    i = 0

elements_quantity = 500 
takes_quantity = 40

prob = collision_probability(elements_quantity, takes_quantity)
print('\nВероятность коллизии 1-го порядка при выборке {0} элементов из множества, состоящего из {1} элементов:\n'.format(takes_quantity, elements_quantity), prob, '%')

elems = elements_by_probability(prob, takes_quantity)
print('Количество элементов во множестве, если вероятность коллизии 1-го порядка равна {0} при выборке из {1} элементов:\n'.format(prob, takes_quantity), elems)

