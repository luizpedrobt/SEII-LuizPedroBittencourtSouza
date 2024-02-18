import requests
import time
import concurrent.futures

img_urls = [
    'https://unsplash.com/pt-br/fotografias/uma-pessoa-no-meio-de-um-deserto-9f7oiGARGIg',
    'https://unsplash.com/pt-br/fotografias/uma-trilha-no-meio-de-uma-floresta-com-muitas-arvores-PsK4jh88Smw',
    'https://unsplash.com/pt-br/fotografias/um-gazebo-no-meio-de-um-parque-cercado-por-arvores-s7BiK60BL2o',
    'https://unsplash.com/pt-br/fotografias/uma-pequena-cachoeira-no-meio-de-uma-floresta-8cP10iwyzJ4'
    ]

t1 = time.perf_counter()

def download_img(img_url):
    for img_url in img_urls:
        img_bytes = requests.get(img_url).content
        img_name = img_url.split('/')[5]
        img_name = f'{img_name}.jpg'
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
            print(f'{img_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_img, img_urls)

t2 = time.perf_counter()

print(f'Finished in {t2 - t1} seconds')
