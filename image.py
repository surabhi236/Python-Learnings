import random
import urllib

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.urlretrieve(url, full_name)

download_web_image("https://www.google.co.in/search?q=image&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwiLqp_N0-zSAhVEPI8KHQQ8AQUQsAQIIg&biw=1291&bih=634#imgrc=TVEPc8yBbrThFM:")