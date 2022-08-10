# /usr/bin/python
# coding:utf-8

from PIL import Image,ImageFont,ImageDraw

FONT_PATH = "C:/Windows/Fonts/simhei.ttf"

def draw_pieslice(background,title,info_list):
    draw = ImageDraw.Draw(background)

    font_title = ImageFont.truetype(FONT_PATH,25,encoding = 'utf-8')
    font_normal = ImageFont.truetype(FONT_PATH,15,encoding = 'utf-8')

    title_w,title_h = draw.textsize(title,font_title,spacing = 6)
    normal_w,normal_h = draw.textsize(info_list[0][0]+" "+"88%",font_normal,spacing = 6)
    font_h = ( len(info_list) + 1 ) * ( normal_h + 10 ) - 20

    background_w,background_h = ( 360 + normal_h + normal_w,350 + title_h if 300 > font_h else 50 + title_h + font_h )

    background = background.resize((background_w,background_h))
    draw = ImageDraw.Draw(background)

    title_center_manger = int((background_w - title_w) / 2)

    draw.text((title_center_manger,20),title,fill = (0,0,0),font = font_title)
    draw.text((340,background_h - font_h - 20),"图例",fill = (0,0,0),font = font_normal)

    all_data_num = 0

    for data in info_list:
        all_data_num += data[1]

    start_angle = 0
    step_color = int( 205 / len(info_list) )
    tmp_location = 1
    for data in info_list:
        tmp_color = tmp_location * step_color + 50
        pieslice_color = (tmp_color,tmp_color,tmp_color)
        add_angle = ( data[1] / all_data_num ) * 360
        draw.pieslice((10,40 + title_h,310,340 + title_h),start = start_angle,end = start_angle + add_angle,fill = pieslice_color,outline = (0,0,0))
        draw.text((340,background_h - font_h - 20 + tmp_location * ( normal_h + 10 )),data[0] + " " + str(int(( data[1] / all_data_num ) * 100)) + "%",fill = (0,0,0),font = font_normal)
        draw.rectangle((350 + normal_w,background_h - font_h - 20 + tmp_location * ( normal_h + 10 ),350 + normal_w + normal_h,background_h - font_h - 20 + tmp_location * ( normal_h + 10 ) + normal_h),fill = pieslice_color,outline = (0,0,0))

        tmp_location += 1
        start_angle = start_angle + add_angle
    
    return background

if __name__ == '__main__':
    background = Image.new("RGB",(10,10),(255,255,255))
    background = draw_pieslice(background,"测试数据集",[["A",15],["B",15],["C",20],["D",5],["E",1]])
    background.save("./tmp.png")