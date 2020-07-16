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
matriz = []
nums_only = np.empty(1)


def get_nums():
    global nums_only
    aux = []
    for i in range(len(matriz)):
        aux.append(matriz[i][0])
    nums_only= np.array(aux)

def can_move_to_empty(num,n):
    empty_pos = np.where(nums_only.reshape(n,n) == -1)
    selected_pos = np.where(nums_only.reshape(n,n) == num)
    if selected_pos[0][0]==empty_pos[0][0] and (selected_pos[1][0]==empty_pos[1][0]-1 or selected_pos[1][0]==empty_pos[1][0]+1):
        return True
    elif  selected_pos[1][0]==empty_pos[1][0] and (selected_pos[0][0]==empty_pos[0][0]-1 or selected_pos[0][0]==empty_pos[0][0]+1):
        return True
    else:
        return False

def move_matriz(num,n):
    if can_move_to_empty(num,n):
        empty_pos = np.where(nums_only == -1)
        selected_pos = np.where(nums_only == num)
        nums_only[empty_pos], nums_only[selected_pos] = nums_only[selected_pos], nums_only[empty_pos]
        matriz[empty_pos[0][0]], matriz[selected_pos[0][0]] = matriz[selected_pos[0][0]], matriz[empty_pos[0][0]]
        print(nums_only)
    else:
        print("No se puede mover")
    pass

def verificar(num):
    aux=0
    for i in nums_only:
        if np.where(nums_only == i)[0][0]==i:
            aux = aux +1
    print(aux)
    if aux == num*num -1:
        return True
    else:
        return False

def read_image():
    rana_pepe = mpimg.imread('meme.jpg',format='jpg')
    plt.imshow(rana_pepe)
    plt.show()
    return rana_pepe

def dividir_imagen(imagen, n):
    global matriz
    altura = int(imagen.shape[0]/4)
    ancho = int(imagen.shape[1]/4)
    bander = 0
    for i in range(n):
        for j in range(n):
            matriz.append([bander,np.array((imagen[altura*i:altura*(i+1),ancho*j:ancho*(j+1)]))])    
            bander = bander +1  
    
def hide_one(numero):
    global nums_only
    to_hide_o = random.randint(0,numero*numero-1)
    nums_only[to_hide_o]=-1
    matriz[to_hide_o][0]=-1

    pass

def get_min_aprox(numero,n):
    pass

def graficar():
    fig=plt.figure(figsize=(8, 8))
    columns = 4
    rows = 4
    img = np.empty(1)
    for i in range(1, columns*rows +1):
        if matriz[i-1][0]==-1:
            img = np.random.randint(10, size=(3,3))
        elif matriz[i-1][0]!=-1:
            img = matriz[i-1][1]
        fig.add_subplot(rows, columns, i)
        plt.imshow(img)
        plt.axis('off')
        plt.title(f"{matriz[i-1][0]}")
    plt.show()
    pass


dividir_imagen(read_image(),4)
get_nums()
print(nums_only)
hide_one(4)
np.random.shuffle(matriz)
get_nums()
while not verificar(4):
    graficar()
    get_nums()
    print(nums_only.reshape(4,4))
    num_selected = int(input('Numero sel')) 
    move_matriz(num_selected,4)