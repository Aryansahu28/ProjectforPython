import PIL.Image

#ascii characters used to build the ascii image
ASCII_CHARS = ["@","#","S","%","?","*","+",";",":",",","."]

# resize image according to a new width 
def resize_image(image,new_width=100):
    width,height = image.size
    ratio = height / width
    new_height = int(ratio * new_width)
    size = {new_width,new_height}
    resized_image = image.resize(size,resample=None)
    return (resized_image)

#convert each pixel to grayscale
def grayify(image):
    grayify_image = image.convert("L")
    return (grayify_image)

#convert pixels to a string of ASCII character
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main(new_width=100):
    path = input("Enter the valid path of the image: ")
    try:
        image = PIL.Image.open(path)
    except:
        print("Invalid Location of Path")
    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data)
    print(pixel_count)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count , new_width))

    with open("ascii_image.txt","w") as f:
        f.write(ascii_image)
    
main()