# Simple Event Simulator
This project is a simple event simulator, which comes from [Micorsoft/AirSim](https://github.com/microsoft/AirSim/blob/b272597854f389e03bf7d9b9581666c91f2e24f9/docs/event_sim.md)

+ Conda Environment:    **event_simulator**

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
| video  | str  | the input video |
| height, width | int | resolution of the images |

For example:
```bash
python simulation.py --save --debug --video './my_video' --height 'my_height' --width 'my_width'
```