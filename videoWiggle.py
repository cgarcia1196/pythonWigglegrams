import cv2 as cv
import imgWiggleGif as IWG

video = input("enter video name(example: bf3_Trim.mp4): ")

cap = cv.VideoCapture('videos/{}'.format(video))
gif = []
frameCount = 0
#loop through each frame of video
while cap.isOpened():
    frameCount += 1
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    #only uses every third frame
    if frameCount % 3 != 0:
        continue

    cv.imwrite('frames/frame%d.jpg' % (frameCount,), frame)
    im  = IWG.Image.open('frames/frame%d.jpg' % (frameCount,))

    #split each 3d frame into two images
    #insert each image into the gif list
    IWG.splitImg(im)

    #delete frame image
    try:
        IWG.os.remove('frames/frame%d.jpg' % (frameCount,))
    except: 
        print("cant removed frame: {}".format(frameCount))
        pass

cap.release()
cv.destroyAllWindows()

#save gif
gifName = input('GIF name: ')
IWG.saveGif(gifName)

print('gif saved to images folder')
IWG.os.system('pause')