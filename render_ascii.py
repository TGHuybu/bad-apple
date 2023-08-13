import time
import cv2
import numpy as np
from PIL import Image


def make_frames(path, width, out):
    PIXELS = [' ', '.', '^', '*', ':', ';', '%', '$', '&', '@', '#']

    video = cv2.VideoCapture(path)

    scale = 0.43    # Pixel scale (depends on terminal font)
    columns = width    # Width of the rendered frame
    rows = 0

    frames = []
    frame_cnt = 0

    print("Starting...")
    t_start = time.time()

    while True:
        ret, frame = video.read()

        if not ret: 
            print("Something went wrong :( Or the video has ended")
            break

        frame_cnt += 1

        frame = Image.fromarray(frame)
        frame = frame.convert("L")      # Convert frame to greyscale
        frame_width = frame.size[0]
        frame_height = frame.size[1]

        crop_w = frame_width / columns
        crop_h = crop_w / scale
        rows = frame_height / crop_h

        rendered = ""

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

        frames.append(rendered)

    t_end = time.time()
    print(f"Done in {t_end - t_start} seconds!")

    video.release()

    with open(out, "w") as out_f:
        out_f.write(str(int(rows)) + '\n')
        out_f.writelines(frames)


if __name__ == "__main__":
    path = "bad_apple.mp4"
    out = "bad_apple_frames.txt"

    make_frames(path, 70, out)
