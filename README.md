# Valorant Ai Trigger-bot

Description:
this is a trigger bot that utilizes the yolov11 model to predict the position of enemies and target head and torso using computer vision

How to use:
1. create a custom environment , preferably python 3.8.10 others work too I think
2. install the varies dependencies given in main.py [note: `pip install pywin32` for `win32gui` ]
3. `python main.py` to run
4. make sure to change put keybindings for fire to 'p'.

Problems faced and areas to improve:
1. latency issue takes about 70 to 120 ms to process a single frame , changes depending on the performance of gpu [I think]
2. right now the dataset consists of 640 imgs and was trained on 50 epochs much training should be provided.
