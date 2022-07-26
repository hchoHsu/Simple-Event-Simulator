import cv2 as cv
import numpy as np

WIDTH, HEIGHT = 346, 260

folder_path = 'sample/'
event_folder_path = 'sample/events/'

raw_images = ['174_462_474_s_41211687.png',
              '175_462_474_s_41251687.png',
              '176_462_474_s_41291686.png',
              '177_462_474_s_41331686.png',
              '178_462_474_s_41371686.png',
              '179_462_474_s_41411685.png',
              '180_462_474_s_41451685.png',
              '181_462_474_s_41491685.png',
              '182_462_474_s_41531684.png']

evt_images = ['1.png','2.png','3.png','4.png',
              '5.png','6.png','7.png','8.png','9.png']

if __name__ == '__main__':
    out = cv.VideoWriter('sample_demo.mp4', cv.VideoWriter_fourcc(*'mp4v'), 1, (WIDTH*2, HEIGHT))

    for i in range(len(evt_images)):
        frame = np.zeros((HEIGHT, WIDTH*2, 3), np.uint8)
        frame[:HEIGHT, :WIDTH, :3] = cv.imread(folder_path + raw_images[i])
        frame[:HEIGHT, WIDTH:WIDTH*2, :3] = cv.imread(event_folder_path + evt_images[i])

        out.write(frame)
        cv.imshow('Left:RawImage, Right:EventImage', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
