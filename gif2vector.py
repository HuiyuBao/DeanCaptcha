from PIL import Image
def gif2chars(file_path):
    im = Image.open(file_path)
    colors = im.getcolors()
    list.sort(colors,reverse=True)
    char_colors = [colors[1][1],colors[2][1],colors[3][1],colors[4][1]]
    character = list()
    for j in range(4):
        character.append(im.point(lambda i: i == int(char_colors[j])))
    most_color = list()
    least_color = list()
    for j in range(4):
        temp_im = character[j]
        colors = temp_im.getcolors()
        list.sort(colors)
        most_color.append(colors[1][1])
        least_color.append(colors[0][1])
    return character, most_color, least_color
def remove_redunant_whitespace(pillow_img):
    width, height = pillow_img.size
    print(width, height)
    pixel_values = list(pillow_img.getdata())



    print(pixel_values)
    return

def img2str(img):
    return

def gif2charvectors(file_path):
    character, most_color, least_color = gif2chars(file_path)
    remove_redunant_whitespace(character[0])
gif2charvectors("test.gif")
