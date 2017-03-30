import random
from urllib.request import urlretrieve

def download_web_image(url):
 name = random.randrange(1, 1000)
 full_name = str(name) + '.jpg'
 urlretrieve(url, full_name)

download_web_image('https://www.thenewboston.com/photos/users/2/resized/23471ba4417d650505928a0b1f1fd8b1.jpg')
