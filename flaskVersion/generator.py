import random

def randNames(f_names, l_names): 
    f_names = f_names.copy()
    l_names = l_names.copy()
    names = []
    while(len(f_names) > 0):
        f_index = random.randint(0, len(f_names) - 1)
        l_index = random.randint(0, len(l_names) - 1)
        f = f_names.pop(f_index)
        l = l_names.pop(l_index)
        age = random.randint(18,50)
        names.append((f,l,age))
    return names

f_names = ['cade','john']
l_names = ['smith', 'williams']

people = randNames(f_names, l_names)

print(people)
