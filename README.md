# eyes-free-track
This is a place to store our code and notes about the eyes free track project

Notes from 2/3 Meeting - Brainstorm for how to detect track and obstacles
- use color - do we need to consider brightness? what if it is dark outside?
- use the width of a track lane line (there is work on inferring depth in an image, and from there, we can calculate lengths)
- if we can detect lane lines, calculate the angle with respect to the bottom of the photo (if symmetrical, going straight, if not, veering)
- if we can detect the track color, then we can "forget the top portion" of the picture to make edge and hough easier to use
- using edge and hough, figure out the patterns of the remaining lines to infer the person's location on the track
- if we can detect colors, we can also detect objects and pedestrians
