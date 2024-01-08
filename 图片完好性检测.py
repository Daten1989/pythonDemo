import os
import time

from PIL import Image

IMG_PATH = 'images'

def image_is_broken_check():
    '''
    检测异常图片
    :return:
    '''
    start_time = time.time()
    # 获取指定目录下所有图片
    img_name_list = os.listdir(IMG_PATH)
    # 遍历读取图片
    for img_name in img_name_list:
        # 图片全路径
        local_img_path = os.path.join(IMG_PATH, img_name)
        print(f'image name: {img_name}')
        try:
            Image.open(local_img_path).verify()
            Image.open(local_img_path).load()
            print(f'normal image:{img_name}')
        except Exception as e:
            print(f'image ({img_name}) broken check error: {e}')
            continue
    print(f'total spend:{1000*(time.time() - start_time)} ms')

if __name__ == '__main__':
    image_is_broken_check()