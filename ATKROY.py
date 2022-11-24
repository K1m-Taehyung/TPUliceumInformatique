from PIL import Image, ImageDraw, ImageFont

def f(t,n):
    im = Image.new('RGB', (200,200), color=('#FAACAC'))
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', size=12)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (15,100),
        t, 
        font = font,
        fill=('#1C0606') )
    im.save(f'c:/VS/{n}.jpg')
t=['БЫСТРА НА БАРЬБУ ЗАПИСАЛСЯ НЕФАР',
   'ПАТЛЫ СБРИЛ БАРАДУ АТРАСТИЛ',
   'МЕТРО ЛЮБЛИНО РАБОТАЕМ']
for i in range(3):
    f(t[i],i)

from moviepy.editor import *

import os
directory = 'C:\VS'
files = os.listdir(directory)
images = list(filter(lambda x: x.endswith('.jpg'), files))
clips = [ImageClip(m).set_duration(2) for m in images]

final_clip = concatenate_videoclips(clips, method='compose')
final_clip.write_videofile('test.webm', fps=24)
