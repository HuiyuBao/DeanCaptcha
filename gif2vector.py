from PIL import Image
def gif2chars(file_path):
    '''get the individual images from gif file_path
    Read gif file from file path, extract the four individual characters from the image and return four individual pictures, as a list of pillow image objects. Note the size (width * height) of the image is NOT CHANGED, meaning lots of whitespace remains. Also, the RGB color information is stripped(TODO: is it really true?)
    '''
    im = Image.open(file_path)
    colors = im.getcolors()
    list.sort(colors,reverse=True)
    char_colors = list()
    for i in range(4):
        char_colors.append(colors[i+1][1])
    characters = list()
    for j in range(4):
        characters.append(im.point(lambda i: i == int(char_colors[j])))
    # a simple algorithm: pick the four most common colors, apart from the background. Vola! pick all pixels of each color, thus getting the four images.
    return characters
def remove_redunant_whitespace(pillow_img):
    '''removes redunant whitespace and resize image of individual characters
    removes whitespace and turns the size into 16*16.Returns a pillow image object, 16 by 16 TODO: check if this size is necessary
    '''
    colors = pillow_img.getcolors()
    list.sort(colors)
    background_color = colors[1][1]
    char_color= colors[0][1]
    width, height = pillow_img.size
    pixel_values = list(pillow_img.getdata())
    #

    print(pixel_values)
    return

def img2str(img):
    return

def gif2charvectors(file_path):
    character = gif2chars(file_path)
    remove_redunant_whitespace(character[0])
gif2charvectors("test.gif")
