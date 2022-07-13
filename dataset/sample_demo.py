import cv2 as cv
import numpy as np
import os

WIDTH, HEIGHT = 346, 260

folder_path = 'sample/'

raw_images = ['174_462_474_s_41211687.png',
              '175_462_474_s_41251687.png',
              '176_462_474_s_41291686.png',
              '177_462_474_s_41331686.png',
              '178_462_474_s_41371686.png',
              '179_462_474_s_41411685.png',
              '180_462_474_s_41451685.png',
              '181_462_474_s_41491685.png',
              '182_462_474_s_41531684.png']

evt_images = ['ev_sample1.png','ev_sample2.png','ev_sample3.png','ev_sample4.png',
              'ev_sample5.png','ev_sample6.png','ev_sample7.png','ev_sample8.png','ev_sample9.png']

if __name__ == '__main__':
    out = cv.VideoWriter('sample_demo.mp4', cv.VideoWriter_fourcc(*'mp4v'), 1, (WIDTH*2, HEIGHT))

    for i in range(len(evt_images)):
        frame = np.zeros((HEIGHT, WIDTH*2, 3), np.uint8)
        frame[:HEIGHT, :WIDTH, :3] = cv.imread(folder_path + raw_images[i])
        frame[:HEIGHT, WIDTH:WIDTH*2, :3] = cv.imread(folder_path + evt_images[i])

        out.write(frame)
        cv.imshow('Left:RawImage, Right:EventImage', frame)
        if cv.waitKey(100) & 0xFF == ord('q'):
            break
