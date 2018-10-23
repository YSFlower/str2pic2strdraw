# -*- coding: utf-8 -*-
# 1024  代码skr秀
import pygame
from PIL import Image

def print_boda():
    chars = '''
    #                   _oo0oo_
    #                  o8888888o
    #                  88" . "88
    #                  (| -_- |)
    #                  0\  =  /0
    #                ___/`---'\___
    #              .' \\|     |// '.
    #             / \\|||  :  |||// \\
    #            / _||||| -:- |||||- \\
    #           |   | \\\  -  /// |   |
    #           | \_|  ''\---/''  |_/ |
    #           \  .-\__  '-'  ___/-. /
    #         ___'. .'  /--.--\  `. .'___
    #      ."" '<  `.___\_<|>_/___.' >' "".
    #     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
    #     \  \ `_.   \_ __\ /__ _/   .-` /  /
    # =====`-.____`.___ \_____/___.-`___.-'=====
    #                       `=---='
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    #           佛祖保佑         永无BUG'''

    chars = chars.replace('#','')
    print(chars)

def init_img(text):
    pygame.init()
    font = pygame.font.SysFont("arial", 20)
    ftext = font.render(text, True, (0,0,0),(255,255,255))
    pygame.image.save(ftext,'image.jpg')

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    init_img(u'123123')
    file_name = 'image.jpg'
    im = Image.open(file_name)
    # im = im.resize((80,80), Image.NEAREST)
    width,height = im.size
    txt = ""

    for i in range(height):
        txt += '      '
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print_boda()
    print(txt)


    output_file = 'output.txt'
    #字符画输出到文件
    if output_file:
        with open(output_file,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)