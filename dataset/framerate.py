import cv2
import argparse

parser = argparse.ArgumentParser(description="Get framerate from video")
parser.add_argument("--video", type=str, default="./video-regular-fast.mp4")

if __name__ == '__main__':
    args = parser.parse_args()
    
    video = cv2.VideoCapture(args.video)

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
     
    video.release(); 
