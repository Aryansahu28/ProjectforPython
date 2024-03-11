import PIL.Image

#Ascii codes squence wise
ASCII_CHARS = ["@","#","S","%","?","*","+",";",":",",","."]

#We will resize the image
def resize_image(image,new_width=100):
    width,height = image.size
    ratio = height/width
    new_height = (ratio*new_width)
    resized_image = image.resize({new_width,new_height},resample=None)
    return resized_image

def grayify(image):
    grayify_image = image.convert("L")
    return grayify_image

def pixel_to_ascii(image):
    pixels = image.getdata()
    characters ="".join(ASCII_CHARS[pixel//23]for pixel in pixels)
    return characters

def main(new_width=100):
    path = input("Enter the path of image\n")
    try:
        image = PIL.Image.open(path)
    except:
        print("You entered wrong path of file")

    pixel_image = pixel_to_ascii(grayify(resize_image(image)))

    

    