from PIL import Image
import os 

gif = []
# splitting 3d image into two, left and right images
# then inserting them into the gif list
def splitImg(im):

    width, height = im.size

    #left image crop coordinates
    leftOffcet = 0
    rightOffcet = 0
    left = 0 + leftOffcet
    right = width/2 - rightOffcet
    top = 0
    bottom = height

    imLeft = im.crop((left, top, right, bottom))

    #right image crop coordinates
    left = width/2 + rightOffcet
    right = width - leftOffcet
    top = 0
    bottom = height

    imRight = im.crop((left, top, right, bottom))

    # insert left and right image into gif list
    gif.append(imLeft)
    gif.append(imRight)

def saveGif(name = 'gif_result', frameDuration = 120):
    gif[0].save('images/{}.gif'.format(name), save_all = True, optimize = False, append_images = gif[1:], loop = 0, duration = frameDuration)

if __name__ == "__main__":

    #check that the input file is valid
    while True:
        imgLoc = input("enter image file(default image example 'corridor3D.webp'): ")
        try:
            imageObj = Image.open('images/' + imgLoc)
            break
        except FileNotFoundError:
            print("File cannot be found, try another location")
        except PIL.UnidentifiedImageError:
            print("image cannot be opened try another file(image formats %s)" % (PIL.features.pillinfo(),))

    splitImg(imageObj)
    gifName = input('gif name: ')
    saveGif(gifName)

    print('gif saved to images folder')
    os.system('pause')