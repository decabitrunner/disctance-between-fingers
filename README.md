# disctance-between-fingers
A project providing something no one would need but why not?

## What dose it do?

* Using object recognition it recognises fingers __a__ , __b__ and calculates the distance between the points. It dose that for __n__ mesurments. The visualization of that can be showed below:
![alt text](https://github.com/decabitrunner/disctance-between-fingers/blob/main/res/tracked.PNG)

* Than it processes the values to basic avreages and dumps them to a json file.
* Plots the results on a graph.

## [settings.json](https://github.com/decabitrunner/disctance-between-fingers/blob/main/settings.json)

```json
{
  "finger_1": "Thumb",
  "finger_2": "Index Finger",
  "number_of_distances": 100,
  "graph_against": "sample count",
  "display": true,
  "save_raw_data": true
}
```
### Here you adjust the settings for the script.

The aceptable data for fingers 
```
['Thumb', 'Index Finger', 'Middle Finger', 'Ring Finger', 'Pinky Finger']
```

The aceptable data for other values

| Key           | type          | Special restrictions  |
| ------------- |:-------------:| -----:|
| `"number_of_distances"`| int| Positive|
| `"graph_against"`     | str    |   "sample count" or "minutes" |
| `"display"` | boolean      |    None not allowed |
|  `"display"`  | boolean       |    None not allowed   |
|   `"save_raw_data"` | boolean |    None not allowed      |
