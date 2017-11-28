from PIL import Image
<<<<<<< HEAD
import numpy
=======
>>>>>>> 5198eec3b3abd0188a76f5dc4f7de3ad9a3b4d78
# test
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

    left, right, up, down = 0, 0, 0, 0

    for i in range(height):
        flag = 1
        for j in range(width):
            if pixel_values[i*width+j] == char_color:
                flag = 0
        if flag == 0:
            up = i
            break
    for i in range(height - 1, -1, -1):
        flag = 1
        for j in range(width):
            if pixel_values[i*width+j] == char_color:
                flag = 0
        if flag == 0:
            down = i
            break
    for j in range(width):
        flag = 1
        for i in range(height):
            if pixel_values[i*width+j] == char_color:
                flag = 0
        if flag == 0:
            left = j
            break
    for j in range(width - 1, -1, -1):
        flag = 1
        for i in range(height):
            if pixel_values[i*width+j] == char_color:
                flag = 0
        if flag == 0:
            right = j
            break

    # let the size be height = 12 and width = 10
    if (up > 0) and ((up + 10) < height):
        up = up -1
        down = up + 11
    elif up == 0:
        down = 11
    else:
         up = down - 11

    if (left > 1) and ((left)+7 < width):
        left = left - 2
        right = left + 9
    elif (left == 0) or (left == 1):
        right = left + 9
    else:
        left = right -9
    '''
        for i in range(up, down + 1, 1):
            for j in range(left, right , 1):
                print(pixel_values[i*width+j],end="")
            print(pixel_values[i*width+right])

        print("\n")
    '''
    box = (left, up, right + 1, down + 1)
    transformed_img = pillow_img.crop(box)

    return left, transformed_img

def img2str(img):
    n_array = numpy.array(img.getdata())
    #print (n_array)
    return n_array

def gif2charvectors(file_path):
    character = gif2chars(file_path)
    chars = list()
    ans = list()
    for i in range(4):
        chars.append(remove_redunant_whitespace(character[i]))
    list.sort(chars)

    for i in range(4):
        ans.append(img2str(chars[i][1]))
    print(ans)

gif2charvectors("test.gif")
