import requests
import random
import scipy.ndimage
import scipy.misc
import shutil

def get_random_meme():
    response = requests.get("https://api.imgflip.com/get_memes")
    # Print the status code of the response.
    lista = response.json()['data']['memes']
    a = random.randint(1,len(lista))
    r = requests.get(lista[a]['url'])
    with open("meme.jpg", 'wb') as f:
        f.write(r.content) 
    


get_random_meme()