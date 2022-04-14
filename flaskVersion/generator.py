import random

f_names = [
            'cade',
            'john',
            'mary',
            'patricia',
            'lisa',
            'charles',
            'jennifer',
            'thomas',
            'stephanie',
            'will',
            'joe',
            'betty',
            'grace',
            'matthew',
            'mark',
            'quin']
l_names = [
        'smith',
        'williams',
        'lopez',
        'lueker',
        'johnson',
        'oneal',
        'connors',
        'richardson',
        'robinson',
        'rogers',
        'michaels',
        'nelson',
        'edwards',
        'doe',
        'mitchel',
        'lafrance']

def randNames(f_names, l_names): 
    f_names = f_names.copy()
    l_names = l_names.copy()
    names = []
    id = 0
    while(len(f_names) > 0):
        f_index = random.randint(0, len(f_names) - 1)
        l_index = random.randint(0, len(l_names) - 1)
        f = f_names.pop(f_index)
        l = l_names.pop(l_index)
        age = random.randint(18,50)
        names.append((id,f,l,age))
        id = id + 1
    return names


people = randNames(f_names, l_names)

# print(people)
