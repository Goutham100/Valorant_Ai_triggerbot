# Valorant Ai Trigger-bot
https://www.buymeacoffee.com/Goutham0

Description:
this is a trigger bot that utilizes the yolov11 model to predict the position of enemies and target head and torso using computer vision

How to use:
1. create a custom environment , preferably python 3.8.10 others work too I think
2. https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Windows <-- download cuda
3. `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118`
4. install the varies dependencies given in main.py [note: `pip install pywin32` for `win32gui` ]
5. `python main.py` to run
6. make sure to change put keybindings for fire to 'p'.
7. change the enemy color to purple for better accuracy

Problems faced and areas to improve:
1. right now the dataset consists of 640 imgs and was trained on 50 epochs much training should be provided.
