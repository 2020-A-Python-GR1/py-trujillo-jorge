import requests
import random
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def get_random_meme():
    response = requests.get("https://api.imgflip.com/get_memes")
    # Print the status code of the response.
    lista = response.json()['data']['memes']
    a = random.randint(1,len(lista))
    r = requests.get(lista[a]['url'])
    with open("meme.jpg", 'wb') as f:
        f.write(r.content) 
    
original = np.empty(1)
to_hide = 0

def create_back(numero):
    global original, to_hide
    original = np.arange(0,numero*numero)
    to_hide = random.randint(0,numero*numero-1)
    original[to_hide]= -1
    print(original)
    np.random.shuffle(original)

def can_move_to_empty(num,n):
    empty_pos = np.where(original.reshape(n,n) == -1)
    selected_pos = np.where(original.reshape(n,n) == num)
    if selected_pos[0][0]==empty_pos[0][0] and (selected_pos[1][0]==empty_pos[1][0]-1 or selected_pos[1][0]==empty_pos[1][0]+1):
        return True
    elif  selected_pos[1][0]==empty_pos[1][0] and (selected_pos[0][0]==empty_pos[0][0]-1 or selected_pos[0][0]==empty_pos[0][0]+1):
        return True
    else:
        return False
    
def move(num,n):
    if can_move_to_empty(num,n):
        empty_pos = np.where(original == -1)
        selected_pos = np.where(original == num)
        original[empty_pos], original[selected_pos] = original[selected_pos], original[empty_pos]
        print(original)
    else:
        print("No se puede mover")
    pass


def verificar(num):
    aux=0
    for i in original:
        if np.where(original == i)[0][0]==i:
            aux = aux +1
    print(aux)
    if aux == num*num -1:
        return True
    else:
        return False


#num = int(input('Numero')) 
#create_back(num)

#while not verificar(num):
#    print(original.reshape(num,num))
#    num_selected = int(input('Numero sel')) 
#    move(num_selected,num)

