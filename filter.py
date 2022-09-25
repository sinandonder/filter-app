from PIL import Image
import math



def zero_padding(image, mask_size = 3):
    mask_size = mask_size // 2
    width, height = image.size
    new_width, new_height = width + (mask_size * 2), height + (mask_size * 2)

    result = Image.new(image.mode, (new_width, new_height), (0))
    result.paste(image, (mask_size, mask_size))
    return result

def zero_padding_remove(image, mask_size = 3):
    mask_size = mask_size // 2
    width, height = image.size
    new_width, new_height = width - (mask_size * 2), height - (mask_size * 2)

    result = Image.new(image.mode, (new_width, new_height), (255))
    result.paste(image,(-mask_size, -mask_size))
    return result

def gaussian(image, mask_size = 5):

    if mask_size < 3:
        return image

    image = zero_padding(image, mask_size=mask_size)
    ms = int((mask_size - 1) / 2)
    width, height = image.size
    pixels = image.load()

    for x in range(ms, width - ms):
        for y in range(ms, height - ms):
            sum = 0
            
            sum += pixels[x - 1, y - 1]
            sum += pixels[x - 1, y]
            sum += pixels[x - 1, y + 1]
            sum += pixels[x, y - 1]
            sum += pixels[x, y]
            sum += pixels[x, y + 1]
            sum += pixels[x + 1, y - 1]
            sum += pixels[x + 1, y]
            sum += pixels[x + 1, y + 1]

            pixels[x, y] = round(sum / (mask_size * mask_size))
    
    image = zero_padding_remove(image, mask_size=mask_size)
    
    return image


def sobel(image, direction = "xy", mask_size=3):
    image = gaussian(image)
    image = zero_padding(image, mask_size=mask_size)
    ms = int((mask_size - 1) / 2)
    width, height = image.size
    pixels = image.load()

    sobel_mask_hor = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    sobel_mask_ver= [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    
    

    for x in range(ms, width - ms):
        for y in range(ms, height - ms):
            horizantalG = (sobel_mask_hor[0][0] * pixels[x - 1, y - 1]) + \
                          (sobel_mask_hor[0][1] * pixels[x - 1, y]) + \
                          (sobel_mask_hor[0][2] * pixels[x - 1, y + 1]) + \
                          (sobel_mask_hor[1][0] * pixels[x, y - 1]) + \
                          (sobel_mask_hor[1][0] * pixels[x, y - 1]) + \
                          (sobel_mask_hor[1][1] * pixels[x, y]) + \
                          (sobel_mask_hor[1][2] * pixels[x, y + 1]) + \
                          (sobel_mask_hor[2][0] * pixels[x + 1, y - 1]) + \
                          (sobel_mask_hor[2][1] * pixels[x + 1, y]) + \
                          (sobel_mask_hor[2][2] * pixels[x + 1, y + 1])
            
            verticalG =  (sobel_mask_ver[0][0] * pixels[x - 1, y - 1]) + \
                         (sobel_mask_ver[0][1] * pixels[x - 1, y]) + \
                         (sobel_mask_ver[0][2] * pixels[x - 1, y + 1]) + \
                         (sobel_mask_ver[1][0] * pixels[x, y - 1]) + \
                         (sobel_mask_ver[1][0] * pixels[x, y - 1]) + \
                         (sobel_mask_ver[1][1] * pixels[x, y]) + \
                         (sobel_mask_ver[1][2] * pixels[x, y + 1]) + \
                         (sobel_mask_ver[2][0] * pixels[x + 1, y - 1]) + \
                         (sobel_mask_ver[2][1] * pixels[x + 1, y]) + \
                         (sobel_mask_ver[2][2] * pixels[x + 1, y + 1])

            if direction == 'x':
                pixels[x - 1, y - 1] = abs(horizantalG)
            elif direction == 'y':
                pixels[x - 1, y - 1] = abs(verticalG)
            else:
                mag = math.sqrt(pow(horizantalG, 2.0) + pow(verticalG, 2.0))
                pixels[x - 1, y - 1] = int(mag)
    

    
    image = zero_padding_remove(image, mask_size=mask_size)
    
    return image


def prewitt(image, direction = "xy", mask_size=3):
    
    image = zero_padding(image, mask_size=mask_size)
    ms = int((mask_size - 1) / 2)
    width, height = image.size
    pixels = image.load()

    prewitt_mask_hor = [[1 ,1 ,1], [0, 0, 0],[-1, -1, -1]]
    prewitt_mask_ver= [[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]
    
    

    for x in range(ms, width - ms):
        for y in range(ms, height - ms):
            horizantalG = (prewitt_mask_hor[0][0] * pixels[x - 1, y - 1]) + \
                          (prewitt_mask_hor[0][1] * pixels[x - 1, y]) + \
                          (prewitt_mask_hor[0][2] * pixels[x - 1, y + 1]) + \
                          (prewitt_mask_hor[1][0] * pixels[x, y - 1]) + \
                          (prewitt_mask_hor[1][0] * pixels[x, y - 1]) + \
                          (prewitt_mask_hor[1][1] * pixels[x, y]) + \
                          (prewitt_mask_hor[1][2] * pixels[x, y + 1]) + \
                          (prewitt_mask_hor[2][0] * pixels[x + 1, y - 1]) + \
                          (prewitt_mask_hor[2][1] * pixels[x + 1, y]) + \
                          (prewitt_mask_hor[2][2] * pixels[x + 1, y + 1])
            
            verticalG =  (prewitt_mask_ver[0][0] * pixels[x - 1, y - 1]) + \
                         (prewitt_mask_ver[0][1] * pixels[x - 1, y]) + \
                         (prewitt_mask_ver[0][2] * pixels[x - 1, y + 1]) + \
                         (prewitt_mask_ver[1][0] * pixels[x, y - 1]) + \
                         (prewitt_mask_ver[1][0] * pixels[x, y - 1]) + \
                         (prewitt_mask_ver[1][1] * pixels[x, y]) + \
                         (prewitt_mask_ver[1][2] * pixels[x, y + 1]) + \
                         (prewitt_mask_ver[2][0] * pixels[x + 1, y - 1]) + \
                         (prewitt_mask_ver[2][1] * pixels[x + 1, y]) + \
                         (prewitt_mask_ver[2][2] * pixels[x + 1, y + 1])

            if direction == 'x':
                pixels[x - 1, y - 1] = abs(horizantalG)
            elif direction == 'y':
                pixels[x - 1, y - 1] = abs(verticalG)
            else:
                mag = math.sqrt(pow(horizantalG, 2.0) + pow(verticalG, 2.0))
                pixels[x - 1, y - 1] = int(mag)
    

    
    image = zero_padding_remove(image, mask_size=mask_size)


    
    return image


def binary(image, k = 0):
    max = 0
    width, height = image.size
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            if pixels[x , y] > max:
                max = int(pixels[x, y])
    
    
    max = max * (k / 100)
    
    for x in range(width):
        for y in range(height):
            if pixels[x , y] < max:
                pixels[x, y] = 0
            else: 
                pixels[x, y] = 255
    
    return image
            
if __name__ == "__main__":
    image = Image.open("test.jpeg").convert('L')

    gaus = gaussian(image, 2)
    gaus.show()