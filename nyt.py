import requests
requests.packages.urllib3.disable_warnings()
from datetime import datetime
#from PIL import Image
import pdf2image
import os

import logging

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, 'test_log.log')

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def get_pdf():
    today = datetime.now()
    today_str = f'{today.year}-{today.month:02}-{today.day:02}'
    path_to_pdf = f'https://static01.nyt.com/images/{today.year}/{today.month:02}/{today.day:02}/nytfrontpage/scan.pdf'
    session = requests.Session()
    session.trust_env = False
    response = session.get(path_to_pdf, verify=False)
    if response.status_code == 200:
        path_to_pdf = f'https://static01.nyt.com/images/{today.year}/{today.month:02}/{today.day:02}/nytfrontpage/scan.pdf'
        response = session.get(path_to_pdf, verify=False)
        path_pdf = os.path.join(dir_path, 'pdf')
        filename_pdf = os.path.join(path_pdf, f'{today_str}.pdf')
        logger.info(filename_pdf)
        with open(filename_pdf,'wb') as f:
            for bits in response.iter_content():
                f.write(bits)
        im = pdf2image.convert_from_path(
            filename_pdf,
        )
        if im: logger.info(im)
        path_img = os.path.join(dir_path, 'static/images')
        filename_img = os.path.join(path_img, f'{today_str}.jpg')
        logger.info(filename_img)
        for img in im:
            img.save(filename_img,'JPEG')
    return

if __name__ == '__main__':
    print(f'[I] Grabbing PDF for {datetime.now()}')
    get_pdf()
