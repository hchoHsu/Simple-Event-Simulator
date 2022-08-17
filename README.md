# Simple Event Simulator
This project is a simple event simulator, which comes from [Micorsoft/AirSim](https://github.com/microsoft/AirSim/blob/b272597854f389e03bf7d9b9581666c91f2e24f9/docs/event_sim.md). It can convert a continuous sequence of images into events.

+ Conda Environment:    **event_simulator**

## Prerequisites
To run the simulation, you can refer to the environment.yml we provided to build the conda environment (which is what we recommend)

```bash
conda env create -f environment.yml
```
and easily enter the conda environment by
```bash
conda activate event_simulator
```

Or you can also use Python with the following packages installed
```bash
numpy
cv2
matplotlib
numba
```

## Demo
You can run the simulation demo using the following command line:
```bash
python simulation.py --debug
```

## Simulation
There're a few config you can set:

| Config | Type | Discreption |
| ------ | ---- | ----------- |
| debug  | bool | visualize the simulation |
| save   | bool | save the event as 'events.pkl' under folder 'result' |
| height, width | int | resolution of the images |
| pathdir | str | path to your raw images |
| savedir | str | path to save the generated event images |

For example:
```bash
python simulation.py --save --debug --pathdir './path/to/image_sequences/' --savedir './path/to/save/event_images/' --height 'my_height' --width 'my_width'
```

And also to change the event threshold, you can find the below section at ```event_simulator.py```:

```python=9
TOL = 0.1
MINIMUM_CONTRAST_THRESHOLD = 0.01
```

You can change the value of **TOL** to increase or decrease the event signal sensitivity.
