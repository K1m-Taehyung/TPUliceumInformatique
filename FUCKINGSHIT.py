from PIL import Image, ImageDraw, ImageFont
im = Image.new('RGB', (200,200), color=('#FAACAC'))
font = ImageFont.truetype('C:/Users/student/Desktop/FRAHV.ttf', size=18)
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (20,100),
    'ПАПАЛСЯ ЖЫДКИЙ', 
    font = font,
    fill=('#1C0606')
    )
im.show()



