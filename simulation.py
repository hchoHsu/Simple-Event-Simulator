import numpy as np
import time
import cv2
import os
import matplotlib.pyplot as plt
import argparse
import sys, signal
import pickle
from event_simulator import *

parser = argparse.ArgumentParser(description="Simulate event data from AirSim")
parser.add_argument("--debug", action="store_true", help="Show the generated event")
parser.add_argument("--save", action="store_true", help="Save the event information.")
parser.add_argument("--height", type=int, default=260)
parser.add_argument("--width", type=int, default=346)
parser.add_argument("--pathdir", type=str, default="./dataset/sample/", help="Image dataset path")
parser.add_argument("--savedir", type=str, default="./dataset/sample/events", help="Event Image path")

class AirSimEventGen:
    def __init__(self, W, H, save=False, debug=False):
        self.ev_sim = EventSimulator(W, H)
        self.H = H
        self.W = W

        self.init = True
        self.start_ts = None

        self.rgb_image_shape = [H, W, 3]
        self.debug = debug
        self.save = save

        self.event_file = open("./results/events.pkl", "ab")
        self.event_fmt = "%1.7f", "%d", "%d", "%d"

        if debug:
            self.fig, self.ax = plt.subplots(1, 1)

    def visualize_events(self, event_img, idx):
        event_img = self.convert_event_img_rgb(event_img)
        self.ax.cla()
        self.ax.imshow(event_img, cmap="viridis")
        plt.draw()
        plt.pause(0.1)

    def convert_event_img_rgb(self, image):
        image = image.reshape(self.H, self.W)
        out = np.zeros((self.H, self.W, 3), dtype=np.uint8)
        out[:, :, 0] = np.clip(image, 0, 1) * 255
        out[:, :, 2] = np.clip(image, -1, 0) * -255

        return out

    def _stop_event_gen(self, signal, frame):
        print("\nCtrl+C received. Stopping event sim...")
        self.event_file.close()
        sys.exit(0)

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        images.append(os.path.join(folder,filename))
    images = sorted(images)

    return images

if __name__ == "__main__":
    args = parser.parse_args()
    os.makedirs(args.savedir, exist_ok=True)

    event_generator = AirSimEventGen(args.width, args.height, save=args.save, debug=args.debug)
    i = 0
    start_time = 0
    t_start = time.time()

    signal.signal(signal.SIGINT, event_generator._stop_event_gen)

    images = load_images_from_folder(args.pathdir)

    for imgname in images:
        if not imgname.endswith(".jpg") and not imgname.endswith(".png"):
            continue
        img = cv2.imread(imgname)
        # img = cv2.resize(cv2.imread(imgname), (160,120), interpolation=cv2.INTER_AREA)

        ts = time.time_ns()

        if event_generator.init:
            event_generator.start_ts = ts
            event_generator.init = False

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
        # Add small number to avoid issues with log(I)
        img = cv2.add(img, 0.001)

        ts = time.time_ns()
        ts_delta = (ts - event_generator.start_ts)

        # Event sim keeps track of previous image automatically
        event_img, events = event_generator.ev_sim.image_callback(img, ts_delta)

        if events is not None and events.shape[0] > 0:
            if event_generator.save:
                # Using pickle dump in a per-frame fashion to save time, instead of savetxt
                # Optimizations possible
                pickle.dump(events, event_generator.event_file)

            if event_generator.debug:
                event_generator.visualize_events(event_img, i)

            if os.path.isdir(args.savedir) != True:
                os.makedirs(args.savedir, exist_ok=True)
            img_saved = event_generator.convert_event_img_rgb(event_img)
            plt.imsave(os.path.join(args.savedir, f"{i}.png"), img_saved, cmap="viridis")
        else:
            plt.imsave(os.path.join(args.savedir, f"{i}.png"), np.zeros(shape=(img.shape[0], img.shape[1], 3)), cmap="viridis")

        i += 1
