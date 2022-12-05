'''
I used GeeksforGeeks to get reference on how to 
convert a frame to ASCII characters
'''

import cv2
import numpy as np
import sys
from PIL import Image

def main():
    PIXELS = [' ', '.', '`', '^', '*', ':', ';', '%', '$', '&', '@', '#']   # Change the PIXELS mapping to increase/decrease details
    # PIXELS.reverse()    # Flip brightness mapping

    video = cv2.VideoCapture("bad_apple.mp4")

    scale = 0.43    # Pixel scale (depends on terminal font)
    columns = 50    # Width of the rendered frame

    while True:
        ret, frame = video.read()

        if not ret: 
            print("Something went wrong :( Or the video has ended")
            break;

        frame = Image.fromarray(frame)
        frame = frame.convert("L")      # Convert frame to greyscale
        frame_width = frame.size[0]
        frame_height = frame.size[1]

        crop_w = frame_width / columns
        crop_h = crop_w / scale
        rows = frame_height / crop_h

        rendered = " "

        for row in range(int(rows)):
            top_y = int(row * crop_h)
            bottom_y = int((row + 1) * crop_h)

            if row == rows - 1:
                bottom_y = frame_height

            for col in range(int(columns)):
                top_x = int(col * crop_w)
                bottom_x = int((col + 1) * crop_w)
                
                if col == columns - 1:
                    bottom_x = frame_width

                cropped = frame.crop((top_x, top_y, bottom_x, bottom_y))    # left, upper, right, lower

                image_array = np.array(cropped)
                x, y = image_array.shape
                brightness = np.average(image_array.reshape(x * y))

                pixel_range = len(PIXELS) - 1
                rendered += PIXELS[int((brightness * pixel_range) / 255)]

            rendered += '\n'

        sys.stdout.write('\r' + rendered)

    video.release()


if __name__ == "__main__":
    main()

    # PIXELS = [' ', '#']

    # frame = Image.open("test_frame.png")
    # terminal_image = []

    
    # frame = frame.convert("L")
    # frame_width = frame.size[0]
    # frame_height = frame.size[1]

    # scale = 0.43

    # columns = 150
    # crop_w = frame_width / columns
    # crop_h = crop_w / scale
    # rows = frame_height / crop_h

    # print(crop_w, " x ", crop_h)

    # for row in range(int(rows)):
    #     top_y = int(row * crop_h)
    #     bottom_y = int((row + 1) * crop_h)

    #     if row == rows - 1:
    #         break

    #     terminal_image.append(" ")

    #     for col in range(int(columns)):
    #         top_x = int(col * crop_w)
    #         bottom_x = int((col + 1) * crop_w)
            
    #         if col == columns - 1:
    #             break

    #         cropped = frame.crop((top_x, top_y, bottom_x, bottom_y))  # left, upper, right, lower

    #         image_array = np.array(cropped)
    #         x, y = image_array.shape
    #         brightness = np.average(image_array.reshape(x * y))

    #         terminal_image[row] += PIXELS[int(brightness / 255)]

    # for row in terminal_image:
    #     print(len(row), row)

    
    # # open file
    # f = open("b.txt", 'w')
 
    # # write to file
    # for row in terminal_image:
    #     f.write(row + '\n')
 
    # # cleanup
    # f.close()
