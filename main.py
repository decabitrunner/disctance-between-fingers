import cv2
import mediapipe as mp
import math
import matplotlib.pyplot as plt
import statistics
import json
import time
import datetime

w = 1920
h = 1080
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
capture. set(cv2.CAP_PROP_FRAME_WIDTH, w)
capture. set(cv2.CAP_PROP_FRAME_HEIGHT, h)
mhands = mp.solutions.hands
hands = mhands.Hands()
draw = mp.solutions.drawing_utils

px = 0
py = 0
cord1 = (0, 0)
cord2 = (0, 0)
fingers = ['Thumb', 'Index Finger', 'Middle Finger', 'Ring Finger', 'Pinky Finger']
settings = {}
distances = []
minutes = []
with open('settings.json', 'r') as jf:
    settings = json.load(jf)

while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)




    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            for id, lm in enumerate(handLms.landmark):

                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y*h)

                try:
                    index1 = fingers.index(settings["finger_1"]) + 1
                    index2 = fingers.index(settings["finger_2"]) + 1
                except ValueError:
                    raise ValueError('Check readme.md for docs of setting format')

                frame = cv2.putText(
                    frame,
                    str(len(distances)),
                    (10, 70),
                    cv2.FONT_HERSHEY_DUPLEX,
                    1.0,
                    (125, 246, 55),
                    1
                )


                if id == index1*4:
                    cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                    cord1 = (cx, cy)


                if id == index2*4:
                    cv2.circle(frame, (cx, cy), 15, (31, 124, 255), cv2.FILLED)
                    cord2 = (cx, cy)

            distance = math.hypot(cord1[0] - cord2[0], cord1[1] - cord2[1])
            distances.append(distance)
            x = datetime.datetime.now()
            minutes.append(x.strftime('%M'))
            draw.draw_landmarks(frame, handLms, mhands.HAND_CONNECTIONS)


        if len(distances) == settings["number_of_distances"]:
                break

    if settings["display"] == True:
        cv2.imshow('images', frame)
        cv2.waitKey(1)

print(f'Collected {len(distances)} lengths. Making graph...')

results = {}
if settings["save_raw_data"] == True:
    results["raw"] = distances
results["average"] = sum(distances)/len(distances)
results["mode"] = max(set(distances), key = distances.count)
results["median"] = statistics.median(distances)
results["range"] = (max(distances), min(distances))
results["samples"] = len(distances)



with open('results.json', 'w') as file:
    json.dump(results, file, indent=6)

y = distances
if settings["graph_against"] == 'minutes':
    x = minutes
elif settings["graph_against"] == 'sample count':
    x = []
    for i in range(1, len(distances)+1):
        x.append(i)
plt.plot(x, y)
plt.xlabel(settings["graph_against"])
plt.ylabel('Distance')
plt.title(f'Distance between the {settings["finger_1"]} and {settings["finger_2"]}')
plt.show()
