import requests
from PIL import Image


def download_images():
    image_url = 'https://cdndoc.pcs.baidu.com/rest/2.0/docview/doc?datatype=pic&dp_logid=82417374270175427&expires=3h&fid=2214641459-250528-541256104930233&ipmd5=022b5d5c91659fc347079bb4dafbc4f0&method=data&nf=1&object=249165934pea5716d1dd1b2e7b3df77f&rt=sh&sign=FOTRE-DCb740ccc5511e5e8fedcff06b081203-hwSJEpewlwl1OAm1yaeondzgTak%253D&timestamp=1681411172&uar=50e85a8a3f03d0d15161aea21d38acbd&env=web&product=share&pagenum={}'
    for number in range(303,445):
        img_data = requests.get(image_url.format(number),verify=False).content
        with open('{}.jpg'.format(number), 'wb') as handler:
            handler.write(img_data)


def convert_to_pdf():
    image_1 = Image.open(r'images\1.jpg')
    im_1 = image_1.convert('RGB')
    image_list = []
    for number in range(2,445):
        image_loop = Image.open('images\\{}.jpg'.format(number))
        im_loop = image_loop.convert('RGB')
        image_list.append(im_loop)    
    im_1.save(r'my_images.pdf', save_all=True, append_images=image_list)

download_images()
convert_to_pdf()

